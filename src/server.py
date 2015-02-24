#!/usr/bin/env python
# -*- coding: utf-8 -*-

import dbs.__all__
from dbs import *


class ServerFactory(object):
    """ DB server class to invoke correct DB class and act as a factory for all
    possible DBs.
    """
    def __init__(self):
        """ Gets all possible classes to be invoked. """

        self.classes = dbs.__all__

    def __call__(self, dbcls):
        """ Initializes database specific class if it's already implemented.
        :param dbcls: name of class for DB.
        """
        if dbcls in self.classes:
            return globals()[dbcls]()
        else:
            raise NotImplementedError('No implementation for this database')


class SyncServer(object):
    """ Worker class to sync all servers sent and register last sync if
    daemon break.
    """
    def __init__(self, cfg):
        """ Receives configuration file to set new sync times and get last
        sync.
        :param cfg: configuration file.
        """
        self.config = cfg

    def __call__(self, *servers):
        """ Receives dbs to sync and if parent is BaseDB instance, than sync
        these servers.
        :param servers: multiple dbs instances
        """
        pass