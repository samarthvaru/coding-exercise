class Solution:

  def maxSubarrayLength(self, s: List[int], k: int) -> int:
    count = {}

    l = 0
    res = 0
    for r in range(len(s)):
      count[s[r]] = 1 + count.get(s[r], 0)
      while count[s[r]] > k:
        count[s[l]] -= 1
        l += 1

      res = max(res, r - l + 1)

    return res
