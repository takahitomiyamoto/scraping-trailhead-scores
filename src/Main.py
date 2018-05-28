#!/usr/bin/env python3
# coding: UTF-8

import csv
import os
from services import TrailheadService
from utils import LogUtils

class Main:
    # constants
    CSV_FILE_NAME = 'data/trailhead_users.csv'
    TSV_FILE_NAME = 'result/trailhead_scores.tsv'

    # main
    def main(self):
        _user_list = []
        _trailhead_score_list = []

        # start Log
        logger = LogUtils.LogUtils()

        # read from .csv
        logger.debug('Read ' + os.getcwd() + '/' + self.CSV_FILE_NAME)
        with open(self.CSV_FILE_NAME) as csv_file:
            _csv_reader = csv.reader(csv_file)
            for csv_reader_row in _csv_reader:
                _user_list.append(csv_reader_row)

        logger.debug('CSV Size: ' + str(len(_user_list)))

        # loop for each users
        for user_list_row in _user_list:
            service = TrailheadService.TrailheadService(user_list_row)
            _trailhead_score = service.get_trailhead_score(user_list_row)
            logger.debug('***** ' + _trailhead_score)
            _trailhead_score_list.append(_trailhead_score)

        logger.debug('TSV Size: ' + str(len(_trailhead_score_list)))

        # write to .tsv
        with open(self.TSV_FILE_NAME, 'w') as tsv_file:
            for trailhead_score_list_row in _trailhead_score_list:
                print(trailhead_score_list_row, file=tsv_file)

        logger.debug('Save ' + os.getcwd() + '/' + self.TSV_FILE_NAME)


# execute main
main = Main()
main.main()
