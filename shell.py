# -*- coding: utf-8 -*-
from mr.developer.commands import ChoicesPseudoAction
from mr.developer.commands import Command

import os


class CmdShell(Command):

    def __init__(self, develop):
        Command.__init__(self, develop)
        description = 'Runs the given shell command on active sources.'
        self.parser = self.develop.parsers.add_parser(
            'shell',
            description=description
        )
        self.develop.parsers._name_parser_map['s'] = self.develop.parsers._name_parser_map['shell']  # noqa
        self.develop.parsers._choices_actions.append(
            ChoicesPseudoAction('shell', 's', help=description)
        )
        self.parser.add_argument(
            dest='cmd',
            help='The command to run, i.e. "git grep SOMETHING".'
        )
        self.parser.set_defaults(func=self)

    def __call__(self, args):
        packages = self.get_packages(None, develop=True)
        for name in sorted(packages):
            source = self.develop.sources[name]
            if os.path.isdir(source['path']):
                os.chdir(source['path'])
                os.system(args.cmd)
