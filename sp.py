# -*- coding: utf-8 -*-
"""
Created on Tue Sep 27 11:11:10 2016

@author: lty765
"""
'''
need to add:
tranform to a single list
searching of a certain type of file 
'''
#Seek all files in a certain directory
#nta:file name
def fileseek(addr):
    import os
    try:
        os.chdir(addr) 
        temp = []
        for file in os.listdir(addr):
            if os.path.isdir(file):
                newfile = os.path.join(os.getcwd(),file)
                temp.append(fileseek(newfile))
                os.chdir('..')
            else:          
                temp.append(file)
        return temp
    except:
        return  []
    
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
#currently not use,spending too much time!
def diskseek():
    hard_disk = disk()
    temp = []
    for item in hard_disk:
        if item != 'C:':
            temp.append(fileseek(item+'\\'))
    return temp


#done 
def test(choose_disk='H:'):
    disk_now = disk()
    if choose_disk in disk_now:        
        import time
        start = time.time()
        fileseek(choose_disk+'\\')
        end = time.time()
        cost = end - start
        print(cost)
    else:
        print('Disk doesn\'t exist,please try another disk.')
    
    
    
    
    
    
    
    
   
