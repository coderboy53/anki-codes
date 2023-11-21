'''
if word_type in ['Godan verb','Ichidan verb','I-adjective (keiyoushi)']:
            # set up the selenium driver with firefox
            driver = webdriver.Firefox(service=Service(r'/usr/local/bin/geckodriver'))
            driver.get('https://jisho.org/search/'+urllib.parse.quote(self.keyword)) # open the URL
            time.sleep(2)
            driver.find_element(By.CLASS_NAME,'show_inflection_table').click() # click the show inflections button
            time.sleep(2)
            table = driver.find_element(By.XPATH,'/html/body/div[2]/div/table') # get the inflection table
            time.sleep(2)
            soup = BeautifulSoup(table.get_attribute('outerHTML'),'html.parser') # get the parsed HTML soup
            # soup = BeautifulSoup(table.get_attribute)
            table = pd.read_html(str(soup.prettify()),index_col=0,header=0) # create a pandas dataframe with the table
            # table = str(soup.prettify())
            driver.quit()
            # return the word type and the dataframe
            return word_type, table
'''