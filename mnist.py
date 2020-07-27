from keras.datasets import mnist
dataset = mnist.load_data('mymnist.db')

train , test = dataset
X_train , y_train = train
X_test , y_test = test
img1 = X_train[7]

import cv2
X_train_1d = X_train.reshape(-1 , 28*28)
X_test_1d = X_test.reshape(-1 , 28*28)

X_train = X_train_1d.astype('float32')
X_test = X_test_1d.astype('float32')

from keras.utils.np_utils import to_categorical
import matplotlib.pyplot as plt
from keras.optimizers import Adam
from keras.models import Sequential
from keras.layers import Dense
import keras
import sys

y_train_cat = to_categorical(y_train)
y_test_cat = to_categorical(y_test)
model = keras.backend.clear_session()	
model = Sequential()

sys.stdin = open('input.txt', 'r')

l1nn = int(input())
l2nn = int(input())
l3nn = int(input())
l4nn = int(input())
epch = int(input())

model.add(Dense(units=l1nn, input_dim=28*28, activation='relu'))
model.add(Dense(units=l2nn, activation='relu'))
model.add(Dense(units=l3nn, activation='relu'))
model.add(Dense(units=l4nn, activation='relu'))
model.add(Dense(units=10, activation='softmax'))
model.summary()


# In[7]:


model.compile(optimizer=Adam(), loss='categorical_crossentropy', 
             metrics=['accuracy']
             )
h = model.fit(X_train, y_train_cat, epochs=epch)

scores = model.evaluate(X_test, y_test_cat, verbose=1)
print('Test loss:', scores[0]*100)
print('Test accuracy:', scores[1]*100)

accuracy = str(scores[1]*100)
accuracy_file = open('accuracy.txt','w')
accuracy_file.write(accuracy)
accuracy_file.close()
