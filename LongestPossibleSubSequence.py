'''
LCS Problem Statement: Given two sequences, find the length of longest subsequence present in both of them. 
A subsequence is a sequence that appears in the same relative order, but not necessarily contiguous. 
For example, “abc”, “abg”, “bdf”, “aeg”, ‘”acefg”, .. etc are subsequences of “abcdefg”. 
So a string of length n has 2^n different possible subsequences.

Examples:
LCS for input Sequences “ABCDGH” and “AEDFHR” is “ADH” of length 3.
LCS for input Sequences “AGGTAB” and “GXTXAYB” is “GTAB” of length 4.

Algorithm:
dp[i][j]= dp[i-1][j-1] + 1, if string1[i] == string2[j]
          max(dp[i-1][j], dp[i][j-1]) , else  
'''
dp = None

#Display the dp[][] array
def displayDp():
    global dp
    for i in dp:
        for j in i:
            print(j,end="\t")
        print()
        
#Create a dp[][] and returns the length of the longest possible sub-sequence
def generateDp(string1, string2):
    global dp
    dp = [[0]*(len(string2)+1) for i in range(len(string1)+1)]
    for i in range(1,len(string1)+1):
        for j in range(1,len(string2)+1):
            if(string1[i-1] == string2[j-1]):
                dp[i][j] = dp[i-1][j-1] + 1
            else:
                dp[i][j] = max([dp[i-1][j],dp[i][j-1]])
    return dp[-1][-1]
                  
string1 = "AGGTAB"
string2 = "GXTXAYB"
print(generateDp(string1, string2))
