import time
import random
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
from lxml import html
import pyautogui
import win32gui, win32com.client
from tkinter import *
from tkinter import filedialog
import re
 
 
def windowEnumerationHandler(hwnd, top_windows):
    top_windows.append((hwnd, win32gui.GetWindowText(hwnd)))


def getJobLinks(page):
	links = []
	for link in page.find_all('a'):
		url = link.get('href')
		
		if url:		
			if '/jobs/view' in url:
				links.append(url)
	return links
	
def getEasy(page):
	links = []
	achou = page.find("button", class_="jobs-s-apply__button js-apply-button")
	return str(achou)
	
def loadPage(browser):
	tpage = 0
	while tpage < 4000:
	 browser.execute_script("window.scrollTo(0,"+str(tpage)+" );")
	 tpage += 200
	 time.sleep(1)
	return BeautifulSoup(browser.page_source, "lxml")

def avoidLock():
    x, y = pyautogui.position()
    pyautogui.moveTo(x+200, None, duration=1.0)
    pyautogui.moveTo(x, None, duration=0.5)
    pyautogui.keyDown('ctrl')
    pyautogui.press('esc')
    pyautogui.keyUp('ctrl')
    time.sleep(0.5)
    pyautogui.press('esc')	

def containEasy(browser,cargo,local,pp):
	while True:
		browser.get("https://www.linkedin.com/jobs/search/?f_E=2&keywords="+cargo+local+"&start="+str(pp))
		avoidLock()
		pagina = loadPage(browser)
		feasy = pagina.find("div", class_= re.compile(r'job-card__easy-apply'))
		if feasy:
			break
		else:
			pp = pp + 25
	return (browser, pp)

def ViewBot(browser):
	visited = {}
	pList = []
	count = 0
	count5 = 0
	tpage = 0
	pp = 0
	top_windows = []
	win32gui.EnumWindows(windowEnumerationHandler, top_windows)
	for i in top_windows:
	   if "easyapplybot" in i[1].lower():
            plbot = i
	   if "python.exe" in i[1].lower():
            plbot = i
	   if "linkedin - google chrome" in i[1].lower():
            nvgd = i
	time.sleep(random.uniform(3.5,6.9))
	win32gui.ShowWindow(plbot[0],5)
	shell = win32com.client.Dispatch("WScript.Shell")
	shell.SendKeys('%')
	win32gui.SetForegroundWindow(plbot[0])
	aux = input('Enter the desired job title : ')
	cargo = aux.replace(" ","%20")
	print("Location codes: \n[1] GLOBAL\n[2] Country\n[3] State\n[4] City")
	aux = input('Enter the location code: ')
	if aux == "1":
	 aux2 = "Worldwide"
	if aux == "2":
	 aux2 = input('Enter the country name: ')
	if aux == "3":
	 aux2 = input('Enter the state name: ')
	if aux == "4":
	 aux2 = input('Enter the city name: ')
	local = "&location=" + aux2.replace(" ","%20") + "&sortBy=DD"
	print("\nPlease select your curriculum\n")
	time.sleep(1)
	root = Tk()
	resumeloctn = filedialog.askopenfilename(parent=root, initialdir="/",
                                    title='Please select your curriculum')
	
	root.destroy()
	shell.SendKeys('%')
	win32gui.SetForegroundWindow(nvgd[0])
	browser,pp = containEasy(browser,cargo,local,pp)
	
	while True:
		#sleep to make sure everything loads, add random to make us look human.
		time.sleep(random.uniform(3.5,6.9))
		
		page = BeautifulSoup(browser.page_source, 'lxml')
		
		
		jobs = getJobLinks(page)
		if jobs:
				for job in jobs:
				 root = 'http://www.linkedin.com'
				 roots = 'https://www.linkedin.com'
				 if root not in job or roots not in job:
				 	job = 'https://www.linkedin.com'+job
				 browser.get(job)
				 time.sleep(random.uniform(3.5,4.5))
				 print( "\n" + str(count5 + pp + 1))
				 pagina = BeautifulSoup(browser.page_source, "lxml")
				
				 tej = getEasy(pagina)
				 ember = pagina.find("div", class_="jobs-s-apply--top-card jobs-s-apply--fadein mr2 jobs-s-apply ember-view")
				 count5 += 1
				
				 if len(tej) > 4:
				  tej = "* Easy Apply Button"
				  embert = str(ember)
				  list_of_words = embert.split()
				  next_word = list_of_words[6]
				  pember = next_word[:(len(next_word)-1)]
				  xpath='//*[@'+pember+']/button'
				  time.sleep(1.5)
				  triggerDropDown = browser.find_element_by_xpath(xpath)
				  time.sleep(0.5)
				  triggerDropDown.click()
				  time.sleep(1.5)
				  browser.find_element_by_xpath('//*[@id="file-browse-input"]').send_keys(resumeloctn)
				  time.sleep(random.uniform(10,14))
				  browser.find_element_by_xpath("//*[contains(text(), 'Submit application')]").click() 
				  time.sleep(random.uniform(2,3.5))
				 
				 else:
				  tej = "* NOT Easy Apply Button"
				  
				 try:
				  print ("-> "+browser.title+"\n"+tej+" - Checked! \n")
				 except:
				  pass
           
				
				
				if count5 == len(jobs):
				  pp = pp + 25
				  count5 = 0
				  print("Going to next jobs page !")
				  avoidLock()
				  browser,pp = containEasy(browser,cargo,local,pp)
		else:
				print ("I'm Lost Exiting")
				break

			
		
def Main():
	print("\n\n       ===== Please Login to your LinkedIn account =====\n\n")
	time.sleep(3)
	
	options = Options()
	options.add_argument("--start-maximized")
	options.add_argument("--ignore-certificate-errors") 
	options.add_argument("user-agent=Chrome/51.0.2704.79 Safari/537.36 Edge/14.14393") 
	browser = webdriver.Chrome(chrome_options=options) 
	browser.get("https://linkedin.com/uas/login") 
	time.sleep(8)
	
	
		
	while True:
	 if browser.title != "Sign In to LinkedIn":
	  print("\nStarting LinkedIn bot\n")
	  break
	 else:
	  time.sleep(2)
	  print("\nPlease Login to your LinkedIn account\n")
	  
	ViewBot(browser)
	browser.close()

if __name__ == '__main__':
	Main()
