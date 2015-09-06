#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import shelltools
from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import pythonmodules
from pisi.actionsapi import get
WorkDir = "sip-%s" % get.srcVERSION()
py3dir = "python3.4"

def setup():
    pythonmodules.run('configure.py \
                    -b /usr/bin \
                    -d /usr/lib/%s/site-packages/ \
                    -e /usr/include/%s/ \
                    CFLAGS="%s" CXXFLAGS="%s"' % (py3dir, py3dir, get.CFLAGS(), get.CXXFLAGS()), pyVer = "3")

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s -C sipgen" % get.installDIR())

    autotools.rawInstall("DESTDIR=%s" % get.installDIR())
    pisitools.rename("/usr/bin/sip", "sip3")


# By PiSiDo 2.3.1