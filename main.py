import pdb
import json
import os
import time
import settings as s

import tools.scraping as scrap
from tools.tool_requests import get_request, basic_auth, send_to_telegram, Response
from tools.tool_json_db import create_file, get_data_from_json, save_data_as_json

def auth_tesmanian():
    bauth = basic_auth(s.AUTH_URL, s.LOGIN, s.PASSWORD)
    if isinstance(bauth, Response):
        s.logger.info(f"auth: {bauth.status_code}")
    else:
        s.logger.error(f"auth: {bauth}")



def main():
    path_json = os.path.join(s.BASE_DIR, s.JSON_DB_DIR, s.JSON_DB)
    create_file(path_json)

    s.logger.info("Start scrapign")
    
    auth_tesmanian()    

    while 1:
        response = get_request(s.PARSING_URL)
        if isinstance(response, Response):
            s.logger.info(f"get news: {response.status_code}")
            if response.status_code == 401:
                auth_tesmanian()
        else:
            s.logger.error(f"get news: {response}")
            time.sleep(s.PERIOD)
            continue       

        soup = scrap.parsing_request(response)
        all_news = scrap.get_news_tasmania(soup)
        last_news = scrap.get_last_news_tasmania(soup)

        storage_news = get_data_from_json(path_json)
        if not storage_news:
            save_data_as_json(all_news, path_json)  # save all_news to jsondb
            storage_news = all_news

        title_last_news = list(last_news.keys())[0]
        if title_last_news not in storage_news.keys():

            s.logger.info(title_last_news)

            # save to database
            storage_news.update(last_news)
            save_data_as_json(storage_news, path_json)

            # send to bot
            message = f"{title_last_news}\n\n{last_news[title_last_news]}"
            send = send_to_telegram(
                message=message, apiToken=s.BOT_TOKEN, chatID=s.CHAT_ID)
            if not isinstance(send, Response):
                s.logger.error(f"NOT sending {title_last_news}\n{send}")
        
        # pdb.set_trace()        
        time.sleep(s.PERIOD)


if __name__ == "__main__":
    main()
