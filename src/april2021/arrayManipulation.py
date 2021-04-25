print("test")
def arrayManipulation(n, queries):
    # print(n, "n")
    # print(queries, "queries")
    
    # create list containing n index of 0
    ans = [0] * n
    high = -9999999999
    # loop thru queries
    for i in range(len(queries)):
        # get amount from queries i 2
        amount = queries[i][2]
        # print(amount, "amount")
        # find starting and ending index to apply amount
        start = queries[i][0] -1
        end = queries[i][1] -1
        # print(start, "start", end, "end")
        # loop thru and add amount to coorisponding index in ans
        while start <= end:
            total = ans[start] + amount
            ans[start] = total
            # if total > high:
            #     high = total
            # increase start by 1 to move index
            start += 1
    high = 0
    for n in ans:
        if n > high:
            high = n
            
    return high

    print(arrayManipulation(4, [1,3,5]))