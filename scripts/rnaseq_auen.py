from keras.layers import Input, Dense
from keras.models import Model
import numpy as np
import sys
from keras.utils import np_utils
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split

# 
# load the data
import numpy as np
X_fname      = sys.argv[1]
y_fname      = sys.argv[2]

X = np.loadtxt(open(X_fname, "rb"), dtype=float, delimiter='\t')
y = np.loadtxt(open(y_fname, "rb"), dtype=int, delimiter='\t')

rs = np.random.randint(10,100)
x_train, x_test, y_train, y_test = train_test_split(  X, y, test_size=0.33, random_state=rs)

# one hot encode y
encoder = LabelEncoder()
encoder.fit(y_train)
y_encoded = encoder.transform(y_train)
y_onehot = np_utils.to_categorical(y_encoded)

encoder.fit(y_test)
y_test_encoded = encoder.transform(y_test)
y_test_onehot = np_utils.to_categorical(y_test_encoded)

# get the input diminsion for the first layer and output dim for last layer
input_dim = x_train.shape[1]
output_dim = x_train.shape[1]


# this is the size of our encoded representations
encoding_dim = 80 

# this is our input placeholder
input_data = Input(shape=(input_dim,))

# "encoded" is the encoded representation of the input
encoded = Dense(encoding_dim, activation='relu')(input_data)

# "decoded" is the lossy reconstruction of the input
decoded = Dense(output_dim, activation='sigmoid')(encoded)

# this model maps an input to its reconstruction
autoencoder = Model(input=input_data, output=decoded)

# this model maps an input to its encoded representation
encoder = Model(input=input_data, output=encoded)

# create a placeholder for an encoded (80-dimensional) input
encoded_input = Input(shape=(encoding_dim,))

# retrieve the last layer of the autoencoder model
decoder_layer = autoencoder.layers[-1]

# create the decoder model
decoder = Model(input=encoded_input, output=decoder_layer(encoded_input))

autoencoder.compile(optimizer='adadelta', loss='binary_crossentropy')


# lets train the autoencoder for 50 epochs
from keras.callbacks import TensorBoard

autoencoder.fit(x_train, x_train,
                nb_epoch=50,
                batch_size=256,
                shuffle=True,
                validation_data=(x_test, x_test),
		callbacks=[TensorBoard(log_dir='/tmp/autoencoder')])



