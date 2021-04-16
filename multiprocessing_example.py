#!/usr/bin/env python3

import os
import multiprocessing
import time

TIME_TO_SLEEP        = 0.5   # Seconds
NUMBER_OF_PROCESSES  = 4


## Decorator function that adds timing to other functions
def time_me(function):
	def inner():
		start = time.time()
		function()
		print(f"The code ran in: {time.time()-start} seconds")
	return inner

# Fcuntion to be multiprocessed
def multi_func():
	pid = os.getpid()
	print(f'Running on core: {pid}.')
	
	for _ in range(10_000_000):
		f = (9_999_999.9 * 944_438_468 + 18_468_468)/9_999.26494
	
	time.sleep(TIME_TO_SLEEP)

@time_me
def print_with_processes():
	processes_ = []
	for _ in range(NUMBER_OF_PROCESSES):
		process = multiprocessing.Process(target = multi_func)
		processes_.append(process)
		process.start()

	for process_ in processes_:
		process_.join()

@time_me
def print_normal():
	for _ in range(NUMBER_OF_PROCESSES):
		multi_func()

##

print("Going to try normal printing!")
print_normal()

print("Going to try multi-processed printing!")
print_with_processes()