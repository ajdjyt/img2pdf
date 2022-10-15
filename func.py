def parentdir(inp):
   import os
   if inp == "os":
      method = os.getcwd()
   elif inp == "file":
      method = __file__
   elif inp == "both":
      return parentdir("os"), parentdir("file")   
   else:
      return ""
   full_path = os.path.realpath(method)
   dirname = os.path.dirname(full_path)
   out = ""
   for i in range(len(dirname)):
      if str(dirname[i]) == "\\" :
         out = ""
      else :
         out += dirname[i]
   return (out)

def revpdf(inpdf):
   from PyPDF2 import PdfFileWriter, PdfFileReader
   output_pdf = PdfFileWriter()
   with open(inpdf, 'rb') as readfile:
      input_pdf = PdfFileReader(readfile)
      total_pages = input_pdf.getNumPages()
      for page in range(total_pages - 1, -1, -1):
         output_pdf.addPage(input_pdf.getPage(page))
      outpdf = inpdf + "reverse.pdf"
      with open(outpdf, "wb") as writefile:
         output_pdf.write(writefile)

def removepage(inpdf):
    from PyPDF2 import PdfFileWriter, PdfFileReader
    infile = PdfFileReader(inpdf,'rb')
    output = PdfFileWriter()
    for i in range(infile.getNumPages()):
        if i != 0:
           p = infile.getPage(i)
           output.addPage(p)
    outfile = inpdf + ".work"
    with open(outfile, 'wb') as f:
        output.write(f)

def copypdfs(indir):
   import os
   import shutil
   os.chdir(indir)
   for i in os.listdir():
      os.chdir(i)
      for j in os.listdir():
         f = os.path.splitext(j)
         if f[1] == ".pdf":
            print(j)
            shutil.copy(j,"../")
      os.chdir("..")

def rename(indir,prepend,postpend):
   import os
   os.chdir(indir)
   for i in os.listdir():
      if os.path.splitext(i)[1] == ".pdf":
         new = str(prepend) + str(i) + str(postpend)
         print(new)
         os.rename(i,new)