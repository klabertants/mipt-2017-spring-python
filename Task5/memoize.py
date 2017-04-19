import sys
import functools
	
def memoize(func):
	@functools.wraps(func)
	def wrapper(*args, **kwargs):
		arguments = (args, tuple(kwargs.items()))
		if not hasattr(func, 'results'):
			func.results = dict()
		if arguments not in func.results:
			func.results[arguments] = func(*args, **kwargs)
		return func.results[arguments]
	
	return wrapper

exec(sys.stdin.read())
