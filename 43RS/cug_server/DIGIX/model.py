from base import *
from utils import *

# 参数变量
os.environ['CUDA_VISIBLE_DEVICES'] = '1'  # 指定GPU
learning_rate = 1e-3
batch = 8192 * 4
n_epoch = 100
embedding_dim = 8  # embedding维度一般来说越大越好，但是维度越大跑起来越慢

#读取数据
print(os.getcwd())
train_df = pd.read_csv('./data/train_df.csv')
test_df = pd.read_csv('./data/test_df.csv')
train_df = reduce_mem_usage(train_df)
test_df = reduce_mem_usage(test_df)
all_df = df = pd.concat([train_df.drop(columns=['label']), test_df],axis=0)
sparse_features = ['city_rank', 'creat_type_cd', 'device_size', 'gender', 'indu_name', 'inter_type_cd', 'residence',
                   'slot_id', 'net_type', 'task_id', 'adv_id', 'adv_prim_id', 'age', 'app_first_class',
                   'app_second_class', 'career', 'city', 'consume_purchase', 'dev_id', 'tags']
dense_features = ['spread_app_id', 'device_name', 'his_app_size', 'his_on_shelf_time', 'app_score', 'emui_dev',
                  'list_time', 'device_price', 'up_life_duration', 'up_membership_grade', 'membership_life_duration',
                  'communication_avgonline_30d', 'id', 'city_rank_count', 'creat_type_cd_count', 'dev_id_count',
                  'device_size_count', 'gender_count', 'indu_name_count', 'inter_type_cd_count', 'residence_count',
                  'slot_id_count', 'net_type_count', 'task_id_count', 'adv_id_count', 'adv_prim_id_count', 'age_count',
                  'app_first_class_count', 'app_second_class_count', 'career_count', 'city_count',
                  'consume_purchase_count', 'tags_count']
target = 'label'

# 2.count #unique features for each sparse field,and record dense feature field name
fixlen_feature_columns = [SparseFeat(feat, vocabulary_size=all_df[feat].nunique(), embedding_dim=embedding_dim)
                          for i, feat in enumerate(sparse_features)] + [DenseFeat(feat, 1, )
                                                                        for feat in dense_features]

dnn_feature_columns = fixlen_feature_columns
linear_feature_columns = fixlen_feature_columns

feature_names = get_feature_names(linear_feature_columns + dnn_feature_columns)

# 3.generate input data for model
train_model_input = {name: train_df[name] for name in feature_names}
test_model_input = {name: test_df[name] for name in feature_names}

# 4.Define Model,train,predict and evaluate
plateau = ReduceLROnPlateau(monitor='val_auc', verbose=1, mode='max', factor=0.3, patience=5)
early_stopping = EarlyStopping(monitor='val_auc', patience=8, mode='max')
# checkpoint = ModelCheckpoint(weights_path,
#                              monitor='val_auroc',
#                              verbose=0,
#                              mode='max',
#                              save_best_only=True)
model = DeepFM(linear_feature_columns, dnn_feature_columns, task='binary', dnn_dropout=0.1, dnn_hidden_units=(512, 128))

# def auroc(y_true, y_pred):
#     return tf.py_func(roc_auc_score, (y_true, y_pred), tf.double)
model.compile(optimizer=Adam(lr=learning_rate), loss = multi_category_focal_loss2(alpha=0.1, gamma=2),
              metrics=['AUC'], )

history = model.fit(train_model_input, train_df[target].values, callbacks=[early_stopping, plateau],
                    shuffle=True, validation_split=0.2,
                    batch_size=batch, epochs=n_epoch, verbose=1)
y_pred = model.predict(test_model_input, batch_size=batch)

# 保存结果
res = pd.DataFrame()
res['id'] = range(1, 1000001)
res['probability'] = y_pred
res.to_csv('./data/deepFM.csv', index=False)
