#!/usr/bin/env python3
# coding: UTF-8
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

class TrailheadUtils:
    # constants
    # BASE_URL = 'https://trailhead.salesforce.com/en/me/'
    BASE_URL = 'https://trailblazer.me/id?uid='
    SUFFIX_URL = '&cmty=trailhead'
    XPATH_BADGES = '//*[@id="lightning"]/div/div/div[2]/div/div[2]/div/div/div[2]/c-trailhead-rank/c-lwc-card/article/div/slot/div[2]/c-lwc-tally[1]/span/span[1]'
    XPATH_POINTS = '//*[@id="lightning"]/div/div/div[2]/div/div[2]/div/div/div[2]/c-trailhead-rank/c-lwc-card/article/div/slot/div[2]/c-lwc-tally[2]/span/span[1]'
    XPATH_TRAILS = '//*[@id="lightning"]/div/div/div[2]/div/div[2]/div/div/div[2]/c-trailhead-rank/c-lwc-card/article/div/slot/div[2]/c-lwc-tally[3]/span/span[1]'
    XPATH_RANKS = '//*[@id="lightning"]/div/div/div[2]/div/div[2]/div/div/div[2]/c-trailhead-rank/c-lwc-card/article/div/slot/div[1]/img'
    XPATH_DROPDOWN = '//*[@id="lightning"]/div/div/div[2]/div/div[2]/div/div/div/c-lwc-trailhead-badges/c-lwc-card/article/c-lwc-card-header/div/header/div[2]/slot/slot/lightning-combobox/div/lightning-base-combobox/div'
    XPATH_DROPDOWN_SUPERBADGES = '//*[@id="input-96-1-96"]/span[2]'
    # XPATH_SUPERBADGES = '//*[@id="lightning"]/div/div/div[2]/div/div[2]/div/div/div/c-lwc-trailhead-badges/c-lwc-card/article/c-lwc-card-header/div/header/div[1]/div/h2'
    XPATH_SUPERBADGES = '//*[@id="lightning"]/div/div/div[2]/div/div[2]/div/div/div[1]/c-lwc-achievements/c-lwc-card/article/div/slot/h3[2]'
    # XPATH_ABOUT_ME = '//*[@id="main-wrapper"]/main/div/div/div/div[1]/div[2]/section/form/div[1]/h2'
    # XPATH_RELATIONSHIP = '//*[@id="main-wrapper"]/main/div/div/div/div[1]/div[2]/section/form/div[2]/div[5]/div/div/span'
    # XPATH_COMPANY = '//*[@id="main-wrapper"]/main/div/div/div/div[1]/div[2]/section/form/div[2]/div[6]/div/div/span'

    # get the target_url
    def get_target_url(self, user_id):
        _target_url = self.BASE_URL + user_id + self.SUFFIX_URL
        return _target_url

    # get the numbers of superbadges
    def get_numbers_of_superbadges(self, text, numbers_of_badges):
        _numbers_of_superbadges_text = text
        _numbers_of_superbadges_text = _numbers_of_superbadges_text.replace(
            'Badges (', '')
        _numbers_of_superbadges_text = _numbers_of_superbadges_text.replace(
            ' of ' + numbers_of_badges + ')', '')
        _numbers_of_superbadges = _numbers_of_superbadges_text
        return _numbers_of_superbadges

    def get_numbers_of_superbadges2(self, driver):
        try:
            wait = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.XPATH, '//*[@id="lightning"]/div/div/div[2]/div/div[2]/div/div/div[1]/c-lwc-achievements'))
            )
            element_superbadges = wait.until(driver.find_element_by_xpath(XPATH_SUPERBADGES))
            # SELECTOR_SUPERBADGES = '#lightning > div > div > div.main > div > div.slds-container_x-large.slds-container_center.profile-content > div > div > div.slds-col.slds-size_1-of-1.slds-medium-size_1-of-2.slds-large-size_2-of-3.slds-shrink-none > c-lwc-achievements > c-lwc-card > article > div > slot > h3:nth-child(6)'
            # element_superbadges = driver.find_element_by_css_selector(SELECTOR_SUPERBADGES)

            _numbers_of_superbadges = element_superbadges.text
        except:
            _numbers_of_superbadges = 'zero'
        return _numbers_of_superbadges

    # get the trailhead score
    # def get_trailhead_score(self, user_name, user_id, numbers_of_badges, numbers_of_points, numbers_of_trails, numbers_of_superbadges, name_of_ranks):
    def get_trailhead_score(self, params):
        _trailhead_score = ''
        _trailhead_score = _trailhead_score + params['user_name'] + '\t'
        _trailhead_score = _trailhead_score + params['user_id'] + '\t'
        _trailhead_score = _trailhead_score + \
            params['numbers_of_badges'] + '\t'
        _trailhead_score = _trailhead_score + \
            params['numbers_of_points'] + '\t'
        _trailhead_score = _trailhead_score + \
            params['numbers_of_trails'] + '\t'
        _trailhead_score = _trailhead_score + \
            params['numbers_of_superbadges'] + '\t'
        _trailhead_score = _trailhead_score + params['name_of_ranks']
        # _trailhead_score = _trailhead_score + params['name_of_ranks'] + '\t'
        # _trailhead_score = _trailhead_score + params['name_of_relationship'] + '\t'
        # _trailhead_score = _trailhead_score + params['name_of_company'] + '\t'
        return _trailhead_score
