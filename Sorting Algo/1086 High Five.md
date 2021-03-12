```
class Solution:
    def highFive(self, items: List[List[int]]) -> List[List[int]]:
        items.sort(key=lambda items:[items[0],items[1]],reverse=True)
        res = []
        dic = {}
        for item in items:
            if item[0] in dic:
                if dic[item[0]] < 5:
                    dic[item[0]] = dic[item[0]] + 1
                    res[-1][1] += item[1]
            else:
                dic[item[0]] =  1
                res.append(item)
        for i in range(len(res)): res[i][1] = res[i][1]//5
        res.reverse()
        return res
```
