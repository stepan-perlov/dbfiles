import os

from invoke import Collection
from invoke import task

CUR_DIR = os.path.abspath(os.path.dirname(__file__))


@task
def local(ctx):
    """
        Install dbfiles on local machine
    """
    with ctx.cd(CUR_DIR):
        ctx.run("sudo pip3 install --upgrade .", )


@task
def up(ctx):
    """
     Deploy new release to pypi. Using twine util
    """
    ctx.run("rm -rf dist")
    ctx.run("rm -rf dbfiles.egg-info")
    ctx.run("python3 ./setup.py sdist")
    ctx.run("twine upload dist/{}".format(ctx.run("ls dist").stdout.strip()))
