import random

def generate_random_list(size):
	return [random.randint(1,size**2) for i in range(size)]

def generate_corpus(size):
	return [generate_random_list(s) for s in range(1,size+1)]