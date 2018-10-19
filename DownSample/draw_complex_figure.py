import matplotlib.pyplot as plt
import numpy as np

filename = 'original_out.txt'
with open(filename) as f:
	lines = f.readlines()[-200:]
realpart = np.zeros(len(lines))
imagpart = np.zeros(len(lines))
for idx, line in enumerate(lines):
	realpart[idx] = line[2:12]
	imagpart[idx] = line[-14:-3]

x = np.linspace(0, len(lines)-1, len(lines))
plt.plot(x, realpart)
plt.plot(x, realpart, 'b*')
#plt.plot(x, imagpart)
#plt.plot(x, imagpart, 'go')
plt.show()
