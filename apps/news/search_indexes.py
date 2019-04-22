#!/usr/bin/env python
# coding=utf-8

# Author:cage
# search_indexes.py 2019-04-21 16:39

from haystack import indexes
from .models import News

class NewsIndex(indexes.SearchIndex,indexes.Indexable):
    text = indexes.CharField(document=True,use_template=True)

    def get_model(self):
        return News

    def index_queryset(self, using=None):
        return self.get_model().objects.all()