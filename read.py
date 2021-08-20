file1 = open('hehe11', 'r')
Lines = file1.readlines()


file2 = open('out111', 'w')
  
count = 0
# Strips the newline character
for line in Lines:
    print(file2.tell())
    count += 1
    splitline=line.split("/")
    file2.write("{} {} \n".format("\\rm -rf ",splitline[2].strip()))
    print(file2.tell())

file1.close()
file2.close()
