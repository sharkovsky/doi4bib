from doi4bib import add_dois_to_bib
from unittest.mock import patch
import json

__author__ = "sharkovsky"
__copyright__ = "sharkovsky"
__license__ = "mit"


def test_handle_empty_db():
    assert len(add_dois_to_bib(dict()).keys()) == 0


def test_handle_already_existing_doi():
    entry = dict(
            title='my title',
            doi='already existing'
            )
    db = dict(
            key=entry
            )
    output = add_dois_to_bib(db)
    assert output['key']['doi'] == 'already existing'


@patch('doi4bib.import_dois.urlopen')
def test_handle_result_full_similarity(m_urlopen):
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
    entry = dict(
            title='existing_title',
            )
    db = dict(
            key=entry
            )
    output = add_dois_to_bib(db)
    assert 'doi' in output['key']
    assert output['key']['doi'] == '12.3456/42.42'


@patch('doi4bib.import_dois.urlopen')
def test_handle_result_low_similarity(m_urlopen):
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
    entry = dict(
            title='existing Title',
            )
    db = dict(
            key=entry
            )
    output = add_dois_to_bib(db)
    assert 'doi' in output['key']
    assert output['key']['doi'] == '12.3456/42.42'


@patch('doi4bib.import_dois.urlopen')
def test_handle_result_no_similarity(m_urlopen):
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
    entry = dict(
            title='completely different',
            )
    db = dict(
            key=entry
            )
    output = add_dois_to_bib(db)
    assert 'doi' not in output['key']
