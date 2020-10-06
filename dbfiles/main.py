import os
import argparse
import yaml

from dbfiles.schema import Schema
from dbfiles.schema import Item
from dbfiles.result import Result


def parseArgs():
    parser = argparse.ArgumentParser(prog="dbfiles")

    parser.add_argument("--src-root", dest="srcRoot", default=os.path.abspath(os.getcwd()))
    parser.add_argument("--dst-root", dest="dstRoot", default=os.path.abspath(os.getcwd()))
    parser.add_argument("--schemas", nargs="*", dest="schemas", required=True)
    parser.add_argument("--name", dest="name", required=True)
    parser.add_argument("--one-file", dest="oneFile", action="store_true", default=False)
    parser.add_argument("--debug", dest="debug", action="store_true", default=False)

    return parser.parse_args()


def main():
    args = parseArgs()

    Schema.setArgs(args)
    Compiler.setArgs(args)

    compiler = Compiler.create()

    try:
        for schemaPath in args.schemas:
            counter = Counter()
            schema = Schema(counter, schemaPath)
            schema.parse()
            compiler.add(schema)

        compiler.make()
    finally:
        compiler.onDone()

if __name__ == "__main__":
    main()
