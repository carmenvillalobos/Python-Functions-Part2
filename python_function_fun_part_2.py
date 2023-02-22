#1
def arb_args(*arg):
    for i in arg:
        print(i)


#2
def inner_func(x,y):
  def inner_1():
    return x+y
  def inner_2():
    return x-y
  print(inner_1()+inner_2())

#3
def lunch_lady(name, lunch="Mystery Meat"):
  print(name, lunch)

# Alternative solution
# def lunch_lady(student_name, lunch_preference):
#     if len(lunch_preference) == 0:
#         print(student_name, "Mystery Meat")
#     else:
#         print(student_name, lunch_preference)

#4
def sum_n_product(int1,int2):
    sum = int1 + int2
    product = int1 * int2
    return sum, product

# Alternative solution
# def sum_n_product(x,y):
#   return x+y,x*y

#5
alias_arb_args = arb_args

#6
def arb_mean(*args):
  total = 0
  for a in args:
    total += a
  print(a/len(args))

# arb_mean(1,2,3) ??

#7
def arb_longest_string(*args):
  long = 0
  longest = ""
  for i in args:
    if len(i) > long:
      long = len(i)
      longest = i
  return longest