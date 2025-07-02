import pandas as pd
import numpy as np
import json

from app_store_scraper import AppStore
# -*- coding: utf-8 -*-

# App details for "ドコモ-バイクシェア-バイクシェアサービス"
app_name = u'ドコモ-バイクシェア-バイクシェアサービス'
# Encoding into bytes (UTF-8)
app_name_utf8 = app_name.encode('utf-8')
print(app_name_utf8)  # Outputs the byte string

# If you're passing this to a function that expects bytes
def process_utf8_input(data):
    print(data.decode('utf-8'))  # Decodes back into a readable string

process_utf8_input(app_name_utf8)

app_id = '1216653677'
slack = AppStore(country='jp', app_name=app_name_utf8, app_id=app_id)
slack.review(how_many=200000000000000000)
slackdf = pd.DataFrame(np.array(slack.reviews),columns=['review'])
slackdf2 = slackdf.join(pd.DataFrame(slackdf.pop('review').tolist()))
slackdf2.head()
slackdf2.to_csv('Docomo.csv')
