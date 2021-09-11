# from datetime import datetime
# str = '11-28-97'
# bday = datetime.strptime(str, '%m-%d-%y')
# print(bday.year)

# diff = datetime.now() - bday
# print(diff.total_seconds())
import random 

# ls =  ['mozzilla', 'chrome', 'opera', 'explorer', 'safari', 'brave']
# while True:
#     if random.choice(ls) == 'opera':
#         print("Found opera")
#         break
#     else:
#         print("not yet")

def key(x):
    return x[1]

a = [(1, 2), (3, 1), (5, 10), (11, -3)]
a.sort(key=key)
print(a)