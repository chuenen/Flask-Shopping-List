import requests


def http_get(url, **params):
    resp = requests.get(url, **params)
    resp.raise_for_status()
    return resp

def http_post(url, **params):
    resp = requests.post(url, **params)
    resp.raise_for_status()
    return resp

def http_delete(url):
    resp = requests.delete(url)
    resp.raise_for_status()
    return resp


# vi:et:ts=4:sw=4:cc=80
