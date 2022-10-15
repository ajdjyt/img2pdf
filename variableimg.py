from PIL import Image
import os
import shutil
from func import parentdir,removepage,copypdfs,rename
imlist = []
c = 0
#indir=input("Enter directory in documents: ")
#sfx=input("give a suffix: ")
sfx=""
osdir="C:\\Users\\ajdj\\Documents\\Pratibha\\docs\\consent" #+ str(indir)
os.chdir(osdir)
for i in os.listdir():
    f=os.path.splitext(i)
    if f[1]!=".pdf":
        c+=1
        im = Image.open(i).convert("RGB")
        imlist.append(im)
    pdfname = os.getcwd() + "\\" + str(i) + ".pdf"
    print(i)
if c != 0:
    im.save(pdfname, "PDF" ,resolution=100.0, save_all=True, append_images=imlist)
    removepage(pdfname)
    os.remove(pdfname)
    newpdf = pdfname + ".work"
    os.rename(newpdf,pdfname)
imlist = []
os.chdir("..")