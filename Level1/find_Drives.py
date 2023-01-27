import os
class SystemDiverFinder:
    def __init__(self):
        pass
    def find_drivers(self):
        print("This is the find drivers method of System Driver Finder Class")

        drives=[]
        for x in range(65,91):
            if os.path.exists(chr(x)+ ":"):
                drives.append(chr(x))

        return drives

'''
if __name__=='__main__':
    obj=SystemDiverFinder()
    print(obj.find_drivers())
    '''
