#!/usr/bin/env python3
# coding: UTF-8

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import utils.Trailhead
import csv

# constants
UTF_8 = 'utf-8'
CSV_FILE_NAME = 'data/trailhead_users.csv'
TSV_FILE_NAME = 'result/trailhead_scores.tsv'

# global variables
_user_list = []
_trailhead_score_list = []

# main
def main():
    # read from .csv
    with open(CSV_FILE_NAME) as csv_file:
        _csv_reader = csv.reader(csv_file)
        for csv_reader_row in _csv_reader:
            _user_list.append(csv_reader_row)

    # loop for each users
    for user_list_row in _user_list:
        get_trailhead_score(user_list_row)

    # write to .tsv
    with open(TSV_FILE_NAME, 'w') as tsv_file:
        for trailhead_score_list_row in _trailhead_score_list:
            print(trailhead_score_list_row, file=tsv_file)

# get the trailhead score
def get_trailhead_score(user):
    # Chrome headless mode
    _options = Options()
    _options.set_headless(True)

    # initialize
    trailhead = utils.Trailhead.Trailhead(user)

    # open Chrome
    _target_url = trailhead.get_target_url()
    driver = webdriver.Chrome(chrome_options=_options)
    driver.get(_target_url)

    # fetch the numbers of Badges
    _numbers_of_badges = driver.find_element_by_xpath(trailhead.XPATH_BADGES).text

    # fetch the numbers of Points
    _numbers_of_points = driver.find_element_by_xpath(trailhead.XPATH_POINTS).text

    # fetch the numbers of Trails Completed
    _numbers_of_trails = driver.find_element_by_xpath(trailhead.XPATH_TRAILS).text

    # click the dropdown and select Superbadges
    driver.find_element_by_xpath(trailhead.XPATH_DROPDOWN).click()
    driver.find_element_by_xpath(trailhead.XPATH_DROPDOWN_SUPERBADGES).click()

    # fetch the numbers of Superbadges
    _numbers_of_superbadges_text = driver.find_element_by_xpath(trailhead.XPATH_SUPERBADGES).text
    _numbers_of_superbadges = trailhead.get_numbers_of_superbadges(_numbers_of_superbadges_text, _numbers_of_badges)

    # add the trailhead score
    _trailhead_score = trailhead.get_trailhead_score(_numbers_of_badges, _numbers_of_points, _numbers_of_trails, _numbers_of_superbadges)
    _trailhead_score_list.append(_trailhead_score)

    # close Chrome
    driver.close()
    driver.quit()


# execute main
main()
