# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# sum all the items in a list.
def listsum(l):
    sum = 0
    for i in l:
        sum = sum + i
    return sum

def listsum1(x, y):
    return x + y


#multiply all the items in a list.
def listmul(x, y):
    return x * y

#get the largest number from a list
def numLarge(lt):
    tmp = 0
    for i in lt:
        if i > tmp:
            tmp = i
        else:
            tmp = tmp
    return tmp

#get the smallest number from a list
def numSmall(lt):
    tmp = lt[0]
    for i in lt:
        if i < tmp:
            tmp = i
    return tmp

#count the number of strings where the string length is 2 or more and the first and last character are same from a given list of strings
def chklist(lt):
    chk=[]
    for i in lt:
        if len(i)>=2:
            if i[0]==i[-1]:
                chk.append(i)
        else:
            continue
    return len(chk)
def chklist1(lt):
    chk = [i for i in lt if ((len(i)>=2) & (i[0]==i[-1]))]
    return len(chk)

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

    #lt = list(map(int, input('enter the number').split()))
    lt = list(map(str, input('enter the list').split()))
    print(lt)

    # sum all the items in a list.
    #print(listsum([1, 3, 5, 7, 89]))

    import functools

    # multiply all the items in a list.
    #print('listMul= {}'.format(functools.reduce(listmul, lt)))

    #print('listsum= {}'.format(functools.reduce(listsum1, lt)))

    #print('listLarge= {}'.format(numLarge(lt)))

    #print('listSmall= {}'.format(numSmall(lt)))

    print('chklist= {}'.format(chklist1(lt)))


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
