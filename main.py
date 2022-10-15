from PIL import Image
import os
import shutil
from func import parentdir,removepage,copypdfs,rename
imlist = []
c = 0
indir = "Boruto Naruto Next Generations"
indir = input("Enter directory name: ")
sfx = input("Enter suffix for pdfs: ") + "  "
osdir = "~/Anime/Mangas/" + str(indir)
os.chdir(osdir)
for i in os.listdir():
    if os.path.splitext(i)[1] == ".pdf":
        os.remove(i)
for i in os.listdir():
    os.chdir(i)
    for j in os.listdir():
        f = os.path.splitext(j)
        if f[1] != ".pdf":
            c += 1
            im = Image.open(j).convert('RGB')
            imlist.append(im)
        else : 
            os.remove(j)
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
#copydir= "~/Anime/Mangas/" + indir
#copypdfs(copydir)
#rendir="~/Anime/Mangas/" + indir
#rename(rendir,sfx,"")
