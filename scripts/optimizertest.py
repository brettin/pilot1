import optimizer as opt

opt1 = opt.opt_builder(optimizer="SGD")
opt.opt_builder(optimizer="SGD",lr=.1)
opt2 = opt.opt_builder(optimizer="RMSprop")
opt3 = opt.opt_builder(optimizer="Adagrad")
opt4 = opt.opt_builder(optimizer="Adadelta")
opt5 = opt.opt_builder(optimizer="Adam")
opt6 = opt.opt_builder(optimizer="Adamax")
opt7 = opt.opt_builder(optimizer="Nadam")

opts=['SGD', 'RMSprop', 'Adagrad', 'Adadelta', 'Adam', 'Adamax', 'Nadam']
lrs=[ 0.1, 0.2, 0.3]

for o in opts:
	for lr in lrs:
		opt.opt_builder(optimizer=o,lr=lr)
