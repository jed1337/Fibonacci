from collections import defaultdict

top_down = defaultdict(lambda: -1)
top_down[0] = 1
top_down[1] = 1


def fibonacci_top_down(n):
    if top_down[n] != -1:
        return top_down[n]
    top_down[n] = fibonacci_top_down(n - 1) + fibonacci_top_down(n - 2)
    return top_down[n]


def fibonacci(n):
    if n == 0 or n == 1:
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)


def fibonacci_generator(n):
	"""Get the first n fibonacci numebrs"""
	
	a,b = 1,1
	yield a
	for i in range(n):
		yield a
		b,a = a, a+b	


for i in range(1000):
    print(fibonacci_top_down(i))
    # print(fibonacci(i))
