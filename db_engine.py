# -*- coding: utf-8 -*-
#####################################################################################################################
#                                                                                                                   #
# Database working solution                                                                                         #
#                                                                                                                   #
# MIT License                                                                                                       #
# Copyright (c) 2020 Michael Nikitenko and Yuri Legkiy                                                              #
#                                                                                                                   #
#####################################################################################################################


from typing import Union

import psycopg2
from psycopg2.extras import DictCursor
from psycopg2.errors import NotNullViolation, UndefinedColumn, InvalidTextRepresentation, InFailedSqlTransaction

from configs import DB_NAME, DB_USER, DB_PASS, DB_HOST


conn = psycopg2.connect(dbname=DB_NAME, user=DB_USER, password=DB_PASS, host=DB_HOST)
cursor = conn.cursor(cursor_factory=DictCursor)


def prepare_data_to_db(data: dict) -> dict:
    """Подготавливает данные для вставки в SQL запросы"""
    for key in data:
        value_type = type(data[key])
        if not data[key]:       # Если передано None
            data[key] = 'NULL'
        if value_type == str:   # Если передана строка, то её нужно обрамлять в кавычки
            data[key] = f"'{data[key]}'"
    return data


def get_channels_list() -> list:
    """Возвращает список каналов"""
    query = """SELECT ch.id, title, username, link,  about, img, author, organization, 
    tgstat_id, tg_id, t.name 
    FROM channels AS ch
    LEFT JOIN themes AS t ON t.id = ch.theme_id"""
    cursor.execute(query=query)
    res = cursor.fetchall()
    return res


def get_channel_by_id(channel_id: int):
    """Получает id канала в базе и возвращает информацию о канале"""
    query = f"""SELECT title, username, link, about, img, author, organization, tgstat_id, tg_id, t.name as theme 
    FROM channels AS ch
    LEFT JOIN themes AS t ON t.id = ch.theme_id
    WHERE ch.id = {channel_id}"""
    empty_answer = {'title': None, 'username': None, 'link': None, 'about': None, 'img': None, 'author': None,
                    'organization': None, 'tgstat_id': None, 'tg_id': None, 'theme': None}

    try:                                    # Попытка выполнить запрос с обработкой исключений
        cursor.execute(query=query)
    except UndefinedColumn as e:            # Если передана строка
        print(e)
        return empty_answer
    except InFailedSqlTransaction as e:     # Если передана строка с кавычкой
        print(e)
        return empty_answer

    res = cursor.fetchone()                 # Если запрос отработал удачно. Попытка достать строку.
    if res is None:                         # Если в базе нет такой строки, то возвращаем словарь с пустыми значениями
        return empty_answer
    else:                                   # Иначе возвращаем строку с данными
        return res


def get_posts_list(channel_id: int) -> list:
    """Получает id канала ивозвращает список постов канала"""
    query = f"""SELECT 'date', views, link FROM posts WHERE channel_id = {channel_id}"""
    try:                                    # Пытаемся выполнить запрос
        cursor.execute(query=query)
    except UndefinedColumn as e:            # Если передана строка или None
        print(e)
        return []
    except InFailedSqlTransaction as e:     # Если передана строка в кавычках
        print(e)
        return []
    res = cursor.fetchall()
    return res


def get_channel_data(channel_id: int) -> dict:
    """Возвращает информацию о канале"""
    query = f"""SELECT parsing_date, subs, arg_post_reach, err, daily_reach, ci_index
    FROM channel_data WHERE channel_id = {channel_id}"""
    empty_answer = {'parsing_date': None, 'subs': None, 'arg_post_reach': None, 'err': None, 'daily_reach': None,
                    'ci_index': None}

    try:                                    # Пытаемся выполнить запрос
        cursor.execute(query=query)
    except UndefinedColumn as e:            # Если передана строка, либо None
        print(e)
        return empty_answer
    except InFailedSqlTransaction as e:     # Если передана строка в кавычках
        print(e)
        return empty_answer

    res = cursor.fetchall()                 # Если запрос отработал удачно
    if res is None:                         # Если в базе нет такой строки, то возвращаем словарь с пустыми значениями
        return empty_answer
    else:                                   # Иначе возвращаем строку с данными
        return res


def insert_channel(title: str, username: str, link: str, about: str, img: str, author: str,
                   organization: str, theme_id: int, tgstat_id: int, tg_id: int) -> Union[int, None]:
    """Добавляет канал в базу данных"""
    d = prepare_data_to_db({'title': title, 'username': username, 'link': link, 'about': about, 'img': img,
                            'author': author, 'organization': organization, 'theme_id': theme_id,
                            'tgstat_id': tgstat_id, 'tg_id': tg_id})
    query = f"""INSERT INTO channels 
    (title, username, link, about, img, author, organization, theme_id, tgstat_id, tg_id)
    VALUES ({d['title']}, {d['username']}, {d['link']}, {d['about']}, {d['img']}, {d['author']}, {d['organization']},
    {d['theme_id']}, {d['tgstat_id']}, {d['tg_id']}) RETURNING id;"""
    try:
        cursor.execute(query=query)
    except NotNullViolation as e:
        print(e)
        return None
    res = cursor.fetchone()[0]
    conn.commit()
    return res


def insert_channel_data(channel_id: int, parsing_date: int, subs: int, arg_post_reach: int, err: float,
                        daily_reach: int, ci_index: float) -> int:
    """Добавляет показатели канала в базу данных"""
    d = prepare_data_to_db({'channel_id': channel_id, 'parsing_date': parsing_date, 'subs': subs,
                            'arg_post_reach': arg_post_reach, 'err': err, 'daily_reach': daily_reach,
                            'ci_index': ci_index})
    return d['channel_id']  # TODO: Реализовать вставку данных о канале в БД


def insert_posts(posts_data: list) -> bool:
    """Добавляет посты в базу данных"""
    for post in posts_data:
        print(post)
    return True     # TODO: Реализовать вставку списка постов в БД


def insert_theme(theme_name: str) -> int:
    """Добавляет тематику каналов в базу данных"""
    d = prepare_data_to_db({'theme_name': theme_name})
    print(d['theme_name'])
    return 1    # TODO: Реализовать вставку темы в базу данных


def update_channel_by_tg_id(title: str, username: str, link: str, about: str, img: str, author: str, organization: str,
                            theme_id: int, tgstat_id: int, tg_id: int) -> bool:
    """Обновляет информацию о канале в базе данных"""
    if not tg_id:   # Если не передан основной параметр. ID телеграм канала который надо отредактировать
        return False
    d = prepare_data_to_db(
        {
            'title': title,
            'username': username,
            'link': link,
            'about': about,
            'img': img,
            'author': author,
            'organization':  organization,
            'theme_id': theme_id,
            'tgstat_id': tgstat_id
        }
    )
    query = f"""UPDATE channels 
    SET title = {d['title']}, username = {d['username']}, link = {d['link']}, about = {d['about']}, img = {d['img']}, 
    author = {d['author']}, organization = {d['organization']}, theme_id = {d['theme_id']}, tgstat_id = {d['tgstat_id']} 
    WHERE tg_id = {tg_id};"""
    try:
        cursor.execute(query=query)
    except NotNullViolation as e:
        print(e)
        return False
    conn.commit()
    return True


def update_channel_data(channel_data_id: int, channel_id: int, parsing_date: int, subs: int,
                        arg_post_reach: int, err: float, daily_reach: int, ci_index: float) -> int:
    """Обновляет показатели канала в конкретную дату в базе данных"""
    d = prepare_data_to_db({'channel_data_id': channel_data_id, 'channel_id': channel_id, 'parsing_date': parsing_date,
                            'subs': subs, 'arg_post_reach': arg_post_reach, 'err': err, 'daily_reach': daily_reach,
                            'ci_index': ci_index})
    return d['channel_data_id']     # TODO: Реализовать обновление показателей канала


def update_post(channel_id: int, date: int, views: int, link: str) -> bool:  # По ссылке на пост
    """Обновляет информацию о публикации в базе данных"""
    d = prepare_data_to_db({'channel_id': channel_id, 'date': date, 'views': views, 'link': link})
    print(d)
    return True     # TODO: Реализовать обновление постов


def update_theme(theme_id: int, theme_name: str) -> bool:
    """Обновляет информацию о тематике в базе данных"""
    d = prepare_data_to_db({'theme_name': theme_name, 'theme_id': theme_id})
    print(d)
    return True     # TODO: Реализовать обновление темы


def delete_channel_by_tg_id(tg_id: int) -> bool:
    """Удаляет канал из базы данных"""
    query = f"""WITH deleted AS (DELETE FROM channels WHERE tg_id = {tg_id} RETURNING *) SELECT count(*) FROM deleted"""
    try:
        cursor.execute(query=query)
    except UndefinedColumn as e:            # Если передана строка
        print(e)
        return False
    except InvalidTextRepresentation as e:  # Если передана строка в кавычках
        print(e)
        return False
    res = cursor.fetchone()[0]
    conn.commit()
    if res == 0:                            # Если количество удалённых строк равно нулю, значит что-то пошло не так
        return False
    return True


def delete_channel_data(channel_data_id: int) -> bool:
    """Удаляет показатели канала за конкретную дату"""
    print(channel_data_id)
    return True     # TODO: Реализовать удаление показателей канала


def delete_post(post_id: int) -> bool:
    """Удаляет публикацию из базы данных"""
    print(post_id)
    return True     # TODO: Реализовать удаление поста


def delete_theme(theme_id) -> bool:
    """Удаляет тематику из базы данных"""
    print(theme_id)
    return True     # TODO: Реализовать удаление темы


if __name__ == '__main__':
    print('db_engine')
    # channels_list = get_channels_list()
    # print(type(channels_list))
    # for channel in channels_list:
    #     print(channel)
    #     posts = get_posts_list(channel['id'])
    #     channel_data = get_channel_data(channel['id'])
    #     print('data')
    #     for data in channel_data:
    #         print(data)
    #     print('posts')
    #     for post in posts:
    #         print(post)
    # channel_id = insert_channel(
    #     title=None,
    #     username='@greta_tuborg',
    #     link='https://t.me/tipidor',
    #     about='tuborg description',
    #     img='//static10.tgstat.ru/channels/_0/9e/9ebe56f04checked27f86706abed6436.jpg',
    #     author='Мишаня',
    #     organization='SC',
    #     theme_id=1,
    #     tgstat_id=5969949,
    #     tg_id=1457040805
    # )
    # print(channel_id)
    # channel = get_channel_by_id(channel_id)
    # print(channel)
    # # channel = get_channel_by_id(1000)
    # # print(channel)
    # # channel = get_channel_by_id('1000')
    # # print(channel)
    # # channel = get_channel_by_id('a')
    # # print(channel)
    # # channel = get_channel_by_id('\'a\'')
    # # print(channel)
    # update_status = update_channel_by_tg_id(
    #     title='updated title',
    #     username=None,
    #     link=None,
    #     about=None,
    #     img=None,
    #     author=None,
    #     organization=None,
    #     theme_id=None,
    #     tgstat_id=None,
    #     tg_id=channel['tg_id']
    # )
    # print(update_status)
    # updated_channel = get_channel_by_id(channel_id)
    # print(updated_channel)
    # delete_status = delete_channel_by_tg_id(tg_id=channel['tg_id'])
    # # delete_status = delete_channel_by_tg_id(tg_id=100)
    # print(delete_status)
    # posts = get_posts_list(1000)
    # print(posts)
    # posts = get_posts_list('a')
    # posts = get_posts_list("'a'")
    # posts = get_posts_list(None)
    # channel_data = get_channel_data(1000)
    # print(channel_data)
    # channel_data = get_channel_data('a')
    # print(channel_data)
    # channel_data = get_channel_data("'a'")
    # print(channel_data)
    # channel_data = get_channel_data(None)
    # print(channel_data)
