# -*- coding: utf-8 -*-
#####################################################################################################################
#                                                                                                                   #
# Database working solution                                                                                         #
#                                                                                                                   #
# MIT License                                                                                                       #
# Copyright (c) 2020 Michael Nikitenko and Yuri Legkiy                                                              #
#                                                                                                                   #
#####################################################################################################################


import psycopg2
from psycopg2.extras import DictCursor

from configs import DB_NAME, DB_USER, DB_PASS, DB_HOST


conn = psycopg2.connect(dbname=DB_NAME, user=DB_USER, password=DB_PASS, host=DB_HOST)
cursor = conn.cursor(cursor_factory=DictCursor)


def get_channels_list() -> list:
    """Возвращает список каналов"""
    query = """SELECT ch.id, title, username, link,  about, img, author, organization, t.name 
    FROM channels AS ch
    LEFT JOIN themes AS t ON t.id = ch.theme_id"""
    cursor.execute(query=query)
    res = cursor.fetchall()
    return res


def get_posts_list(channel_id: int) -> list:
    """Получает id канала ивозвращает список постов канала"""
    query = f"""SELECT 'date', views, link FROM posts WHERE channel_id = {channel_id}"""
    cursor.execute(query=query)
    res = cursor.fetchall()
    return res


def get_channel_data(channel_id: int) -> list:
    """Возвращает информацию о канале"""
    query = f"""SELECT parsing_date, subs, arg_post_reach, err, daily_reach, ci_index
    FROM channel_data WHERE channel_id = {channel_id}"""
    cursor.execute(query=query)
    res = cursor.fetchall()
    return res


def insert_channel(title: str, username: str, link: str, about: str, img: str, author: str,
                   organization: str, theme_id: int, tgstat_id: int, tg_id: int) -> int:
    """Добавляет канал в базу данных"""
    pass


def insert_channel_data(channel_id: int, parsing_date: int, subs: int, arg_post_reach: int, err: float,
                        daily_reach: int, ci_index: float) -> int:
    """Добавляет показатели канала в базу данных"""
    pass


def insert_posts(posts_data: list) -> bool:
    """Добавляет посты в базу данных"""
    pass


def insert_theme(theme_name: str) -> int:
    """Добавляет тематику каналов в базу данных"""
    pass


def update_channel(channel_id: int, title: str, username: str, link: str, about: str, img: str,
                   author: str, organization: str, theme_id: int, tgstat_id: int, tg_id: int) -> bool:
    """Обновляет информацию о канале в базе данных"""
    pass


def update_channel_data(channel_data_id: int, channel_id: int, parsing_date: int, subs: int,
                        arg_post_reach: int, err: float, daily_reach: int, ci_index: float) -> int:
    """Обновляет показатели канала в конкретную дату в базе данных"""
    pass


def update_post(channel_id: int, date: int, views: int, link: str) -> bool:  # По ссылке на пост
    """Обновляет информацию о публикации в базе данных"""
    pass


def update_theme(theme_id: int, theme_name: str):
    """Обновляет информацию о тематике в базе данных"""
    pass


def delete_channel(channel_id: int) -> bool:
    """Удаляет канал из базы данных"""
    pass


def delete_channel_data(channel_data_id: int) -> bool:
    """Удаляет показатели канала за конкретную дату"""
    pass


def delete_post(post_id: int) -> bool:
    """Удаляет публикацию из базы данных"""
    pass


def delete_theme(theme_id) -> bool:
    """Удаляет тематику из базы данных"""
    pass


if __name__ == '__main__':
    channels_list = get_channels_list()
    print(type(channels_list))
    for channel in channels_list:
        print(channel)
        posts = get_posts_list(channel['id'])
        channel_data = get_channel_data(channel['id'])
        print('data')
        for data in channel_data:
            print(data)
        print('posts')
        for post in posts:
            print(post)
