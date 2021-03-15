# -*- coding: utf-8 -*-
#####################################################################################################################
#                                                                                                                   #
# Database working solution                                                                                         #
#                                                                                                                   #
# MIT License                                                                                                       #
# Copyright (c) 2020 Michael Nikitenko                                                                              #
#                                                                                                                   #
#####################################################################################################################


import psycopg2
from psycopg2.extras import DictCursor

from configs import DB_NAME, DB_USER, DB_PASS, DB_HOST


conn = psycopg2.connect(dbname=DB_NAME, user=DB_USER, password=DB_PASS, host=DB_HOST)
cursor = conn.cursor(cursor_factory=DictCursor)