'''
    RadioNL audio Add-on
    This program is free software: you can redistribute it and/or modify
    it under the terms of the GPL-3.0 License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.
    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.
    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <http://www.gnu.org/licenses/>.
'''

import os
import sys
import urllib.parse
from kodi_six import xbmc, xbmcaddon, xbmcvfs
from resources.lib import xbmcutil

__addon__               = xbmcaddon.Addon()
__author__              = __addon__.getAddonInfo('author')
__addon_id__		= __addon__.getAddonInfo('id')
__addon_name__ 	        = __addon__.getAddonInfo('name')
__addon_path__	   	= __addon__.getAddonInfo('path')
__addon_version__	= __addon__.getAddonInfo('version')
__addon_fanart__	= __addon__.getAddonInfo('fanart')
__addon_icon__		= __addon__.getAddonInfo('icon')
__country_code__	= 'NL'

__profile__             = xbmc.translatePath(__addon__.getAddonInfo('profile'))

args = urllib.parse.parse_qs(sys.argv[2][1:])

addon_handle=int(sys.argv[1])
xbmcutil.addon_handle=addon_handle

__settings__= xbmcaddon.Addon(id='plugin.audio.radionl')
rootDir = xbmc.translatePath(__settings__.getAddonInfo('path'))
streamDir = os.path.join(rootDir, "streams")

def browse(strDir):
    for directory in getDirs(strDir) :
        xbmcutil.addMenuItem('[COLOR orange]'+directory+'[/COLOR]', os.path.join(strDir, directory), 'false')
    for file in getFiles(strDir) :
        if(file[-5:] == '.strm') :
            background = os.path.join(rootDir, 'resources/fanart.jpg')
            if(os.path.isfile(os.path.join(strDir, file[:-5]+'.tbn'))) :
                iconFile = os.path.join(strDir, file[:-5]+'.tbn')
            else :
                iconFile = os.path.join(rootDir, 'resources/logo.png')
            xbmcutil.addMenuItem(file[:-5], os.path.join(strDir, file), 'true', icon=iconFile, fanart=background)
    xbmcutil.endOfList()

def getDirs(strRoot) :
    dirs = list()
    dirList = os.listdir(strRoot)
    for directory in dirList:
        if os.path.isdir(os.path.join(strRoot, directory)) == True:
            dirs.append(directory)
    dirs.sort()
    return dirs

def getFiles(strRoot) :
    files = list()
    dirList = os.listdir(strRoot)
    for directory in dirList:
        if os.path.isdir(os.path.join(strRoot, directory)) == True:
            print('')
        else :
            files.append(directory)
    files.sort()
    return files
    
argBrowse = args.get('browse', None)

if argBrowse is not None :
    browse(argBrowse[0])
else:
    browse(streamDir)
