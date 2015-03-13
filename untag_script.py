import os
from untag import *
def transcribe(files,origin_dir,destiny_dir):
	for file in files:
		temp = strip_tags(file,origin_dir)
		generate_untag_file(file,temp,origin_dir,destiny_dir)
if __name__=='__main__':
	dir="/Users/JudeWang/Documents/Web2KnowledgeBase/course-cotrain-data/fulltext"
	dir_course=dir+'/course'
	dir_non_course=dir+'/non-course'
	#print dir_course,dir_non_course
	courseFiles = [ f for f in os.listdir(dir_course)  ]
	#nonCourseFiles = [ f for f in os.listdir(dir_non_course)  ]
	#print len(courseFiles)
	#print courseFiles[1]
	#print dir_course
	#print dir_course.replace("/course$","/untag_course$")
	#print dir_course[:-6]
	transcribe(courseFiles,dir_course,dir_course[:-6]+'untag_course')
	#transcribe(nonCourseFiles,dir_non_course,dir_non_course.replace("\\non_course\\","\\untag_non_course\\"))
