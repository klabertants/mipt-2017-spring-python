import time
import sys
import functools
		

def profiler(func):
	@functools.wraps(func)
	def wrapper(*args, **kwargs):
		if sys._getframe().f_back.f_code.co_name != func.__name__:
			wrapper.calls = 0
		wrapper.calls += 1
		start = time.monotonic()
		result = func(*args, **kwargs)
		wrapper.last_time_taken = time.monotonic() - start
		return result

	wrapper.calls = 0
	return wrapper

exec(sys.stdin.read())
