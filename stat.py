import numpy as np
import pandas as pd

population = [4779736,710231,6392017,2915918,37253956,5029196,3574097,897934]


population.sort()


# for i in population:
# 	print(i)

# print("\n\n")
med = np.mean(population)
# print(np.median(population))

for i in population:
	deviate = i - med;
	if (deviate<0):
		# print(-(deviate))
		pass
	else:
		# print(deviate)
		pass

# print(len("TWFueSBoYW5kcyBtYWtlIGxpZ2h0IHdvcmsu"))

l = [1,2,3,3,5,6,7,9]
df = pd.DataFrame(l)
print(df,end = "\n\n")

mean = df.mean()
suma = 0
for i in l:
	suma = (i - mean)**2

n = len(l)
var = suma/(n-1)

# print(f"variance : {var}")
# print(f"std : {var**(1/2)}")

print(df.std(),end = "\n")

print("25th percentile : ",df.quantile(0.25))

df.hist()