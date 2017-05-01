import os
import shutil


cur_dir = os.getcwd()


#Move all the docx files
docx = [x for x in os.listdir(cur_dir) if os.path.splitext(x)[1]  in ('.docx','.doc')]
docx_dir = cur_dir + '\\docs'

if len(docx) > 0:
	try:
		os.makedirs(docx_dir)
	except OSError as e:
		if not os.path.isdir(docx_dir):
			raise
	for i in docx:
		shutil.move(cur_dir + '\\' + i,docx_dir)

#Move all the pdf files
pdf = []
pdf_dir = cur_dir + '\\pdfs'
for x in os.listdir(cur_dir):
	if not os.path.isdir(x):
		if os.path.splitext(x)[1] in ('.pdf'):
			pdf.append(x)

if len(pdf) > 0:
	try:
		os.makedirs(pdf_dir)
	except OSError as e:
		if not os.path.isdir(pdf_dir):
			raise
	for i in pdf:
		shutil.move(cur_dir + '\\' + i,pdf_dir)

#Move all the ppt files
ppt = [x for x in os.listdir(cur_dir) if os.path.splitext(x)[1]  in ('.pptx','.ppt')]
ppt_dir = cur_dir + '\\ppts'

if len(ppt) > 0:
	try:
		os.makedirs(ppt_dir)
	except OSError as e:
		if not os.path.isdir(ppt_dir):
			raise
	for i in ppt:
		shutil.move(cur_dir + '\\' + i,ppt_dir)


#Move all the image files
img = [x for x in os.listdir(cur_dir) if os.path.splitext(x)[1]  in ('.jpg','.png','.jpeg','.JPG')]
img_dir = cur_dir + '\\images'

if len(img) > 0:
	try:
		os.makedirs(img_dir)
	except OSError as e:
		if not os.path.isdir(img_dir):
			raise
	for i in img:
		shutil.move(cur_dir + '\\' + i,img_dir)

xls = [x for x in os.listdir(cur_dir) if os.path.splitext(x)[1] in ('.xls','.xlsx')]
xls_dir = cur_dir + '\\xls'

if len(xls) > 0:
	try:
		os.makedirs(xls_dir)
	except OSError as e:
		if not os.path.isdir(xls_dir):
			raise
	for i in xls:
		shutil.move(cur_dir + '\\' + i,xls_dir)

mp3 = [x for x in os.listdir(cur_dir) if os.path.splitext(x)[1] in ('.mp3','.avi','.mp4')]
mp3_dir = cur_dir + '\\mp3'

if len(mp3) > 0:
	try:
		os.makedirs(mp3_dir)
	except OSError as e:
		if not os.path.isdir(mp3_dir):
			raise
	for i in mp3:
		shutil.move(cur_dir + '\\' + i,mp3_dir)

# You can add more extensions here if you want.

print 'Docx found -', len(docx)
print 'Pdfs found -',len(pdf)
print 'Ppt found -',len(ppt)
print 'Images found -',len(img)
print 'Excel files found - ', len(xls)
print 'Songs found - ', len(mp3)