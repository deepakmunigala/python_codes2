s = 'I am Sam'

print('Sam' in s)
# True

print('sam' in s)
# False

print('I' in s and 'Sam' in s)
# True

s = 'I am Sam'

print(s.find('Sam'))
# 5

print(s.find('XXX'))
# -1

print(s.find('am'))
# 2

print(s.find('am', 3))
# 6

print(s.find('am', 3, 5))
# -1

print(s.rfind('am'))
# 6

print(s.rfind('XXX'))
# -1

print(s.rfind('am', 2))
# 6

print(s.rfind('am', 2, 5))
# 2

print(s.index('am'))
# 2

# print(s.index('XXX'))
# ValueError: substring not found

print(s.rindex('am'))
# 6

# print(s.rindex('XXX'))
# ValueError: substring not found

s = 'I am Sam'

print(s.upper())
# I AM SAM

print(s.lower())
# i am sam

print('sam' in s)
# False

print('sam' in s.lower())
# True

print(s.find('sam'))
# -1

print(s.lower().find('sam'))
# 5

s = '私はSam'

print(s.lower())
# 私はsam

print(s.upper())
# 私はSAM
