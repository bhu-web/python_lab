import numpy as np 
import time 
# Define the size of the array 
size = 10**6  # 1 million elements 
# Create a Python list and a NumPy array with the same values 
python_list = list(range(size)) 
numpy_array = np.arange(size) 
# Measure time taken for element-wise addition with Python list 
start_time = time.time() 
python_list_result = [x + 1 for x in python_list] 
end_time = time.time() 
python_list_time = end_time - start_time 
# Measure time taken for element-wise addition with NumPy array 
start_time = time.time() 
numpy_array_result = numpy_array + 1 
end_time = time.time() 
numpy_array_time = end_time - start_time 
# Print the results 
print(f"Time taken using Python list: {python_list_time:.6f} seconds") 
print(f"Time taken using NumPy array: {numpy_array_time:.6f} seconds") 
print(f"NumPy is approximately {python_list_time/numpy_array_time:.2f} times faster for this operation.")
