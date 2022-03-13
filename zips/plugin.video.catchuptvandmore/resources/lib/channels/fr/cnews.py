# -*- coding: utf-8 -*-
# Copyright: (c) 2016, SylvainCecchetto
# GNU General Public License v2.0+ (see LICENSE.txt or https://www.gnu.org/licenses/gpl-2.0.txt)

# This file is part of Catch-up TV & More

from __future__ import unicode_literals
from builtins import str
import re

from codequick import Listitem, Resolver, Route
import htmlement
import urlquick

from resources.lib import resolver_proxy, web_utils
from resources.lib.menu_utils import item_post_treatment


# URL :
URL_ROOT_SITE = 'https://www.cnews.fr'

# Live :
URL_LIVE_CNEWS = URL_ROOT_SITE + '/le-direct'

# Replay CNews
URL_REPLAY_CNEWS = URL_ROOT_SITE + '/replay'
URL_EMISSIONS_CNEWS = URL_ROOT_SITE + '/service/dm_loadmore/dm_emission_index_emissions/%s/0'
# num Page
URL_VIDEOS_CNEWS = URL_ROOT_SITE + '/service/dm_loadmore/dm_emission_index_sujets/%s/0'
# num Page


@Route.register
def list_categories(plugin, item_id, **kwargs):
    """
    Build categories listing
    - Tous les programmes
    - Séries
    - Informations
    - ...
    """
    resp = urlquick.get(URL_REPLAY_CNEWS)
    root = resp.parse("menu", attrs={"class": "index-emission-menu"})

    for category in root.iterfind("ul/li"):
        if category.find('a') is not None:
            category_name = category.find('a').text
        else:
            category_name = category.text
        if 'mission' in category_name:
            category_url = URL_EMISSIONS_CNEWS
        else:
            category_url = URL_VIDEOS_CNEWS

        if category_name != 'Les tops':
            item = Listitem()
            item.label = category_name
            item.set_callback(list_videos,
                              item_id=item_id,
                              category_url=category_url,
                              page='0')
            item_post_treatment(item)
            yield item


@Route.register
def list_videos(plugin, item_id, category_url, page, **kwargs):

    resp = urlquick.get(category_url % page, max_age=-1)
    parser = htmlement.HTMLement()
    parser.feed(resp.json())
    data = parser.close()

    for video_datas in data.iterfind(".//a"):
        video_title = video_datas.find('.//img').get('title')
        video_image = video_datas.find('.//img').get('data-echo')
        video_url = URL_ROOT_SITE + video_datas.get('href')

        item = Listitem()
        item.label = video_title
        item.art['thumb'] = item.art['landscape'] = video_image

        item.set_callback(get_video_url,
                          item_id=item_id,
                          video_url=video_url)
        item_post_treatment(item, is_playable=True, is_downloadable=True)
        yield item

    # More videos...
    yield Listitem.next_page(item_id=item_id,
                             category_url=category_url,
                             page=str(int(page) + 1))


@Resolver.register
def get_video_url(plugin,
                  item_id,
                  video_url,
                  download_mode=False,
                  **kwargs):

    resp = urlquick.get(video_url,
                        headers={'User-Agent': web_utils.get_random_ua()},
                        max_age=-1)
    video_id = re.compile(r'video_id\"\:\"(.*?)[\?\"]').findall(
        resp.text)[0]
    return resolver_proxy.get_stream_dailymotion(plugin, video_id,
                                                 download_mode)


@Resolver.register
def get_live_url(plugin, item_id, **kwargs):

    resp = urlquick.get(URL_LIVE_CNEWS,
                        headers={'User-Agent': web_utils.get_random_ua()},
                        max_age=-1)
    live_id = re.compile(r'video_id\"\:\"(.*?)[\?\"]',
                         re.DOTALL).findall(resp.text)[0]
    return resolver_proxy.get_stream_dailymotion(plugin, live_id, False)
