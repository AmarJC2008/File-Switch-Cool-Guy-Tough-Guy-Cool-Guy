def swapFileData():
    fileName1 = input("Swapping the file1")
    fileName2 = input("Swapping the file2")
    with open(fileName1, 'r')as e:
     data_e = e.read()
    with open(fileName2, 'r')as ea:
     data_ea = ea.read()
    with open(fileName1, 'w')as e:
     e.write(data_ea) 
    with open(fileName2, 'w')as ea:
     ea.write(data_e)

swapFileData()   