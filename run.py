import time


def sequential(data, target):
    """Linear Search implementation to find a targeted value in a list"""
    for i in range(len(data)):
        if data[i] == target:
            return f"Found at index {i}"


def binary(data, target, low, high):
    """Binary Seach to find the targeted value, using a sorted list"""
    if low > high:
        return f"Can't Find the element"
    else:
        mid = (low + high) // 2
        if target == data[mid]:
            return f"Found at index {mid}"
        elif target < data[mid]:
            return binary(data, target, low, mid - 1)
        else:
            return binary(data, target, mid + 1, high)


with open("numbers.txt") as f:
    numbers = f.readlines()

# Remove the new Line
numbers = [x.strip() for x in numbers]

# convert the strings to int
numbers = [int(x) for x in numbers]

#   _      _
#  | |    (_)
#  | |     _ _ __   ___  __ _ _ __
#  | |    | | '_ \ / _ \/ _` | '__|
#  | |____| | | | |  __/ (_| | |
#  |______|_|_| |_|\___|\__,_|_|

# Implementation for the linear Search
start_time = time.time()
print(
    sequential(
        numbers,
        547,
    )
)
print(f"Time: {(time.time() - start_time)} Second")

#   ____  _
#  |  _ \(_)
#  | |_) |_ _ __   __ _ _ __ _   _
#  |  _ <| | '_ \ / _` | '__| | | |
#  | |_) | | | | | (_| | |  | |_| |
#  |____/|_|_| |_|\__,_|_|   \__, |
#                             __/ |
#                            |___/


# First Sorting the numbers
numbers.sort()
start_time = time.time()
# Implementation for the linear Search
print(binary(numbers, 547, 0, 999999))
print(f"Time: {(time.time() - start_time)}  Second")
