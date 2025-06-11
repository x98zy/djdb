# -*- encoding: utf-8 -*-
'''
@File    :   command.py
@Time    :   2025/06/11 19:47:17
@Author  :   xzy 
@Version :   1.0
@Contact :   1580987871@qq.com
'''

# here put the import lib
import sys
import time


def main():
    try:
        import djdb
        from django import VERSION
        from django.core.management import execute_from_command_line
    except ImportError:
        raise ImportError("Couldn't import Django. Are you sure it's installed and "
                          "available on your PYTHONPATH environment variable? Did you "
                          "forget to activate a virtual environment?")
    allow_commands = [
        'shell',
        'check',
        'compilemessages',
        'dbshell',
        'dumpdata',
        'flush',
        'inspectdb',
        'loaddata',
        'makemessages',
        'makemigrations',
        'migrate',
        'showmigrations',
        'sqlflush',
        'sqlmigrate',
        'sqlsequencereset',
        'squashmigrations',
        'clear',
        'help'
    ]
    sys.stdout.write("Django version is %s\n" % str(VERSION))
    subcommand = sys.argv[1] if len(sys.argv) > 1 else None
    print(111111, subcommand)
    if subcommand in ("help", None):
        sys.stdout.write("djdb allow commands is %s" %
                         ("\n".join(allow_commands)))
        sys.exit()
    if subcommand == "shell":
        sys.argv += ["-i", "ipython"]
    bt = time.time()
    execute_from_command_line(sys.argv)
    et = time.time()
    sys.stdout.write("djdb command end at %s using=%s" % (et, et - bt))


if __name__ == "__main__":
    main()
