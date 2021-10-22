1. exp_optimize_all_goal：包含了所有的goal

goal只包含104：

1. exp_optimize_after_bug：包含三个实验室

goal只包含104，bug前的实验：

1. exp_optimize_left_join：t_daily_exp_data 左连接 t_ocpa_middle_table_d（这份数据和线上完全一模一样）

![image-20210609193912990](https://tva1.sinaimg.cn/large/008i3skNgy1grc8zglxsmj30q406wmyb.jpg)

1. exp_optimize_inner_jion：t_daily_exp_data 内连接 t_ocpa_middle_table_d

![image-20210609193928331](https://tva1.sinaimg.cn/large/008i3skNgy1grc8zo4pp1j30qj071ab6.jpg)

内连接会导致数据减少

goal只包含104，bug前的实验，去掉了fraud_type=0：

