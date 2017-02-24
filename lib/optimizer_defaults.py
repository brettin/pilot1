
defaults_for = {'SGD': {}, 'RMSprop' : {}, 'Adadelta' : {}, 'Adam' : {}, 'Adamax' : {}, 'Nadam' : {} }

defaults_for['SGD']      = {'lr' :0.01, 'momentum' : 0.0, 'decay' : 0.0, 'nesterov' : False}
defaults_for['RMSprop']  = {'lr' :0.001, 'rho' : 0.9, 'epsilon' : 1e-08, 'decay' : 0.0}
defaults_for['Adagrad']  = {'lr' :0.01, 'epsilon' : 1e-08, 'decay' : 0.0}
defaults_for['Adadelta'] = {'lr' :1.0, 'rho' : 0.95, 'epsilon' : 1e-08, 'decay' : 0.0}
defaults_for['Adam']     = {'lr' :0.001, 'beta_1' : 0.9, 'beta_2' : 0.999, 'epsilon' : 1e-08, 'decay' : 0.0}
defaults_for['Adamax']   = {'lr' :0.002, 'beta_1' : 0.9, 'beta_2' : 0.999, 'epsilon' : 1e-08, 'decay' : 0.0}
defaults_for['Nadam']    = {'lr' :0.002, 'beta_1' : 0.9, 'beta_2' : 0.999, 'epsilon' : 1e-08, 'schedule_decay' : 0.004}
