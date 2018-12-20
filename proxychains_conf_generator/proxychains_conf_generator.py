#!/usr/bin/env python3
# -*- coding:utf-8 -*-
import xprint as xp


class Generator:
    def __init__(self,
                 proxy: str or list = 'socks5 127.0.0.0 1080',
                 chain_mode: str = 'strict_chain',
                 quiet_mode: bool = False,
                 ):
        self._proxy = list()
        self._chain_mode = chain_mode
        self._quite_mode = quiet_mode

        if isinstance(proxy, str):
            self._proxy.append(proxy)
        else:
            self._proxy = proxy

    def write(self,
              path_to_conf: str = '/etc/proxychains.conf',
              plain_to_console: bool = False,
              ):

        xp.about_t('Generating', path_to_conf, 'for proxychains')

        configs = list()

        configs.append('{chain_mode}'.format(chain_mode=self._chain_mode))
        if self._quite_mode:
            configs.append('quiet_mode')
        configs.append('proxy_dns')
        configs.append('remote_dns_subnet 224')
        configs.append('tcp_read_time_out 15000')
        configs.append('tcp_connect_time_out 8000')
        configs.append('')
        configs.append('[ProxyList]')
        configs.append('{proxy}'.format(proxy='\n'.join(self._proxy)))
        configs = '\n'.join(configs)

        # write
        with open(path_to_conf, 'wb') as f:
            f.write(configs.encode('utf-8'))
        xp.success()

        # plain to console
        if plain_to_console:
            xp.plain_text(configs)

        return path_to_conf
