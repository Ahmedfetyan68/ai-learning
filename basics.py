mylist = [1,2,3,4,54,2,31,4,53,3,4,4]
def list_stats(numlist): 
    average = sum(int(x) for x in numlist) / len(numlist)
    Max=max(numlist)
    Sum=sum(numlist)
    print("Average:", average)
    print("Max:", Max)
    print("Sum:", Sum)

    for i in range(len(numlist)-1 , -1, -1):
        if numlist[i]%2 ==0:
            print("Removing index", i, "value", numlist[i])
            numlist.pop(i)

list_stats(mylist) 
    