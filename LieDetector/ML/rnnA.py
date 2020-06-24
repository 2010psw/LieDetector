import numpy as np
import tensorflow as tf

from tensorflow.keras.layers import Embedding, Dense, LSTM
from tensorflow.keras.models import Sequential
from tensorflow.keras.models import load_model
from tensorflow.keras.callbacks import EarlyStopping, ModelCheckpoint
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.models import model_from_json
from tensorflow.keras.preprocessing.sequence import pad_sequences
import numpy as np

import json

import os, sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from DB import conn

def train(new_list):

    ##########################아이디 목록 가져오기#########################
    id_list = conn.select_id()
    print(id_list)
    print(len(id_list))
    tokenizer = Tokenizer()

    lb_list = []
    ####################################################################
    x_train = []
    y_train = []

    for i in id_list :
        list = []
        for j in conn.select_gsr(i):

            list.append(str(j))

        list.append('#')

        for j in conn.select_hrt(i):
            list.append(str(j))
        lb_list.append(conn.select_lb(i))
        x_train.append(list)

    x_train.append(new_list)
    tokenizer.fit_on_texts(x_train)
    x_train.remove(new_list)

    print('word_index')
    print(tokenizer.word_index)

    jsonn = json.dumps(tokenizer.word_index)
    f3 = open('word.json', 'w')
    f3.write(jsonn)
    f3.close()


    x_train = tokenizer.texts_to_sequences(x_train)
    print('x_tr')
    print(x_train)

    for i in range(len(id_list)):
        y_train.append(lb_list[i])
    print('y_tr')
    print(y_train)


    try:
        model = Sequential()
        model.add(Embedding(300,1, input_length=21))
        model.add(LSTM(200))
        model.add(Dense(1, activation='sigmoid'))

        #데이터가 더 많아질 경우 변경가능
        # es = EarlyStopping(monitor='val_loss', mode='min', verbose=1, patience=4)
        # save_weights_only = 'true'
        # mc = ModelCheckpoint('best_model.h5', monitor='val_acc', mode='max', verbose=1, save_best_only=True)

        mc = ModelCheckpoint('best_model.h5', monitor='val_acc', mode='max', verbose=1, save_weights_only='true', period=3)
        model.compile(optimizer='rmsprop', loss='binary_crossentropy', metrics=['acc'])

        ##############모델저장#################
        model_json = model.to_json()
        with open('model.json', 'w') as json_file :
            json_file.write(model_json)
        #################################
        # history = model.fit(x_train, y_train, epochs=15, callbacks=[es, mc], batch_size=60, validation_split=0.2)
        history = model.fit(x_train, y_train, epochs=15, callbacks=[mc], batch_size=4)

        print(123)
        print(123)
        print(123)
        json_file = open("model.json", "r")
        loaded_model_json = json_file.read()
        json_file.close()
        loaded_model = model_from_json(loaded_model_json)

        loaded_model.load_weights('best_model.h5')
        loaded_model.compile(optimizer='rmsprop', loss='binary_crossentropy', metrics=['acc'])

        new_np = np.array(new_list)

        tokenizer.fit_on_texts(new_list)


        asdf = tokenizer.texts_to_sequences(new_list)
        sequences = tokenizer.texts_to_sequences(new_list)
        x_test = pad_sequences(sequences, maxlen=21)
        value_predicted = loaded_model.predict(x_test)
        print(value_predicted)
    except Exception as msg:
        print(msg)



