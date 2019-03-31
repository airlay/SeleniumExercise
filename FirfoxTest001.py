from selenium import webdriver

# from selenium.webdriver.common.keys import Keys

# create a new Firefox session
driver = webdriver.Firefox()
driver.implicitly_wait(3)
driver.maximize_window()

# Navigate to the application home page
driver.get("https://www.google.com")



# get the search textbox
search_field = driver.find_element_by_name('q')
# search_field = driver.find_element_by_id("gsr")
search_field.clear()

# enter search keyword and submit
search_field.send_keys("Selenium WebDriver Interview questions")
search_field.submit()

# get the list of elements which are displayed after the search
# currently on result page using find_elements_by_class_name method
lists = driver.find_elements_by_class_name("LC20lb")

# get the number of elements found
print("Found " + str(len(lists)) + " searches:")


# ids = driver.find_elements_by_class_name('//*[@id]')
# for i in ids:
#     # print ii.tag_name
#
#     print(i.get_attribute('id'))
#     # id name as string

# iterate through each element and print the text that is
# name of the search
i = 0
for listitem in lists:
    print(listitem)
    print(listitem.get_attribute("href"))
    print(listitem.text)
    # print(listitem.tag_name)

    print(type(listitem))
    print('***************************')
    i = i + 1
    if i > 10:
        break
# close the browser window
driver.quit()
