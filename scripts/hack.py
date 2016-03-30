#!/usr/bin/env python2

import os

migrations = {
    '9.0': {
        'addons': {
            'addons': {
                'type': 'link',
                'url': os.path.join('server', 'addons'),
            },
            'mic_shared': {
                'type': 'git',
                'url': 'git@github.com:microcom/mic-shared.git',
                'branch': '9.0-migration-hack',
            },
            'mic': {
                'type': 'git',
                'url': 'git@github.com:microcom/mic.git',
                'branch': '9.0-migrate',
            },
        },
        'server': {
            'type': 'git',
            'url': 'git@github.com:microcom/OpenUpgrade.git',
            'branch': '9.0-hacked',
            'addons_dir': os.path.join('openerp', 'addons'),
            'root_dir': os.path.join(''),
            'cmd': 'openerp-server --update=all --database=%(db)s '
                   '--config=%(config)s --stop-after-init --no-xmlrpc',
            },
    },
}
