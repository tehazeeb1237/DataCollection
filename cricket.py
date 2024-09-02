import csv
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Initialize Chrome webdriver
driver = webdriver.Chrome()
driver.get(url="https://www.cricbuzz.com/cricket-series/7607/indian-premier-league-2024/matches")
# Open CSV file in write mode
with open('cricket_data.csv', 'w', newline='') as csvfile:
csvwriter = csv.writer(csvfile)
# Write headers to CSV file
csvwriter.writerow(['Stadium', 'Toss', 'Team', 'Runs', 'Extras', 'Wickets_lost',     'Overs_played','Wickets_taken', 'Overs_bowled', 'Result'])
 for i in range(1, 74):
        print(i)
 elements = WebDriverWait(driver, 20).until(EC.presence_of_all_elements_located((By.XPATH,         f"(//a[@class='cb-text-complete'])[{i}]")))
        for element in elements:
            driver.execute_script("arguments[0].click();", element)

        stdm = driver.find_element(by=By.XPATH, value="//span[@class='text-hvr-underline text-gray']/span[@itemprop='name']").text
        stadium = list(stdm.split(","))
        
        driver.find_element(by=By.XPATH, value="(//a[@class='cb-nav-tab '])[1]").click()
        toss = driver.find_element(by=By.XPATH, value="(//div[@class='cb-col cb-col-73'])[3]").text

        names = driver.find_elements(by=By.XPATH, value="//div[@class='cb-col cb-col-100 cb-scrd-hdr-rw']/span")
        name = []
        name.append(names[0].text)
        name.append(names[2].text)

        runs = driver.find_elements(by=By.XPATH, value="//div[@class='cb-col cb-col-8 text-bold text-black text-right']")
        extras = driver.find_elements(by=By.XPATH, value="//div[@class='cb-col cb-col-8 text-bold cb-text-black text-right']")
        wkts_overs = driver.find_elements(by=By.XPATH, value="//div[@class='cb-col-32 cb-col']")
        wkt_over = []
        wkt_over.append(wkts_overs[1].text)
        wkt_over.append(wkts_overs[3].text)

        n1 = list(name[0].split(" "))
        n2 = list(name[1].split(" "))
        k = list(toss.split(" "))
        r1, r2, t1, t2 = 0, 0, 0, 0

        if n1[0] == k[0]:
            r1 = 1
        else:
            r2 = 1

        if runs[0].text > runs[1].text:
            t1 = 1
        else:
            t2 = 1

        for j in range(2):  # Using a different variable name for inner loop
            wkts = wkt_over[j]
            wickets_lost = wkts[2:3]
            overs_played = wkts[10:12]
            over = wkt_over[-1 + j]
            wickets_taken = over[2:3]
            overs_bowled = over[10:12]

            if j == 0:
                if r1 == 1:
                    t = "win"
                else:
                    t = "lost"
                if t1 == 1:
                    res = "win"
                else:
                    res = "lost"
            else:
                if r2 == 1:
                    t = "win"
                else:
                    t = "lost"
                if t2 == 1:
                    res = "win"
                else:
                    res = "lost"

            # Write data to CSV file
            csvwriter.writerow([stadium[0], t, name[j], runs[j].text, extras[j].text, wickets_lost, overs_played, wickets_taken, overs_bowled, res])

        driver.back()
        driver.back()

# Close Chrome webdriver
driver.quit()