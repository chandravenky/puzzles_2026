class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """

        min_length = len(strs[0])
        shortest_string = strs[0]

        if len(strs)==1:
            return strs[0]

        for string in strs[1:]:
            if len(string) <min_length:
                min_length = len(string)
                shortest_string = string

        output = ""

        print(shortest_string)

        for index in range(0, len(shortest_string)):
            for string in strs:
                if string[index] == shortest_string[index]:
                    continue
                
                else:
                    return output
                
            output = output + shortest_string[index]

        return output
