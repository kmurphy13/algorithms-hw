import matplotlib.pyplot as plt
import math

fig = plt.figure("Function Growth, n = 20", figsize=(7, 7))
ax = fig.add_subplot(111)

n = 1002
lin = [x for x in range(1,n)]
quad = [x*x for x in range(1,n)]
log = [math.log(x) for x in range(1,n)]
nlog = [n*math.log(x) for x in range(1,n)]
cubic = [x*x*x for x in range(1,n)]
expon = [2**x for x in range(1,n)]

lin_plot = ax.plot(lin,label= "O(n)")
quad_plot = ax.plot(quad, label="O(n^2)")
log_plot = ax.plot(log, label = "O(log(n))")
nlog_plot = ax.plot(nlog, label ="O(nlog(n))")
cubic_plot = ax.plot(cubic, label="O(n^3)")
expon_plot = ax.plot(expon, label="O(2^n)")

ax.legend()

plt.title("Function Growth, n=1000")
plt.xlabel("Input Size")
plt.ylabel("Run Time")
plt.legend()
plt.show()