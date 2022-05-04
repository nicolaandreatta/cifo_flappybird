import numpy as np 
import pandas as pd
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras.layers import Dense
from tensorflow.keras.models import Sequential
from tensorflow.keras.models import Model


def create_net():
    model = Sequential()
    #using 2 inputs for now (x distance to hole, y distance to hole) but many more could also be tested
    model.add(Dense(3, input_dim = 4, activation = 'relu'))
    #adding two hidden layers for now, we can just take one out, it should be fine either way
    model.add(Dense(3, activation = 'relu'))
    #We can also play around with relu and try other things, but I like relu as a starting point
    #outputs 0-1 values, if > 0.5 then it's a one
    model.add(Dense(1, activation = 'sigmoid'))

    #model.compile()
    return model

model = create_net()

