# -*- coding: utf-8 -*-
"""removeBackupFile.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1BGr0BdJAaVppNm3mcJJmyDCC79-W76tF
"""

import ftplib
from pathlib import Path
import urllib

import glob
import shutil

def dir_exis(server,pat):
    # path="backup/jp_bkp/bkp"    
    x = pat.split('/')
    print(x)
    y=[]
    dir=[]
    for i in x:
       if i=='':
          continue
       print(i)
      #  unwanted_num = {'.','..'}
 
      #  list1 = [ele for ele in list1 if ele not in unwanted_num]
       y.append(i)
      #  print(y)
       if i=='backup':
         var="/"
       
       elif i==y[1]: 
         var="/backup"+'/'+y[1]  
       elif i==y[2]: 
        var="/backup"+'/'+y[1]+'/'+y[2] 
       elif i==y[3]: 
        var="/backup"+'/'+y[1]+'/'+y[2]+'/'+y[3]
       elif i==y[4]: 
        var="/backup"+'/'+y[1]+'/'+y[2]+'/'+y[3]+'/'+y[4]
       elif i==y[5]: 
        var="/backup"+'/'+y[1]+'/'+y[2]+'/'+y[3]+'/'+y[4]+'/'+y[5] 
       elif i==y[6]: 
        var="/backup"+'/'+y[1]+'/'+y[2]+'/'+y[3]+'/'+y[4]+'/'+y[5]+'/'+y[6]
       elif i==y[7]: 
        var="/backup"+'/'+y[1]+'/'+y[2]+'/'+y[3]+'/'+y[4]+'/'+y[5]+'/'+y[6]+'/'+y[7]
       elif i==y[8]: 
        var="/backup"+'/'+y[1]+'/'+y[2]+'/'+y[3]+'/'+y[4]+'/'+y[5]+'/'+y[6]+'/'+y[7]+'/'+y[8]
       elif i==y[9]: 
        var="/backup"+'/'+y[1]+'/'+y[2]+'/'+y[3]+'/'+y[4]+'/'+y[5]|+'/'+y[6]+'/'+y[7]+'/'+y[8]+'/'+y[9]   
       elif i==y[10]: 
        var="/backup"+'/'+y[1]+'/'+y[2]+'/'+y[3]+'/'+y[4]+'/'+y[5]|+'/'+y[6]+'/'+y[7]+'/'+y[8]+'/'+y[9]+'/'+y[10]
    # print(var)
       try:
         server.cwd(var)
         file=server.nlst()
        
         for j in file:
            if j.find('.') == -1:
              dir.append(j)
         
         
         if "backup" not in dir:
            print("Not Exist")
            if x.index(i)==1:   
               name="/backup"
       
            create_directory(server,name) 
       except:
              print("Directory not exist")
              create_directory(server,var)
               
# dir_exis(server,"/backup/jp_bkp/bkp/bp/jp/dp")

def create_directory(server,name):
     
    #dat=ftplib.FTP_TLS.cwd(self=server,dirname=path)
    ftplib.FTP_TLS.mkd(self=server,dirname=name)

import datefinder
file=[]
def check_date(string):
   original_string = string
   characters_to_remove = "_.php"

   new_string = original_string
   for character in characters_to_remove:
      new_string = new_string.replace(character, "")  
      
  #  print(string)
   matches = datefinder.find_dates(new_string)
   for mat in matches:
     if mat:
        return 1
     else:
        return -1

pip install datefinder

server = ftplib.FTP_TLS()
server.connect('host')
server.login('user',"password")
files = ftplib.FTP_TLS.nlst(self=server)
dot=[]
dir=[]
digit_file=[]
files = ftplib.FTP_TLS.nlst(self=server)
       
def parse_directory(server,path):
    all_files=[]
    dot_file=[]
    dir=[]
    file=[]
    digit_file=[]
    listf=""
    try:
       server.cwd(path)
       listf=server.nlst()
    except:
       pass   
    parent_dir=ftplib.FTP_TLS.pwd(self=server)
    # print(listf)
    for i in listf:
       if i.find('.') != -1:
           txt=["bkp",".zip","r.sh","backup","BKP","delcheck.php","reseller.php","google926510c7acb140b4.html","google","lwHostsCheck.php"



,"BACKUP","g9r7z.php","hkv1i.php",".pdf","viewer.php","plupload.silverlight.xap","-old","-new","bkup","phpdead","phpdeaddd2","-dead","nisar","searchcerti_pav_nisar","nisar1","-live","phpdedd"]
           empty=[]
           for j in txt:
               if i.find(j)!=-1 or check_date(i)==1 and i.find("js")==-1 and i.find("png")==-1 and i.find("jpg")==-1:
                  file.append(i)
                  dir_path="/backup/"
                  pat="/backup"+parent_dir
                  print(pat)
              
                  dir_exis(server,pat)
               
                  fromname=parent_dir+'/'+i
                  try:
                    success = ftplib.FTP_TLS.rename(self=server,fromname= parent_dir+'/'+i,toname=dir_path+'/'+parent_dir+'/'+i)
                  except:
                    pass 

          #  if i.find('bkp') != -1 or i.find('BKP') != -1 or i.find('backup') != -1 or i.find('old') != -1 or i.find('zip') != -1 or i.find('r.sh') != -1   or i.find('plupload.silverlight.xap') != -1  or i.find('new') != -1 or check_date(i)==1  and i.find('jpg') == -1 and i.find('png') == -1:
              # file.append(i)     
                
              # print(parent_dir)
                 
              
       else: 
          dot.append(i)
          if i!="images" and i!="dialyorders" and i!="2015" and i!="2016" and i!="2017" and i!="Reports" and i!="js" and i!="ptsans" and i!="i18n"   and i!="test-logs"  and i!="jp.afhsnj-testrest.com" and i!="jp":
             parse_directory(server,parent_dir+'/'+i)

 
    return all_files           
     
        
 
 

 

 
print(parse_directory(server,"/public_html"))

