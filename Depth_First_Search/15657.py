n, m = map(int, input().split())
nums = list(map(int, input().split()))

nums.sort()

sequence = []

def dfs(start):
    if len(sequence) == m:
        print(" ".join(map(str, sequence)))
        return
    
    for i in range(start, n):
        sequence.append(nums[i])
        dfs(i)
        sequence.pop()

dfs(0)
