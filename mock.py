import requests

from configs import API_TOKEN


# https://api.tgstat.ru/channels/stat
payload_stat = {
    'token': API_TOKEN,
    'channelId': 5969949,
}
channels_stat = {
    "status": "ok",
    "response": {
        "id": 5969949,
        "title": "Gretый Tuborg",
        "username": "@greta_tuborg",
        "participants_count": 18,   # Количество подписчиков
        "avg_post_reach": 19,
        "err_percent": 105.6,
        "daily_reach": 71,
        "ci_index": None
    }
}

# https://api.tgstat.ru/channels/posts
payload_posts = {
        'token': API_TOKEN,
        'channelId': '@greta_tuborg',
        'limit': 50,
        'extended': 1,
    }
channels_posts ={
    "status": "ok",
    "response": {
        "count": 9,
        "total_count": 9,
        "channel": {
            "id": 5969949,
            "tg_id": 1457040805,
            "link": "t.me/greta_tuborg",
            "username": "@greta_tuborg",
            "title": "Gretый Tuborg",
            "about": "Самые объективные и неподкупные посты вы найдёте только здесь.",
            "image100": "//static10.tgstat.ru/channels/_100/9e/9ebe56f04cecdcdb27f86706abed6436.jpg",
            "image640": "//static10.tgstat.ru/channels/_0/9e/9ebe56f04cecdcdb27f86706abed6436.jpg",
            "participants_count": 18,
            "tgstat_restrictions": []
        },
        "items": [
            {
                "id": 15761865587,
                "date": 1615742287,
                "views": 4,
                "link": "t.me/greta_tuborg/274",
                "channel_id": 5969949,
                "forwarded_from": 2519,
                "is_deleted": 0,
                "deleted_at": None,
                "text": "",
                "media": {
                    "media_type": "mediaDocument",
                    "mime_type": "video/mp4",
                    "size": 3155305,
                    "duration": 13,
                    "file_name": "@dvachannel ⚡ Двач.mp4",
                    "file_size": None,
                    "file_url": None,
                    "file_thumbnail_url": None
                }
            },
            {
                "id": 15761865587,
                "date": 1615742277,
                "views": 4,
                "link": "t.me/greta_tuborg/273",
                "channel_id": 5969949,
                "forwarded_from": 2519,
                "is_deleted": 0,
                "deleted_at": None,
                "text": "",
                "media": {
                    "media_type": "mediaDocument",
                    "mime_type": "video/mp4",
                    "size": 3155305,
                    "duration": 13,
                    "file_name": "@dvachannel ⚡ Двач.mp4",
                    "file_size": None,
                    "file_url": None,
                    "file_thumbnail_url": None
                }
            },
            {
                "id": 15761865587,
                "date": 1615742267,
                "views": 4,
                "link": "t.me/greta_tuborg/272",
                "channel_id": 5969949,
                "forwarded_from": 2519,
                "is_deleted": 0,
                "deleted_at": None,
                "text": "",
                "media": {
                    "media_type": "mediaDocument",
                    "mime_type": "video/mp4",
                    "size": 3155305,
                    "duration": 13,
                    "file_name": "@dvachannel ⚡ Двач.mp4",
                    "file_size": None,
                    "file_url": None,
                    "file_thumbnail_url": None
                }
            },
            {
                "id": 15761865587,
                "date": 1615742257,
                "views": 4,
                "link": "t.me/greta_tuborg/271",
                "channel_id": 5969949,
                "forwarded_from": 2519,
                "is_deleted": 0,
                "deleted_at": None,
                "text": "",
                "media": {
                    "media_type": "mediaDocument",
                    "mime_type": "video/mp4",
                    "size": 3155305,
                    "duration": 13,
                    "file_name": "@dvachannel ⚡ Двач.mp4",
                    "file_size": None,
                    "file_url": None,
                    "file_thumbnail_url": None
                }
            },
            {
                "id": 15761865587,
                "date": 1615742247,
                "views": 4,
                "link": "t.me/greta_tuborg/270",
                "channel_id": 5969949,
                "forwarded_from": 2519,
                "is_deleted": 0,
                "deleted_at": None,
                "text": "",
                "media": {
                    "media_type": "mediaDocument",
                    "mime_type": "video/mp4",
                    "size": 3155305,
                    "duration": 13,
                    "file_name": "@dvachannel ⚡ Двач.mp4",
                    "file_size": None,
                    "file_url": None,
                    "file_thumbnail_url": None
                }
            },
        ]
    }
}

# https://api.tgstat.ru/channels/get
payload_get = {
    'token': API_TOKEN,
    'channelId': 5969949,
}
channels_get = {
    "status": "ok",
    "response": {
        "id": 5969949,
        "tg_id": 1457040805,
        "link": "t.me/greta_tuborg",
        "username": "@greta_tuborg",
        "title": "Gretый Tuborg",
        "about": "Самые объективные и неподкупные посты вы найдёте только здесь.",
        "image100": "//static10.tgstat.ru/channels/_100/9e/9ebe56f04cecdcdb27f86706abed6436.jpg",
        "image640": "//static10.tgstat.ru/channels/_0/9e/9ebe56f04cecdcdb27f86706abed6436.jpg",
        "participants_count": 18,
        "tgstat_restrictions": []
    }
}


if __name__ == '__main__':
    print('Тестовый скрипт для всей хуйни')
    # payload = {
    #     'token': API_TOKEN,
    #     'channelId': '@greta_tuborg',
    #     'limit': 50,
    #     'extended': 1,
    # }   # channels/posts
    # payload = {
    #     'token': API_TOKEN,
    #     'channelId': 5969949,
    # }
    # req = requests.get(url='https://api.tgstat.ru/channels/get', params=payload)
    # print('text')
    # print(req.json())
