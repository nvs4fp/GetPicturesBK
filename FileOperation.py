# To study how to operate file
if __name__=="__main__":
    fp = "finput.txt"
    f = open(fp,'w')
    f.write("This is a test file!")
    f.close()
    f = open(fp, 'r')
    print(f.read())
    f.close()