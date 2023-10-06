#!/usr/bin/python3

"""
    This fabric script generates a .tgz file
"""

from fabric.api import local
from time import strftime


def do_pack():

    """
        This function converts and compress the contents
        of web_static folder in an archive
    """

    time = strftime("%Y%m%d%H%M%S")
    try:
        local("mkdir -p versions")
        local("tar -cvzf versions/web_static_{}.tgz web_static/"
              .format(time))

        return "versions/web_static_{}.tgz".format(time)
    except Exception:
        return None
