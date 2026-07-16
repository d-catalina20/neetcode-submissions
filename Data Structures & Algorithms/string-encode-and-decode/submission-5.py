class Solution:

    def encode(self, strs: List[str]) -> str:
        if strs == []:
            return "#$#"
        rez = []
        for s in strs:
            if s == "":
                rez.append("*%")
            else:
                rez.append(s)
        separator = "$#$"
        enc = separator.join(rez)
        print(enc)
        return enc

    def decode(self, s: str) -> List[str]:
        if s == "#$#":
            return []
        l = s.split("$#$")
        rez = []
        for elem in l:
            if elem == "*%":
                rez.append("")
            else:
                rez.append(elem)
        return rez

