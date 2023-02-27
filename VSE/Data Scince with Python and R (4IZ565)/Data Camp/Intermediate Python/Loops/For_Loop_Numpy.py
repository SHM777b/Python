# Import numpy as np
import numpy as np

# For loop over np_height
for val in np_height:
    print("{} inches".format(val))

# For loop over np_baseball
for val in np.nditer(np_baseball):
    print(val)
