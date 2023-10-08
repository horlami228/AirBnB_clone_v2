#!/usr/bin/python3

"""
    deploy web static
"""
from fabric.api import run, put, env, local
from os import path
env.hosts = [
        "ubuntu@54.174.245.243",
        "ubuntu@3.84.158.22"
]


def do_deploy(archive_path):
    """
        deploying our webpages
    """
    # check if file exists
    if not path.exists(archive_path):
        return False
    try:
        filename = archive_path[9:34]
        # transfer archive file
        put(archive_path, remote_path="/tmp/")

        # create path with archive name without
        # the .tgz
        run("sudo mkdir -p /data/web_static"
            "/releases/{}/".format(filename))

        # decrompress the archive
        run("sudo tar -zxf /tmp/{}.tgz"
            " -C /data/web_static/releases/{}/".format(filename, filename))

        # move all files from the directory out of the folder
        source_path = "/data/web_static/releases/{}/\
            web_static".format(filename)
        destination_path = "/data/web_static/releases/{}".format(filename)

        run("sudo rsync -a {}/* {}".format(source_path, destination_path))

        # remove the archive file
        run("sudo rm /tmp/{}.tgz".format(filename))

        # remove the web_static decompress file
        run("sudo rm -rf /data/web_static/"
            "releases/{}/web_static".format(filename))

        # delete formal linking
        run("sudo rm -rf /data/web_static/current")

        # create a new sym link
        run("sudo ln -s /data/web_static/releases/"
            "{}/ /data/web_static/current".format(filename))
    except Exception as e:
        return False
    return True
