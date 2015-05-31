# soa-search
===
### 存储数据
使用parseall.py

---
### 搜索接口
```
#query要查询的字符串
#num要查询的数量
#start开始结果的编号
search(query, num=10, start=0)
```
---
### 返回格式介绍（json格式）
+ took:所用时间
+ time_out:是否超时
+ hits:找到的结果
	+ total:总个数
	+ max_score:最大得分
	+ hits:结果
		+ _id:id
		+ _source:原始数据（暂时只返回title部分）
		+ highlight:高亮部分，寻找到的字符会被`<em></em>`括起来

---
### 返回结果示例
```
{
  "took" : 372,
  "timed_out" : false,
  "_shards" : {
    "total" : 5,
    "successful" : 5,
    "failed" : 0
  },
  "hits" : {
    "total" : 15,
    "max_score" : 0.19905654,
    "hits" : [ {
      "_index" : "wiki",
      "_type" : "pages",
      "_id" : "1453",
      "_score" : 0.39811307,
      "_source":{"title":"ALGOL"},
      "highlight" : {
        "text" : [ " before and 6 after the decimal point.\n\n===Timeline: <em>H
ello</em> world===\nThe variations and lack of", " [[<em>hello</em> world progra
m]].\n\n====ALGOL 58 (IAL)====\n{{main|ALGOL 58}}\nALGOL 58 had no I/O facilitie
s", " [[<em>hello</em> world program]] in ALGOL.\n\n BEGIN\n   FILE F(KIND=REMOT
E);\n   EBCDIC ARRAY E[0:11];\n   REPLACE E", " BY \"<em>HELLO</em> WORLD!\";\n
  WRITE(F, *, E);\n END.\n\nA simpler program using an inline format:\n\n BEGIN"
, "\n   FILE F(KIND=REMOTE);\n   WRITE(F, <\"<em>HELLO</em> WORLD!\">);\n END.\n
\nAn even simpler program using the Display" ]
      }
    }, {
      "_index" : "wiki",
      "_type" : "pages",
      "_id" : "1335",
      "_score" : 0.31724128,
      "_source":{"title":"Associative property"},
      "highlight" : {
        "text" : [ " <code>\"<em>hello</em>\"</code>, <code>\" \"</code>, <code>
\"world\"</code> can be computed by concatenating the", " first two strings (giv
ing <code>\"<em>hello</em> \"</code>) and appending the third string (<code>\"wo
rld\"</code", " string (<code>\"<em>hello</em>\"</code>) with the result. The tw
o methods produce the same result; string" ]
      }
    }, {
      "_index" : "wiki",
      "_type" : "pages",
      "_id" : "1456",
      "_score" : 0.26074126,
      "_source":{"title":"AWK"},
      "highlight" : {
        "text" : [ " applications ==\n\n=== <em>Hello</em> World ===\n\nHere is
the customary \"[[<em>Hello</em> world]]\" program written in AWK", ":\n<source
lang=\"awk\">\nBEGIN { print \"<em>Hello</em>, world!\" }\n</source>\n\nNote tha
t an explicit <code>exit</code", " called <code>hello.awk</code> that prints the
 string ''<em>Hello</em>, world!'' may be built by creating a", " -f\nBEGIN { pr
int \"<em>Hello</em>, world!\" }\n</source>\n\nThe <code>-f</code> tells ''awk''
 that the argument" ]
      }
    }, {
      "_index" : "wiki",
      "_type" : "pages",
      "_id" : "1242",
      "_score" : 0.22349252,
      "_source":{"title":"Ada (programming language)"},
      "highlight" : {
        "text" : [ " from [[Pascal (programming language)|Pascal]].\n\n=== \"<em
>Hello</em>, world!\" in Ada ===\n\nA common example of a", " language's [[Synta
x (programming languages)|syntax]] is the [[<em>Hello</em> world program]]: \n(h
ello.adb", ")\n<syntaxhighlight lang=\"ada\">\nwith Ada.Text_IO; use Ada.Text_IO
;\nprocedure <em>Hello</em> is\nbegin\n  Put_Line", " (\"<em>Hello</em>, world!\
");\nend <em>Hello</em>;\n</syntaxhighlight>\nThis program can be compiled by us
ing the freely" ]
      }
    }, {
      "_index" : "wiki",
      "_type" : "pages",
      "_id" : "1010",
      "_score" : 0.17474853,
      "_source":{"title":"April 15"},
      "highlight" : {
        "text" : [ ")\n*  2013   &ndash; [[Dave McArtney]], New Zealand singer-s
ongwriter and guitarist ([[<em>Hello</em> Sailor (band", ")|<em>Hello</em> Sailo
r]]) (b. 1951)\n*  2013   &ndash; [[Scott Miller (pop musician)|Scott Miller]],
American" ]
      }
    }, {
      "_index" : "wiki",
      "_type" : "pages",
      "_id" : "1451",
      "_score" : 0.14899501,
      "_source":{"title":"APL (programming language)"},
      "highlight" : {
        "text" : [ ">\n\n== Examples ==\nThis displays \"<em>Hello</em>, world\"
:\n\n<pre>\n'<em>Hello</em>, world'\n</pre>\n'<em>Hello</em> World,' sample user
", " session on YouTube<ref>{{cite web|last1=Dyalog APL/W|title=Producing a stan
dalone '<em>Hello</em> World", " languages. APL is economical in its character u
sage.\n\nThe '<em>Hello</em>, world' string constant above" ]
      }
    }, {
      "_index" : "wiki",
      "_type" : "pages",
      "_id" : "316",
      "_score" : 0.13256119,
      "_source":{"title":"Academy Award for Best Production Design"},
      "highlight" : {
        "text" : [ ">[[Raphael Bretton]]\n| ''[[<em>Hello</em>, Dolly! (film)|<e
m>Hello</em>, Dolly!]]''\n|-\n| [[Maurice Carter (film designer" ]
      }
    }, {
      "_index" : "wiki",
      "_type" : "pages",
      "_id" : "856",
      "_score" : 0.13221994,
      "_source":{"title":"Apple Inc."},
      "highlight" : {
        "text" : [ "/index.htm |title=Apple: <em>Hello</em>, iPhone |author=Owen
 Thomas |date=January 9, 2007 |publisher=CNNMoney", " iMac|accessdate=August 13,
 2008}}</ref> and \"Say <em>hello</em> to iPhone\" has been used in iPhone", " a
dvertisements.<ref>{{cite web|url=http://billday.com/2007/06/29/say-<em>hello</e
m>-to-iphone/|title=BillDay.com \" Say", " <em>hello</em> to iPhone|accessdate=A
ugust 13, 2008| archiveurl= https://web.archive.org/web/20080907003704", "/http:
//billday.com/2007/06/29/say-<em>hello</em>-to-iphone/| archivedate= September 7
, 2008| deadurl= no" ]
      }
    }, {
      "_index" : "wiki",
      "_type" : "pages",
      "_id" : "1140",
      "_score" : 0.12821154,
      "_source":{"title":"Amplitude modulation"},
      "highlight" : {
        "text" : [ ".   His first transmitted words were, \"<em>Hello</em>. One,
 two, three, four.  Is it snowing where you are, Mr" ]
      }
    }, {
      "_index" : "wiki",
      "_type" : "pages",
      "_id" : "1325",
      "_score" : 0.123565875,
      "_source":{"title":"Casa Mil脿"},
      "highlight" : {
        "text" : [ " and ceased to say <em>hello</em> to him, arguing that the w
eird building by Gaud铆 would lower the price of land" ]
      }
    } ]
  }
}
```
