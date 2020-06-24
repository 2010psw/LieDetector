from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.models import model_from_json
from tensorflow.keras.preprocessing.sequence import pad_sequences
import numpy as np
import json

def pred(new_list):
    try:
        #테스트용 코드, 아두이노없을때 사용
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

        asdf = tokenizer.texts_to_sequences(new_np)

        sequences = tokenizer.texts_to_sequences(new_list)

        x_test = pad_sequences(sequences, maxlen=21)

        value_predicted = loaded_model.predict(x_test)

        sum = 0
        result = value_predicted
        data = []
        for i in value_predicted:
            data.append(i.tolist())
        print(data)
        print(type(data))

        # result = str((sum/21*100)[0])[0:5]
        # print('진실일 확률')
        # print(result)

        return data
    except Exception as msg:
        print(msg)