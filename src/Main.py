#!/usr/bin/env python3
# coding: UTF-8

import csv
from services import TrailheadService

class Main:
    # constants
    CSV_FILE_NAME = 'data/trailhead_users.csv'
    TSV_FILE_NAME = 'result/trailhead_scores.tsv'

    # global variables
    user_list = []
    trailhead_score_list = []

    # main
    def main(self):
        # read from .csv
        with open(self.CSV_FILE_NAME) as csv_file:
            _csv_reader = csv.reader(csv_file)
            for csv_reader_row in _csv_reader:
                self.user_list.append(csv_reader_row)

        # loop for each users
        for user_list_row in self.user_list:
            service = TrailheadService.TrailheadService(user_list_row)
            _trailhead_score = service.get_trailhead_score(user_list_row)
            self.trailhead_score_list.append(_trailhead_score)

        # write to .tsv
        with open(self.TSV_FILE_NAME, 'w') as tsv_file:
            for trailhead_score_list_row in self.trailhead_score_list:
                print(trailhead_score_list_row, file=tsv_file)


# execute main
main = Main()
main.main()
