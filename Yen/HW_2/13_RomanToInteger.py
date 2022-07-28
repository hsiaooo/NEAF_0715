class Solution:
    def romanToInt(self, s: str) -> int:

        # 建立 dict
        rom_dict = {"M": 1000, "D": 500, "C": 100, "L": 50, "X": 10, "V": 5, "I": 1}
        rom2_dict = {"CM": 900, "CD": 400, "XC": 90, "XL": 40, "IX": 9, "IV": 4}

        summ = int()
        
        # 如果在 s 中有 rom2_dict 的 key，加總它的相對數值，然後在 s 中清除
        for rom in list(rom2_dict.keys()):
            if rom in s:
                summ += int(rom2_dict[rom])
                s = s.replace(rom, "")
        # 加總 s 中的對應數值
        for ss in s:
            summ += rom_dict.get(ss)

        return summ

s13 = Solution()
a = s13.romanToInt("MCMXCIV")
print(a)