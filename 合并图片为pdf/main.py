import os
from PIL import Image
from reportlab.lib.pagesizes import portrait
from reportlab.pdfgen import canvas
from PyPDF2 import PdfFileMerger

def get_files(path, param=".pdf"):
	files = os.listdir(path)
	files = [path + "/" + f for f in files if f.endswith(param)]
	return files


def img_to_pdf(dataPath, picFile):
	
	(width, height) = Image.open(picFile).size
	pdfFile = dataPath + "/" + picFile.split("/")[-1].split(".")[0] + ".pdf"
	pdf = canvas.Canvas(pdfFile, pagesize = portrait((width, height)))
	pdf.drawImage(picFile, 0, 0, width, height)
	pdf.save()

def merge_pdf(dataPath):
	outPath = dataPath
	pdfList = get_files(dataPath, ".pdf")
	if pdfList:
		merger = PdfFileMerger()
		for pdf in pdfList:
			merger.append(pdf,
						  bookmark = pdf.split("/")[-1].split(".")[0],
                          import_bookmarks = False)
		merger.write(dataPath.split("/")[-1] + ".pdf")

if __name__ == "__main__":
	root_files = os.listdir(os.getcwd())
	paths = list()
	for root_file in root_files:
		if os.path.isdir(root_file):
			paths.append(root_file)
	for path in paths:
		print(path)
		files = get_files(path, ".jpg")
		for file in files:
			img_to_pdf(path, file)
		merge_pdf(path)