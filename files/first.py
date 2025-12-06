def read(file_path):
    f = open(file_path,)
    lines=f.readlines()
    for i in range(len(f)):
        print(f"{f[i]}\n")
    f.close()
    return lines
def write(file_path, lines):
    w = open(file_path,)
    for i in range(len(lines)):
        if(i % 2==1):
            w.write(lines[i])
    w.close()

file_path = "files/textfile1.txt"
write("files/textfile2.txt", read(file_path))
