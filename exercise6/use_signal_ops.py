import matplotlib.pyplot as plt
import signal_ops

values = [72, 75, 71, 89, 77]

print("MIN:", signal_ops.signal_min(values))
print("MAX:", signal_ops.signal_max(values))
print("AVG:", round(signal_ops.signal_avg(values), 2))

plt.plot([1, 2, 3], [3, 1, 4])
plt.show()