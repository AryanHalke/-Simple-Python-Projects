import PyPDF2


pdfiles = ["TASK11.pdf", "TASK12.pdf"]
merge = PyPDF2.PdfMerger()
for filename in pdfiles:
    pdfFile = open(filename, 'rb')
    pdfReader = PyPDF2.PdfReader(pdfFile)
    merge.append(pdfReader)
pdfFile.close()
merge.write('merged.pdf')
