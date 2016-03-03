#!/usr/bin/env python2

migrations = {
    '9.0test': {
        'addons': {
            'addons': {
                'type': 'link',
                'url': os.path.join('server', 'addons'),
            },
            # 'mic_shared': {
            #     'type': 'git',
            #     'url': 'git@github.com:microcom/mic-shared.git',
            #     'branch': '9.0-fix-referral',
            # },
            # 'mic': {
            #     'type': 'git',
            #     'url': 'git@github.com:microcom/mic.git',
            #     'branch': '9.0-migrate',
            # },
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
