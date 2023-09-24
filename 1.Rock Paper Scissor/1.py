import re
x = 'Thisis123string###'
y = re.search("(?<=123)\w+",x)
y = str(y[0]) + '###'
print(y)