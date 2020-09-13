from algos import quicksort, mergesort, bubblesort, pysort
import random
import time

"""
    Analyzes the performance of individual sorting algorithms.
"""

def generate_list(range_size, max_int):
    """
        Generate's a list of integers and appends them to a list within a 
        given range.

        Params
        ------
        range_size: int 
            defines range for random list
        max_int: int
            maximum integer to test in random list range

        Output
        ------
        random_list list of integers
    """
    random_list = []
    for num in range(range_size):
        random_list.append(random.randint(1,max_int))
    return random_list


def algo_time(call_func, arr):
    """
        Calculate the performance of each algorithm.
    """
    start_time = time.time()
    call_func(arr) # Use arg and pass in function as object
    end_time = time.time()
    elapsed_time = end_time - start_time
    print(f"{str.capitalize(call_func.__name__)}\t-> Algorithm time: {elapsed_time:.8f}")

# Take in user input
def user_input():
    """
        Takes in user input.
    """
    user_size = int(input("Specify the number of items in the list: "))
    user_range = int(input("Specify the max range: "))
    num_runs = int(input("Specify how many times to run this analyzer: "))
    for num in range(num_runs):
        print(f"Run: {num+1}")
        l1 = generate_list(user_size, user_size)
        algo_time(bubblesort, l1.copy()) # Use copy to prevent use of sorted list below
        algo_time(mergesort, l1)
        algo_time(quicksort, l1)
        algo_time(pysort, l1) # Built in sorted algo is heavily optimized
        print("-" * 45)

if __name__ == "__main__":
    user_input()