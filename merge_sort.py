def merge(arr, lowest_index, highest_index):
    if lowest_index < highest_index:
        middle_index = int((lowest_index + highest_index) / 2)

        merge(arr, lowest_index, middle_index)
        merge(arr, middle_index + 1, highest_index)

        sort_arr(arr, lowest_index, highest_index, middle_index)


def sort_arr(arr, lowest_index, highest_index, middle_index):
    sorted_arr = [None] * len(arr)
    sorted_arr_index = lowest_index
    first_subarr_index = lowest_index
    second_subarr_index = middle_index + 1

    while first_subarr_index <= middle_index and second_subarr_index <= highest_index:
        if arr[first_subarr_index].nome <= arr[second_subarr_index].nome:
            sorted_arr[sorted_arr_index] = arr[first_subarr_index]

            first_subarr_index += 1
        else:
            sorted_arr[sorted_arr_index] = arr[second_subarr_index]

            second_subarr_index += 1

        sorted_arr_index += 1

    if first_subarr_index <= middle_index:
        for i in range(first_subarr_index, middle_index + 1):
            sorted_arr[sorted_arr_index] = arr[i]

            sorted_arr_index += 1
    elif second_subarr_index <= highest_index:
        for i in range(second_subarr_index, highest_index + 1):
            sorted_arr[sorted_arr_index] = arr[i]

            sorted_arr_index += 1

    for i in range(lowest_index, highest_index + 1):
        arr[i] = sorted_arr[i]
