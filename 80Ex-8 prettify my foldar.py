#Oh soldier prettify my folder

#Path, dictionary file , formate
# like
# def soldier("C://","Bappy.txt","jpg")

import os
def soldier(path,file,format):
    os.chdir(path)
    i = 1
    files = os.listdir(path)
    # print(files)
    with open(file) as f:
        filelist = f.read().split("\n")
        # print(filelist)

    for file in files:
        # print(file)
        if file not in filelist:
            os.rename(file,file.capitalize())


        if os.path.splitext(file)[1] == format:
            os.rename(file,f"{i}{format}")
            i+=1


# soldier(r"C:\Users\ACT\Desktop\testing",
#         r"C:/Users/ACT/PycharmProjects/MyPrograms/ext.txt",".jpg")

if __name__ == '__main__':
    a = input("Path:")
    b = input("File:")
    c = input("Format:")
    soldier(a,b,c)
    print("Done!!")



