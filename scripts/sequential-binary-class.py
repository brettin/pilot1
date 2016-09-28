import numpy as np


X_fname = "GDC_downloads/data/ByType.2/X"
# y_fname = "GDC_downloads/data/ByType.2/y"
y_fname = "y_cat"

X_train = np.loadtxt(open(X_fname, "rb"), dtype=float, delimiter='\t')
Y_train = np.loadtxt(open(y_fname, "rb"), dtype=int, delimiter='\t')

print X_train.shape
print Y_train.shape

# (243, 60483)
# (243,)
# it appears that the 


# create a sequential model
from keras.models import Sequential
model = Sequential()


from keras.layers import Dense, Activation

model.add(Dense(64, input_dim=60483, init='uniform', activation='relu'))
# model.add(Activation("relu"))

model.add(Dense(32, init='uniform', activation='relu'))
# model.add(Activation("softmax"))

model.add(Dense(1, init='uniform', activation='sigmoid'))

# when the model looks good, configure it with compile
model.compile(loss='binary_crossentropy', optimizer='sgd', metrics=['accuracy'])

# You can now iterate on your training data in batches:
model.fit(X_train, Y_train, nb_epoch=50, batch_size=10000)

# Evaluate your performance in one line:
scores = model.evaluate(X_train, Y_train)


print "\n\nModel Evaluation"
print("%s: %.2f%%" % (model.metrics_names[1], scores[1]*100))


print "done"

