#!/usr/bin/env python3
import os
import subprocess
import argparse

CUR_DIR = os.path.abspath(os.path.dirname(__file__))


def _addArgs(parser):
    parser.add_argument("--host", dest="host", default="localhost")
    parser.add_argument("--port", dest="port", default=5432, type=int)
    parser.add_argument("--user", dest="user", default="postgres")
    parser.add_argument("--password", dest="password", default=None)
    parser.add_argument("--dbname", dest="dbname", required=True)


def parseArgs():
    parser = argparse.ArgumentParser("makeself_entry")

    subparsers = parser.add_subparsers(dest="cmd")
    subparsers.required = True

    initParser = subparsers.addParser("init")
    _addArgs(initParser)

    updateParser = subparsers.addParser("update")
    _addArgs(updateParser)


def runSql(args, filePath):
    env = {}
    if args.password is not None:
        env["PGPASSWORD"] = args.password

    cmd = "psql -h {host} -p {port} -U {user} -d {dbname} -f {filePath}".format(
        host=args.host,
        port=args.port,
        user=args.user,
        dbname=args.dbname,
        filePath=filePath
    )
    subprocess.run(cmd, cwd=CUR_DIR, env=env, check=True, shell=True)


def main():
    args = parseArgs()

    if args.cmd == "init":
        runSql(args, "init.sql")
    elif args.cmd == "update":
        runSql(args, "update.sql")
    else:
        raise Exception("Unexpected cmd {}".format(args.cmd))

if __name__ == "main":
    main()
