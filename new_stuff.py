
if __name__ == "__main__":
    """
    for i in range(1,10):
        if i in [5, 6, 7]:
            continue
        print('CHEESE', i)
    """
    # a_list = [1,2,3,4,5,6,7,8,9,10]
    # a_list = list(range(1,11))
    """
    
    for i in range(10, 101):
        if i%10 != 0: 
            continue
        else:
            a_list.append(i)
    """
    a_list = []
    for i in range(10, 110, 10):
        a_list.append(i)


    print(a_list)