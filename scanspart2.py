from PIL import Image
import os
from func import parentdir,removepage,copypdfs,rename
imlist= []
c = 0
pwd = "C:/Users/aj/Pictures/scans"
sfx = ""
sfx = input("Enter suffix: ")
os.chdir(pwd)
for i in os.listdir():
#   print(i)
    os.chdir(i)
    for j in os.listdir():
        print(j)
        f = os.path.splitext(j)
        if f[1] != ".pdf":
            c +=1
            im = Image.open(j).convert('RGB')
            imlist.append(im)
        else:
            os.remove(j)
    pdfname = os.getcwd() + "\\" + str(i) + ".pdf"
    print(i)
    if c!=0:
        im.save(pdfname, "PDF" ,resolution=100.0, save_all=True, append_images= imlist)
        removepage(pdfname)
        os.remove(pdfname)
        newpdf = pdfname + ".work"
        os.rename(newpdf,pdfname)
    imlist = []
    os.chdir("..")