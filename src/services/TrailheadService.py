#!/usr/bin/env python3
# coding: UTF-8

import os
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.options import Options
from utils import TrailheadUtils
from utils import LogUtils


class TrailheadService:
    # constructor
    def __init__(self, user):
        self.user_name = user[0]
        self.user_id = user[1]

    # get the trailhead score
    def get_trailhead_score(self, user):
        # Chrome headless mode
        _options = Options()
        _options.set_headless(False)

        # maximized window
        _options.add_argument("--start-maximized")

        # set URL
        utils = TrailheadUtils.TrailheadUtils()
        _target_url = utils.get_target_url(self.user_id)
        # print(_target_url)

        # start Log
        # logger = LogUtils.LogUtils()
        # logger.debug('OPEN ' + _target_url + ' (' + self.user_name + ')')

        # open Chrome
        driver = webdriver.Chrome(executable_path='/usr/local/bin/chromedriver', chrome_options=_options)
        driver.implicitly_wait(60)
        driver.get(_target_url)
        # driver.refresh()
        # driver.implicitly_wait(60)
        # driver.maximize_window()
        driver.implicitly_wait(60)
        # driver.refresh()

        # fetch the numbers of Badges
        _numbers_of_badges = driver.find_element_by_xpath(
            utils.XPATH_BADGES).text

        # fetch the numbers of Points
        _numbers_of_points = driver.find_element_by_xpath(
            utils.XPATH_POINTS).text

        # fetch the numbers of Trails Completed
        _numbers_of_trails = driver.find_element_by_xpath(
            utils.XPATH_TRAILS).text

        # fetch the name of Trailblazer Ranks
        _name_of_ranks = driver.find_element_by_xpath(
            utils.XPATH_RANKS).get_attribute('alt')

        # click the dropdown and select Superbadges
        # driver.find_element_by_xpath(utils.XPATH_DROPDOWN).click()
        # driver.find_element_by_xpath(utils.XPATH_DROPDOWN_SUPERBADGES).click()

        # fetch the numbers of Superbadges
        # _numbers_of_superbadges_text = driver.find_element_by_xpath(
        #     utils.XPATH_SUPERBADGES).text
        # _numbers_of_superbadges = utils.get_numbers_of_superbadges(
        #     _numbers_of_superbadges_text, _numbers_of_badges)
        # _numbers_of_superbadges = 'zero'
        # try:
        #     element_superbadges = driver.find_element_by_xpath(utils.XPATH_SUPERBADGES)
        # # if element_superbadges:
        #     _numbers_of_superbadges_ = element_superbadges.text
        # # else:
        # #     _numbers_of_superbadges = '0'
        # except:
        #     _numbers_of_superbadges_ = '0'

        _numbers_of_superbadges = utils.get_numbers_of_superbadges2(driver)

        # fetch the Relationship to Salesforce
        # _name_of_relationship = driver.find_element_by_xpath(utils.XPATH_RELATIONSHIP).text

        # fetch the Company/Institution
        # _name_of_company = driver.find_element_by_xpath(utils.XPATH_COMPANY).text

        # add the trailhead score
        _params = {
            'user_name': self.user_name,
            'user_id': self.user_id,
            'numbers_of_badges': _numbers_of_badges,
            'numbers_of_points': _numbers_of_points,
            'numbers_of_trails': _numbers_of_trails,
            'numbers_of_superbadges': _numbers_of_superbadges,
            'name_of_ranks': _name_of_ranks
            # 'name_of_ranks' : _name_of_ranks,
            # 'name_of_relationship' : _name_of_relationship,
            # 'name_of_company' : _name_of_company
        }
        # _trailhead_score = utils.get_trailhead_score(self.user_name, self.user_id, _numbers_of_badges, _numbers_of_points, _numbers_of_trails, _numbers_of_superbadges, _name_of_ranks)
        _trailhead_score = utils.get_trailhead_score(_params)
        # trailhead_score_list.append(_trailhead_score)

        # take the screenshot
        # element = driver.find_element_by_xpath(utils.XPATH_ABOUT_ME)
        # TrailheadService.getScreenshot(self, driver, element, self.user_name)

        # close Chrome
        driver.close()
        driver.quit()

        # end Log
        # logger.debug('SUCCESS')
        return _trailhead_score

    def getScreenshot(self, driver, element, user_name):
        driver.execute_script(
            'window.scrollTo(0, document.body.scrollHeight);')
        action = ActionChains(driver)
        action.move_to_element(element)
        action.perform()
        path_list = [os.getcwd(), 'result', 'screenshot', user_name + '.png']
        filename = os.path.join(*path_list)
        driver.save_screenshot(filename)
