# bonus 10

# try:
#     width = float(input('width: '))
#     length = float(input('length: '))
#
#     if width == length:
#         exit('That looks like a square') # break and give message
#     area = width * length
#
#     print(area)
#
# except ValueError:
#     print('Enter a number') # we dont give continue because its not in a loop


# --------------

# bonus 11

def get_average():
    print('code snippet - 1')
    with open('files/data.txt' , 'r') as file:
        data = file.readlines()

    values = data[1:]
    values = [float(i) for i in values]

    avg = sum(values) / len(values)
    return avg


average = get_average()
print(average)

# --------------
def get_average():
    print('code snippet - 2')
    with open('files/data.txt' , 'r') as file:
        data = file.readlines()
        values = data[1:]
        values = [float(i) for i in values]

    avg = sum(values) / len(values)
    return avg


average = get_average()
print(average)
