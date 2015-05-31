#encoding=utf8
import pycurl
import StringIO
import json
#query:查询字符串,num:需要的数量,start:开始的结果编号
def search(query, num=10, start=0):
    c = pycurl.Curl()
    searchdoc = {
        "query": {
            "match" : {
                "text" : {
                    "query":query,
                    "minimum_should_match": "30%",
                }
            }
        },
        "rescore": {
            "window_size" : 50,
            "query" : {
                "rescore_query" : {
                    "match_phrase": {
                        "text" : {
                            "query" : query,
                            "slop" : 50
                        }
                    }
                }
            }
        },
        "highlight" : {
            "fields" : {
                "text" : {}
            }
        }
    }
    b = StringIO.StringIO()
    searchjson = json.dumps(searchdoc)
    url = 'http://localhost:9200/wiki/pages/_search?pretty&_source=title&'+'size='+str(num)+'&from='+str(start)
    c.setopt(pycurl.URL, url)
    c.setopt(pycurl.CUSTOMREQUEST, "GET")
    c.setopt(pycurl.WRITEFUNCTION, b.write)
    c.setopt(pycurl.POSTFIELDS, searchjson)
    c.perform()
    print b.getvalue()
    return b.getvalue()
