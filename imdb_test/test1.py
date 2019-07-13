from __future__ import absolute_import, division, print_function, unicode_literals

import tensorflow as tf

import tensorflow_hub as hub
import tensorflow_datasets as tfds

print("버전: ", tf.__version__)
"""
print("즉시 실행 모드: ", tf.executing_eagerly())
print("허브 버전: ", hub.__version__)
print("GPU ", "사용 가능" if tf.test.is_gpu_available() else "사용 불가능")
"""

