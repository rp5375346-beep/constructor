# f=lambda a,b: a+b
# print(f(10,20))
# #create a lambda fun which finds max num from two nums
# f2=lambda num1,num2: num1 if num1>num2 else num2
# print(f2(45,78))
#find num even odd
# f3=lambda num1: num1 if num1%2==0: print(even) else : print(odd)
# print(f3(45))
# f3 = lambda num1: "even" if num1 % 2 == 0 else "odd"
# print(f3(45))
# l=[1,2,3,4,5,6,7,8,9]
# square_list=list(map(lambda num:num**2,l))
# print("original list",l)
# print("squared list",square_list)
# l=[1,2,3,4,5,5,6,7]
# filter_list=(list(filter(lambda num:num%2==0,l)))
# print("original list" ,l)
# print("filter list",filter_list)

# name = ["Raj", "pavan", "nayan", "rahul"]
# upper_list = list(map(lambda x: x.upper(), name))
# print("upper list:", upper_list)
# db = [("raj", 89), ("pavan", 67),("nayan" ,58)]

# filter_list = list(filter(lambda stu: stu[1] < 75, db))

# print("filter list:", filter_list)
#filter even num and create its squared list
l = [1, 2, 3, 4, 5, 6]

squared_list = list(map(lambda num: num**2, filter(lambda num: num % 2 == 0, l)))

print("Filtered and squared list:", squared_list)
