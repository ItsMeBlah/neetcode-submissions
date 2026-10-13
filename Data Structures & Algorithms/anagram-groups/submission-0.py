class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        if len(strs) < 2:
            return [strs]

        str_dict = {}

        for single_str in strs:
            sorted_string = "".join(sorted(single_str))
            
            # check if exist or not 
            if str_dict.get(sorted_string, 0) == 0:
                str_dict[sorted_string] = []
                str_dict[sorted_string].append(single_str)
            else:
                str_dict[sorted_string].append(single_str)

        return list(str_dict.values())
