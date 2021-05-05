file = open('animals.txt', 'r')
file_1 = open('animals_new.txt', 'w')
for i in file.readlines():
    file_1.write(i.rstrip('\n') + ' ')
file.close()
file_1.close()
