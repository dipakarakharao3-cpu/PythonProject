# import numpy as np
# arr = np.array([[[1,2,3,4],[5,6,7,8,],[9,10,11,12],[13,14,15,16]]])
# for x in arr:
#     for y in x:
#         for z in y:
#             print(z)
#
#

#
# import numpy as np
#
# arr = np.array([[1, 2], [3, 4]],)
#
# for x in np.nditer(arr):
#   print(x)
#
# import numpy as np
# arr = np.array([1,2,3,4])
# for x in  np.nditer(arr, flags=['buffered'], op_dtypes=['S']):
#     print(x)

# import numpy as np
#
# arr = np.array([[1, 2, 3,4],[5,6,7,8],[9,10,11,12]])
#
# for x in np.nditer(arr[:,2::1]):
#   print(x)


# Enumerate on following 1D arrays elements:

import numpy as np
arr = np.array([[1,2,3,4,5,6],[7,8,9,10,11,12]])
for idx, x in np.ndenumerate(arr):
    print(idx, x)