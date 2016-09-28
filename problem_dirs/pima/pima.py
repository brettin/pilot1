import numpy


# load pima indians dataset
dataset = numpy.loadtxt("pima-indians-diabetes.csv", delimiter=",")
# split into input (X) and output (Y) variables
X = dataset[:,0:8]
Y = dataset[:,8]

print dataset.shape
print X.shape
print Y.shape

# 6,148,72,35,0,33.6,0.627,50,1
# 1,85,66,29,0,26.6,0.351,31,0

# it appears that the input X data has 768 rows (patients)
# it appears that the input X data has 9 columns (features)
# it appears that the input Y data has 768 rows (labels)
# it appears that the input Y data has 1 col (label value)
# (768, 9)
# (768, 8)
# (768,)

# create model
from keras.models import Sequential
model = Sequential()

# add layers
from keras.layers import Dense, Activation
model.add(Dense(12, input_dim=8, init='uniform', activation='relu'))
model.add(Dense(8, init='uniform', activation='relu'))
model.add(Dense(1, init='uniform', activation='sigmoid'))

# Compile model
model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])


# Fit the model
model.fit(X, Y, nb_epoch=150, batch_size=10)

# evaluate the model
scores = model.evaluate(X, Y)
print "\n\nModel Evaluation"
print("%s: %.2f%%" % (model.metrics_names[1], scores[1]*100))

