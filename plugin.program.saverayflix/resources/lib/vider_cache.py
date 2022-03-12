#!/usr/bin/python3
# creation par rayflix le 18 11 21
import xbmc
from io import BytesIO
from urllib.request import urlopen
import shutil
import sys

xbmc.executebuiltin("Notification(FICHIER TEMP,Effacement en cours...)")

# suppression dossier temporaire
dirPath = xbmc.translatePath('special://home/temp/temp/')
try:
   shutil.rmtree(dirPath)
except:
   print('Error while deleting directory')
xbmc.sleep(1000)

xbmc.executebuiltin("Notification(DOSSIER PACKAGES,Effacement en cours...)")

# suppression dossier packages
dirPath = xbmc.translatePath('special://home/addons/packages/')
try:
   shutil.rmtree(dirPath)
except:
   print('Error while deleting directory')
xbmc.sleep(1000)

xbmc.executebuiltin("Notification(DOSSIER THUMBNAILS,Effacement en cours...)")

# suppression dossier thumbnails
dirPath = xbmc.translatePath('special://home/userdata/Thumbnails/')
try:
   shutil.rmtree(dirPath)
except:
   print('Error while deleting directory')
xbmc.sleep(1000)

xbmc.executebuiltin("Notification(CACHE TEMP,Effacement en cours...)")

# suppression dossier cache
dirPath = xbmc.translatePath('special://home/cache/temp/')
try:
   shutil.rmtree(dirPath)
except:
   print('Error while deleting directory')
xbmc.sleep(1000)

# actualisation du skin
xbmc.executebuiltin("Notification(ACTUALISATION , Patientez...)")
xbmc.sleep(2000)
xbmc.executebuiltin('ReloadSkin')

sys.exit()