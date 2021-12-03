# Make a calculator using Python with addition , subtraction ,
# multiplication ,division and power.


print("Calculator")

val1 = int(input("Enter Your First Value :"))
val2 = int(input("Enter Your Second Value :"))
opr = input("Enter Your Operator :")
if opr == '+':
    print(val1 + val2)
elif opr == '-':
        print(val1 - val2)
elif opr == '*':
        print(val1 * val2)
elif opr == '/':
    print(val1 / val2)
else:
    print("You Enter Wrong Value")



# 2. Write a program to check if there is any numeric value in list using for
# loop.


list = [10, 18, 20, 7, 46, 365]
print("Checking if 15 exists in list")
count = list.count(7)
if count > 0:
    print("Yes, 7 exists in list")
else:
    print("No, 7 does not exists in list")




# 3. Write a Python script to add a key to a dictionary.

dictionaries = {1:10, 2:20}

dictionaries.update({3:30})
print(dictionaries)


# 4. Write a Python program to sum all the numeric items in a dictionary.


dictionaries = {'data1':100,'data2':-54,'data3':247}
print(sum(dictionaries.values()))



# 5. Write a program to identify duplicate values from list.


def duplicate(li):
    n=len(li)
    dup=[]
    for i in range(n):
        k = i + 1
        for j in range(k,n):
            if li[i] == li[j] and li[i] not in dup:
                dup.append(li[i])
    return dup

li=[ 10, 20, 36, -1, 28, 10, 80, -1, 28, 36]
print("Duplicate: ",duplicate(li))

# 6. Write a Python script to check if a given key already exists in a dictionary

d = {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}
def key(x):
    if x in d:
        print('Key is available')
    else:
        print('Key is not here')
key(5)
key(9)