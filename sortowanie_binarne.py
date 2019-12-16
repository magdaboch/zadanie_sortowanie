start_list = [0, 1, 2, 3, 4, 5]
value_x = 3
def algorytm_binarny(start_list, value_x):
    left = 0
    right = len(start_list)
    while left <= right:
        mid = int((left + right)/2)
        if start_list[mid] == value_x:
            return mid
        elif start_list[mid] < value_x:
            left = mid + 1
        else:
            right = mid - 1

def algorytm_binarny_rekursywnie(start_list, left=0, right=len(start_list)-1, value_x=value_x):
    #left = 0
    #right = len(start_list)-1
    if right > left:
        mid = int((left + right) / 2)
        if start_list[mid] == value_x:
            return mid
        elif start_list[mid] < value_x:
            algorytm_binarny_rekursywnie(start_list, mid+1, right, value_x)
        else:
            algorytm_binarny_rekursywnie(start_list, left, mid -1, value_x)


def algorytm_liniowy(start_list, value_x):
    for i in start_list:
        if i == value_x:
            return start_list[i]

if __name__ == '__main__':
    start_list = [0, 1, 2, 3, 4, 5]
    value_x = 3
    print(algorytm_binarny(start_list, value_x))
    print(algorytm_liniowy(start_list, value_x))
    print(algorytm_binarny_rekursywnie(start_list, left, right, value_x))
