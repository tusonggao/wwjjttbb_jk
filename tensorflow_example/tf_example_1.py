# 参考 hands-on 第十章

import numpy as np
import time
import tensorflow as tf


from tensorflow.contrib.learn.python.learn.datasets.mnist import read_data_sets

mnist = read_data_sets("MNIST_data/", one_hot=True)
print(type(mnist))

print('mnist.train.num_examples', mnist.train.num_examples)