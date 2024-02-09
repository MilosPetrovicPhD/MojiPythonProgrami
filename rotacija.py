print("Hello, Milos");
import PyPDF2, os
# Get all the PDF filenames.
pdfFiles = []
for filename in os.listdir('.'):
    if filename.endswith('.pdf'):
        pdfFiles.append(filename)
pdfFiles.sort(key = str.lower)

# Loop through all the PDF files.
for filename in pdfFiles:
    pdfFileObj = open(filename, 'rb')
    pdfReader = PyPDF2.PdfReader(pdfFileObj)
    pdfWriter = PyPDF2.PdfWriter()
    # Loop through all the pages (except the first) and add them.
    for pageNum in range(0, len(pdfReader.pages)):
        pageObj = pdfReader.pages[pageNum]
        pageObj.rotate(360)
        pdfWriter.add_page(pageObj)
        imeFajla = str(filename) + '.pdf'
        pdfOutput = open(imeFajla, 'wb')
        pdfWriter.write(pdfOutput)
        pdfOutput.close()

# Save the resulting PDF to a file.
#pdfOutput = open('p.pdf', 'wb')