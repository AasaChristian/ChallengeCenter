def matchingStrings(strings, queries):
    # create a list of zero's the same length as queries list
    quelen = len(queries)
    ans = [0] * quelen
    # loop thru strings
    for s in strings:
        # inside string loops loop thru queries 
        # if the current queries matches the current string, increase ans array with the same index by 1
        for i in range(len(queries)):
            if queries[i] == s:
                ans[i] += 1
    return ans

print(matchingStrings(["sad","sad", "lad", "ed", "lad", "mad"],["lad", "ed", "mad", "mad"]))