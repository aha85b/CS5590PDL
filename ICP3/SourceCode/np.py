# Import numpy
import numpy as np

# Crate random vector
rV = np.random.uniform(1.0, 20.0, 20)

# Resize it
resizeV = np.resize(rV, (4, 5))


print("Resized Verctor\n", resizeV)

# Replacing the max in each row
newArray = np.where(resizeV == np.max(resizeV, axis=1).reshape(-1,1), 0, resizeV)

print("Max replaced by 0\n", newArray)