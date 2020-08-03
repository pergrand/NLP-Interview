# -*- coding: utf-8 -*-
class Solution:
    def minimumTotal(self, triangle):
        n = len(triangle)
        f = [[0] * n for _ in range(n)]
        print(f)
        f[0][0] = triangle[0][0]

        for i in range(1, n):
            f[i][0] = f[i - 1][0] + triangle[i][0]
            for j in range(1, i):
                f[i][j] = min(f[i - 1][j - 1], f[i - 1][j]) + triangle[i][j]
            f[i][i] = f[i - 1][i - 1] + triangle[i][i]
        print(f)

        return min(f[n - 1])




solution = Solution()
inputs = [[2],[3,4],[6,5,7],[4,1,8,3]]
res = solution.minimumTotal(inputs)

print(res)


class Solution2:
    def minimumTotal(self, triangle) :
        n = len(triangle)
        f = [0] * n
        f[0] = triangle[0][0]

        for i in range(1, n):
            f[i] = f[i - 1] + triangle[i][i]
            for j in range(i - 1, 0, -1):
                f[j] = min(f[j - 1], f[j]) + triangle[i][j]
            f[0] += triangle[i][0]

        print(f)

        return min(f)

solution2 = Solution2()
inputs = [[2],[3,4],[6,5,7],[4,1,8,3]]
res = solution2.minimumTotal(inputs)

print(res)



class Solution3:
    def minPoint(self,triangel,i,j):
        if i == len(triangel)-1:       #最底层，递归基
            return triangel[i][j]
        else:
            return triangel[i][j] + min(self.minPoint(triangel,i+1,j),self.minPoint(triangel,i+1,j+1))    #顶点值 he #子问题的较小者

    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        return self.minPoint(triangle,0,0)

solution3=Solution3()

res = solution3.minimumTotal(inputs)

print(res)