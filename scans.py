from PIL import Image
import os
from func import parentdir,removepage,copypdfs,rename
imlist = []
c = 0
sfx = input("Enter suffix for pdfs: ") + "  "
osdir = "C:/Users/ajdj/Desktop/Fee/house/"
os.chdir(osdir) # cd into dir
print(os.listdir())
for i in os.listdir(): # for every directory in dir
    print(i,os.listdir())
    os.chdir(str(i)) # cd into every directory in dir
    for j in os.listdir(): # for every item in every directory in dir
        f = os.path.splitext(j) # get name of items without parent dir names e.g C:/Users --> Users
        if f[1] != ".pdf": # Check if item is pdf
            c += 1 # counter for number of items
            im = Image.open(j).convert('RGB') # get image from every item in every directory in dir 
            imlist.append(im) # add image to list
        else : 
            os.remove(j) # delete pdf if already exists
    pdfname = os.getcwd() + "\\" + str(i) + ".pdf" # generate pdf name
    print(i) # print generated name
    if c != 0: # if number of items is not 0
        im.save(pdfname, "PDF" ,resolution=100.0, save_all=True, append_images= imlist) # save pdf
        removepage(pdfname) # delete last page of pdf as its duplicate
        os.remove(pdfname) # remove old pdf with extra page
        newpdf = pdfname + ".work" # newpdf nane
        os.rename(newpdf,pdfname) # move new pdf to output position
    imlist = [] # reset item list for next dir
    os.chdir("..")


