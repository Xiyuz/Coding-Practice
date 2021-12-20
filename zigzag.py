class Solution:
    def convert(self, s: str, numRows: int) -> str:
        zigzag = {}
        existence_dict = {k:[] for k in range(numRows)}
        col = 0
        count = 0
        res = ""
        stop_flag = False
        while(count < len(s)):
            if (stop_flag == False):
                for row in range(numRows):
                    zigzag[(row,col)] = s[count]
                    existence_dict[row].append(col)
                    count = count + 1
                    if count >= len(s):
                        stop_flag = True
                        break
                    print(zigzag)
                        
            if (stop_flag == False):
                for row in reversed(range(1,numRows-1)):
                    col = col + 1
                    zigzag[(row,col)] = s[count]
                    existence_dict[row].append(col)
                    count = count + 1
                    if count >= len(s):
                        stop_flag = True
                        break
            col = col + 1
        #print(zigzag)
        for row in range(numRows):
            for col in existence_dict[row]:
                res = res + zigzag[(row,col)]
        print(existence_dict)
        return res
        
    def convert2(self, input: str, rows: int) -> int:
            if rows == 1:
                return input
            else:
                lines = [''] * rows

                j = 0
                k = rows - 1
                for i in range(len(input)):
                    if j < rows:
                        lines[j] += input[i]
                        j += 1

                    if j >= rows:
                        if 1 <= k <= rows - 2:
                            lines[k] += input[i]
                        k -= 1

                    if k == 0 and j >= rows:
                        j = 0
                        k = rows - 1

                return ''.join(lines)
solution = Solution()
solution.convert2( "PAYPALISHIRING",4)       
                
                
        
            
            
                
        
        