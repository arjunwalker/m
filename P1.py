import csv

with open('T1.csv', 'r') as f:
    reader = csv.reader(f)
    your_list = list(reader)

print(your_list)

h = [['0', '0', '0', '0', '0', '0']]

for i in your_list:
    #print(i)
    if i[-1] == "TRUE":
        print("YES")
        j = 0
        for x in i:
            if x != "TRUE":
                #print(x)
                if x != h[0][j] and h[0][j] == '0':
                    print(x)
                    h[0][j] = x
                elif x != h[0][j] and h[0][j] != '0':
                    h[0][j] = '?'
                else:
                    print("Do not do anything")




            j = j + 1

print(h)
