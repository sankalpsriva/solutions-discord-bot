import os 
import pandas as pd
import tensorflow as tf
import numpy as np
from keras.layers import TextVectorization
from better_profanity import profanity
from keras.models import Sequential
from keras.layers import LSTM, Dropout, Bidirectional, Dense, Embedding

df = pd.read_csv("train.csv")
df_X = df['comment_text'] # Message Content 
df_Y = df[df.columns[2:]].values # Message Toxcicty count

WORDS = 200000

text_vec = TextVectorization(max_tokens=WORDS, output_sequence_length=180, output_mode='int')

text_vec.adapt(df_X.values)
text_vec.get_vocabulary()
vectorized_text = text_vec(df_X.values)

# Data Piplines
dataset = tf.data.Dataset.from_tensor_slices((vectorized_text, df_Y))
dataset = dataset.cache()
dataset = dataset.shuffle(160000)
dataset = dataset.batch(16)
dataset = dataset.prefetch(8)

batch_X, batch_Y = dataset.as_numpy_iterator().next()

train = dataset.take(int(len(dataset) * 0.7))
val = dataset.skip(int(len(dataset) * 0.7)).take((int(len(dataset) * 0.2)))
test = dataset.skip(int(len(dataset) * 0.9)).take(int(len(dataset) * 0.2))

train_gen = train.as_numpy_iterator()

model = Sequential() 
model.add(Embedding(WORDS + 1,  32))
model.add(Bidirectional(LSTM(32, activation='tanh')))
model.add(Dense(128, activation='relu'))
model.add(Dense(256, activation='relu'))
model.add(Dense(128, activation='relu'))
model.add(Dense(6, activation='sigmoid'))

model.compile(loss = 'BinaryCrossentropy', optimizer = "Adam")
model.summary()

hist = model.fit(train, epochs = 10, validation_data = val)
model.save("toxicity_dectector.model")