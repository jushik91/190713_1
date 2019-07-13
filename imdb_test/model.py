import tensorflow_datasets as tfds
import tensorflow_hub as hub
import tensorflow as tf

class Imdb:
    def __int__(self):
        pass

    def create_model(self):
        train_validation_split = tfds.split.TRAIN.subsplit([6,4])

        (train_data, validataion_data), test_data = tfds.load(
            name = "imdb_reviews",
            split = (train_validation_split, tfds.Split.TEST),
            as_supervised=True)


        train_examples_batch, train_labels_batch = next(iter(train_data.batch(10)))

        embedding = "https://tfhub.dev/google/tf2-preview/gnews-swivel-20dim/1"
        hub_layer = hub.KerasLayer(embedding, input_shape=[],
                                   dtype=tf.string, trainable=True)
        hub_layer(train_examples_batch[:3])



