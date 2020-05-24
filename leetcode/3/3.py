class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        i = 0
        x = dict()
        max_length = 0
        l = 0
        while i < len(s):
            if s[i] in x:
                # print(s[i-l:i])
                max_length = l if max_length < l else max_length
                l = 0
                # print('new l = ' + str(l) + ' max = ' + str(max_length))
                i = x[s[i]]
                x.clear()
            else:
                x[s[i]] = i
                l += 1
                # print('put ' + s[i] + ' = ' + str(i) + ' l = ' + str(l))
            i += 1
        max_length = l if max_length < l else max_length
        return max_length

    def lengthOfLongestSubstring2(self, s: str) -> int:
        if s == '':
            return 0
        if len(s) == 1:
            return 1

        def find_left(st, i):
            tmp_str = st[i]
            j = i - 1
            while j >= 0 and st[j] not in tmp_str:
                tmp_str += st[j]
                j -= 1
            return len(tmp_str)
        length = 0
        for i in range(0, len(s)):
            length = max(length, find_left(s, i))
        return length

    def lengthOfLongestSubstring3(self, s: str) -> int:
        res = 0
        mark = set()  # 用集合标明是否有出现重复字母
        r = 0  # 右指针
        for i in range(len(s)):
            if i != 0:
                mark.remove(s[i - 1])
            while r < len(s) and s[r] not in mark:  # 如果不满足条件说明r走到了s的尽头或r指向的元素
                mark.add(s[r])  # 将当前r指向的字母加入集合
                r += 1
            res = max(res, r - i)  # 在每一个位置更新最大值
        return res


if __name__ == "__main__":
    s = Solution()
    print(s.lengthOfLongestSubstring2('abababc'))
