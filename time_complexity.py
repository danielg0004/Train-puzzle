# Framework for testing time complexities empirically

from train import Train
from algorithms import slow_algorithm, fast_algorithm
import matplotlib.pyplot as plt

lengths = []
steps = []

NUMBER_OF_DATA_POINTS = 100

for _ in range(NUMBER_OF_DATA_POINTS):
    
    train = Train()
    res = fast_algorithm(train) # Choose algorithm here

    if len(train._lights) != res:
        print("The alogirthm failed with length " + str(len(train._lights)) + ", returning " + str(res) + ".")
        quit()
        
    lengths.append(res)
    steps.append(train.steps)


# Sorting results before graphing

sorted_data = sorted(zip(lengths, steps))
lengths, steps = zip(*sorted_data)

# Graph lengths vs. steps

sorted_data = sorted(zip(lengths, steps))
lengths, steps = zip(*sorted_data)
plt.plot(lengths, steps, color="red", marker="o", linestyle="-", label="Trend")

plt.xlabel("Length of the list")
plt.ylabel("Steps of the algorithm")
plt.title('Relationship Between List X and List Y')
plt.grid(True)
plt.legend()

plt.show()