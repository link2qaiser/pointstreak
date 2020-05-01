
from selenium import webdriver
import time
import csv
import sys
driver = webdriver.Chrome()

def saveCsv(toCSV,file_name):
    print(file_name)
    keys = toCSV[0].keys()

    with open(file_name+".csv", 'w') as output_file:
        dict_writer = csv.DictWriter(output_file, keys)
        dict_writer.writeheader()
        dict_writer.writerows(toCSV)

def savePlayers(url):
    global driver
    driver.get(url)


    xpathTd = '//*[@id="ps-content-bootstrapper"]/div/div/div[2]/div[3]/div/div/table/tbody/tr'
    players = driver.find_elements_by_xpath(xpathTd)

    grandArr = []
    for item in players:
        try:
            row = {}
            row['num'] = item.find_element_by_xpath('.//td[1]').text
            row['player'] = item.find_element_by_xpath('.//td[2]').text
            row['bt'] = item.find_element_by_xpath('.//td[3]').text
            row['ht'] = item.find_element_by_xpath('.//td[4]').text
            row['wt'] = item.find_element_by_xpath('.//td[5]').text
            row['collage'] = item.find_element_by_xpath('.//td[6]').text
            row['class'] = item.find_element_by_xpath('.//td[7]').text
            row['hometown'] = item.find_element_by_xpath('.//td[8]').text
            grandArr.append(row)
        except:
            pass
    h2 = driver.find_element_by_xpath('//*[@id="ps-content-bootstrapper"]/div/div/div[2]/div[2]/div[3]/h2/span[1]/a').text
    
    saveCsv(grandArr,h2)
    

def getColls(mainUrl):
    driver.get(mainUrl)

    colls = driver.find_elements_by_xpath(
        '//*[@id="featured-client"]/div/ul[2]/li/a')

    collAllLinks = []
    #Colls Link
    for coll in colls:
        collLink = coll.get_attribute("href")
        collAllLinks.append(collLink)
        break
    return collAllLinks
def getLeague(collAllLinks):
    leagAllLink = []
    for link in collAllLinks:
        driver.get(link)
        leags = driver.find_elements_by_xpath(
            '//*[@id="ps-content-bootstrapper"]/div/div/div[2]/div[4]/div/div/table/tbody/tr/td[1]/a'
        )
        for leag in leags:
            leagLink = leag.get_attribute("href")
            leagAllLink.append(leagLink)
        break
    return leagAllLink


  




#Open the main URL
mainUrl = 'http://baseball.pointstreak.com/'
collAllLinks = getColls(mainUrl)
leagAllLink = getLeague(collAllLinks)

#print(leagAllLink)
for link in leagAllLink:
    link = link.replace("team_home.html","team_roster.html")
    savePlayers(link)
    time.sleep(3)


