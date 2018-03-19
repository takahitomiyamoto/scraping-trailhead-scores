#!/usr/bin/env python3
# coding: UTF-8

from selenium import webdriver
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
        _options.set_headless(True)

        # set URL
        utils = TrailheadUtils.TrailheadUtils()
        _target_url = utils.get_target_url(self.user_id)

        # start Log
        logger = LogUtils.LogUtils()
        logger.debug('OPEN ' + _target_url + ' (' + self.user_name + ')')

        # open Chrome
        driver = webdriver.Chrome(chrome_options=_options)
        driver.get(_target_url)

        # fetch the numbers of Badges
        _numbers_of_badges = driver.find_element_by_xpath(utils.XPATH_BADGES).text

        # fetch the numbers of Points
        _numbers_of_points = driver.find_element_by_xpath(utils.XPATH_POINTS).text

        # fetch the numbers of Trails Completed
        _numbers_of_trails = driver.find_element_by_xpath(utils.XPATH_TRAILS).text

        # fetch the name of Trailblazer Ranks
        _name_of_ranks = driver.find_element_by_xpath(utils.XPATH_RANKS).get_attribute('alt')

        # click the dropdown and select Superbadges
        driver.find_element_by_xpath(utils.XPATH_DROPDOWN).click()
        driver.find_element_by_xpath(utils.XPATH_DROPDOWN_SUPERBADGES).click()

        # fetch the numbers of Superbadges
        _numbers_of_superbadges_text = driver.find_element_by_xpath(utils.XPATH_SUPERBADGES).text
        _numbers_of_superbadges = utils.get_numbers_of_superbadges(_numbers_of_superbadges_text, _numbers_of_badges)

        # add the trailhead score
        _trailhead_score = utils.get_trailhead_score(self.user_name, self.user_id, _numbers_of_badges, _numbers_of_points, _numbers_of_trails, _numbers_of_superbadges, _name_of_ranks)
        # trailhead_score_list.append(_trailhead_score)

        # close Chrome
        driver.close()
        driver.quit()

        # end Log
        logger.debug('SUCCESS')
        return _trailhead_score

