a = 'C:\development\inside\est-project_management\inside\myfile.txt'
x = a.lstrip('C:\development\inside\est-project_management\inside\ ').rstrip('.txt')
print(a.split('\\')[-1].split('.')[0])

