from selenium import webdriver
import unittest, datetime
import xmlrunner

class TestCase(unittest.TestCase):

    def setUp(self):
        unittest.TestCase.setUp(self)

    def tearDown(self):
        unittest.TestCase.tearDown(self)

    def testMet1(self):
        driver = webdriver.Chrome()
        driver.get("http://next-episode.net")
        episodes = ['Elementary', "Grey's Anatomy", "The Vampire Diaries"]
        driver.maximize_window()
        assert "Next Episode" in driver.title
        now = datetime.datetime.now()
        crt_date = now.strftime("%d/%m")
        f = open('episode_list', 'a')
        f.write(crt_date + "\n")
        for episode in episodes:
            driver.find_element_by_link_text(episode).click()
            assert episode in driver.title
            ep_nr = driver.find_element_by_xpath(".//*[@id='previous_episode']/div[9]/div[2]").text
            new_episode = episode + " " + ep_nr 
            f.write(new_episode + "\n")
        f.close()
        driver.close()

if __name__ == '__main__':
	unittest.main(testRunner=xmlrunner.XMLTestRunner(output='test-reports'))