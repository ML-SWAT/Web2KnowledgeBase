import os
from untag import *
import glob
def transcribe(files, destination):
	for file_path in files:
		if os.path.isdir(file_path):
			continue
		plain_text = strip_tags(file_path)
		write_file(file_path, plain_text, destination)

if __name__=='__main__':
	folder = "webkb"
	files = glob.glob("webkb/*/*/*")
	transcribe(files,'untag_webkb')
