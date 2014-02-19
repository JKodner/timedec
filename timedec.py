import time
def count(func):
	def wrapper():
		start = time.time()
		func()
		return time.time() - start
	return wrapper