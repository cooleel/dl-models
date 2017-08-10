"""
Numpy learning
"""
import numpy as np
import os
# 导入CSV数据
TRAIN_NITRATION = os.path.join(os.path.dirname(
    __file__), "d:\\train_nitration_941_standard.csv")
train_nitration_set = np.genfromtxt(
    TRAIN_NITRATION, delimiter=',', skip_header=1)

# 分类矩阵为第一列数据
n_target = train_nitration_set[:, 0]

# 特征矩阵 212*941
n_features = train_nitration_set[:, 1:]

# 输出两个矩阵的Shape
print("Target Shape: ", n_target.shape)
print("Features Shape: ", n_features.shape)
print("Train Set Shape:", train_nitration_set.shape)


def random_sample(train_set, size=10, isReplace=True):
    """
    训练集随机放回抽样
    ---
    参数
    ---
    train_set: 训练集或数据集矩阵
    size: 抽样数，默认10个
    isReplace: 是否放回抽样
    返回
    ---
    target: 训练集抽样的分类结果矩阵
    sample_input: 训练集抽样的输入矩阵
    """
    # 计算机训练集实例数（训练集的行数）
    instance_num = np.arange(1, train_set.shape[0])
    # 随机生成抽样行
    sample_row = np.random.choice(instance_num, size, isReplace)

    # 输出抽样行矩阵切片（列数为训练集的列数）
    sample_set = np.empty(shape=[train_set.shape[1], ])
    # print(sample_set.shape)
    
    # 循环抽取对应行构建出抽样矩阵
    for i in sample_row:
        sample_set = np.vstack((sample_set, train_set[i, :]))
    # 剔除第一行初始值
    sample_set = np.delete(sample_set, 0, 0)
    
    # 返回抽样的分类结果和输入数据（通常是特征值），默认第一列为target（分类结果）
    target = sample_set[:, 0]
    features = sample_set[:, 1:] 
    return (target, features)

batch_x, batch_y = random_sample(train_nitration_set, 4, True)
print(batch_y)