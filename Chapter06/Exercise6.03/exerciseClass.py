import pickle
import os


class NN_Model(object):
	"""docstring for TrainedModel"""
	def __init__(self):
		path = os.getcwd()+'/model_exercise.pkl'
		file = open(path, 'rb')
		self.model = pickle.load(file)

	def predict(self, season, age, childish, trauma, surgical, fevers, alcohol, smoking, sitting):
		X = [[season, age, childish, trauma, surgical, fevers, alcohol, smoking, sitting]]
		return self.model.predict(X)