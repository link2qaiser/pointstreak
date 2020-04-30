from selenium import webdriver
driver = webdriver.Chrome()


def getPoints():
    global driver

    #driver.get(url)
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
    print(grandArr)


#url = 'http://baseball.pointstreak.com/team_roster.html?teamid=65683&seasonid=32546&sortby=jersey'

#getPoints(url)

#Open the main URL
mainUrl = 'http://baseball.pointstreak.com/'

driver.get(mainUrl)

colls = driver.find_elements_by_xpath(
    '//*[@id="featured-client"]/div/ul[2]/li/a')

#Colls Link
for coll in colls:
    collLink = coll.get_attribute("href")
    driver.get(collLink)
    #League Links
    leags = driver.find_elements_by_xpath(
        '//*[@id="ps-content-bootstrapper"]/div/div/div[2]/div[4]/div/div/table/tbody/tr/td[1]/a'
    )
    for leag in leags:
        leagLink = leag.get_attribute("href")
        driver.get(leagLink)
        driver.find_element_by_xpath(
            '/html/body/div[3]/div[1]/div/div/div[1]/div/div[2]/ul[1]/li[7]/a'
        ).click()
        getPoints()
