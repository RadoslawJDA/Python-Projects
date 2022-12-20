
def binary_search(list, search):
    start = 0
    end = len(list)
    steps = 0

    while start <= end:
        print(f'steps: {steps}  list: {list[start:end+1]}')

        steps += 1
        middle = (start + end) // 2

        if search == list[middle]:
            return middle
        elif search < list[middle]:
            end = middle - 1
        else:
            start = middle + 1

    return -1
