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


# @task
# def docs():
#     """
#         Deploy documentation to pythonhosted. Using sphinx
#     """
#     local("rm -rf build/html")
#     local("python ./setup.py build_sphinx")
#     local("python ./setup.py upload_sphinx")

# @task
# def syncMezzo():
#     """
#         Copy current module version to mezzo project
#     """
#     local("rm -f /opt/mezzo/dependencies/pgup.tar.gz")
#     local("rm -rf /opt/mezzo/dependencies/pgup")
#     local("mkdir /opt/mezzo/dependencies/pgup")
#     local("cp -R etc pgup /opt/mezzo/dependencies/pgup")
#     local("cp LICENSE MANIFEST.in README.md setup.py /opt/mezzo/dependencies/pgup")
#     with lcd("/opt/mezzo/dependencies"):
#         local("tar cfvz pgup.tar.gz pgup")
#         local("rm -rf pgup")
