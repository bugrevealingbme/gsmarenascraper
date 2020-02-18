# -*- coding: utf-8 -*- 

import requests
from bs4 import BeautifulSoup
import urllib.request
import mysql.connector
from sys import argv
import re


sayac=0
while True:
 #try:
  f=open('butuncihazlar.txt')
  lines = f.readlines()
  url = "https://www.gsmarena.com/motorola_one_action-9739.php"
  try:
    if (str(lines[sayac]) == ""):
      print("Bitti.")
      break
  except:
    print("Bitti.")
    break  
  headers = {'User-Agent': 'Mozilla/5.0'}
  sayac+=1
  url_oku = requests.get(url, headers=headers)
  html_content = url_oku.text
  soup = BeautifulSoup(html_content,'html.parser')
  
  cihazyazilacak = soup.find('td',{'data-spec' : 'year'}).text
  cihazexport = open("cihaz1.txt", "wb")
  cihazexport.write(str(cihazyazilacak.strip()).encode('utf-8'))
  cihazexport.write(str("\n").encode('utf-8'))
  cihazexport.close()

  cihazyazilacak = soup.find('h1',{'data-spec' : 'modelname'}).text
  modelname = cihazyazilacak
  
  for child in soup.find_all("a", {"class":"noUnd"}):
   child.string = 'silinecekasdads'
  for child in soup.find_all("a", {"href":"glossary.php3?term=benchmarking"}):
   child.string = 'silinecekasdads'
  for child in soup.find_all("a", {"href":"gsmarena_lab_tests-review-751p5.php"}):
   child.string = 'silinecekasdads'
  for child in soup.find_all("a", {"href":"gsmarena_lab_tests-review-751p3.php"}):
   child.string = 'silinecekasdads'
  for child in soup.find_all("a", {"href":"gsmarena_lab_tests-review-751p4.php"}):
   child.string = 'silinecekasdads'
  for child in soup.find_all("a", {"href":"gsmarena_lab_tests-review-751p2.php"}):
   child.string = 'silinecekasdads'
  for child in soup.find_all("a", {"href":"gsmarena_lab_tests-review-751p4.php"}):
   child.string = 'silinecekasdads'
  for child in soup.find_all("a", {"href":"gsmarena_lab_tests-review-751p6.php"}):
   child.string = 'silinecekasdads'
  for child in soup.find_all("a", {"href":"gsmarena_lab_tests-review-751p7.php"}):
   child.string = 'silinecekasdads'
  for child in soup.find_all("a", {"href":"gsmarena_lab_tests-review-751p1.php"}):
   child.string = 'silinecekasdads'
  for child in soup.find_all("td", {"data-spec":"batlife"}):
   child.decompose()
  for child in soup.find_all("td", {"data-spec":"tbench"}):
   child.decompose()
   
  for child in soup.find_all("td", {"class":"ttl"}):
   child.string = 'altsatiryarrak'+child.text+'altsatir'

  f=open('cihaz1.txt')
  lines = f.readlines()
  kontrol = "" 
  try:
    linestl = lines[0].strip()
    if (int(linestl[:4]) < 2011):
      print("Bu cihaz 2011 öncesi tanıtıldığı için pas geçildi!")
      kontrol = "Dur"
      continue
  except:
    print("Eklenmedi!")
    with open('eklenmedi.txt', 'a') as file:
      file.write(url)
      file.write("\n") 
    continue
  if (kontrol == "Dur"):
    continue   
  f.close()

  try:  
    cihazyazilacak= soup.find('span',{'data-spec' : 'displaysize-hl'}).text
    cihazexport = open("cihaz1.txt", "ab")
    if (cihazyazilacak != "" and cihazyazilacak != "-" and cihazyazilacak != " " and cihazyazilacak != "null" and cihazyazilacak != "Null"):
      cihazexport.write(str("displaysizehlaltsatir").encode('utf-8'))
      cihazexport.write(str(cihazyazilacak).encode('utf-8'))
      cihazexport.write(str("altsatir").encode('utf-8'))
  except:
    pass
  try:  
    cihazyazilacak= soup.find('div',{'data-spec' : 'displayres-hl'}).text
    if (cihazyazilacak != "" and cihazyazilacak != "-" and cihazyazilacak != " " and cihazyazilacak != "null" and cihazyazilacak != "Null"):
      cihazexport = open("cihaz1.txt", "ab")
      cihazexport.write(str("displayrehlsaltsatir").encode('utf-8'))
      cihazexport.write(str(cihazyazilacak).encode('utf-8'))
      cihazexport.write(str("altsatir").encode('utf-8'))
  except:
    pass
  try: 
    cihazyazilacak= soup.find('span',{'data-spec' : 'camerapixels-hl'}).text
    if (cihazyazilacak != "" and cihazyazilacak != "-" and cihazyazilacak != " " and cihazyazilacak != "null" and cihazyazilacak != "Null"):
      cihazexport.write(str("camerapixelshlaltsatir").encode('utf-8'))
      cihazexport = open("cihaz1.txt", "ab")
      cihazexport.write(str(cihazyazilacak).encode('utf-8'))  
      cihazexport.write(str("altsatir").encode('utf-8'))
  except:
    pass
  try:  
    cihazyazilacak = soup.find('div',{'data-spec' : 'videopixels-hl'}).text
    if (cihazyazilacak != "" and cihazyazilacak != "-" and cihazyazilacak != " " and cihazyazilacak != "null" and cihazyazilacak != "Null"):
      cihazexport.write(str("videopixelshlaltsatir").encode('utf-8'))
      cihazexport = open("cihaz1.txt", "ab")
      cihazexport.write(str(cihazyazilacak).encode('utf-8'))  
      cihazexport.write(str("altsatir").encode('utf-8'))
  except:
    pass
  try:  
    cihazyazilacak = soup.find('span',{'data-spec' : 'ramsize-hl'}).text
    if (cihazyazilacak != "" and cihazyazilacak != "-" and cihazyazilacak != " " and cihazyazilacak != "null" and cihazyazilacak != "Null"):
      cihazexport.write(str("ramsizehlaltsatir").encode('utf-8'))
      cihazexport = open("cihaz1.txt", "ab")
      cihazexport.write(str(cihazyazilacak).encode('utf-8'))  
      cihazexport.write(str("altsatir").encode('utf-8'))
  except:
    pass
  try:  
    cihazyazilacak= soup.find('div',{'data-spec' : 'chipset-hl'}).text
    if (cihazyazilacak != "" and cihazyazilacak != "-" and cihazyazilacak != " " and cihazyazilacak != "null" and cihazyazilacak != "Null"):
      cihazexport.write(str("chipsethlaltsatir").encode('utf-8'))
      cihazexport = open("cihaz1.txt", "ab")
      cihazexport.write(str(cihazyazilacak).encode('utf-8'))
      cihazexport.write(str("altsatir").encode('utf-8'))
  except:
    pass
  try:  
    cihazyazilacak = soup.find('span',{'data-spec' : 'batsize-hl'}).text
    if (cihazyazilacak != "" and cihazyazilacak != "-" and cihazyazilacak != " " and cihazyazilacak != "null" and cihazyazilacak != "Null"):
      cihazexport.write(str("batsizehlaltsatir").encode('utf-8'))
      cihazexport = open("cihaz1.txt", "ab")
      cihazexport.write(str(cihazyazilacak).encode('utf-8'))
      cihazexport.write(str("altsatir").encode('utf-8'))
  except:
    pass  
  try:
    cihazyazilacak = soup.find('div',{'data-spec' : 'battype-hl'}).text
    if (cihazyazilacak != "" and cihazyazilacak != "-" and cihazyazilacak != " " and cihazyazilacak != "null" and cihazyazilacak != "Null"):
      cihazexport.write(str("battypehlaltsatir").encode('utf-8'))
      cihazexport = open("cihaz1.txt", "ab")
      cihazexport.write(str(cihazyazilacak).encode('utf-8')) 
      cihazexport.write(str("altsatir").encode('utf-8'))  
  except:
    pass
  cihazyazilacak = soup.find('div',{'class' : 'specs-photo-main'}).find('img', src=True)
  fotoexport = open("butunfotolarlink.txt", "ab")
  fotoexport.write(str(cihazyazilacak['src'].strip()).encode('utf-8') + "\n".encode('utf-8'))
  cihazexport = open("cihaz1.txt", "ab")
  cihazyazilacak = str(cihazyazilacak['src'].strip())
  cihazyazilacak = re.sub(r'https://cdn2.gsmarena.com/vv/bigpic/', '', cihazyazilacak)  
  cihazexport.write(str("Photo altsatir"+cihazyazilacak).encode('utf-8'))
  cihazexport.write(str("\n").encode('utf-8'))
  cihazexport.close()
  
  cihazyazilacak = soup.find_all('td', {'class':['ttl', 'nfo']})
  cihazexport = open("cihaz1.txt", "ab")
  cihazexport.write(str(cihazyazilacak).encode('utf-8'))
  cihazexport.write(str("\n").encode('utf-8'))
  cihazexport.close()
  
  fh = open("cihaz1.txt", "r", encoding="utf-8")
  lines = fh.readlines()
  fh.close()
  lines = filter(lambda x: not x.isspace(), lines)
  fh = open("cihaz1.txt", "w", encoding="utf-8")
  fh.write("".join(lines))
  fh.close()

  with open('cihaz1.txt', 'r', encoding="utf-8") as file :
    filedata = file.read()
  filedata = filedata.replace('[<td', '<td')
  with open('cihaz1.txt', 'w', encoding="utf-8") as file:
    file.write(filedata.strip())   
  
  with open('cihaz1.txt', 'r', encoding="utf-8") as file :
    filedata = file.read()
  filedata = filedata.replace('</td>, <', '</td> <')
  with open('cihaz1.txt', 'w', encoding="utf-8") as file:
    file.write(filedata.strip()) 
	
  with open('cihaz1.txt', 'r', encoding="utf-8") as file :
    filedata = file.read()
  filedata = filedata.replace('</td>', '</td>\n')
  with open('cihaz1.txt', 'w', encoding="utf-8") as file:
    file.write(filedata.strip()) 
	
  with open('cihaz1.txt', 'r', encoding="utf-8") as file :
    filedata = file.read()
  filedata = filedata.replace('<td class="ttl">', '')
  with open('cihaz1.txt', 'w', encoding="utf-8") as file:
    file.write(filedata.strip()) 

  with open('cihaz1.txt', 'r', encoding="utf-8") as file :
    filedata = file.read()
  filedata = filedata.replace('<td class="nfo">', '')
  with open('cihaz1.txt', 'w', encoding="utf-8") as file:
    file.write(filedata.strip())

  with open('cihaz1.txt', 'r', encoding="utf-8") as file :
    filedata = file.read()
  filedata = filedata.replace('</td>', '')
  with open('cihaz1.txt', 'w', encoding="utf-8") as file:
    file.write(filedata.strip()) 

  with open('cihaz1.txt', 'r', encoding="utf-8") as file :
    filedata = file.read()
  filedata = filedata.replace('</a>', '')
  with open('cihaz1.txt', 'w', encoding="utf-8") as file:
    file.write(filedata.strip()) 

  with open('cihaz1.txt', 'r', encoding="utf-8") as file :
    filedata = file.read()
  filedata = re.sub(r'<a href=".*?">', '', filedata)
  with open('cihaz1.txt', 'w', encoding="utf-8") as file:
    file.write(filedata.strip())

  with open('cihaz1.txt', 'r', encoding="utf-8") as file :
    filedata = file.read()
  filedata = re.sub(r'<a class=".*?">', '', filedata)
  with open('cihaz1.txt', 'w', encoding="utf-8") as file:
    file.write(filedata.strip())

  with open('cihaz1.txt', 'r', encoding="utf-8") as file :
    filedata = file.read()
  filedata = re.sub(r'<td class=".*?" data-spec="', 'yarrak', filedata)
  with open('cihaz1.txt', 'w', encoding="utf-8") as file:
    file.write(filedata.strip())

  with open('cihaz1.txt', 'r', encoding="utf-8") as file :
    filedata = file.read()
  filedata = filedata.replace('">', 'altsatir')
  with open('cihaz1.txt', 'w', encoding="utf-8") as file:
    file.write(filedata.strip())	
	
  f=open('cihaz1.txt', encoding="utf-8")
  lines = f.readlines()
  k=1
  kk=2
  cihazexport = open("cihaz1.txt", "wb")

  try:
    for line in lines:
      with open('cihaz1.txt', 'r', encoding="utf-8") as file:
        filedata = file.read()
      linesk = lines[k].strip()
      lineskk = lines[kk].strip()
      if (linesk == ""):
        linesk = "null"			  
      filedata =  linesk + lineskk
      with open('cihaz1.txt', 'a', encoding="utf-8") as file:
       file.write(filedata.strip()) 
      k+=2
      kk+=2
  except:
    pass
	
  with open('cihaz1.txt', 'r', encoding="utf-8") as file :
    filedata = file.read()
  filedata = filedata.replace('altsatir', '\n')
  with open('cihaz1.txt', 'w', encoding="utf-8") as file:
    file.write(filedata.strip()) 	
	
  with open('cihaz1.txt', 'r', encoding="utf-8") as file :
    filedata = file.read()
  filedata = filedata.replace('<br>', '<br />')
  with open('cihaz1.txt', 'w', encoding="utf-8") as file:
    file.write(filedata.strip()) 	
	
  with open('cihaz1.txt', 'r', encoding="utf-8") as file :
    filedata = file.read()
  filedata = filedata.replace('</br>', '')
  with open('cihaz1.txt', 'w', encoding="utf-8") as file:
    file.write(filedata.strip())
	
  with open('cihaz1.txt', 'r', encoding="utf-8") as file :
    filedata = file.read()
  filedata = filedata.replace('\xa0', '')
  with open('cihaz1.txt', 'w', encoding="utf-8") as file:
    file.write(filedata.strip()) 

  with open('cihaz1.txt', 'r', encoding="utf-8") as file :
    filedata = file.read()
  filedata = filedata.replace(']', '')
  with open('cihaz1.txt', 'w', encoding="utf-8") as file:
    file.write(filedata.strip()) 

  with open("cihaz1.txt", "r", encoding="utf-8") as text:
       lines=text.readlines()
  mynewtext=[]
  for line in lines:
       if line.strip() != "":
            mynewtext.append(line)
       else:
            mynewtext.append("null\n")
  with open("cihaz1.txt","w", encoding="utf-8") as text:
       for i in mynewtext:
            text.write(i)

  with open("cihaz1.txt", "r", encoding="utf-8") as text:
       lines=text.readlines()
  mynewtext=[]
  for line in lines:
       if line.strip() != "yarrak":
         mynewtext.append(line)
       else:
         mynewtext.append("\n")
  with open("cihaz1.txt","w", encoding="utf-8") as text:
       for i in mynewtext:
            text.write(i)
	
  k=0
  with open("cihaz1.txt", "r", encoding="utf-8") as text:
       lines=text.readlines()
  mynewtext=[]
  for line in lines:
       if len(line)>=2:
            mynewtext.append(line)
       else:
            mynewtext.append("others"+str(k)+"\n")
            k+=1
  with open("cihaz1.txt","w", encoding="utf-8") as text:
       for i in mynewtext:
            text.write(i)

  k=0
  kk=1
  with open("cihaz1.txt", "r", encoding="utf-8") as text:
       lines=text.readlines()
  mynewtext=[]
  try:
    for line in lines:
      linestl = lines[k].strip()
      linestlk = lines[kk].strip()
      if (linestl[:6] == "yarrak" and linestl[:6] == linestlk[:6]):
         pass        
      else:
            mynewtext.append(line)
      k+=1
      kk+=1
    with open("cihaz1.txt","w", encoding="utf-8") as text:
       for i in mynewtext:
            text.write(i)
  except:
    with open("cihaz1.txt","w", encoding="utf-8") as text:
      for i in mynewtext:
        text.write(i)
      text.write(linestl)
    pass
	
  k=0
  kk=1
  with open("cihaz1.txt", "r", encoding="utf-8") as text:
       lines=text.readlines()
  mynewtext=[]
  try:
    for line in lines:
      linestl = lines[k].strip()
      linestlk = lines[kk].strip()
      if (linestl[:6] == "yarrak" and linestl[:6] == linestlk[:6]):
         pass        
      else:
            mynewtext.append(line)
      k+=1
      kk+=1
    with open("cihaz1.txt","w", encoding="utf-8") as text:
       for i in mynewtext:
            text.write(i)
  except:
    with open("cihaz1.txt","w", encoding="utf-8") as text:
      for i in mynewtext:
        text.write(i)
      text.write(linestl)
    pass
	
  fh = open("cihaz1.txt", "r", encoding="utf-8")
  lines = fh.readlines()
  fh.close()
  lines = filter(lambda x: not x.isspace(), lines)
  fh = open("cihaz1.txt", "w", encoding="utf-8")
  fh.write("".join(lines))
  fh.close()		
  
  f=open('cihaz1.txt', encoding="utf-8")
  lines = f.readlines()
  k=0
  kk=1
  try:
    for line in lines:
      linestl = lines[k].strip()
      linestlk = lines[kk].strip()
      if (linestl[:6] == "others" and linestlk[:6] == "yarrak"): 
        with open('cihaz1.txt', 'r', encoding="utf-8") as file:
          filedata = file.read()
        filedata = filedata.replace(linestl, '')
        with open('cihaz1.txt', 'w', encoding="utf-8") as file:
         file.write(filedata)
      k+=1
      kk+=1
  except:
    pass	

  f=open('cihaz1.txt', encoding="utf-8")
  lines = f.readlines()
  k=0
  kk=1
  try:
    for line in lines:
      linestl = lines[k].strip()
      linestlk = lines[kk].strip()  
      if (linestl[:6] == "yarrak" and linestlk[:6] == "others"):
        with open('cihaz1.txt', 'r', encoding="utf-8") as file:
          filedata = file.read()
        filedata = filedata.replace(linestlk, '')
        with open('cihaz1.txt', 'w', encoding="utf-8") as file:
         file.write(filedata)
      k+=1
      kk+=1
  except:
    pass	

  with open("cihaz1.txt", "r", encoding="utf-8") as text:
       lines=text.readlines()
  mynewtext=[]
  for line in lines:
       if ("silinecekasdads" not in line.strip()):
            mynewtext.append(line)
       else:
            pass
  with open("cihaz1.txt","w", encoding="utf-8") as text:
       for i in mynewtext:
            text.write(i)
	
  fh = open("cihaz1.txt", "r", encoding="utf-8")
  lines = fh.readlines()
  fh.close()
  lines = filter(lambda x: not x.isspace(), lines)
  fh = open("cihaz1.txt", "w", encoding="utf-8")
  fh.write("".join(lines))
  fh.close()		

  with open('cihaz1.txt', 'r', encoding="utf-8") as file :
    filedata = file.read()
  filedata = filedata.replace('yarrak', '')
  with open('cihaz1.txt', 'w', encoding="utf-8") as file:
    file.write(filedata.strip()) 

  with open('cihaz1.txt', 'r', encoding="utf-8") as fin:
      data = fin.read().splitlines(True)
  with open('cihaz1.txt', 'r', encoding="utf-8") as f:
    lines = f.read().splitlines()
    last_line = lines[-1]
  for line in lines:
    if (last_line == "null" or last_line[:6] == "others"  or last_line == "silinecekasdads"):
      with open('cihaz1.txt', 'w', encoding="utf-8") as fout:
          fout.writelines(data[:-1])
  
  f=open('cihaz1.txt' , encoding="utf-8")
  lines = f.readlines()
  cnx = mysql.connector.connect(host='localhost',user='root',password='',database='phonedb', charset='utf8')
  cursor = cnx.cursor()
  eklemodel = (modelname.replace("'","").replace(":","").strip())
  modelname = eklemodel
  newmodelname = re.sub(r'.*?.\(', '', modelname)
  if(newmodelname == modelname):
    outmodelname = modelname.replace(" ","")
  else:
    newmodelname = newmodelname.replace(")","")
    try:
      if (int(newmodelname) >= 2010):
         outmodelname = modelname.replace("(","").replace(")","").replace(" ","")  
      else:
         outmodelname = modelname
         outmodelname = outmodelname.replace(" ","")	   
    except:
      outmodelname = modelname
      outmodelname = outmodelname.replace(" ","")  
  try:
    cursor.execute("INSERT INTO `yenicihaz` (Modelname, Outmodel) VALUES ('"+ eklemodel.strip() +"', '" + outmodelname.strip() + "')")
  except Exception as e:
    print("Bu cihaz zaten mevcut! Güncellendi! Kod: "+str(e))
    pass  
  cnx.commit()
  i=0
  j=1
  cck=0
  for line in lines:
    try:
      ekle = (lines[i].replace(" ","").replace("-","").replace("(","").replace(")","").replace("/","").replace("'","").replace(":","").replace(".","").replace(",","").strip())
    except:
      break
    ekle2 = (lines[j].replace("'","").strip())
    if (ekle == "net4g"):
      cck+=1
      if (cck == 2):
        ekle = "net5g"
    try:
      # cursor.execute("ALTER TABLE gsmarena ADD `" + ekle + "` text")
      cursor.execute("UPDATE `yenicihaz` SET `"+ ekle.strip() +"` = RTRIM('" + ekle2.strip() + "') Where Modelname = '"+ eklemodel.strip() +"'")
    except: 
        pass
    
    cnx.commit()
    i+=2
    j+=2
  print("Eklendi:" + eklemodel)
  if(url is None):
    break
			
  break
 #except:
 # print("Hata!")
 # with open('hata.txt', 'a') as file:
 #   file.write(url)
 #   file.write("\n") 
 # pass