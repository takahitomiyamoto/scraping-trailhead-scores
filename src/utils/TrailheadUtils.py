#!/usr/bin/env python3
# coding: UTF-8

class TrailheadUtils:
    # constants
    BASE_URL = 'https://trailhead.salesforce.com/en/me/'
    XPATH_BADGES = '//*[@id="main-wrapper"]/div[2]/div/div/div[1]/section/div[2]/div[2]/div/div[1]/div[2]'
    XPATH_POINTS = '//*[@id="main-wrapper"]/div[2]/div/div/div[1]/section/div[2]/div[2]/div/div[2]/div[2]'
    XPATH_TRAILS = '//*[@id="main-wrapper"]/div[2]/div/div/div[1]/section/div[2]/div[2]/div/div[3]/div[2]'
    XPATH_RANKS = '//*[@id="main-wrapper"]/div[2]/div/div/div[1]/section/div[1]/a/img'
    XPATH_DROPDOWN = '//*[@id="main-wrapper"]/div[2]/div/div/div[1]/div[1]/section/div[1]/button'
    XPATH_DROPDOWN_SUPERBADGES = '//*[@id="main-wrapper"]/div[2]/div/div/div[1]/div[1]/section/div[1]/ul/li[1]/a'
    XPATH_SUPERBADGES = '//*[@id="main-wrapper"]/div[2]/div/div/div[1]/div[1]/section/h2'

    # get the target_url
    def get_target_url(self, user_id):
        _target_url = self.BASE_URL + user_id
        return _target_url

    # get the numbers of superbadges
    def get_numbers_of_superbadges(self, text, numbers_of_badges):
        _numbers_of_superbadges_text = text
        _numbers_of_superbadges_text = _numbers_of_superbadges_text.replace('Badges (', '')
        _numbers_of_superbadges_text = _numbers_of_superbadges_text.replace(' of ' + numbers_of_badges + ')', '')
        _numbers_of_superbadges = _numbers_of_superbadges_text
        return _numbers_of_superbadges

    # get the trailhead score
    def get_trailhead_score(self, user_name, user_id, numbers_of_badges, numbers_of_points, numbers_of_trails, numbers_of_superbadges, name_of_ranks):
        _trailhead_score = ''
        _trailhead_score = _trailhead_score + user_name + '\t'
        _trailhead_score = _trailhead_score + user_id + '\t'
        _trailhead_score = _trailhead_score + numbers_of_badges + '\t'
        _trailhead_score = _trailhead_score + numbers_of_points + '\t'
        _trailhead_score = _trailhead_score + numbers_of_trails + '\t'
        _trailhead_score = _trailhead_score + numbers_of_superbadges + '\t'
        _trailhead_score = _trailhead_score + name_of_ranks
        return _trailhead_score
