# Module: default
# Author: Rayflix
# Created on: 19.01.2022
import sys
import xbmcplugin
import xbmcvfs
from urllib.parse import quote_plus, unquote_plus
import xbmcgui
import xbmc

artworkPath = xbmcvfs.translatePath('special://home/addons/plugin.program.preniumuptobox/resources/media/')
fanart = artworkPath + "fanart.jpg"

def add_dir(name, url, mode, thumb):
    u = sys.argv[0] + "?url=" + quote_plus(url) + "&mode=" + str(mode) + "&name=" + quote_plus(name)
    liz = xbmcgui.ListItem(name)
    liz.setArt({'icon': thumb})
    liz.setProperty("fanart_image", fanart)
    ok = xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]), url=u, listitem=liz, isFolder=True)
    return ok

def main_menu():
	add_dir("[COLOR deepskyblue]1 CHOISIR COMPTE PRENIUM : [/COLOR]", 'cpt_ray0', 'call_save', artworkPath + 'icone.png')
	add_dir("Past - RAYFLIX Compte Integre 1", 'cpt_ray1', 'call_save', artworkPath + 'icone.png')
	add_dir("Past - RAYFLIX Compte Integre 2", 'cpt_ray2', 'call_save', artworkPath + 'icone.png')
	add_dir("Past - RAYFLIX Compte Integre 3", 'cpt_ray3', 'call_save', artworkPath + 'icone.png')
	add_dir("Past - RAYFLIX Compte Integre 4", 'cpt_ray4', 'call_save', artworkPath + 'icone.png')
	add_dir("Past - RAYFLIX Compte Integre 5", 'cpt_ray5', 'call_save', artworkPath + 'icone.png')
	add_dir("Past - RAYFLIX Compte Integre 6", 'cpt_ray6', 'call_save', artworkPath + 'icone.png')
	add_dir("Past - RAYFLIX Compte Integre 7", 'cpt_ray7', 'call_save', artworkPath + 'icone.png')
	add_dir("Past - RAYFLIX Compte Integre 8", 'cpt_ray8', 'call_save', artworkPath + 'icone.png')
	add_dir("Past - RAYFLIX Compte Integre 9", 'cpt_ray9', 'call_save', artworkPath + 'icone.png')
	add_dir("Past - RAYFLIX Compte Integre 10", 'cpt_ray10', 'call_save', artworkPath + 'icone.png')
	add_dir("Past - RAYFLIX Compte Integre 11", 'cpt_ray11', 'call_save', artworkPath + 'icone.png')
	add_dir("Past - RAYFLIX Compte Integre 12", 'cpt_ray12', 'call_save', artworkPath + 'icone.png')
	add_dir("Past - RAYFLIX Compte Integre 13", 'cpt_ray13', 'call_save', artworkPath + 'icone.png')
	add_dir("Past - RAYFLIX Compte Integre 14", 'cpt_ray14', 'call_save', artworkPath + 'icone.png')
	add_dir("Past - RAYFLIX Compte Integre 15", 'cpt_ray15', 'call_save', artworkPath + 'icone.png')
	
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