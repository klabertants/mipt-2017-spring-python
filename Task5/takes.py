import sys
import functools

def takes(*types):
	
	def taker(func):
		@functools.wraps(func)
		
		def decorator(*args, **kwargs):
			arguments = args + tuple(kwargs)
			for index, argument in enumerate(arguments):
				if index >= len(types):
					pass
				else:
					if type(argument) != types[index]:
						raise TypeError
			result = func(*args, **kwargs)
			return result
		return decorator
		
	return taker

exec(sys.stdin.read())
