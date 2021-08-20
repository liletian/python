#file1 = open('hehe11', 'r')
file1 = open('out11', 'r')
Lines = file1.readlines()


file2 = open('out111', 'w')
  
count = 0
# Strips the newline character
for line in Lines:
#    print(file2.tell())
    count += 1
#    splitline=line.split("/")
    splitline=line.split(" ")
#    file2.write(splitline[0])
#    file2.write(splitline[1])
#    file2.write(splitline[2])
#    print("Line{}: {}".format(count, splitline))
#    print("{} {}".format("\\rm -rf ",splitline[2].strip()))
#    print("\rm -rf ", splitline[2].strip())
#    file2.write("{} {} \n".format("\\rm -rf ",splitline[2].strip()))
#    print(file2.tell())
count = 16
with open('out11', 'r') as fd:
    while(count>0):
        print fd.tell()
        fd.readline()
        print fd.tell()
        count=count-1

file1.close()
file2.close()
