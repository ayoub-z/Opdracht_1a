import string
import os

os.chdir(r'D:\Users 2.0\A.Z 2.0\Desktop\Start\Coding\.vscode\School\Formatieve_opdr. 1a')



with open('opdr8.txt', 'r') as f:
    lines = f.readlines()

lines = [lines.replace(' ', '') for line in lines]
with open('opdr8_copy.txt', 'w') as f:
    f.writelines(lines)


















# with open('opdr8.txt', 'r') as f:
#     for line in f:
#         CleanLine = line.strip()
#         print(CleanLine)
#         if CleanLine:
#                 print(CleanLine, end = '')
#     data = file.read()
#     data1 = re.sub(r"[\n\t\s]*", "", data)
#     print(data)
#     with open('opdr8_copy.txt', 'w') as file1:
#         file1.write(data1)
#         print(data1)










