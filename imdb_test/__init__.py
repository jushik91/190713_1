import tensorflow_datasets as tfds
import tensorflow as tf
from imdb_test.model import Imdb

if __name__ == '__main__':
    imdb = Imdb()
    imdb.create_model()
