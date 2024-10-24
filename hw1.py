from typing import List, Tuple

def getResult(queries: List[Tuple[str, int]]):
    # 宣告一個二維變數 alphabet，並調整符號與字母的關係
    alphabet: List[List[chr]] = [
        ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')'],  # 第一行符號
        ['Q', 'W', 'E', 'R', 'T', 'Y', 'U', 'I', 'O', 'P'],  # 第二行字母
        ['A', 'S', 'D', 'F', 'G', 'H', 'J', 'K', 'L'],        # 第三行字母
        ['Z', 'X', 'C', 'V', 'B', 'N', 'M']                   # 第四行字母
    ]
    
    results = []
    
    for s, k in queries:
        found = False
        for i in range(len(alphabet)):
            if s in alphabet[i]:
                j = alphabet[i].index(s)
                found = True
                
                if k == 1: #上
                    results.append(alphabet[i - 1][j] if i > 0 else alphabet[-1][j])
                        
                elif k == 2: # 下
                    results.append(alphabet[i + 1][j] if i < len(alphabet) - 1 else alphabet[0][j])
                        
                elif k == 3: # 右
                    results.append(alphabet[i][j + 1] if j < len(alphabet[i]) - 1 else alphabet[i][0])
                        
                elif k == 4: # 左
                    results.append(alphabet[i][j - 1] if j > 0 else alphabet[i][-1])
                break
                
        if not found:
            results.append('-1')
    
    return results

# 輸入範例
test_N = 3
test_queries = [('S', 1), ('B', 3), ('!', 1)]
output = getResult(test_queries)

for item in output:
    print(item)