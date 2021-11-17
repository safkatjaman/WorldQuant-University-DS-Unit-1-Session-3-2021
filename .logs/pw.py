%logstop
%logstart -rtq ~/.logs/pw.py append
import seaborn as sns
sns.set()
# Wed, 17 Nov 2021 05:32:28
%logstop
%logstart -ortq ~/.logs/pw.py append
%matplotlib inline
import matplotlib
import seaborn as sns
sns.set()
matplotlib.rcParams['figure.dpi'] = 144%logstop
%logstart -rtq ~/.logs/pw.py append
import seaborn as sns
sns.set()
# Wed, 17 Nov 2021 05:32:29
from static_grader import grader# Wed, 17 Nov 2021 05:32:36
%%bash
mkdir pw-data
wget http://dataincubator-wqu.s3.amazonaws.com/pwdata/201701scripts_sample.json.gz -nc -P ./pw-data
wget http://dataincubator-wqu.s3.amazonaws.com/pwdata/practices.json.gz -nc -P ./pw-data# Wed, 17 Nov 2021 05:32:42
import gzip
import simplejson as json# Wed, 17 Nov 2021 05:32:47
with gzip.open('./pw-data/201701scripts_sample.json.gz', 'rb') as f:
    scripts = json.load(f)

with gzip.open('./pw-data/practices.json.gz', 'rb') as f:
    practices = json.load(f)# Wed, 17 Nov 2021 05:33:00
scripts[:2]# Wed, 17 Nov 2021 05:33:27
with gzip.open('./pw-data/201701scripts_sample.json.gz', 'rb') as f:
    scripts = json.load(f)

with gzip.open('./pw-data/practices.json.gz', 'rb') as f:
    practices = json.load(f)# Wed, 17 Nov 2021 05:33:33
%logstop
%logstart -ortq ~/.logs/pw.py append
%matplotlib inline
import matplotlib
import seaborn as sns
sns.set()
matplotlib.rcParams['figure.dpi'] = 144%logstop
%logstart -ortq ~/.logs/pw.py append
%matplotlib inline
import matplotlib
import seaborn as sns
sns.set()
matplotlib.rcParams['figure.dpi'] = 144
scripts[:2]
with gzip.open('./pw-data/201701scripts_sample.json.gz', 'rb') as f:
    scripts = json.load(f)

with gzip.open('./pw-data/practices.json.gz', 'rb') as f:
    practices = json.load(f)
# Wed, 17 Nov 2021 05:33:33
from static_grader import grader# Wed, 17 Nov 2021 05:33:36
%%bash
mkdir pw-data
wget http://dataincubator-wqu.s3.amazonaws.com/pwdata/201701scripts_sample.json.gz -nc -P ./pw-data
wget http://dataincubator-wqu.s3.amazonaws.com/pwdata/practices.json.gz -nc -P ./pw-data# Wed, 17 Nov 2021 05:33:50
%logstop
%logstart -ortq ~/.logs/pw.py append
%matplotlib inline
import matplotlib
import seaborn as sns
sns.set()
matplotlib.rcParams['figure.dpi'] = 144%logstop
%logstart -ortq ~/.logs/pw.py append
%matplotlib inline
import matplotlib
import seaborn as sns
sns.set()
matplotlib.rcParams['figure.dpi'] = 144
scripts[:2]
with gzip.open('./pw-data/201701scripts_sample.json.gz', 'rb') as f:
    scripts = json.load(f)

with gzip.open('./pw-data/practices.json.gz', 'rb') as f:
    practices = json.load(f)
%logstop
%logstart -ortq ~/.logs/pw.py append
%matplotlib inline
import matplotlib
import seaborn as sns
sns.set()
matplotlib.rcParams['figure.dpi'] = 144
from static_grader import grader
%%bash
mkdir pw-data
wget http://dataincubator-wqu.s3.amazonaws.com/pwdata/201701scripts_sample.json.gz -nc -P ./pw-data
wget http://dataincubator-wqu.s3.amazonaws.com/pwdata/practices.json.gz -nc -P ./pw-data
# Wed, 17 Nov 2021 05:34:03
import gzip
import simplejson as json# Wed, 17 Nov 2021 05:34:04
with gzip.open('./pw-data/201701scripts_sample.json.gz', 'rb') as f:
    scripts = json.load(f)

with gzip.open('./pw-data/practices.json.gz', 'rb') as f:
    practices = json.load(f)# Wed, 17 Nov 2021 05:34:09
scripts[:2]#[Out]# [{'bnf_code': '0101010G0AAABAB',
#[Out]#   'items': 2,
#[Out]#   'practice': 'N81013',
#[Out]#   'bnf_name': 'Co-Magaldrox_Susp 195mg/220mg/5ml S/F',
#[Out]#   'nic': 5.98,
#[Out]#   'act_cost': 5.56,
#[Out]#   'quantity': 1000},
#[Out]#  {'bnf_code': '0101021B0AAAHAH',
#[Out]#   'items': 1,
#[Out]#   'practice': 'N81013',
#[Out]#   'bnf_name': 'Alginate_Raft-Forming Oral Susp S/F',
#[Out]#   'nic': 1.95,
#[Out]#   'act_cost': 1.82,
#[Out]#   'quantity': 500}]
# Wed, 17 Nov 2021 05:34:21
practices[0]#[Out]# {'code': 'A81001',
#[Out]#  'name': 'THE DENSHAM SURGERY',
#[Out]#  'addr_1': 'THE HEALTH CENTRE',
#[Out]#  'addr_2': 'LAWSON STREET',
#[Out]#  'borough': 'STOCKTON ON TEES',
#[Out]#  'village': 'CLEVELAND',
#[Out]#  'post_code': 'TS18 1HU'}
# Wed, 17 Nov 2021 05:34:33
len(scripts)#[Out]# 382726
# Wed, 17 Nov 2021 05:34:41
from statistics import *

def describe(key):
    list_ = []
    if key == 'items' or key == 'quantity' or key == 'nic' or key == 'act_cost':
        for item in scripts:
            list_.append(item[key])
        l = sorted(list_)
    else:
        return 'Error!'
    
    total = sum(list_)
    med = median(l)
    avg = mean(l)
    s = stdev(l)
    
    mid = len(l) // 2
        
    if (len(l) % 2 == 0):
   # even
       q25 = median(l[:mid])
       q75 = median(l[mid:])
    else:
   # odd
       q25 = median(l[:mid])
       q75 = median(l[mid+1:])

    return (total, avg, s, q25, med, q75)# Wed, 17 Nov 2021 05:34:46
summary = [('items', describe('items')),
           ('quantity', describe('quantity')),
           ('nic', describe('nic')),
           ('act_cost', describe('act_cost'))]# Wed, 17 Nov 2021 05:34:53
grader.score.pw__summary_statistics(summary)# Wed, 17 Nov 2021 05:35:05
scripts[:2]#[Out]# [{'bnf_code': '0101010G0AAABAB',
#[Out]#   'items': 2,
#[Out]#   'practice': 'N81013',
#[Out]#   'bnf_name': 'Co-Magaldrox_Susp 195mg/220mg/5ml S/F',
#[Out]#   'nic': 5.98,
#[Out]#   'act_cost': 5.56,
#[Out]#   'quantity': 1000},
#[Out]#  {'bnf_code': '0101021B0AAAHAH',
#[Out]#   'items': 1,
#[Out]#   'practice': 'N81013',
#[Out]#   'bnf_name': 'Alginate_Raft-Forming Oral Susp S/F',
#[Out]#   'nic': 1.95,
#[Out]#   'act_cost': 1.82,
#[Out]#   'quantity': 500}]
# Wed, 17 Nov 2021 05:35:09
bnf_names = {item['bnf_name'] for item in scripts}
assert(len(bnf_names) == 5619)# Wed, 17 Nov 2021 05:35:15
groups = {name: [] for name in bnf_names}
for script in scripts:
    groups[script['bnf_name']].append(script['items'])# Wed, 17 Nov 2021 05:35:33
l_sum = []
for dic in groups:
    l_sum.append(sum(groups[dic]))
#print(l_sum)
max_item = [(dic, max(l_sum)) for dic in groups if sum(groups[dic]) == max(l_sum)]# Wed, 17 Nov 2021 05:35:35
grader.score.pw__most_common_item(max_item)# Wed, 17 Nov 2021 05:35:44
def group_by_field(data, fields):
    names = {tuple(item[field] for field in fields) for item in data}
    groups = {name: [] for name in names}
    for item in data:
        name = tuple(item[field] for field in fields) 
        groups[name].append(item)
    return groups# Wed, 17 Nov 2021 05:36:21
scripts[:2]#[Out]# [{'bnf_code': '0101010G0AAABAB',
#[Out]#   'items': 2,
#[Out]#   'practice': 'N81013',
#[Out]#   'bnf_name': 'Co-Magaldrox_Susp 195mg/220mg/5ml S/F',
#[Out]#   'nic': 5.98,
#[Out]#   'act_cost': 5.56,
#[Out]#   'quantity': 1000},
#[Out]#  {'bnf_code': '0101021B0AAAHAH',
#[Out]#   'items': 1,
#[Out]#   'practice': 'N81013',
#[Out]#   'bnf_name': 'Alginate_Raft-Forming Oral Susp S/F',
#[Out]#   'nic': 1.95,
#[Out]#   'act_cost': 1.82,
#[Out]#   'quantity': 500}]
# Wed, 17 Nov 2021 05:36:26
practices[:2]#[Out]# [{'code': 'A81001',
#[Out]#   'name': 'THE DENSHAM SURGERY',
#[Out]#   'addr_1': 'THE HEALTH CENTRE',
#[Out]#   'addr_2': 'LAWSON STREET',
#[Out]#   'borough': 'STOCKTON ON TEES',
#[Out]#   'village': 'CLEVELAND',
#[Out]#   'post_code': 'TS18 1HU'},
#[Out]#  {'code': 'A81002',
#[Out]#   'name': 'QUEENS PARK MEDICAL CENTRE',
#[Out]#   'addr_1': 'QUEENS PARK MEDICAL CTR',
#[Out]#   'addr_2': 'FARRER STREET',
#[Out]#   'borough': 'STOCKTON ON TEES',
#[Out]#   'village': 'CLEVELAND',
#[Out]#   'post_code': 'TS18 2AW'}]
# Wed, 17 Nov 2021 05:36:34
practices[0]#[Out]# {'code': 'A81001',
#[Out]#  'name': 'THE DENSHAM SURGERY',
#[Out]#  'addr_1': 'THE HEALTH CENTRE',
#[Out]#  'addr_2': 'LAWSON STREET',
#[Out]#  'borough': 'STOCKTON ON TEES',
#[Out]#  'village': 'CLEVELAND',
#[Out]#  'post_code': 'TS18 1HU'}
# Wed, 17 Nov 2021 05:36:40
practice_postal = {}
for practice in practices:
    l=[]
    if practice['code'] in practice_postal:
        l=[practice['post_code'], practice_postal[practice['code']]]
        # print(l)
        practice_postal.update({practice['code']: sorted(l)[0]})
    else:
        practice_postal.update({practice['code']: practice['post_code']})
        # print(practice_postal)# Wed, 17 Nov 2021 05:36:47
assert practice_postal['K82019'] == 'HP21 8TR'# Wed, 17 Nov 2021 05:36:52
joined = scripts[:]
for script in joined:
    k = script['practice']
    script['post_code'] = practice_postal[k]# Wed, 17 Nov 2021 05:37:01
data_group={}
for script in joined:
    data_group.update({script['post_code']:script['items']})
grp = {name: [] for name in data_group}
for script in joined:
    grp[script['post_code']].append(script['items'])
items_by_post = [(k,sum(v)) for k,v in grp.items()]# Wed, 17 Nov 2021 05:37:02
postal_totals = [('B11 4BW', 20673)] * 100

grader.score.pw__postal_totals(postal_totals)# Wed, 17 Nov 2021 05:37:09
postal_totals = sorted(items_by_post)[0:100]

grader.score.pw__postal_totals(postal_totals)# Wed, 17 Nov 2021 05:37:47
items_by_post_name = \
    group_by_field(joined, ('post_code', 'bnf_name')).items()# Wed, 17 Nov 2021 05:37:56
total_items_by_bnf_post = \
    {name: sum([d['items'] for d in group])
     for name, group in items_by_post_name}

assert len(total_items_by_bnf_post) == 141196
# Wed, 17 Nov 2021 05:38:03
total_items = [{'post_code': post_code,
                'bnf_name': bnf_name,
                'total': total}
                for (post_code, bnf_name), total
                in total_items_by_bnf_post.items()]# Wed, 17 Nov 2021 05:38:25
total_items[0:2]#[Out]# [{'post_code': 'WA9 1LN', 'bnf_name': 'Clomipramine HCl_Cap 50mg', 'total': 2},
#[Out]#  {'post_code': 'M30 0NU', 'bnf_name': 'Ketovite_Tab', 'total': 5}]
# Wed, 17 Nov 2021 05:38:33
from collections import OrderedDict 
total_items_by_post_1 = group_by_field(total_items, ('post_code',))
total_items_by_post = OrderedDict(sorted(total_items_by_post_1.items(), key= lambda x: x[0]))# Wed, 17 Nov 2021 05:38:39
assert len(total_items_by_post) == 118# Wed, 17 Nov 2021 05:38:55
max_item_by_post =[
    sorted(group, key= lambda d: (-d['total'], d['bnf_name']))[0]
    for group in list(total_items_by_post.values())
]# Wed, 17 Nov 2021 05:39:01
postal_totals = dict(postal_totals)
len(postal_totals)#[Out]# 100
# Wed, 17 Nov 2021 05:39:07
for script in max_item_by_post[0:100]:
    post_code = script['post_code']
    total = script['total']
    script['proportion'] = total / postal_totals[post_code]# Wed, 17 Nov 2021 05:39:13
items_by_region = [(d['post_code'], d['bnf_name'], d['proportion']) for d in max_item_by_post[0:100]]# Wed, 17 Nov 2021 05:39:19
items_by_region = sorted(items_by_region)# Wed, 17 Nov 2021 05:39:20
grader.score.pw__items_by_region(items_by_region)