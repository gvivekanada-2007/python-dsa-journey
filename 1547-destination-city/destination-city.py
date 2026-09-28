class Solution:
    def destCity(self, paths: list[list[str]]) -> str:
        for i in range(len(paths)):
            destination=paths[i][1]
            found = False
            for j in range(len(paths)):
                if destination==paths[j][0]:
                    found = True
                    break
            if found==False:
                return destination
