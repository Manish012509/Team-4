import os
import time

class FileFinder:
    def __init__(self):
        pass
    def find_file(self,filename,filepath):
        self.filename=filename
        self.filepath=filepath
        files=[]

        for root,dir,file in os.walk(filepath):
           if filename in file:
               files.append(os.path.join(root,filename))
        return files

if __name__=='__main__':
    obj=FileFinder()
    st=time.time()
    print(obj.find_file('demo.txt','C:\\'))
    ed=time.time()
    to=ed-st
    print(to)
