from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from booking.constants import baseurl,month_dict

class ixigo(webdriver.Chrome):

    def __init__(self):
        super(ixigo,self).__init__()

    def first_page(self):
        self.get(baseurl)
    
    def start_from(self,start_journey):
        self.find_element(by = By.XPATH,value= "//div[@class='orgn u-ib u-v-align-bottom']//div[@class='clear-input ixi-icon-cross']").click()
        self.find_element(by= By.XPATH, value="//input[@placeholder='Leaving from']").send_keys(start_journey)
        time.sleep(3)
        self.find_element(by=By.XPATH,value="//div[@data-acindex='0']").click()
    
    def destination(self,end_to):
        self.find_element(by= By.XPATH, value="//input[@placeholder='Going to']").send_keys(end_to)
        time.sleep(3)
        self.find_element(by=By.XPATH,value="/html[1]/body[1]/div[1]/div[1]/div[1]/div[3]/div[1]/div[1]/div[1]/div[1]/div[3]/div[1]/div[3]/div[1]/div[1]").click()

    def date_modifier(self,data:str):
        m = data.split()
        month = month_dict.get(m[1])
        date = "".join(m)
        return month, date


    def d_date(self,date:str):
        month,date = self.date_modifier(date)
        self.find_element(by= By.XPATH,value="//input[@placeholder='depart']").click()
        time.sleep(3)
        
        for i in range(3):
            a= self.find_element(by = By.XPATH, value="/html[1]/body[1]/div[2]/div[2]/div[1]/div[1]").text.split()
            if a[0].lower()[:3] == month:
                break
            else:
                self.find_element(by=By.XPATH,value="//button[@class='ixi-icon-arrow rd-next']").click()
                        
        time.sleep(2)
        try:
            self.find_element(by = By.CSS_SELECTOR,value=f'td[data-date="{date}"]').click()
        except:
            print("\nEnter valid date or date in range")
            self.quit()
            

    def search(self):
        self.find_element(by=By.XPATH,value="//div[@class='search u-ib u-v-align-bottom']//div[@class='u-ripple']").click()
        self.implicitly_wait(5)

    def avl_trains(self):
        
        train_numbers = self.find_elements(by=By.CSS_SELECTOR, value="span[class='train-number']")
        train_names = self.find_elements(by=By.CSS_SELECTOR, value="span[class='train-name']")
        train_times = self.find_elements(by= By.CSS_SELECTOR, value = "div[class ='time']")
        train_dates = self.find_elements(by= By.CSS_SELECTOR, value = "div[class ='date']")
        c= 0
        if train_numbers != []:
            for i in range(len(train_numbers)):
                print("="*70)
                print(train_numbers[i].text,end="\t")
                print(train_names[i].text)
                print(f"Departure:{train_dates[c].text} ---- Arrival:{train_dates[c+1].text}")
                print(f"          {train_times[c].text}                    {train_times[c+1].text}")
                c += 2
            print()
        else:
            print("Sorry!!! No trains avilable")
            print()