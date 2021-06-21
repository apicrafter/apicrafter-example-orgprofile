import requests
import logging
STATREG_URLPAT = 'https://api.crftr.net/rawapi/v2/gks/statreg?apikey=%s&where=%s'
BALANCES_URLPAT = 'https://api.crftr.net/rawapi/v2/gks/orgbalances?apikey=%s&where=%s'
RMSP_URLPAT = 'http://api.crftr.net/rawapi/v3/rmsp/rmsp?apikey=%s&where=%s'
CLEAR_SUPP = 'http://openapi.clearspending.ru/restapi/v3/suppliers/search/?inn=%s'
CLEAR_CUST = 'http://openapi.clearspending.ru/restapi/v3/customers/search/?inn=%s'

DEFAULT_DATACRAFTER_URL = 'http://api.crftr.net/rawapi/v3/'
DIRECT_DATACRAFTER_URL = 'http://api.crftr.net/rawapi/v3/'
LOCAL_DATACRAFTER_URL = 'http://api.crftr.net/rawapi/v3/'

CRAFTER_URL = 'https://api.crftr.net/restapi/'


def crafter_request(endpoint, key, query, prefix=DEFAULT_DATACRAFTER_URL):
    if key:
        url = prefix + endpoint + '?apikey=%s&where=%s' % (key, str(query).replace("'", '"'))
    else:
        url = prefix + endpoint + '?where=%s' % (str(query).replace("'", '"'))
    jdata = requests.get(url).json()
    if 'message' in jdata.keys():
        logging.info(jdata['message'])
        return None
    if '_meta' in jdata.keys():
        if jdata['_meta']['total'] > 0:
            if jdata['_meta']['max_results'] >= jdata['_meta']['total'] :
                return jdata['_items']
            else:
                all = jdata['_items']
                page = 1
                while True:
                    page += 1
                    purl = url + '&page=' % str(page)
                    jdata = requests.get(purl).json()
                    all.expand(jdata['_items'])
                return all

    return None


def crafter_request_all(endpoint, key, query, prefix=DEFAULT_DATACRAFTER_URL):
    if key:
        url = prefix + endpoint + '?apikey=%s&where=%s' % (key, str(query).replace("'", '"'))
    else:
        url = prefix + endpoint + '?where=%s' % (str(query).replace("'", '"'))
    jdata = requests.get(url).json()
    if 'message' in jdata.keys():
        logging.info(jdata['message'])
        return None
    if '_meta' in jdata.keys():
        if jdata['_meta']['total'] > 0:
            return jdata['_items']
    return None

def get_crafter_basic(endpoint, prefix, qkey, value, apikey=None):
    return crafter_request_all(endpoint, key=apikey, query={qkey:value}, prefix=prefix)



def get_egrul(inn, apikey=None):
    """Returns organization record from EGRUL"""
    params = []
    params.append(['INN', inn])
    qp = []
    for p in params:
        qp.append('='.join(p))
    query = '&'.join(qp)
    url = CRAFTER_URL + 'egrul/svjul/' + '?apikey=%s'% (apikey) + '&' + query
    req = requests.get(url)
    jdata = req.json()
    if 'message' in jdata.keys():
        logging.info(jdata['message'])
        return None
    else:
        if 'results' in jdata.keys() and len(jdata['results']) > 0:
            return jdata['results'][0]
    return None

def get_customer(id, keyname="INN", apikey=None):
    """Returns customer profile of organization (44-FZ, 223-FZ)"""
    params = []
    params.append([keyname, id])
    qp = []
    for p in params:
        qp.append('='.join(p))
    query = '&'.join(qp)
    url = CRAFTER_URL + 'v4/customers/' + '?apikey=%s'% (apikey) + '&' + query
    req = requests.get(url)
    jdata = req.json()
    if 'message' in jdata.keys():
        logging.info(jdata['message'])
        all = None
    else:
        all = jdata['results']
    return all


def get_supplier_contracts_44fz(inn, apikey=None):
    """Returns all contracts of organization if it's supplier for 44-fz"""
    params = []
    params.append(['suppliers__INN', inn])
    qp = []
    for p in params:
        qp.append('='.join(p))
    query = '&'.join(qp)
    url = CRAFTER_URL + 'v4/contracts/' + '?apikey=%s'% (apikey) + '&' + query
    all = []
    while True:
        req = requests.get(url)
        jdata = req.json()
        if 'message' in jdata.keys():
            logging.info(jdata['message'])
            break
        else:
            all.extend(jdata['results'])
        if 'next' in jdata.keys() and jdata['next'] is not None:
            url = jdata['next'] + '&apikey=%s' % (apikey)
        else:
            break
    return all

def get_supplier_contracts_223fz(inn, apikey=None):
    """Returns all contracts of organization if it's supplier for 223-fz"""
    params = []
    params.append(['supplierInfo__inn', inn])
    qp = []
    for p in params:
        qp.append('='.join(p))
    query = '&'.join(qp)
    url = CRAFTER_URL + 'v4/223fz/contracts/' + '?apikey=%s'% (apikey) + '&' + query
    all = []
    while True:
        req = requests.get(url)
        jdata = req.json()
        if 'message' in jdata.keys():
            logging.info(jdata['message'])
            break
        else:
            all.extend(jdata['results'])
        if 'next' in jdata.keys() and jdata['next'] is not None:
            url = jdata['next'] + '&apikey=%s' % (apikey)
        else:
            break
    return all

def get_customer_contracts_44fz(inn, apikey=None):
    """Returns all contracts of organization if it's customer for 44-fz"""
    params = []
    params.append(['customer__INN', inn])
    qp = []
    for p in params:
        qp.append('='.join(p))
    query = '&'.join(qp)
    url = CRAFTER_URL + 'v4/contracts/'+ '?apikey=%s'% (apikey) + '&' + query
    all = []
    while True:
        req = requests.get(url)
        jdata = req.json()
        if 'message' in jdata.keys():
            logging.info(jdata['message'])
            break
        else:
            all.extend(jdata['results'])
        if 'next' in jdata.keys() and jdata['next'] is not None:
            url = jdata['next'] + '&apikey=%s' % (apikey)
        else:
            break
    return all



def get_customer_contracts_223fz(inn, apikey=None):
    """Returns all contracts of organization if it's customer for 223-fz"""
    params = []
    params.append(['customer__inn', inn])
    qp = []
    for p in params:
        qp.append('='.join(p))
    query = '&'.join(qp)
    url = CRAFTER_URL + 'v4/223fz/contracts/'+ '?apikey=%s'% (apikey) + '&' + query
    all = []
    while True:
        req = requests.get(url)
        jdata = req.json()
        if 'message' in jdata.keys():
            logging.info(jdata['message'])
            break
        else:
            all.extend(jdata['results'])
        if 'next' in jdata.keys() and jdata['next'] is not None:
            url = jdata['next'] + '&apikey=%s' % (apikey)
        else:
            break
    return all
