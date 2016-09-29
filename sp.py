# -*- coding: utf-8 -*-
"""
Created on Tue Sep 27 11:11:10 2016

@author: lty765
"""

#Seek all files in a certain directory
#nta:file name
def fileseek(addr):
    import os
    os.chdir(addr)
    temp = []
    for file in os.listdir(addr):
      if file!='$RECYCLE.BIN' and file!='System Volume Information' and file!='Config.Msi':
        if os.path.isdir(file):
            newfile = os.path.join(os.getcwd(),file)
            temp.append(fileseek(newfile))
            os.chdir('..')
        else:          
            temp.append(file)
    return temp
    
#print(fileseek('H:\\python'))


#Get the partition of the harddisk
def disk(): 
    import wmi
    c = wmi.WMI ()    
    d = []
    for physical_disk in c.Win32_DiskDrive (): 
        for partition in physical_disk.associators ("Win32_DiskDriveToDiskPartition"): 
            for logical_disk in partition.associators ("Win32_LogicalDiskToPartition"):                 
                 d.append(logical_disk.Caption)
    return d
   
#print(disk())

#nta:disk name
def diskseek():
    hard_disk = disk()
    temp = []
    for item in hard_disk:
        temp.append(fileseek(item))
    return temp
  
def test():
    import time
    start = time.time()
    fileseek('G:\\')
    end = time.time()
    cost = end - start
    print(cost)
    
    
    
    
    
    
    
    
   
