import numpy as np
import tensorflow as tf

from tensorflow.keras.layers import Embedding, Dense, LSTM
from tensorflow.keras.models import Sequential
from tensorflow.keras.models import load_model
from tensorflow.keras.callbacks import EarlyStopping, ModelCheckpoint
# from keras.preprocessing.text import Tokenizer

import os, sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from DB import conn

##########################아이디 목록 가져오기#########################
id_list = conn.select_id()

lb_list = []
####################################################################
x_train = []
y_train = []
x_test = []




for i in id_list :
    list = []
    for j in conn.select_gsr(i):
        list.append(j)
    for j in conn.select_hrt(i):
        list.append(j)
    lb_list.append(conn.select_lb(i))
    x_train.append(list)


for i in range(len(id_list)):
    y_train.append(lb_list[i])


# print('x_train')
# print(type(x_train))   >>>    list
# print(x_train)
# [
#     [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
#     [10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19],
#     [20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29],
#     [30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39],
#     [40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49]
# ]
#
# print('y_train')
# print(type(y_train))  >>>    list
# print(y_train)
#
# [1, 1, 0, 1, 0]



try:
    model = Sequential()
    model.add(Embedding(500,1, input_length=20))
    model.add(LSTM(128))
    model.add(Dense(1, activation='sigmoid'))


    es = EarlyStopping(monitor='val_loss', mode='min', verbose=1, patience=4)
    save_weights_only = 'true'
    # mc = ModelCheckpoint('best_model.h5', monitor='val_acc', mode='max', verbose=1, save_best_only=True)

    mc = ModelCheckpoint('best_model.h5', monitor='val_acc', mode='max', verbose=1, save_weights_only = 'true', period=3)


    model.compile(optimizer='rmsprop', loss='binary_crossentropy', metrics=['acc'])
    # history = model.fit(x_train, y_train, epochs=15, callbacks=[es, mc], batch_size=60, validation_split=0.2)
    history = model.fit(x_train, y_train, epochs=15, callbacks=[mc], batch_size=60)

    loaded_model = load_model('best_model.h5')
    
except Exception as msg:
    print(msg)
