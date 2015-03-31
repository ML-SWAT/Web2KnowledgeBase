import os
import shutil
def rename(directory):
    homedir=os.getcwd()
    path=homedir
    path=homedir+'/'+directory
    file_name=os.listdir(path)
    print path
    j=1
    for i in range(len(file_name)):
        if file_name[i][:5]=='untag':
        	os.rename(path+'/'+file_name[i],path+'/'+str(j))
        	j=j+1
if __name__=='__main__':
    #rename('course_train')
    rename('non_course_test')
    rename('non_course_train')
    rename('course_test')
