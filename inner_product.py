#!/usr/bin/python3

import numpy as np

v1 = np.array([[np.sqrt(3)], [1]])
v2 = np.array([[1], [1]])
inner_result_1 = np.vdot(v1, v2)

print("inner_result_1: ", inner_result_1)
print("\n")


v3 = np.array([[1j], [1]])
v4 = np.array([[-1j], [1]])
inner_result_2 = np.vdot(v3, v4)

print("\n")
print("inner_result_2: ", inner_result_2)
print("\n")


v5 = np.array([[1+2j], [1]])
v6 = np.array([[1-1j], [1]])
inner_result_3 = np.vdot(v3, v4)

print("inner_result_3: ", inner_result_3)
print("\n")