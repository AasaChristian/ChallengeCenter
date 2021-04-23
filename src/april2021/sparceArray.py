# this code challenge was completed in SA2.py
def matchingStrings(strings, queries):
    print(queries, "queries")
    print(strings, "strings")
    # create a list of zero's the same length as queries list
    quelen = len(queries)
    ans = [0] * quelen
    print(ans, "ans")
    # loop thru strings
    for s in strings:
        # inside string loops loop thru queries 
        # if the current queries matches the current string, increase ans array with the same index by 1
        for i in range(len(queries)):
            if queries[i] == s:
                ans[i] += 1
    return ans

