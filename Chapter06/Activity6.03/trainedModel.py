import pickle
import os


class NN_Model(object):
	"""docstring for TrainedModel"""
	def __init__(self):
		path = os.getcwd()+'/final_model.pkl'
		file = open(path, 'rb')
		self.model = pickle.load(file)

	def predict(self, age, job, marital, education, default, balance, housing, loan, day, month, duration, campaign,
				pdays, previous):
		X = [[age, job, marital, education, default, balance, housing, loan, day, month, duration, campaign, pdays,
			  previous]]
		return self.model.predict(X)
