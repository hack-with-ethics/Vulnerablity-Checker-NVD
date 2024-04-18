import requests
import os
import sys
from bs4 import BeautifulSoup as bs
import time

if os.name !="nt":
	os.system("clear")
else:
	os.system("cls")
def Banner():
	print("""  __  __ _____   __          ___    _ _____ _______ ______ _    _       _______ 
 |  \/  |  __ \  \ \        / / |  | |_   _|__   __|  ____| |  | |   /\|__   __|
 | \  / | |__) |  \ \  /\  / /| |__| | | |    | |  | |__  | |__| |  /  \  | |   
 | |\/| |  _  /    \ \/  \/ / |  __  | | |    | |  |  __| |  __  | / /\ \ | |   
 | |  | | | \ \     \  /\  /  | |  | |_| |_   | |  | |____| |  | |/ ____ \| |   
 |_|  |_|_|  \_\     \/  \/   |_|  |_|_____|  |_|  |______|_|  |_/_/    \_\_|   """)	
def GetRequest(url):
	try:
		response = requests.get(url)

		return response.content,response.status_code
	except:
		print("[-]Check The NetWOrk Error Or Some Error Occured !")
		sys.exit(1)
def BasicSearch(query):
	if len(query.split()) == 2:
		q = query.split()
		query = q[0]+"+"+q[1]
	else:
		query = query
	print(query)
	os.system("clear")
	Baseurl = "https://nvd.nist.gov/"
	Searchurl=f"vuln/search/results?form_type=Basic&results_type=overview&query={query}&search_type=all&isCpeNameSearch=false"
	response,status_code= GetRequest(Baseurl+Searchurl)
	Banner()
	if status_code == 200:
		print("="*80)
		print("[+]Url Locked :",Baseurl+Searchurl)
		print("[+]Response Code:",status_code)
		print("="*150)
		time.sleep(3)
		soup = bs(response,"html.parser")

		lst = soup.find_all("tr")
		print("[*]Found Listing...")
		print("*"*150)
		for i in lst:
			try:
				time.sleep(.11)
				link = i.find("a").attrs["href"]
				print("[+]",i.find("a").attrs["href"].split("/")[3])
				print(i.find("td").find("p").text)
				print("[*]Referal Link:",Baseurl+link)
				print("*"*150)
			except:
				pass
		print("*"*150)
		ack = input(str("[+]Do You Need The OutFile The Result To File:"))
		if ack == "y":
			with open("out.html","wb") as File:
				File.write(response)
				File.close()
			print("File Written:",os.getcwd()+"/"+"out.html")
		print("[-]Exiting Script . . ")
def AdvSearch(cve):
	cve = cve.upper()
	url =f"https://nvd.nist.gov/vuln/search/results?form_type=Advanced&results_type=overview&search_type=all&cve_id={cve}&isCpeNameSearch=false"
	response,status_code = GetRequest(url)
	if status_code == 200:
		os.system("clear")
		Banner()
		print("*"*80)
		print('[*]url Locked :',url)
		print('[*]Response Code:',status_code)
		print("*"*80)
		time.sleep(3)
		soup = bs(response,"html.parser")
		lst = soup.find_all("tr")
		time.sleep(.11)
		print("[+]Result ... ")
		for i in lst:
			try:
				link = i.find("a").attrs["href"]
				print("[+]",i.find("a").attrs["href"].split("/")[3])
				print(i.find("td").find("p").text)
				print("[*]Referal Link:",link)
			except:
				pass
		print("="*80)
		ack = input(str("Do You Want TO write TO a File:"))
		if ack == "y":
			with open("Cve.html",'wb') as File:
				File.write(response)
				File.close()
			print("[+]Written Script:",os.getcwd()+"/"+"Cve.html")
		print("Exiting Script .")
Banner()
print("***********************************************************************")
print("[*]Nist Api Access")
print("[*]Author : Mr Whitehat")
print("***********************************************************************")
print("[1]Basic Search")
print("[2]CVE search")
print("[3]Exit ")
ch = input(str("[*]Tool >" ))

if ch == "1":
	Search = input(str("[*]Query [Nginx , apache , vsftp] >"))
	BasicSearch(Search)
elif ch == "3":
	sys.exit(1)
else:
	Search = input(str("[*]Cve Number [cve-2022-0847] >"))
	AdvSearch(Search)
