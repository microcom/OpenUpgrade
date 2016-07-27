#!/usr/bin/env python2

import os

migrations = {
    '9.0': {
        'addons': {
            'addons': {
                'type': 'link',
                'url': os.path.join('server', 'addons'),
            },
        },
        'server': {
            'type': 'git',
            'url': 'git@github.com:microcom/OpenUpgrade.git',
            'branch': '9.0-crc',
            'addons_dir': os.path.join('openerp', 'addons'),
            'root_dir': os.path.join(''),
            'cmd': 'openerp-server --update=all --database=%(db)s '
                   '--config=%(config)s --stop-after-init --no-xmlrpc',
            },
    },
}
