import torch
from torch.backends import cudnn

print(torch.__version__)
a = torch.tensor(1.)

print(a.cuda())
# 若正常则返回 tensor(1., device='cuda:0')

print(cudnn.is_available())
# 若正常则返回 True

print(cudnn.is_acceptable(a.cuda()))
