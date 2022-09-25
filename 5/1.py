import numpy as np

m = np.array([[137, 115, 153], [177, 213, 103], [115, 182, 158]])
f = np.array([[-1, 0, 1], [-2, 1, 2], [-1, 0, 1]])

m = m.flatten()
f = f.flatten()

print(f"Correlação: \n{np.correlate(m, f, 'valid')[0]}\n\nConvolução: \n{np.convolve(m, f, 'valid')[0]}")
