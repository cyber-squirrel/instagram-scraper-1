# -*- coding: utf-8 -*-
from .initializer_model import InitializerModel


class UserStories(InitializerModel):
    def __init__(self, stories=None, owner=None):
        self.owner = owner
        if stories is None:
            self.stories = []
        super().__init__()
