def binary_search(input_array, value):
    l = len(input_array)
    high = int(l)
    low = int(0)
    mid = int(l / 2)

    for i in range(l):
    	if(input_array[mid] < value):
    		low = int(mid)
    		mid = int((low+high) / 2)
    		continue
    	elif(input_array[mid] > value):
    		high = int(mid)
    		mid = int((low+high) / 2)
    		continue
    	elif(input_array[mid] == value):
    		return mid+1
    return -1

test_list = [1,3,9,11,15,19,29]
test_val1 = 25
test_val2 = 15
print(binary_search(test_list, test_val1))
print(binary_search(test_list, test_val2))