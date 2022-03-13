# Module: default
# Author: Arias800, Osmoze06, Rayflix
# Created on: 25.10.2021
import sys
import xbmcplugin
import xbmcvfs
from urllib.parse import quote_plus, unquote_plus
import xbmcgui
import xbmc

artworkPath = xbmcvfs.translatePath('special://home/addons/plugin.program.skinrayflix/resources/media/')
fanart = artworkPath + "fanart.jpg"

def add_dir(name, url, mode, thumb):
    u = sys.argv[0] + "?url=" + quote_plus(url) + "&mode=" + str(mode) + "&name=" + quote_plus(name)
    liz = xbmcgui.ListItem(name)
    liz.setArt({'icon': thumb})
    liz.setProperty("fanart_image", fanart)
    ok = xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]), url=u, listitem=liz, isFolder=True)
    return ok

def main_menu():
	add_dir("[COLOR red]METTRE A JOUR L'ADDON [/COLOR]", 'addon_maj', 'call_save', artworkPath + 'icone.png')
	add_dir("[COLOR deepskyblue]1 CHOISIR PAST RAYFLIX : [/COLOR] Ou choisir un autre plus bas", 'cpt_ray3', 'call_save', artworkPath + 'icone.png')
	add_dir("Past - RAYFLIX VIERGE (pensez a ajouter votre compte)", 'past_ray', 'call_save', artworkPath + 'icone.png')
	add_dir("[COLOR deepskyblue]2 VSTREAM SKIN : [/COLOR] Sélectionner le pack souhaité", 'light_light', 'call_save', artworkPath + 'icone.png')
	add_dir("LIGHT ([COLOR deepskyblue]le + leger[/COLOR])", 'light_light', 'call_save', artworkPath + 'icone.png')
	add_dir("FULL ([COLOR deepskyblue]le + gourmand[/COLOR])", 'full_perso', 'call_save', artworkPath + 'icone.png')
	add_dir("KIDS ([COLOR deepskyblue]special enfants[/COLOR])", 'light_kids', 'call_save', artworkPath + 'icone.png')
	add_dir("[COLOR deepskyblue]2 U2PLAY SKIN : [/COLOR] Sélectionner le pack souhaité", 'light_light', 'call_save', artworkPath + 'icone.png')
	add_dir("LIGHT ([COLOR deepskyblue]le + leger[/COLOR])", 'full_films', 'call_save', artworkPath + 'icone.png')
	add_dir("FULL (a venir)", 'light_series', 'call_save', artworkPath + 'icone.png')
	add_dir("KIDS (a venir)", 'light_films', 'call_save', artworkPath + 'icone.png')
	add_dir("[COLOR deepskyblue]AUTRE PAST VIERGE OU PRENIUM INTEGRE: [/COLOR] Sélectionner les past souhaité", 'past_ray', 'call_save', artworkPath + 'icone.png')
	add_dir("Past - MASTER VIERGE (pensez a ajouter votre compte)", 'past_master', 'call_save', artworkPath + 'icone.png')
	add_dir("Past - MASTER Compte Integre 1", 'cpt_mst1', 'call_save', artworkPath + 'icone.png')
	add_dir("Past - MASTER Compte Integre 2", 'cpt_mst2', 'call_save', artworkPath + 'icone.png')
	add_dir("Past - ALL VIERGE (pensez a ajouter votre compte)", 'past_all', 'call_save', artworkPath + 'icone.png')
	add_dir("Past - ALL Compte Integre 1", 'cpt_all1', 'call_save', artworkPath + 'icone.png')	
	add_dir("Past - ALL Compte Integre 2", 'cpt_all2', 'call_save', artworkPath + 'icone.png')
	
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