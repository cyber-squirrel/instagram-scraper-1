# -*- coding: utf-8 -*-
from igramscraper.exception.instagram_auth_exception import InstagramAuthException
from igramscraper.exception.instagram_exception import InstagramException
from igramscraper.exception.instagram_not_found_exception import (
    InstagramNotFoundException,
)

__all__ = ['InstagramException', 'InstagramNotFoundException', 'InstagramAuthException']
