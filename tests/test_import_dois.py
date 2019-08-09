# -*- coding: utf-8 -*-

from doi4bib import add_dois_to_bib
from doi4bib.import_dois import crossref_query_title
from urllib.error import HTTPError
from unittest.mock import patch
import json

__author__ = "sharkovsky"
__copyright__ = "sharkovsky"
__license__ = "mit"


def test_handle_empty_db():
    assert len(add_dois_to_bib(dict()).keys()) == 0


@patch('doi4bib.import_dois.urlopen')
def test_HTTPError(m_urlopen):
    def raise_except():
        raise HTTPError(None, 500, None, None, None)
    m_urlopen().read.side_effect = raise_except
    result = crossref_query_title('')
    assert result['success'] is False
    assert result['result']['similarity'] == 0
    assert result['result']['crossref_title'] == ''
    assert result['result']['doi'] == ''


@patch('doi4bib.import_dois.urlopen')
def test_existing_title(m_urlopen):
    result = {
              'status': 'ok',
              'message-type': 'work-list',
              'message-version': '1.0.0',
              'message': {
                  'items': [{
                      'title': ['existing_title'],
                      'DOI': '12.3456/42.42'
                      }
                      ]
                  }
              }
    result = json.dumps(result).encode('utf-8')
    m_urlopen().read.return_value = result
    result = crossref_query_title('existing_title')
    assert result['success'] is True
    assert result['result']['crossref_title'] == 'existing_title'
    assert result['result']['similarity'] == 1.0
    assert result['result']['doi'] == '12.3456/42.42'
