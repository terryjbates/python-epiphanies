#!/usr/bin/env python3
#
# solve_double.py

def double(val, n=3):
    def double_it(val):
        return val * 2

    def iterate_n_times(val, n):
        for i in range(n):
            doubled_val = val * 2
            val = doubled_val
            yield doubled_val
            

    output_list = []
    my_iter = iterate_n_times(val, n)
    while True:
        try:
            output_list.append(next(my_iter))
        except StopIteration:
            return output_list
