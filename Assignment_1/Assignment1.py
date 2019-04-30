def partition(arr, start, end):
    pivot = arr[start]
    left = start + 1
    right = end
    done = False
    while not done:
        while left <= right and arr[left] <= pivot:
            left += 1
        while left <= right and pivot <= arr[right]:
            right -= 1
        if right < left:
            done = True
        else:
            arr[left], arr[right] = arr[right], arr[left]
    arr[start], arr[right] = arr[right], arr[start]
    return right


def partition1(arr, start, end):
    pivot = arr[start]
    left = start + 1
    right = end
    done = False
    while not done:
        while left <= right and arr[left] >= pivot:
            left += 1
        while left <= right and pivot >= arr[right]:
            right -= 1
        if right < left:
            done = True
        else:
            arr[left], arr[right] = arr[right], arr[left]
    arr[start], arr[right] = arr[right], arr[start]
    return right


def quick_sort_ascending(arr, start, end):
    if start < end:
        pivot = partition(arr, start, end)
        quick_sort_ascending(arr, start, pivot - 1)
        quick_sort_ascending(arr, pivot + 1, end)
    return arr


def quick_sort_descending(arr, start, end):
    if start < end:
        pivot = partition1(arr, start, end)
        quick_sort_descending(arr, start, pivot - 1)
        quick_sort_descending(arr, pivot + 1, end)
    return arr


insert = input().split(" ")
num = []

if insert[0] == "-o":
    if insert[1] == "A":
        if insert[2] == "-i":
            for i in range(3, len(insert)):
                num.append(int(insert[i]))
            quick_sort_ascending(num, 0, len(num) - 1)
            print(quick_sort_ascending(num, 0, len(num) - 1))
    elif insert[1] == "D":
        if insert[2] == "-i":
            for i in range(3, len(insert)):
                num.append(int(insert[i]))
            quick_sort_descending(num, 0, len(num) - 1)
            print(quick_sort_descending(num, 0, len(num) - 1))
else:
    print("잘못 입력하셨습니다")