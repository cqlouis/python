def fib(n):
	print("*",end = "")
	if n < 0:
		return print("Errous input")
	if n == 0:
		return 0
	if n == 1:
		return 1
	return fib(n - 1) + fib(n - 2)


n = int(input("请输入n: "))
result = fib(n)
print("fibonacci(%d) =  %d" % (n, result))