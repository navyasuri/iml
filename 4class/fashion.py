import tensorflow as tf
from tensorflow import keras

import numpy as np

import matplotlib.pyplot as plt
import matplotlib.image as mpimg

training = False

fashion = keras.datasets.fashion_mnist

# Get the data from the data set
(train_images, train_labels), (test_images, test_labels) = fashion.load_data()

# Check sizes'
print(len(train_labels), train_images.shape)
print(len(test_labels), test_images.shape)

class_names = ['T-shirt/top', 'Trouser', 'Pullover', 'Dress', 'Coat', 'Sandal', 'Shirt', 'Sneaker', 'Bag', 'Ankle boot']
index = np.random.randint(0, 60000)
# imgplot = plt.imshow(train_images[index])
# print("index", index, "label", class_names[train_labels[index]])
# plt.show()

# regularize each pixel to map from grayscale (0, 255) to (0, 1) [just scaling the data]
train_images = train_images/255.0
test_images = test_images/255.0

# Forward Propagation
if training:

    model = keras.Sequential([
        keras.layers.Flatten(input_shape=(28, 28)), 
        keras.layers.Dense(128, activation=tf.nn.relu), 
        keras.layers.Dense(10, activation=tf.nn.softmax)
    ])

    model.compile(optimizer='adam', 
        loss='sparse_categorical_crossentropy',
        metrics=['accuracy'])

    # model.save('fashion.h5')

    model.fit(train_images, train_labels, epochs=5)

    test_loss, test_acc = model.evaluate(test_images, test_labels)

else:
    model = keras.models.load_model('fashion.h5')
    
    predictions = model.predict(test_images)
    random_image = np.random.randint(0, 10000)
    prediction = predictions[random_image]

    print(prediction)

    pred_label = np.argmax(prediction)
    print(class_names[pred_label])
    plt.imshow(test_images[pred_label])
    plt.show()
