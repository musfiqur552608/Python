
str_data = "Hello Everyone!!, 12345 $$// 'anything' \"no\""

# output
print(str_data)
print(len(str_data))


x = 5
y = "5"

# if here we put print(x+y) we get an error, because x is not string. If it is not string we can't concat a integer with a string
print(str(x) + y) #55