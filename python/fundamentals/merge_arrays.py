
if __name__ == "__main__":
    arr1 = [1,2,3]
    arr2 = [4,5,6]

    # there are two ways to merge array
    # 1. using + operator
    print(arr1+arr2)

    # 2. using extend
    arr1.extend(arr2)
    print(arr1)
    pass