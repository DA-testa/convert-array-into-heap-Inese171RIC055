# python3

def sift_down(i, n, data, swaps):
    min_idx = i
    left_child = 2 * i + 1
    right_child = 2 * i + 2
    
    if left_child < n and data[left_child] < data[min_idx]:
        min_idx = left_child
    if right_child < n and data[right_child] < data[min_idx]:
        min_idx = right_child
        
    if i != min_idx:
        data[i], data[min_idx] = data[min_idx], data[i]
        swaps.append((i, min_idx))
        sift_down(min_idx, n, data, swaps)

def build_heap(data):
    n = len(data)
    swaps = []
    # TODO: Creat heap and heap sort
    # try to achieve  O(n) and not O(n2)

    for i in range(n//2, -1, -1):
        sift_down(i, n, data, swaps)

    return swaps


def main():
    
    # TODO : add input and corresponding checks
    # add another input for I or F 
    # first two tests are from keyboard, third test is from a file


    # input from keyboard
    n = int(input())
    data = list(map(int, input().split()))

    # checks if lenght of data is the same as the said lenght
    assert len(data) == n

    # calls function to assess the data 
    # and give back all swaps
    swaps = build_heap(data)

    # TODO: output how many swaps were made, 
    # this number should be less than 4n (less than 4*len(data))


    # output all swaps
    print(len(swaps))
    for i, j in swaps:
        print(i, j)


if __name__ == "__main__":
    choice = input("") 
    print(choice)
    if choice == 'F': 
        filename = input('') 
        with open(filename) as file: 
            for line in file: 
                print(find_mismatch(line.strip())) 
    elif choice == 'I': 
        main()