# Module: save
# Author: Rayflix
# Created on: 18.11.2021
import sys
import xbmcplugin
import xbmcvfs
from urllib.parse import quote_plus, unquote_plus
import xbmcgui
import xbmc

artworkPath = xbmcvfs.translatePath('special://home/addons/plugin.program.saverayflix/resources/media/')
fanart = artworkPath + "fanart.jpg"

def add_dir(name, url, mode, thumb):
    u = sys.argv[0] + "?url=" + quote_plus(url) + "&mode=" + str(mode) + "&name=" + quote_plus(name)
    liz = xbmcgui.ListItem(name)
    liz.setArt({'icon': thumb})
    liz.setProperty("fanart_image", fanart)
    ok = xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]), url=u, listitem=liz, isFolder=True)
    return ok

def main_menu():
	add_dir("[COLOR deepskyblue]1 CREER UNE SAUVEGARDE : [/COLOR]", 'skin_save1', 'call_save', artworkPath + 'icone.png')
	add_dir("Emplacement 1", 'skin_save1', 'call_save', artworkPath + 'icone.png')
	add_dir("Emplacement 2", 'skin_save2', 'call_save', artworkPath + 'icone.png')
	add_dir("Emplacement 3", 'skin_save3', 'call_save', artworkPath + 'icone.png')
	add_dir("[COLOR deepskyblue]2 RESTAURER UNE SAUVEGARDE : [/COLOR]", 'skin_restor1', 'call_save', artworkPath + 'icone.png')
	add_dir("Emplacement 1", 'skin_restor1', 'call_save', artworkPath + 'icone.png')
	add_dir("Emplacement 2", 'skin_restor2', 'call_save', artworkPath + 'icone.png')
	add_dir("Emplacement 3", 'skin_restor3', 'call_save', artworkPath + 'icone.png')
	add_dir("[COLOR deepskyblue]NETTOYER KODI : [/COLOR]vide le cache efface les thumbnails et les packages", 'vider_cache', 'call_save', artworkPath + 'icone.png')
	
def callSave(url):
    plugins = __import__('resources.lib.' + url)
    function = getattr(plugins, "load")
    function()

def get_params():
    param = []
    paramstring = sys.argv[2]
    if len(paramstring) >= 2:
        params_l = sys.argv[2]
        cleanedparams = params_l.replace('?', '')
        pairsofparams = cleanedparams.split('&')
        param = {}
        for i in range(len(pairsofparams)):
            splitparams = pairsofparams[i].split('=')
            if (len(splitparams)) == 2:
                param[splitparams[0]] = splitparams[1]
    return param

params = get_params()

try:
    mode = unquote_plus(params["mode"])
except:
    mode = None

try:
    url = unquote_plus(params["url"])
except:
    pass

if mode is None:
    main_menu()

elif mode == 'call_save':
    callSave(url)

xbmcplugin.endOfDirectory(int(sys.argv[1]))