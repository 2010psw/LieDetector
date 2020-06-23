
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.models import model_from_json
from tensorflow.keras.preprocessing.sequence import pad_sequences
import numpy as np
import json
import pickle
import h5py

def pred(new_list):
    try:
        # new_list = []
        # for i in range(10):
        #     new_list.append('141414')
        # new_list.append('#')
        # for i in range(10):
        #     new_list.append('151515')
        tokenizer = Tokenizer()


        with open('word.json') as json_file:
            word_index = json.load(json_file)
            tokenizer.word_index = word_index

        json_file = open("model.json", "r")
        loaded_model_json = json_file.read()
        json_file.close()
        loaded_model = model_from_json(loaded_model_json)

        loaded_model.load_weights('best_model.h5')
        loaded_model.compile(optimizer='rmsprop', loss='binary_crossentropy', metrics=['acc'])


        new_np = np.array(new_list)
        print('shape=============')
        print(new_np.shape)



        print('test=============')
        asdf = tokenizer.texts_to_sequences(new_np)
        print('test=============')
        print(asdf)
        print('test=============')
        sequences = tokenizer.texts_to_sequences(new_list)

        x_test = pad_sequences(sequences, maxlen=21)
        print(x_test)
        value_predicted = loaded_model.predict(x_test)
        print(len(value_predicted))
        sum = 0
        for i in value_predicted:
            sum = sum+i
        result = str((sum/21*100)[0])[0:5]
        print('진실일 확률')
        print(result)
        return result
    except Exception as msg:
        print(msg)