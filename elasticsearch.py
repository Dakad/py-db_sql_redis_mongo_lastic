
import logging
import json

from elasticsearch import Elasticsearch


def connect_elasticsearch(host="localhost", port=920):
    _es = Elasticsearch([{'host': host, 'port': port}])
    if _es.ping():
        print('Yay Connect')
    else:
        print('Awww it could not connect!')
    return _es


def search(es_object, index_name, **search_kwargs):
    search_object = json.dumps({
        'query': {
            'match': search_kwargs
        }
    })
    res = es_object.search(index=index_name, body=search_object)
    return res


if __name__ == '__main__':
    logging.basicConfig(level=logging.ERROR)

    es = connect_elasticsearch()
    if es is not None:
        search(es, 'recipes', **{'name': 'Koil'})
