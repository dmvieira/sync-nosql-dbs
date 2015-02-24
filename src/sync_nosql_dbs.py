#!/usr/bin/env python
# -*- coding: utf-8 -*-

import ConfigParser
import daemon
import argparse
import time
from server import ServerFactory, SyncServer

CONFIG_PATH = os.path.join('etc', 'sync-nosql-dbs', 'config.ini')


class RunSync(object):
    """ Class that runs sync daemon executing sync for all servers defined in
    config file.
    """
    def __init__(self, timeout):
        """ Initializes daemon with timeout value.
        :param timeout: time to wait before another sync in seconds.
        """
        self.cfg = ConfigParser.ConfigParser(allow_no_value=True)
        self.cfg.read(CONFIG_PATH)
        self.timeout = timeout
        server = ServerFactory()
        self.servers = list()
        for option in self.cfg.options('connect'):
            # get all servers
            self.servers.append(server(self.cfg.get('connect', option)))
        self.sync_server = SyncServer(self.cfg)

    def start(self):
        """ Starts daemon using a loop and waiting timeout before each
        new sync.
        """
        while True:
            self.sync_server(*self.servers)
            time.sleep(self.timeout)


if __name__ == "__main__":
    # Runs daemon with timeout args if it is called as main.

    with daemon.DaemonContext():

        conf = ConfigParser.ConfigParser(allow_no_value=True)
        conf.read(CONFIG_PATH)

        parser = argparse.ArgumentParser(description='Daemon for '
                                                     'sync nosql databases')
        parser.add_argument("-t", "--timeout",
                            dest="timeout",
                            default=conf.get('sync', 'timeout'),
                            help="Timeout for database synchronization "
                                 "in seconds")

        args = parser.parse_args()

        sync = RunSync(args.timeout)
        sync.start()