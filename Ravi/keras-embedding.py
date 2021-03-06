# -*- coding: utf-8 -*-
"""
Created on Wed May 22 16:56:51 2019

@author: Ravi
"""


from keras.preprocessing.text import one_hot
from keras.preprocessing.sequence import pad_sequences
from keras.models import Sequential
from keras.layers import Dense
from keras.layers import Flatten
from keras.layers.embeddings import Embedding

# define documents
docs = ['Well done!',
        'Good work',
        'Great effort',
        'nice work',
        'Excellent!',
        'Weak',
        'Poor effort!',
        'not good',
        'poor work',
        'Could have done better.']

# define class labels
labels = [1,1,1,1,1,0,0,0,0,0]

# integer encode the documents
vocab_size = 50
encoded_docs = [one_hot(d, vocab_size) for d in docs]
print(encoded_docs)

# pad documents to a max length of 4 words
max_length = 4  # could have been larger!
padded_docs = pad_sequences(encoded_docs, maxlen=max_length, padding='post')
print(padded_docs)

# define the model
model = Sequential()
model.input_shape
model.output_shape

# Embedding(input_dim, output_dim, input_length)
model.add(Embedding(vocab_size, 50, input_length=max_length))
model.input_shape  # is the input_length
model.output_shape  # is the output_dim

model.add(Flatten())
model.input_shape  # is the input_length
model.output_shape

model.add(Dense(1, activation='sigmoid'))

# compile the model
model.compile(optimizer='adam', 
              loss='binary_crossentropy', 
              metrics=['acc'])

# summarize the model
model.summary()
# fit the model
model.fit(padded_docs, labels, epochs=50, verbose=0)
# evaluate the model
loss, accuracy = model.evaluate(padded_docs, labels, verbose=0)
print('Accuracy: %f' % (accuracy*100))


###################################################################


















