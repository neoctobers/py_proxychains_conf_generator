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
        self._path_to_conf = '/etc/proxychains.conf'

        if isinstance(proxy, str):
            self._proxy.append(proxy)
        else:
            self._proxy = proxy

    def write(self,
              path_to_conf: str = '/etc/proxychains.conf'):

        xp.about_to('Generate config file for proxychains')

        pc4_config_content = '{chain_mode}\n'.format(chain_mode=self._chain_mode)

        if self._quite_mode:
            pc4_config_content += 'quiet_mode\n'

        pc4_config_content += 'proxy_dns\n' \
                              'remote_dns_subnet 224\n' \
                              'tcp_read_time_out 15000\n' \
                              'tcp_connect_time_out 8000\n' \
                              '\n' \
                              '[ProxyList]\n' \
                              '{proxy}'.format(proxy='\n'.join(self._proxy))

        print(pc4_config_content)
        xp.about_t('Writting', path_to_conf)
        with open(path_to_conf, 'wb') as f:
            f.write(pc4_config_content.encode('utf-8'))
        xp.success()
        return True
