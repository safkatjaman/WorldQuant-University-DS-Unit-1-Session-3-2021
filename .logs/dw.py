%logstop
%logstart -rtq ~/.logs/dw.py append
import seaborn as sns
sns.set()
# Wed, 17 Nov 2021 05:21:15
from static_grader import grader# Wed, 17 Nov 2021 05:21:16
%logstop
%logstart -rtq ~/.logs/dw.py append
import seaborn as sns
sns.set()%logstop
%logstart -rtq ~/.logs/dw.py append
import seaborn as sns
sns.set()
from static_grader import grader
%logstop
%logstart -rtq ~/.logs/dw.py append
import seaborn as sns
sns.set()
# Wed, 17 Nov 2021 05:21:20
!mkdir dw-data
!wget http://dataincubator-wqu.s3.amazonaws.com/dwdata/201701scripts_sample.csv.gz -nc -P ./dw-data/
!wget http://dataincubator-wqu.s3.amazonaws.com/dwdata/201606scripts_sample.csv.gz -nc -P ./dw-data/
!wget http://dataincubator-wqu.s3.amazonaws.com/dwdata/practices.csv.gz -nc -P ./dw-data/
!wget http://dataincubator-wqu.s3.amazonaws.com/dwdata/chem.csv.gz -nc -P ./dw-data/# Wed, 17 Nov 2021 05:21:33
# load the 2017 data
scripts = pd.read_csv('./dw-data/201701scripts_sample.csv.gz')
scripts.head()# Wed, 17 Nov 2021 05:21:36
import pandas as pd
import numpy as np# Wed, 17 Nov 2021 05:21:39
# load the 2017 data
scripts = pd.read_csv('./dw-data/201701scripts_sample.csv.gz')
scripts.head()# Wed, 17 Nov 2021 05:21:46
col_names=[ 'code', 'name', 'addr_1', 'addr_2', 'borough', 'village', 'post_code']
practices = pd.read_csv('./dw-data/practices.csv.gz', names=col_names)
practices.head()# Wed, 17 Nov 2021 05:21:54
chem = pd.read_csv('./dw-data/chem.csv.gz')
chem.head()# Wed, 17 Nov 2021 05:22:05
cols = ['items', 'quantity', 'nic', 'act_cost']
summary = ['mean', 'std', '25%', '50%', '75%']
s = scripts[cols].sum().rename('total')
df = scripts[cols].describe().loc[summary]
summaryDf =  pd.concat([s, df.T], axis=1)# Wed, 17 Nov 2021 05:22:11
summaryDf# Wed, 17 Nov 2021 05:22:18
summary_stats = [(t[0], t[1:]) for t in summaryDf.itertuples(name=None)]# Wed, 17 Nov 2021 05:22:21
grader.score.dw__summary_statistics(summary_stats)# Wed, 17 Nov 2021 05:22:37
%logstop
%logstart -rtq ~/.logs/dw.py append
import seaborn as sns
sns.set()%logstop
%logstart -rtq ~/.logs/dw.py append
import seaborn as sns
sns.set()
from static_grader import grader
%logstop
%logstart -rtq ~/.logs/dw.py append
import seaborn as sns
sns.set()
!mkdir dw-data
!wget http://dataincubator-wqu.s3.amazonaws.com/dwdata/201701scripts_sample.csv.gz -nc -P ./dw-data/
!wget http://dataincubator-wqu.s3.amazonaws.com/dwdata/201606scripts_sample.csv.gz -nc -P ./dw-data/
!wget http://dataincubator-wqu.s3.amazonaws.com/dwdata/practices.csv.gz -nc -P ./dw-data/
!wget http://dataincubator-wqu.s3.amazonaws.com/dwdata/chem.csv.gz -nc -P ./dw-data/
# load the 2017 data
scripts = pd.read_csv('./dw-data/201701scripts_sample.csv.gz')
scripts.head()
import pandas as pd
import numpy as np
# load the 2017 data
scripts = pd.read_csv('./dw-data/201701scripts_sample.csv.gz')
scripts.head()
col_names=[ 'code', 'name', 'addr_1', 'addr_2', 'borough', 'village', 'post_code']
practices = pd.read_csv('./dw-data/practices.csv.gz', names=col_names)
practices.head()
chem = pd.read_csv('./dw-data/chem.csv.gz')
chem.head()
cols = ['items', 'quantity', 'nic', 'act_cost']
summary = ['mean', 'std', '25%', '50%', '75%']
s = scripts[cols].sum().rename('total')
df = scripts[cols].describe().loc[summary]
summaryDf =  pd.concat([s, df.T], axis=1)
summaryDf
summary_stats = [(t[0], t[1:]) for t in summaryDf.itertuples(name=None)]
grader.score.dw__summary_statistics(summary_stats)
%logstop
%logstart -rtq ~/.logs/dw.py append
import seaborn as sns
sns.set()
# Wed, 17 Nov 2021 05:22:52
scripts_grouped = scripts.groupby(['bnf_name']).sum()
max_ = max(dict(scripts_grouped['items']).values())
k = list(dict(scripts_grouped['items']).items())
k[0:2]# Wed, 17 Nov 2021 05:23:00
for key,value in k:
    if value == max_:
        d = (key, value)# Wed, 17 Nov 2021 05:23:06
most_common_item = [d]# Wed, 17 Nov 2021 05:23:08
grader.score.dw__most_common_item(most_common_item)# Wed, 17 Nov 2021 05:23:39
unique_practices = (practices.sort_values('post_code')
                             .groupby('code')
                             .first()
                             .reset_index())

joined = scripts.merge(unique_practices[['code', 'post_code']],
                       left_on='practice', 
                       right_on='code', 
                       how='left')

post_item_totals = joined.groupby(['post_code', 'bnf_name'])['items'].sum().reset_index()


post_item_totals.head()

max_idx = (post_item_totals.groupby('post_code')['items'].idxmax())

max_items = post_item_totals.loc[max_idx].set_index('post_code')

post_totals = joined.groupby('post_code')['items'].sum().rename('post_items')

max_items = pd.concat([max_items, post_totals], axis=1, sort=False)

max_items['proportion'] = max_items['items'] / max_items['post_items']

max_items.drop(['items', 'post_items'], axis=1, inplace=True)# Wed, 17 Nov 2021 05:23:45
max_items.head(10)# Wed, 17 Nov 2021 05:23:47
items_by_region = [("B11 4BW", "Salbutamol_Inha 100mcg (200 D) CFF", 0.0310589063)] * 100# Wed, 17 Nov 2021 05:23:49
grader.score.dw__items_by_region(items_by_region)# Wed, 17 Nov 2021 05:23:56
items_by_region = list(max_items.itertuples(name=None))[:100]# Wed, 17 Nov 2021 05:23:58
grader.score.dw__items_by_region(items_by_region)# Wed, 17 Nov 2021 05:24:10
mask = chem['NAME'].str.contains('|'.join(opioids), case=False)

bad_drugs = chem[mask]['CHEM SUB'].unique()

scripts['opioid'] = scripts['bnf_code'].isin(bad_drugs).astype(int)# Wed, 17 Nov 2021 05:24:15
opioids = ['morphine', 'oxycodone', 'methadone', 'fentanyl', 'pethidine', 'buprenorphine', 'propoxyphene', 'codeine']# Wed, 17 Nov 2021 05:24:17
mask = chem['NAME'].str.contains('|'.join(opioids), case=False)

bad_drugs = chem[mask]['CHEM SUB'].unique()

scripts['opioid'] = scripts['bnf_code'].isin(bad_drugs).astype(int)# Wed, 17 Nov 2021 05:24:24
opioids_per_practice = scripts.groupby('practice')['opioid'].mean()# Wed, 17 Nov 2021 05:24:30
relative_opioids_per_practice = opioids_per_practice - scripts['opioid'].mean()# Wed, 17 Nov 2021 05:24:36
standard_error_per_practice = scripts['opioid'].std() / np.sqrt(scripts.practice.value_counts())
opioid_scores = relative_opioids_per_practice / standard_error_per_practice# Wed, 17 Nov 2021 05:24:44
unique_practices = practices.groupby('code')['name'].min()
anomalies = opioid_scores.rename('score').to_frame().join(unique_practices, how='left')
anomalies = anomalies.join(scripts['practice'].value_counts(), how='left')# Wed, 17 Nov 2021 05:24:54
anomalies = anomalies.sort_values('score', ascending=False).head(100)
anomalies = anomalies[['name', 'score', 'practice']]
anomalies.head()# Wed, 17 Nov 2021 05:25:01
anomalies = list(anomalies.itertuples(index=False, name=None))# Wed, 17 Nov 2021 05:25:02
grader.score.dw__script_anomalies(anomalies)# Wed, 17 Nov 2021 05:25:07
%logstop
%logstart -rtq ~/.logs/dw.py append
import seaborn as sns
sns.set()%logstop
%logstart -rtq ~/.logs/dw.py append
import seaborn as sns
sns.set()
from static_grader import grader
%logstop
%logstart -rtq ~/.logs/dw.py append
import seaborn as sns
sns.set()
!mkdir dw-data
!wget http://dataincubator-wqu.s3.amazonaws.com/dwdata/201701scripts_sample.csv.gz -nc -P ./dw-data/
!wget http://dataincubator-wqu.s3.amazonaws.com/dwdata/201606scripts_sample.csv.gz -nc -P ./dw-data/
!wget http://dataincubator-wqu.s3.amazonaws.com/dwdata/practices.csv.gz -nc -P ./dw-data/
!wget http://dataincubator-wqu.s3.amazonaws.com/dwdata/chem.csv.gz -nc -P ./dw-data/
# load the 2017 data
scripts = pd.read_csv('./dw-data/201701scripts_sample.csv.gz')
scripts.head()
import pandas as pd
import numpy as np
# load the 2017 data
scripts = pd.read_csv('./dw-data/201701scripts_sample.csv.gz')
scripts.head()
col_names=[ 'code', 'name', 'addr_1', 'addr_2', 'borough', 'village', 'post_code']
practices = pd.read_csv('./dw-data/practices.csv.gz', names=col_names)
practices.head()
chem = pd.read_csv('./dw-data/chem.csv.gz')
chem.head()
cols = ['items', 'quantity', 'nic', 'act_cost']
summary = ['mean', 'std', '25%', '50%', '75%']
s = scripts[cols].sum().rename('total')
df = scripts[cols].describe().loc[summary]
summaryDf =  pd.concat([s, df.T], axis=1)
summaryDf
summary_stats = [(t[0], t[1:]) for t in summaryDf.itertuples(name=None)]
grader.score.dw__summary_statistics(summary_stats)
%logstop
%logstart -rtq ~/.logs/dw.py append
import seaborn as sns
sns.set()
scripts_grouped = scripts.groupby(['bnf_name']).sum()
max_ = max(dict(scripts_grouped['items']).values())
k = list(dict(scripts_grouped['items']).items())
k[0:2]
for key,value in k:
    if value == max_:
        d = (key, value)
most_common_item = [d]
grader.score.dw__most_common_item(most_common_item)
unique_practices = (practices.sort_values('post_code')
                             .groupby('code')
                             .first()
                             .reset_index())

joined = scripts.merge(unique_practices[['code', 'post_code']],
                       left_on='practice', 
                       right_on='code', 
                       how='left')

post_item_totals = joined.groupby(['post_code', 'bnf_name'])['items'].sum().reset_index()


post_item_totals.head()

max_idx = (post_item_totals.groupby('post_code')['items'].idxmax())

max_items = post_item_totals.loc[max_idx].set_index('post_code')

post_totals = joined.groupby('post_code')['items'].sum().rename('post_items')

max_items = pd.concat([max_items, post_totals], axis=1, sort=False)

max_items['proportion'] = max_items['items'] / max_items['post_items']

max_items.drop(['items', 'post_items'], axis=1, inplace=True)
max_items.head(10)
items_by_region = [("B11 4BW", "Salbutamol_Inha 100mcg (200 D) CFF", 0.0310589063)] * 100
grader.score.dw__items_by_region(items_by_region)
items_by_region = list(max_items.itertuples(name=None))[:100]
grader.score.dw__items_by_region(items_by_region)
mask = chem['NAME'].str.contains('|'.join(opioids), case=False)

bad_drugs = chem[mask]['CHEM SUB'].unique()

scripts['opioid'] = scripts['bnf_code'].isin(bad_drugs).astype(int)
opioids = ['morphine', 'oxycodone', 'methadone', 'fentanyl', 'pethidine', 'buprenorphine', 'propoxyphene', 'codeine']
mask = chem['NAME'].str.contains('|'.join(opioids), case=False)

bad_drugs = chem[mask]['CHEM SUB'].unique()

scripts['opioid'] = scripts['bnf_code'].isin(bad_drugs).astype(int)
opioids_per_practice = scripts.groupby('practice')['opioid'].mean()
relative_opioids_per_practice = opioids_per_practice - scripts['opioid'].mean()
standard_error_per_practice = scripts['opioid'].std() / np.sqrt(scripts.practice.value_counts())
opioid_scores = relative_opioids_per_practice / standard_error_per_practice
unique_practices = practices.groupby('code')['name'].min()
anomalies = opioid_scores.rename('score').to_frame().join(unique_practices, how='left')
anomalies = anomalies.join(scripts['practice'].value_counts(), how='left')
anomalies = anomalies.sort_values('score', ascending=False).head(100)
anomalies = anomalies[['name', 'score', 'practice']]
anomalies.head()
anomalies = list(anomalies.itertuples(index=False, name=None))
grader.score.dw__script_anomalies(anomalies)
%logstop
%logstart -rtq ~/.logs/dw.py append
import seaborn as sns
sns.set()
# Wed, 17 Nov 2021 05:25:40
standard_error_per_practice = scripts['opioid'].std() / np.sqrt(scripts.practice.value_counts())
opioid_scores = relative_opioids_per_practice / standard_error_per_practice# Wed, 17 Nov 2021 05:25:43
unique_practices = practices.groupby('code')['name'].min()
anomalies = opioid_scores.rename('score').to_frame().join(unique_practices, how='left')
anomalies = anomalies.join(scripts['practice'].value_counts(), how='left')# Wed, 17 Nov 2021 05:25:44
anomalies = anomalies.sort_values('score', ascending=False).head(100)
anomalies = anomalies[['name', 'score', 'practice']]
anomalies.head()# Wed, 17 Nov 2021 05:25:45
anomalies = list(anomalies.itertuples(index=False, name=None))# Wed, 17 Nov 2021 05:25:46
grader.score.dw__script_anomalies(anomalies)# Wed, 17 Nov 2021 05:26:25
scripts16 = pd.read_csv('./dw-data/201606scripts_sample.csv.gz')

pct_growth = (scripts['bnf_name'].value_counts() / scripts16['bnf_name'].value_counts() - 1)

#norm_pct_growth = (pct_growth - scripts['bnf_name'].count() / scripts16['bnf_name'].count()-1)

pct_growth = pd.concat([pct_growth.rename('pct_growth'), scripts16.bnf_name.value_counts().rename('count16')], axis=1, sort=True)

mask = norm_pct_growth['count16'] >= 50
filtered_growth = pct_growth[mask].dropna().sort_values('pct_growth', ascending=False)


extreme_growth = pd.concat([filtered_growth.iloc[:50], filtered_growth.iloc[-50:]])# Wed, 17 Nov 2021 05:27:02
%logstop
%logstart -rtq ~/.logs/dw.py append
import seaborn as sns
sns.set()%logstop
%logstart -rtq ~/.logs/dw.py append
import seaborn as sns
sns.set()
from static_grader import grader
%logstop
%logstart -rtq ~/.logs/dw.py append
import seaborn as sns
sns.set()
!mkdir dw-data
!wget http://dataincubator-wqu.s3.amazonaws.com/dwdata/201701scripts_sample.csv.gz -nc -P ./dw-data/
!wget http://dataincubator-wqu.s3.amazonaws.com/dwdata/201606scripts_sample.csv.gz -nc -P ./dw-data/
!wget http://dataincubator-wqu.s3.amazonaws.com/dwdata/practices.csv.gz -nc -P ./dw-data/
!wget http://dataincubator-wqu.s3.amazonaws.com/dwdata/chem.csv.gz -nc -P ./dw-data/
# load the 2017 data
scripts = pd.read_csv('./dw-data/201701scripts_sample.csv.gz')
scripts.head()
import pandas as pd
import numpy as np
# load the 2017 data
scripts = pd.read_csv('./dw-data/201701scripts_sample.csv.gz')
scripts.head()
col_names=[ 'code', 'name', 'addr_1', 'addr_2', 'borough', 'village', 'post_code']
practices = pd.read_csv('./dw-data/practices.csv.gz', names=col_names)
practices.head()
chem = pd.read_csv('./dw-data/chem.csv.gz')
chem.head()
cols = ['items', 'quantity', 'nic', 'act_cost']
summary = ['mean', 'std', '25%', '50%', '75%']
s = scripts[cols].sum().rename('total')
df = scripts[cols].describe().loc[summary]
summaryDf =  pd.concat([s, df.T], axis=1)
summaryDf
summary_stats = [(t[0], t[1:]) for t in summaryDf.itertuples(name=None)]
grader.score.dw__summary_statistics(summary_stats)
%logstop
%logstart -rtq ~/.logs/dw.py append
import seaborn as sns
sns.set()
scripts_grouped = scripts.groupby(['bnf_name']).sum()
max_ = max(dict(scripts_grouped['items']).values())
k = list(dict(scripts_grouped['items']).items())
k[0:2]
for key,value in k:
    if value == max_:
        d = (key, value)
most_common_item = [d]
grader.score.dw__most_common_item(most_common_item)
unique_practices = (practices.sort_values('post_code')
                             .groupby('code')
                             .first()
                             .reset_index())

joined = scripts.merge(unique_practices[['code', 'post_code']],
                       left_on='practice', 
                       right_on='code', 
                       how='left')

post_item_totals = joined.groupby(['post_code', 'bnf_name'])['items'].sum().reset_index()


post_item_totals.head()

max_idx = (post_item_totals.groupby('post_code')['items'].idxmax())

max_items = post_item_totals.loc[max_idx].set_index('post_code')

post_totals = joined.groupby('post_code')['items'].sum().rename('post_items')

max_items = pd.concat([max_items, post_totals], axis=1, sort=False)

max_items['proportion'] = max_items['items'] / max_items['post_items']

max_items.drop(['items', 'post_items'], axis=1, inplace=True)
max_items.head(10)
items_by_region = [("B11 4BW", "Salbutamol_Inha 100mcg (200 D) CFF", 0.0310589063)] * 100
grader.score.dw__items_by_region(items_by_region)
items_by_region = list(max_items.itertuples(name=None))[:100]
grader.score.dw__items_by_region(items_by_region)
mask = chem['NAME'].str.contains('|'.join(opioids), case=False)

bad_drugs = chem[mask]['CHEM SUB'].unique()

scripts['opioid'] = scripts['bnf_code'].isin(bad_drugs).astype(int)
opioids = ['morphine', 'oxycodone', 'methadone', 'fentanyl', 'pethidine', 'buprenorphine', 'propoxyphene', 'codeine']
mask = chem['NAME'].str.contains('|'.join(opioids), case=False)

bad_drugs = chem[mask]['CHEM SUB'].unique()

scripts['opioid'] = scripts['bnf_code'].isin(bad_drugs).astype(int)
opioids_per_practice = scripts.groupby('practice')['opioid'].mean()
relative_opioids_per_practice = opioids_per_practice - scripts['opioid'].mean()
standard_error_per_practice = scripts['opioid'].std() / np.sqrt(scripts.practice.value_counts())
opioid_scores = relative_opioids_per_practice / standard_error_per_practice
unique_practices = practices.groupby('code')['name'].min()
anomalies = opioid_scores.rename('score').to_frame().join(unique_practices, how='left')
anomalies = anomalies.join(scripts['practice'].value_counts(), how='left')
anomalies = anomalies.sort_values('score', ascending=False).head(100)
anomalies = anomalies[['name', 'score', 'practice']]
anomalies.head()
anomalies = list(anomalies.itertuples(index=False, name=None))
grader.score.dw__script_anomalies(anomalies)
%logstop
%logstart -rtq ~/.logs/dw.py append
import seaborn as sns
sns.set()
standard_error_per_practice = scripts['opioid'].std() / np.sqrt(scripts.practice.value_counts())
opioid_scores = relative_opioids_per_practice / standard_error_per_practice
unique_practices = practices.groupby('code')['name'].min()
anomalies = opioid_scores.rename('score').to_frame().join(unique_practices, how='left')
anomalies = anomalies.join(scripts['practice'].value_counts(), how='left')
anomalies = anomalies.sort_values('score', ascending=False).head(100)
anomalies = anomalies[['name', 'score', 'practice']]
anomalies.head()
anomalies = list(anomalies.itertuples(index=False, name=None))
grader.score.dw__script_anomalies(anomalies)
scripts16 = pd.read_csv('./dw-data/201606scripts_sample.csv.gz')

pct_growth = (scripts['bnf_name'].value_counts() / scripts16['bnf_name'].value_counts() - 1)

#norm_pct_growth = (pct_growth - scripts['bnf_name'].count() / scripts16['bnf_name'].count()-1)

pct_growth = pd.concat([pct_growth.rename('pct_growth'), scripts16.bnf_name.value_counts().rename('count16')], axis=1, sort=True)

mask = norm_pct_growth['count16'] >= 50
filtered_growth = pct_growth[mask].dropna().sort_values('pct_growth', ascending=False)


extreme_growth = pd.concat([filtered_growth.iloc[:50], filtered_growth.iloc[-50:]])
%logstop
%logstart -rtq ~/.logs/dw.py append
import seaborn as sns
sns.set()
# Wed, 17 Nov 2021 05:27:23
extreme_growth.shape# Wed, 17 Nov 2021 05:27:31
script_growth = list(extreme_growth.itertuples(index=True, name=None))# Wed, 17 Nov 2021 05:27:33
grader.score.dw__script_growth(script_growth)# Wed, 17 Nov 2021 05:27:56
p = 1/ scripts['bnf_code'].nunique()
rates = scripts['bnf_code'].value_counts() / scripts['bnf_code'].count()
rare_codes = rates[rates < .1 * p].index
scripts['rare'] = scripts['bnf_code'].isin(rare_codes)# Wed, 17 Nov 2021 05:28:00
rare_scripts = scripts[scripts['rare']].copy()# Wed, 17 Nov 2021 05:28:07
%logstop
%logstart -rtq ~/.logs/dw.py append
import seaborn as sns
sns.set()%logstop
%logstart -rtq ~/.logs/dw.py append
import seaborn as sns
sns.set()
from static_grader import grader
%logstop
%logstart -rtq ~/.logs/dw.py append
import seaborn as sns
sns.set()
!mkdir dw-data
!wget http://dataincubator-wqu.s3.amazonaws.com/dwdata/201701scripts_sample.csv.gz -nc -P ./dw-data/
!wget http://dataincubator-wqu.s3.amazonaws.com/dwdata/201606scripts_sample.csv.gz -nc -P ./dw-data/
!wget http://dataincubator-wqu.s3.amazonaws.com/dwdata/practices.csv.gz -nc -P ./dw-data/
!wget http://dataincubator-wqu.s3.amazonaws.com/dwdata/chem.csv.gz -nc -P ./dw-data/
# load the 2017 data
scripts = pd.read_csv('./dw-data/201701scripts_sample.csv.gz')
scripts.head()
import pandas as pd
import numpy as np
# load the 2017 data
scripts = pd.read_csv('./dw-data/201701scripts_sample.csv.gz')
scripts.head()
col_names=[ 'code', 'name', 'addr_1', 'addr_2', 'borough', 'village', 'post_code']
practices = pd.read_csv('./dw-data/practices.csv.gz', names=col_names)
practices.head()
chem = pd.read_csv('./dw-data/chem.csv.gz')
chem.head()
cols = ['items', 'quantity', 'nic', 'act_cost']
summary = ['mean', 'std', '25%', '50%', '75%']
s = scripts[cols].sum().rename('total')
df = scripts[cols].describe().loc[summary]
summaryDf =  pd.concat([s, df.T], axis=1)
summaryDf
summary_stats = [(t[0], t[1:]) for t in summaryDf.itertuples(name=None)]
grader.score.dw__summary_statistics(summary_stats)
%logstop
%logstart -rtq ~/.logs/dw.py append
import seaborn as sns
sns.set()
scripts_grouped = scripts.groupby(['bnf_name']).sum()
max_ = max(dict(scripts_grouped['items']).values())
k = list(dict(scripts_grouped['items']).items())
k[0:2]
for key,value in k:
    if value == max_:
        d = (key, value)
most_common_item = [d]
grader.score.dw__most_common_item(most_common_item)
unique_practices = (practices.sort_values('post_code')
                             .groupby('code')
                             .first()
                             .reset_index())

joined = scripts.merge(unique_practices[['code', 'post_code']],
                       left_on='practice', 
                       right_on='code', 
                       how='left')

post_item_totals = joined.groupby(['post_code', 'bnf_name'])['items'].sum().reset_index()


post_item_totals.head()

max_idx = (post_item_totals.groupby('post_code')['items'].idxmax())

max_items = post_item_totals.loc[max_idx].set_index('post_code')

post_totals = joined.groupby('post_code')['items'].sum().rename('post_items')

max_items = pd.concat([max_items, post_totals], axis=1, sort=False)

max_items['proportion'] = max_items['items'] / max_items['post_items']

max_items.drop(['items', 'post_items'], axis=1, inplace=True)
max_items.head(10)
items_by_region = [("B11 4BW", "Salbutamol_Inha 100mcg (200 D) CFF", 0.0310589063)] * 100
grader.score.dw__items_by_region(items_by_region)
items_by_region = list(max_items.itertuples(name=None))[:100]
grader.score.dw__items_by_region(items_by_region)
mask = chem['NAME'].str.contains('|'.join(opioids), case=False)

bad_drugs = chem[mask]['CHEM SUB'].unique()

scripts['opioid'] = scripts['bnf_code'].isin(bad_drugs).astype(int)
opioids = ['morphine', 'oxycodone', 'methadone', 'fentanyl', 'pethidine', 'buprenorphine', 'propoxyphene', 'codeine']
mask = chem['NAME'].str.contains('|'.join(opioids), case=False)

bad_drugs = chem[mask]['CHEM SUB'].unique()

scripts['opioid'] = scripts['bnf_code'].isin(bad_drugs).astype(int)
opioids_per_practice = scripts.groupby('practice')['opioid'].mean()
relative_opioids_per_practice = opioids_per_practice - scripts['opioid'].mean()
standard_error_per_practice = scripts['opioid'].std() / np.sqrt(scripts.practice.value_counts())
opioid_scores = relative_opioids_per_practice / standard_error_per_practice
unique_practices = practices.groupby('code')['name'].min()
anomalies = opioid_scores.rename('score').to_frame().join(unique_practices, how='left')
anomalies = anomalies.join(scripts['practice'].value_counts(), how='left')
anomalies = anomalies.sort_values('score', ascending=False).head(100)
anomalies = anomalies[['name', 'score', 'practice']]
anomalies.head()
anomalies = list(anomalies.itertuples(index=False, name=None))
grader.score.dw__script_anomalies(anomalies)
%logstop
%logstart -rtq ~/.logs/dw.py append
import seaborn as sns
sns.set()
standard_error_per_practice = scripts['opioid'].std() / np.sqrt(scripts.practice.value_counts())
opioid_scores = relative_opioids_per_practice / standard_error_per_practice
unique_practices = practices.groupby('code')['name'].min()
anomalies = opioid_scores.rename('score').to_frame().join(unique_practices, how='left')
anomalies = anomalies.join(scripts['practice'].value_counts(), how='left')
anomalies = anomalies.sort_values('score', ascending=False).head(100)
anomalies = anomalies[['name', 'score', 'practice']]
anomalies.head()
anomalies = list(anomalies.itertuples(index=False, name=None))
grader.score.dw__script_anomalies(anomalies)
scripts16 = pd.read_csv('./dw-data/201606scripts_sample.csv.gz')

pct_growth = (scripts['bnf_name'].value_counts() / scripts16['bnf_name'].value_counts() - 1)

#norm_pct_growth = (pct_growth - scripts['bnf_name'].count() / scripts16['bnf_name'].count()-1)

pct_growth = pd.concat([pct_growth.rename('pct_growth'), scripts16.bnf_name.value_counts().rename('count16')], axis=1, sort=True)

mask = norm_pct_growth['count16'] >= 50
filtered_growth = pct_growth[mask].dropna().sort_values('pct_growth', ascending=False)


extreme_growth = pd.concat([filtered_growth.iloc[:50], filtered_growth.iloc[-50:]])
%logstop
%logstart -rtq ~/.logs/dw.py append
import seaborn as sns
sns.set()
extreme_growth.shape
script_growth = list(extreme_growth.itertuples(index=True, name=None))
grader.score.dw__script_growth(script_growth)
p = 1/ scripts['bnf_code'].nunique()
rates = scripts['bnf_code'].value_counts() / scripts['bnf_code'].count()
rare_codes = rates[rates < .1 * p].index
scripts['rare'] = scripts['bnf_code'].isin(rare_codes)
rare_scripts = scripts[scripts['rare']].copy()
%logstop
%logstart -rtq ~/.logs/dw.py append
import seaborn as sns
sns.set()
# Wed, 17 Nov 2021 05:28:49
rare = scripts[scripts['rare']].groupby('practice')['act_cost'].sum()
total = scripts.groupby('practice')['act_cost'].sum()# Wed, 17 Nov 2021 05:29:01
rare_cost_prop = (rare / total).fillna(0) # Wed, 17 Nov 2021 05:29:13
proportion = scripts[scripts['rare']]['act_cost'].sum() / scripts['act_cost'].sum()
relative_rare_cost_prop = rare_cost_prop - proportion# Wed, 17 Nov 2021 05:29:18
standard_errors = relative_rare_cost_prop.std()# Wed, 17 Nov 2021 05:29:25
rare_scores = relative_rare_cost_prop / standard_errors# Wed, 17 Nov 2021 05:29:40
rare_scripts = rare_scores.to_frame().merge(unique_practices, how='left', left_index=True, right_on='code')# Wed, 17 Nov 2021 05:29:46
rare_scripts = rare_scripts[['name', 'act_cost']]# Wed, 17 Nov 2021 05:29:51
rare_scripts = list(rare_scripts.sort_values('act_cost', ascending=False).itertuples(name=None))[:100]# Wed, 17 Nov 2021 05:29:52
grader.score.dw__rare_scripts(rare_scripts)%logstop
%logstart -rtq ~/.logs/dw.py append
import seaborn as sns
sns.set()
# Wed, 17 Nov 2021 05:43:52
opioids_join = '|'.join(opioids)
opioids_join# Wed, 17 Nov 2021 05:43:57
opioids = ['morphine', 'oxycodone', 'methadone', 'fentanyl', 'pethidine', 'buprenorphine', 'propoxyphene', 'codeine']# Wed, 17 Nov 2021 05:43:59
opioids_join = '|'.join(opioids)
opioids_join# Wed, 17 Nov 2021 05:44:06
chem.head()# Wed, 17 Nov 2021 05:44:16
%logstop
%logstart -rtq ~/.logs/dw.py append
import seaborn as sns
sns.set()%logstop
%logstart -rtq ~/.logs/dw.py append
import seaborn as sns
sns.set()
opioids_join = '|'.join(opioids)
opioids_join
opioids = ['morphine', 'oxycodone', 'methadone', 'fentanyl', 'pethidine', 'buprenorphine', 'propoxyphene', 'codeine']
opioids_join = '|'.join(opioids)
opioids_join
chem.head()
%logstop
%logstart -rtq ~/.logs/dw.py append
import seaborn as sns
sns.set()
# Wed, 17 Nov 2021 05:44:17
from static_grader import grader# Wed, 17 Nov 2021 05:44:19
!mkdir dw-data
!wget http://dataincubator-wqu.s3.amazonaws.com/dwdata/201701scripts_sample.csv.gz -nc -P ./dw-data/
!wget http://dataincubator-wqu.s3.amazonaws.com/dwdata/201606scripts_sample.csv.gz -nc -P ./dw-data/
!wget http://dataincubator-wqu.s3.amazonaws.com/dwdata/practices.csv.gz -nc -P ./dw-data/
!wget http://dataincubator-wqu.s3.amazonaws.com/dwdata/chem.csv.gz -nc -P ./dw-data/# Wed, 17 Nov 2021 05:44:41
chem.head()# Wed, 17 Nov 2021 05:45:12
%matplotlib inline
import matplotlib
import seaborn as sns
sns.set()
matplotlib.rcParams['figure.dpi'] = 144# Wed, 17 Nov 2021 05:45:13
from static_grader import grader# Wed, 17 Nov 2021 05:45:24
!mkdir dw-data
!wget http://dataincubator-wqu.s3.amazonaws.com/dwdata/201701scripts_sample.csv.gz -nc -P ./dw-data/
!wget http://dataincubator-wqu.s3.amazonaws.com/dwdata/201606scripts_sample.csv.gz -nc -P ./dw-data/
!wget http://dataincubator-wqu.s3.amazonaws.com/dwdata/practices.csv.gz -nc -P ./dw-data/
!wget http://dataincubator-wqu.s3.amazonaws.com/dwdata/chem.csv.gz -nc -P ./dw-data/# Wed, 17 Nov 2021 05:45:31
import pandas as pd
import numpy as np# Wed, 17 Nov 2021 05:45:36
import pandas as pd
import numpy as np
import gzip# Wed, 17 Nov 2021 05:46:02
# load the 2017 data
scripts = pd.read_csv('./dw-data/201701scripts_sample.csv.gz')
scripts.head()# Wed, 17 Nov 2021 05:46:03
col_names=[ 'code', 'name', 'addr_1', 'addr_2', 'borough', 'village', 'post_code']
practices = pd.read_csv('./dw-data/practices.csv.gz', names=col_names)
practices.head()# Wed, 17 Nov 2021 05:46:04
chem = pd.read_csv('./dw-data/chem.csv.gz')
chem.head()# Wed, 17 Nov 2021 05:46:11
chem.head()# Wed, 17 Nov 2021 05:46:21
opioid_codes = chem.loc[chem['NAME'].str.contains(opioids_join, case=False)]['CHEM SUB'].tolist()
len(opioid_codes)# Wed, 17 Nov 2021 05:46:28
chem_new = chem
chem_new.columns = ['bnf_code','chem_name']
chem_new.head()# Wed, 17 Nov 2021 05:46:37
scripts.head()# Wed, 17 Nov 2021 05:48:01
scripts.shape# Wed, 17 Nov 2021 05:48:05
scrpt = scripts
scrpt.head()# Wed, 17 Nov 2021 05:48:11
scrpt['opioid_prescription'] = scrpt['bnf_code'].isin(opioid_codes)# Wed, 17 Nov 2021 05:48:21
scrpt.head()# Wed, 17 Nov 2021 05:48:23
scrpt.shape# Wed, 17 Nov 2021 05:48:28
practices.head()# Wed, 17 Nov 2021 05:48:32
pract = practices[['code', 'name']]
pract.columns = ['practice', 'name']
pract.head()# Wed, 17 Nov 2021 05:48:37
len(scrpt.loc[scrpt['opioid_prescription']])# Wed, 17 Nov 2021 05:48:41
opioids_per_practice = scrpt.groupby('practice')['opioid_prescription'].mean().rename('frac')
opioids_per_practice.head()# Wed, 17 Nov 2021 05:48:46
opioids_per_practice_std = scrpt.groupby('practice')['opioid_prescription'].std().rename('frac_std')
opioids_per_practice_std.head()# Wed, 17 Nov 2021 05:48:51
overall_rate = scrpt['opioid_prescription'].mean()
overall_rate# Wed, 17 Nov 2021 05:48:55
overall_rate_std = scrpt['opioid_prescription'].std()
overall_rate_std# Wed, 17 Nov 2021 05:48:59
relative_opioids_per_practice = (opioids_per_practice - overall_rate).rename('relative')
relative_opioids_per_practice.head()# Wed, 17 Nov 2021 05:49:04
opioid = scrpt.groupby('practice')['opioid_prescription'].sum().rename('opioid')
opioid.head()# Wed, 17 Nov 2021 05:49:09
total = scrpt.groupby('practice')['bnf_code'].count().rename('total')
total.head()# Wed, 17 Nov 2021 05:49:14
standard_error_per_practice = (overall_rate_std/(total**0.5)).rename('std_err')
standard_error_per_practice.head()# Wed, 17 Nov 2021 05:49:20
opioid_scores = (relative_opioids_per_practice/standard_error_per_practice).rename('opioid_scores')
opioid_scores.head()# Wed, 17 Nov 2021 05:49:25
merged = pd.concat([opioid, total, opioids_per_practice, relative_opioids_per_practice, standard_error_per_practice,opioid_scores], axis=1)# Wed, 17 Nov 2021 05:49:33
merged = merged.reset_index()# Wed, 17 Nov 2021 05:49:38
merged.head()
# Wed, 17 Nov 2021 05:49:42
type(merged)# Wed, 17 Nov 2021 05:49:49
merged.shape# Wed, 17 Nov 2021 05:49:52
pract.reset_index().head()# Wed, 17 Nov 2021 05:52:09
type(pract)# Wed, 17 Nov 2021 05:52:14
final_df = merged.merge(pract, on='practice', how='left')# Wed, 17 Nov 2021 05:52:22
final_df.head()# Wed, 17 Nov 2021 05:52:30
final = final_df.drop_duplicates('name')
final.head()# Wed, 17 Nov 2021 05:52:35
result = final[['name','opioid_scores','total']]
result.head()# Wed, 17 Nov 2021 05:52:40
result = result.head(100)
values = result.values.tolist()# Wed, 17 Nov 2021 05:52:45
answer=[]

for item in values:
    answer.append(tuple(item))# Wed, 17 Nov 2021 05:52:52
def script_anomalies():
    return answer# Wed, 17 Nov 2021 05:53:18
grader.score('dw__script_anomalies', script_anomalies)# Wed, 17 Nov 2021 05:53:38
%matplotlib inline
import matplotlib
import seaborn as sns
sns.set()
matplotlib.rcParams['figure.dpi'] = 144# Wed, 17 Nov 2021 05:53:43
mask = chem['NAME'].str.contains('|'.join(opioids), case=False)

bad_drugs = chem[mask]['CHEM SUB'].unique()

scripts['opioid'] = scripts['bnf_code'].isin(bad_drugs).astype(int)# Wed, 17 Nov 2021 05:53:53
opioids_per_practice = scripts.groupby('practice')['opioid'].mean()# Wed, 17 Nov 2021 05:54:00
grader.score.dw__script_anomalies(anomalies)# Wed, 17 Nov 2021 05:54:05
anomalies = list(anomalies.itertuples(index=False, name=None))# Wed, 17 Nov 2021 05:54:34
grader.score('dw__script_anomalies', script_anomalies)# Wed, 17 Nov 2021 05:57:09
%matplotlib inline
import matplotlib
import seaborn as sns
sns.set()
matplotlib.rcParams['figure.dpi'] = 144# Wed, 17 Nov 2021 05:57:56
opioids = ['morphine', 'oxycodone', 'methadone', 'fentanyl', 'pethidine', 'buprenorphine', 'propoxyphene', 'codeine']# Wed, 17 Nov 2021 05:58:05
bychemsub = chem.groupby('CHEM SUB')['NAME'].unique() #take all the unique chem subs into a pd series# Wed, 17 Nov 2021 06:03:03
%matplotlib inline
import matplotlib
import seaborn as sns
sns.set()
matplotlib.rcParams['figure.dpi'] = 144# Wed, 17 Nov 2021 06:05:57
%logstop
%logstart -ortq ~/.logs/dw.py append
%matplotlib inline
import matplotlib
import seaborn as sns
sns.set()
matplotlib.rcParams['figure.dpi'] = 144%logstop
%logstart -ortq ~/.logs/dw.py append
%matplotlib inline
import matplotlib
import seaborn as sns
sns.set()
matplotlib.rcParams['figure.dpi'] = 144
# Wed, 17 Nov 2021 06:05:58
from static_grader import grader# Wed, 17 Nov 2021 06:06:01
!mkdir dw-data
!wget http://dataincubator-wqu.s3.amazonaws.com/dwdata/201701scripts_sample.csv.gz -nc -P ./dw-data/
!wget http://dataincubator-wqu.s3.amazonaws.com/dwdata/201606scripts_sample.csv.gz -nc -P ./dw-data/
!wget http://dataincubator-wqu.s3.amazonaws.com/dwdata/practices.csv.gz -nc -P ./dw-data/
!wget http://dataincubator-wqu.s3.amazonaws.com/dwdata/chem.csv.gz -nc -P ./dw-data/# Wed, 17 Nov 2021 06:06:05
import pandas as pd
import numpy as np
import gzip# Wed, 17 Nov 2021 06:06:05
# load the 2017 data
scripts = pd.read_csv('./dw-data/201701scripts_sample.csv.gz')
scripts.head()#[Out]#   practice   bnf_code                              bnf_name  items   nic  \
#[Out]# 0   N85639  0106020C0                 Bisacodyl_Tab E/C 5mg      1  0.39   
#[Out]# 1   N85639  0106040M0      Movicol Plain_Paed Pdr Sach 6.9g      1  4.38   
#[Out]# 2   N85639  0301011R0    Salbutamol_Inha 100mcg (200 D) CFF      1  1.50   
#[Out]# 3   N85639  0304010G0  Chlorphenamine Mal_Oral Soln 2mg/5ml      1  2.62   
#[Out]# 4   N85639  0401020K0                      Diazepam_Tab 2mg      1  0.16   
#[Out]# 
#[Out]#    act_cost  quantity  
#[Out]# 0      0.47        12  
#[Out]# 1      4.07        30  
#[Out]# 2      1.40         1  
#[Out]# 3      2.44       150  
#[Out]# 4      0.26         6  
# Wed, 17 Nov 2021 06:06:07
col_names=[ 'code', 'name', 'addr_1', 'addr_2', 'borough', 'village', 'post_code']
practices = pd.read_csv('./dw-data/practices.csv.gz', names=col_names)
practices.head()#[Out]#      code                        name                   addr_1         addr_2  \
#[Out]# 0  A81001         THE DENSHAM SURGERY        THE HEALTH CENTRE  LAWSON STREET   
#[Out]# 1  A81002  QUEENS PARK MEDICAL CENTRE  QUEENS PARK MEDICAL CTR  FARRER STREET   
#[Out]# 2  A81003   VICTORIA MEDICAL PRACTICE        THE HEALTH CENTRE  VICTORIA ROAD   
#[Out]# 3  A81004      WOODLANDS ROAD SURGERY         6 WOODLANDS ROAD            NaN   
#[Out]# 4  A81005          SPRINGWOOD SURGERY       SPRINGWOOD SURGERY   RECTORY LANE   
#[Out]# 
#[Out]#             borough    village post_code  
#[Out]# 0  STOCKTON ON TEES  CLEVELAND  TS18 1HU  
#[Out]# 1  STOCKTON ON TEES  CLEVELAND  TS18 2AW  
#[Out]# 2        HARTLEPOOL  CLEVELAND  TS26 8DB  
#[Out]# 3     MIDDLESBROUGH  CLEVELAND   TS1 3BE  
#[Out]# 4       GUISBOROUGH        NaN  TS14 7DJ  
# Wed, 17 Nov 2021 06:06:09
chem = pd.read_csv('./dw-data/chem.csv.gz')
chem.head()#[Out]#     CHEM SUB                                NAME
#[Out]# 0  0101010A0                     Alexitol Sodium
#[Out]# 1  0101010B0                          Almasilate
#[Out]# 2  0101010C0                 Aluminium Hydroxide
#[Out]# 3  0101010D0  Aluminium Hydroxide With Magnesium
#[Out]# 4  0101010E0                        Hydrotalcite
# Wed, 17 Nov 2021 06:06:15
cols = ['items', 'quantity', 'nic', 'act_cost']
summary = ['mean', 'std', '25%', '50%', '75%']
s = scripts[cols].sum().rename('total')
df = scripts[cols].describe().loc[summary]
summaryDf =  pd.concat([s, df.T], axis=1)# Wed, 17 Nov 2021 06:06:15
summaryDf#[Out]#                  total        mean          std    25%     50%     75%
#[Out]# items     8.888304e+06    9.133136    29.204198   1.00    2.00    6.00
#[Out]# quantity  7.214570e+08  741.329835  3665.426958  28.00  100.00  350.00
#[Out]# nic       7.110042e+07   73.058915   188.070257   7.80   22.64   65.00
#[Out]# act_cost  6.616410e+07   67.986613   174.401703   7.33   21.22   60.67
# Wed, 17 Nov 2021 06:06:16
summary_stats = [(t[0], t[1:]) for t in summaryDf.itertuples(name=None)]# Wed, 17 Nov 2021 06:06:17
grader.score.dw__summary_statistics(summary_stats)# Wed, 17 Nov 2021 06:06:20
scripts_grouped = scripts.groupby(['bnf_name']).sum()
max_ = max(dict(scripts_grouped['items']).values())
k = list(dict(scripts_grouped['items']).items())
k[0:2]#[Out]# [('365 Film 10cm x 12cm VP Adh Film Dress', 2),
#[Out]#  ('365 Non Adherent 10cm x 10cm Pfa Plas Fa', 3)]
# Wed, 17 Nov 2021 06:06:21
for key,value in k:
    if value == max_:
        d = (key, value)# Wed, 17 Nov 2021 06:06:22
most_common_item = [d]# Wed, 17 Nov 2021 06:06:22
grader.score.dw__most_common_item(most_common_item)# Wed, 17 Nov 2021 06:06:25
unique_practices = (practices.sort_values('post_code')
                             .groupby('code')
                             .first()
                             .reset_index())

joined = scripts.merge(unique_practices[['code', 'post_code']],
                       left_on='practice', 
                       right_on='code', 
                       how='left')

post_item_totals = joined.groupby(['post_code', 'bnf_name'])['items'].sum().reset_index()


post_item_totals.head()

max_idx = (post_item_totals.groupby('post_code')['items'].idxmax())

max_items = post_item_totals.loc[max_idx].set_index('post_code')

post_totals = joined.groupby('post_code')['items'].sum().rename('post_items')

max_items = pd.concat([max_items, post_totals], axis=1, sort=False)

max_items['proportion'] = max_items['items'] / max_items['post_items']

max_items.drop(['items', 'post_items'], axis=1, inplace=True)# Wed, 17 Nov 2021 06:06:26
max_items.head(10)#[Out]#                                      bnf_name  proportion
#[Out]# post_code                                                
#[Out]# B11 4BW    Salbutamol_Inha 100mcg (200 D) CFF    0.031059
#[Out]# B12 9LP                     Paracet_Tab 500mg    0.024893
#[Out]# B18 7AL    Salbutamol_Inha 100mcg (200 D) CFF    0.027111
#[Out]# B21 9RY               Metformin HCl_Tab 500mg    0.033294
#[Out]# B23 6DJ      Lansoprazole_Cap 30mg (E/C Gran)    0.021384
#[Out]# B61 0AZ               Omeprazole_Cap E/C 20mg    0.028713
#[Out]# B70 7AW                     Paracet_Tab 500mg    0.025136
#[Out]# B72 1RL               Omeprazole_Cap E/C 20mg    0.020229
#[Out]# B8 1RZ                Metformin HCl_Tab 500mg    0.021348
#[Out]# B9 5PU       Ventolin_Evohaler 100mcg (200 D)    0.024826
# Wed, 17 Nov 2021 06:06:27
items_by_region = list(max_items.itertuples(name=None))[:100]# Wed, 17 Nov 2021 06:06:28
grader.score.dw__items_by_region(items_by_region)# Wed, 17 Nov 2021 06:06:30
opioids = ['morphine', 'oxycodone', 'methadone', 'fentanyl', 'pethidine', 'buprenorphine', 'propoxyphene', 'codeine']# Wed, 17 Nov 2021 06:06:32
mask = chem['NAME'].str.contains('|'.join(opioids), case=False)

bad_drugs = chem[mask]['CHEM SUB'].unique()

scripts['opioid'] = scripts['bnf_code'].isin(bad_drugs).astype(int)# Wed, 17 Nov 2021 06:06:34
opioids_per_practice = scripts.groupby('practice')['opioid'].mean()# Wed, 17 Nov 2021 06:06:35
relative_opioids_per_practice = opioids_per_practice - scripts['opioid'].mean()# Wed, 17 Nov 2021 06:06:37
standard_error_per_practice = scripts['opioid'].std() / np.sqrt(scripts.practice.value_counts())
opioid_scores = relative_opioids_per_practice / standard_error_per_practice# Wed, 17 Nov 2021 06:06:40
unique_practices = practices.groupby('code')['name'].min()
anomalies = opioid_scores.rename('score').to_frame().join(unique_practices, how='left')
anomalies = anomalies.join(scripts['practice'].value_counts(), how='left')# Wed, 17 Nov 2021 06:06:41
anomalies = anomalies.sort_values('score', ascending=False).head(100)
anomalies = anomalies[['name', 'score', 'practice']]
anomalies.head()#[Out]#                                    name      score  practice
#[Out]# Y01852        NATIONAL ENHANCED SERVICE  11.695818         7
#[Out]# Y03006         OUTREACH SERVICE NH / RH   7.339043         2
#[Out]# Y03668  BRISDOC HEALTHCARE SERVICES OOH   6.150582        60
#[Out]# G81703           H&R P C SPECIAL SCHEME   5.123032        36
#[Out]# Y04997                   HMR BARDOC OOH   4.958866       321
# Wed, 17 Nov 2021 06:06:43
anomalies = list(anomalies.itertuples(index=False, name=None))# Wed, 17 Nov 2021 06:06:43
grader.score.dw__script_anomalies(anomalies)# Wed, 17 Nov 2021 06:11:35
anomalies = [("NATIONAL ENHANCED SERVICE", 11.6958178629, 7)] * 100# Wed, 17 Nov 2021 06:11:36
grader.score.dw__script_anomalies(anomalies)# Wed, 17 Nov 2021 06:12:03
import math
import gzip
import pandas as pd
from static_grader import grader


chem = pd.read_csv('./dw-data/chem.csv.gz', compression='gzip', header=0, sep=',', quotechar='"', error_bad_lines=False)
chem.head()
chem.columns

with gzip.open ( './dw-data/201701scripts_sample.csv.gz', 'rb' ) as f:
    scripts = pd.read_csv ( f )

with gzip.open ( './dw-data/practices.csv.gz', 'rb' ) as f:
    practices = pd.read_csv ( f )



practices.columns = ['code', 'name', 'addr_1', 'addr_2', 'borough', 'village', 'post_code'] 
practices = practices[['code', 'name']].sort_values (by = ['name'], ascending = True) 
practices = practices [~practices.duplicated(['code'])] 
opioids = ['morphine', 'oxycodone', 'methadone', 'fentanyl', 'pethidine', 'buprenorphine', 'propoxyphene', 'codeine'] 


check = '|'.join(opioids) 
chem_df1 = chem 
chem_df1 [ 'test' ] = chem_df1 [ 'NAME' ].apply ( lambda x: any ( [ k in x.lower() for k in opioids ] ) ) 
key2 = chem_df1 [ "test" ] == True 
chem_df1 = chem_df1 [ key2 ]  
chem_sub = list (chem_df1['CHEM SUB']) 


scripts['opioid'] = scripts [ 'bnf_code' ].apply(lambda x: 1 if x in chem_sub else 0)
std_devn = scripts.opioid.std ()
overall_rate = scripts.opioid.mean()

scripts = scripts.merge (practices, left_on = 'practice', right_on = 'code')
scripts['cnt'] = 0


opioids_per_practice = scripts.groupby ( [ 'practice', 'name' ], as_index = False ).agg ( { 'opioid': 'mean', 'cnt': 'count' } )
opioids_per_practice.drop_duplicates()

opioids_per_practice['opioid'] = opioids_per_practice ['opioid'] - overall_rate

opioids_per_practice['std_err'] = std_devn / opioids_per_practice['cnt'] ** 0.5
opioids_per_practice['z_score'] = opioids_per_practice['opioid'] / opioids_per_practice['std_err']

result = opioids_per_practice[['name', 'z_score', 'cnt']]


result.sort_values(by = 'z_score', ascending = False, inplace = True)
anomalies = [(k[1], k[2], k[3]) for k in result.itertuples()][:100]# Wed, 17 Nov 2021 06:12:25
anomalies = [("NATIONAL ENHANCED SERVICE", 11.6958178629, 7)] * 100# Wed, 17 Nov 2021 06:12:25
grader.score.dw__script_anomalies(anomalies)%logstop
%logstart -rtq ~/.logs/dw.py append
%matplotlib inline
import matplotlib
import seaborn as sns
sns.set()
matplotlib.rcParams['figure.dpi'] = 144
# Wed, 17 Nov 2021 06:38:58
%logstop
%logstart -rtq ~/.logs/dw.py append
%matplotlib inline
import matplotlib
import seaborn as sns
sns.set()
matplotlib.rcParams['figure.dpi'] = 144%logstop
%logstart -rtq ~/.logs/dw.py append
%matplotlib inline
import matplotlib
import seaborn as sns
sns.set()
matplotlib.rcParams['figure.dpi'] = 144
%logstop
%logstart -rtq ~/.logs/dw.py append
%matplotlib inline
import matplotlib
import seaborn as sns
sns.set()
matplotlib.rcParams['figure.dpi'] = 144
# Wed, 17 Nov 2021 06:38:58
from static_grader import grader# Wed, 17 Nov 2021 06:39:03
!mkdir dw-data
!wget http://dataincubator-wqu.s3.amazonaws.com/dwdata/201701scripts_sample.csv.gz -nc -P ./dw-data/
!wget http://dataincubator-wqu.s3.amazonaws.com/dwdata/201606scripts_sample.csv.gz -nc -P ./dw-data/
!wget http://dataincubator-wqu.s3.amazonaws.com/dwdata/practices.csv.gz -nc -P ./dw-data/
!wget http://dataincubator-wqu.s3.amazonaws.com/dwdata/chem.csv.gz -nc -P ./dw-data/# Wed, 17 Nov 2021 06:39:07
import pandas as pd
import numpy as np
import gzip# Wed, 17 Nov 2021 06:39:07
pd.__version__# Wed, 17 Nov 2021 06:39:07
# load the 2017 data
scripts = pd.read_csv("./dw-data/201701scripts_sample.csv.gz", compression = 'gzip')
scripts.head()# Wed, 17 Nov 2021 06:39:16
# load the 2017 data
scripts = pd.read_csv("./dw-data/201701scripts_sample.csv.gz", compression = 'gzip')
scripts.head()# Wed, 17 Nov 2021 06:39:17
col_names = [ 'code', 'name', 'addr_1', 'addr_2', 'borough', 'village', 'post_code']
practices = pd.read_csv("./dw-data/practices.csv.gz", names = col_names, compression = 'gzip')
practices.head()# Wed, 17 Nov 2021 06:39:20
chem = pd.read_csv("./dw-data/chem.csv.gz", compression = 'gzip')
chem.head()# Wed, 17 Nov 2021 06:39:25
opioids = ['morphine', 'oxycodone', 'methadone', 'fentanyl', 'pethidine', 'buprenorphine', 'propoxyphene', 'codeine']# Wed, 17 Nov 2021 06:39:26
#Detect drug brand names that contain opioids with 'is_opioid'
chem['is_opioid'] = chem['NAME'].str.contains('|'.join(opioids), case=False).astype(int)

#Flag scripts that correspond to an opioid prescription by adding 'is_opioid' column to scripts
scripts = pd.merge(scripts, chem, left_on='bnf_code', right_on='CHEM SUB', how='left')[scripts.columns.tolist()+['is_opioid']]
scripts['is_opioid'] = scripts['is_opioid'].fillna(0).astype(int)# Wed, 17 Nov 2021 06:39:26
scripts.head()# Wed, 17 Nov 2021 06:39:27
opioids_per_practice = scripts.groupby('practice')['is_opioid'].mean()# Wed, 17 Nov 2021 06:39:27
relative_opioids_per_practice = opioids_per_practice - scripts['is_opioid'].mean() # Wed, 17 Nov 2021 06:39:28
standard_error_per_practice = scripts['is_opioid'].std()/np.sqrt(scripts.groupby('practice')['is_opioid'].count())

opioid_scores = (relative_opioids_per_practice/standard_error_per_practice).rename('opioid_score')# Wed, 17 Nov 2021 06:39:29
opioid_scores.head()# Wed, 17 Nov 2021 06:39:29
#We can notice that some codes are associated with multiple names
practices.groupby('code')['name'].nunique().sort_values(ascending=False).head()# Wed, 17 Nov 2021 06:39:30
#Retrieve the first alphabetically name for each practice code
practice_names = practices.groupby('code')['name'].apply(lambda group: sorted([row for row in group])[0])# Wed, 17 Nov 2021 06:39:31
#Compute the number of scripts for each practice
scripts_per_practice = scripts.groupby('practice').size().rename('scripts_number')# Wed, 17 Nov 2021 06:39:32
#Combine each practice name with its opioid score and number of scripts
practice_results = pd.concat([practice_names, opioid_scores, scripts_per_practice], axis=1, join='inner')
practice_results.head()# Wed, 17 Nov 2021 06:39:35
anomalies = sorted([(row[1],row[2],row[3]) for row in practice_results.itertuples()], key=lambda x:x[1], reverse=True)[:100]  
#anomalies = [("NATIONAL ENHANCED SERVICE", 11.6958178629, 7)] * 100# Wed, 17 Nov 2021 06:39:37
anomalies[:5]# Wed, 17 Nov 2021 06:39:38
grader.score.dw__script_anomalies(anomalies)# Wed, 17 Nov 2021 06:39:59
anomalies = sorted([(row[1],row[2],row[3]) for row in practice_results.itertuples()], key=lambda x:x[1], reverse=True)[:100]  
anomalies = [("NATIONAL ENHANCED SERVICE", 11.6958178629, 7)] * 100# Wed, 17 Nov 2021 06:40:00
anomalies[:5]# Wed, 17 Nov 2021 06:40:03
grader.score.dw__script_anomalies(anomalies)# Wed, 17 Nov 2021 06:40:12
anomalies = sorted([(row[1],row[2],row[3]) for row in practice_results.itertuples()], key=lambda x:x[1], reverse=True)[:100]  
# Wed, 17 Nov 2021 06:40:12
anomalies[:5]# Wed, 17 Nov 2021 06:40:17
grader.score.dw__script_anomalies(anomalies)# Wed, 17 Nov 2021 07:00:55
%logstop
%logstart -rtq ~/.logs/dw.py append
%matplotlib inline
import matplotlib
import seaborn as sns
sns.set()
matplotlib.rcParams['figure.dpi'] = 144%logstop
%logstart -rtq ~/.logs/dw.py append
%matplotlib inline
import matplotlib
import seaborn as sns
sns.set()
matplotlib.rcParams['figure.dpi'] = 144
%logstop
%logstart -rtq ~/.logs/dw.py append
%matplotlib inline
import matplotlib
import seaborn as sns
sns.set()
matplotlib.rcParams['figure.dpi'] = 144
from static_grader import grader
!mkdir dw-data
!wget http://dataincubator-wqu.s3.amazonaws.com/dwdata/201701scripts_sample.csv.gz -nc -P ./dw-data/
!wget http://dataincubator-wqu.s3.amazonaws.com/dwdata/201606scripts_sample.csv.gz -nc -P ./dw-data/
!wget http://dataincubator-wqu.s3.amazonaws.com/dwdata/practices.csv.gz -nc -P ./dw-data/
!wget http://dataincubator-wqu.s3.amazonaws.com/dwdata/chem.csv.gz -nc -P ./dw-data/
import pandas as pd
import numpy as np
import gzip
pd.__version__
# load the 2017 data
scripts = pd.read_csv("./dw-data/201701scripts_sample.csv.gz", compression = 'gzip')
scripts.head()
# load the 2017 data
scripts = pd.read_csv("./dw-data/201701scripts_sample.csv.gz", compression = 'gzip')
scripts.head()
col_names = [ 'code', 'name', 'addr_1', 'addr_2', 'borough', 'village', 'post_code']
practices = pd.read_csv("./dw-data/practices.csv.gz", names = col_names, compression = 'gzip')
practices.head()
chem = pd.read_csv("./dw-data/chem.csv.gz", compression = 'gzip')
chem.head()
opioids = ['morphine', 'oxycodone', 'methadone', 'fentanyl', 'pethidine', 'buprenorphine', 'propoxyphene', 'codeine']
#Detect drug brand names that contain opioids with 'is_opioid'
chem['is_opioid'] = chem['NAME'].str.contains('|'.join(opioids), case=False).astype(int)

#Flag scripts that correspond to an opioid prescription by adding 'is_opioid' column to scripts
scripts = pd.merge(scripts, chem, left_on='bnf_code', right_on='CHEM SUB', how='left')[scripts.columns.tolist()+['is_opioid']]
scripts['is_opioid'] = scripts['is_opioid'].fillna(0).astype(int)
scripts.head()
opioids_per_practice = scripts.groupby('practice')['is_opioid'].mean()
relative_opioids_per_practice = opioids_per_practice - scripts['is_opioid'].mean() 
standard_error_per_practice = scripts['is_opioid'].std()/np.sqrt(scripts.groupby('practice')['is_opioid'].count())

opioid_scores = (relative_opioids_per_practice/standard_error_per_practice).rename('opioid_score')
opioid_scores.head()
#We can notice that some codes are associated with multiple names
practices.groupby('code')['name'].nunique().sort_values(ascending=False).head()
#Retrieve the first alphabetically name for each practice code
practice_names = practices.groupby('code')['name'].apply(lambda group: sorted([row for row in group])[0])
#Compute the number of scripts for each practice
scripts_per_practice = scripts.groupby('practice').size().rename('scripts_number')
#Combine each practice name with its opioid score and number of scripts
practice_results = pd.concat([practice_names, opioid_scores, scripts_per_practice], axis=1, join='inner')
practice_results.head()
anomalies = sorted([(row[1],row[2],row[3]) for row in practice_results.itertuples()], key=lambda x:x[1], reverse=True)[:100]  
#anomalies = [("NATIONAL ENHANCED SERVICE", 11.6958178629, 7)] * 100
anomalies[:5]
grader.score.dw__script_anomalies(anomalies)
anomalies = sorted([(row[1],row[2],row[3]) for row in practice_results.itertuples()], key=lambda x:x[1], reverse=True)[:100]  
anomalies = [("NATIONAL ENHANCED SERVICE", 11.6958178629, 7)] * 100
anomalies[:5]
grader.score.dw__script_anomalies(anomalies)
anomalies = sorted([(row[1],row[2],row[3]) for row in practice_results.itertuples()], key=lambda x:x[1], reverse=True)[:100]  
anomalies[:5]
grader.score.dw__script_anomalies(anomalies)
%logstop
%logstart -rtq ~/.logs/dw.py append
%matplotlib inline
import matplotlib
import seaborn as sns
sns.set()
matplotlib.rcParams['figure.dpi'] = 144
# Wed, 17 Nov 2021 07:05:31
%logstop
%logstart -rtq ~/.logs/dw.py append
%matplotlib inline
import matplotlib
import seaborn as sns
sns.set()
matplotlib.rcParams['figure.dpi'] = 144%logstop
%logstart -rtq ~/.logs/dw.py append
%matplotlib inline
import matplotlib
import seaborn as sns
sns.set()
matplotlib.rcParams['figure.dpi'] = 144
%logstop
%logstart -rtq ~/.logs/dw.py append
%matplotlib inline
import matplotlib
import seaborn as sns
sns.set()
matplotlib.rcParams['figure.dpi'] = 144
from static_grader import grader
!mkdir dw-data
!wget http://dataincubator-wqu.s3.amazonaws.com/dwdata/201701scripts_sample.csv.gz -nc -P ./dw-data/
!wget http://dataincubator-wqu.s3.amazonaws.com/dwdata/201606scripts_sample.csv.gz -nc -P ./dw-data/
!wget http://dataincubator-wqu.s3.amazonaws.com/dwdata/practices.csv.gz -nc -P ./dw-data/
!wget http://dataincubator-wqu.s3.amazonaws.com/dwdata/chem.csv.gz -nc -P ./dw-data/
import pandas as pd
import numpy as np
import gzip
pd.__version__
# load the 2017 data
scripts = pd.read_csv("./dw-data/201701scripts_sample.csv.gz", compression = 'gzip')
scripts.head()
# load the 2017 data
scripts = pd.read_csv("./dw-data/201701scripts_sample.csv.gz", compression = 'gzip')
scripts.head()
col_names = [ 'code', 'name', 'addr_1', 'addr_2', 'borough', 'village', 'post_code']
practices = pd.read_csv("./dw-data/practices.csv.gz", names = col_names, compression = 'gzip')
practices.head()
chem = pd.read_csv("./dw-data/chem.csv.gz", compression = 'gzip')
chem.head()
opioids = ['morphine', 'oxycodone', 'methadone', 'fentanyl', 'pethidine', 'buprenorphine', 'propoxyphene', 'codeine']
#Detect drug brand names that contain opioids with 'is_opioid'
chem['is_opioid'] = chem['NAME'].str.contains('|'.join(opioids), case=False).astype(int)

#Flag scripts that correspond to an opioid prescription by adding 'is_opioid' column to scripts
scripts = pd.merge(scripts, chem, left_on='bnf_code', right_on='CHEM SUB', how='left')[scripts.columns.tolist()+['is_opioid']]
scripts['is_opioid'] = scripts['is_opioid'].fillna(0).astype(int)
scripts.head()
opioids_per_practice = scripts.groupby('practice')['is_opioid'].mean()
relative_opioids_per_practice = opioids_per_practice - scripts['is_opioid'].mean() 
standard_error_per_practice = scripts['is_opioid'].std()/np.sqrt(scripts.groupby('practice')['is_opioid'].count())

opioid_scores = (relative_opioids_per_practice/standard_error_per_practice).rename('opioid_score')
opioid_scores.head()
#We can notice that some codes are associated with multiple names
practices.groupby('code')['name'].nunique().sort_values(ascending=False).head()
#Retrieve the first alphabetically name for each practice code
practice_names = practices.groupby('code')['name'].apply(lambda group: sorted([row for row in group])[0])
#Compute the number of scripts for each practice
scripts_per_practice = scripts.groupby('practice').size().rename('scripts_number')
#Combine each practice name with its opioid score and number of scripts
practice_results = pd.concat([practice_names, opioid_scores, scripts_per_practice], axis=1, join='inner')
practice_results.head()
anomalies = sorted([(row[1],row[2],row[3]) for row in practice_results.itertuples()], key=lambda x:x[1], reverse=True)[:100]  
#anomalies = [("NATIONAL ENHANCED SERVICE", 11.6958178629, 7)] * 100
anomalies[:5]
grader.score.dw__script_anomalies(anomalies)
anomalies = sorted([(row[1],row[2],row[3]) for row in practice_results.itertuples()], key=lambda x:x[1], reverse=True)[:100]  
anomalies = [("NATIONAL ENHANCED SERVICE", 11.6958178629, 7)] * 100
anomalies[:5]
grader.score.dw__script_anomalies(anomalies)
anomalies = sorted([(row[1],row[2],row[3]) for row in practice_results.itertuples()], key=lambda x:x[1], reverse=True)[:100]  
anomalies[:5]
grader.score.dw__script_anomalies(anomalies)
%logstop
%logstart -rtq ~/.logs/dw.py append
%matplotlib inline
import matplotlib
import seaborn as sns
sns.set()
matplotlib.rcParams['figure.dpi'] = 144
%logstop
%logstart -rtq ~/.logs/dw.py append
%matplotlib inline
import matplotlib
import seaborn as sns
sns.set()
matplotlib.rcParams['figure.dpi'] = 144
# Wed, 17 Nov 2021 08:20:44
%logstop
%logstart -rtq ~/.logs/dw.py append
%matplotlib inline
import matplotlib
import seaborn as sns
sns.set()
matplotlib.rcParams['figure.dpi'] = 144%logstop
%logstart -rtq ~/.logs/dw.py append
%matplotlib inline
import matplotlib
import seaborn as sns
sns.set()
matplotlib.rcParams['figure.dpi'] = 144
%logstop
%logstart -rtq ~/.logs/dw.py append
%matplotlib inline
import matplotlib
import seaborn as sns
sns.set()
matplotlib.rcParams['figure.dpi'] = 144
from static_grader import grader
!mkdir dw-data
!wget http://dataincubator-wqu.s3.amazonaws.com/dwdata/201701scripts_sample.csv.gz -nc -P ./dw-data/
!wget http://dataincubator-wqu.s3.amazonaws.com/dwdata/201606scripts_sample.csv.gz -nc -P ./dw-data/
!wget http://dataincubator-wqu.s3.amazonaws.com/dwdata/practices.csv.gz -nc -P ./dw-data/
!wget http://dataincubator-wqu.s3.amazonaws.com/dwdata/chem.csv.gz -nc -P ./dw-data/
import pandas as pd
import numpy as np
import gzip
pd.__version__
# load the 2017 data
scripts = pd.read_csv("./dw-data/201701scripts_sample.csv.gz", compression = 'gzip')
scripts.head()
# load the 2017 data
scripts = pd.read_csv("./dw-data/201701scripts_sample.csv.gz", compression = 'gzip')
scripts.head()
col_names = [ 'code', 'name', 'addr_1', 'addr_2', 'borough', 'village', 'post_code']
practices = pd.read_csv("./dw-data/practices.csv.gz", names = col_names, compression = 'gzip')
practices.head()
chem = pd.read_csv("./dw-data/chem.csv.gz", compression = 'gzip')
chem.head()
opioids = ['morphine', 'oxycodone', 'methadone', 'fentanyl', 'pethidine', 'buprenorphine', 'propoxyphene', 'codeine']
#Detect drug brand names that contain opioids with 'is_opioid'
chem['is_opioid'] = chem['NAME'].str.contains('|'.join(opioids), case=False).astype(int)

#Flag scripts that correspond to an opioid prescription by adding 'is_opioid' column to scripts
scripts = pd.merge(scripts, chem, left_on='bnf_code', right_on='CHEM SUB', how='left')[scripts.columns.tolist()+['is_opioid']]
scripts['is_opioid'] = scripts['is_opioid'].fillna(0).astype(int)
scripts.head()
opioids_per_practice = scripts.groupby('practice')['is_opioid'].mean()
relative_opioids_per_practice = opioids_per_practice - scripts['is_opioid'].mean() 
standard_error_per_practice = scripts['is_opioid'].std()/np.sqrt(scripts.groupby('practice')['is_opioid'].count())

opioid_scores = (relative_opioids_per_practice/standard_error_per_practice).rename('opioid_score')
opioid_scores.head()
#We can notice that some codes are associated with multiple names
practices.groupby('code')['name'].nunique().sort_values(ascending=False).head()
#Retrieve the first alphabetically name for each practice code
practice_names = practices.groupby('code')['name'].apply(lambda group: sorted([row for row in group])[0])
#Compute the number of scripts for each practice
scripts_per_practice = scripts.groupby('practice').size().rename('scripts_number')
#Combine each practice name with its opioid score and number of scripts
practice_results = pd.concat([practice_names, opioid_scores, scripts_per_practice], axis=1, join='inner')
practice_results.head()
anomalies = sorted([(row[1],row[2],row[3]) for row in practice_results.itertuples()], key=lambda x:x[1], reverse=True)[:100]  
#anomalies = [("NATIONAL ENHANCED SERVICE", 11.6958178629, 7)] * 100
anomalies[:5]
grader.score.dw__script_anomalies(anomalies)
anomalies = sorted([(row[1],row[2],row[3]) for row in practice_results.itertuples()], key=lambda x:x[1], reverse=True)[:100]  
anomalies = [("NATIONAL ENHANCED SERVICE", 11.6958178629, 7)] * 100
anomalies[:5]
grader.score.dw__script_anomalies(anomalies)
anomalies = sorted([(row[1],row[2],row[3]) for row in practice_results.itertuples()], key=lambda x:x[1], reverse=True)[:100]  
anomalies[:5]
grader.score.dw__script_anomalies(anomalies)
%logstop
%logstart -rtq ~/.logs/dw.py append
%matplotlib inline
import matplotlib
import seaborn as sns
sns.set()
matplotlib.rcParams['figure.dpi'] = 144
%logstop
%logstart -rtq ~/.logs/dw.py append
%matplotlib inline
import matplotlib
import seaborn as sns
sns.set()
matplotlib.rcParams['figure.dpi'] = 144
%logstop
%logstart -rtq ~/.logs/dw.py append
%matplotlib inline
import matplotlib
import seaborn as sns
sns.set()
matplotlib.rcParams['figure.dpi'] = 144
# Wed, 17 Nov 2021 08:27:21
opioids = ['morphine', 'oxycodone', 'methadone', 'fentanyl', 'pethidine', 'buprenorphine', 'propoxyphene', 'codeine']# Wed, 17 Nov 2021 08:27:28
import pandas as pd
import numpy as np
import gzip# Wed, 17 Nov 2021 08:27:28
pd.__version__# Wed, 17 Nov 2021 08:27:29
# load the 2017 data
scripts = pd.read_csv("./dw-data/201701scripts_sample.csv.gz", compression = 'gzip')
scripts.head()# Wed, 17 Nov 2021 08:27:30
col_names = [ 'code', 'name', 'addr_1', 'addr_2', 'borough', 'village', 'post_code']
practices = pd.read_csv("./dw-data/practices.csv.gz", names = col_names, compression = 'gzip')
practices.head()# Wed, 17 Nov 2021 08:27:30
chem = pd.read_csv("./dw-data/chem.csv.gz", compression = 'gzip')
chem.head()# Wed, 17 Nov 2021 08:28:04
'|'.join(opioids)# Wed, 17 Nov 2021 08:28:33
scripts.head()# Wed, 17 Nov 2021 08:28:34
%logstop
%logstart -rtq ~/.logs/dw.py append
%matplotlib inline
import matplotlib
import seaborn as sns
sns.set()
matplotlib.rcParams['figure.dpi'] = 144%logstop
%logstart -rtq ~/.logs/dw.py append
%matplotlib inline
import matplotlib
import seaborn as sns
sns.set()
matplotlib.rcParams['figure.dpi'] = 144
%logstop
%logstart -rtq ~/.logs/dw.py append
%matplotlib inline
import matplotlib
import seaborn as sns
sns.set()
matplotlib.rcParams['figure.dpi'] = 144
from static_grader import grader
!mkdir dw-data
!wget http://dataincubator-wqu.s3.amazonaws.com/dwdata/201701scripts_sample.csv.gz -nc -P ./dw-data/
!wget http://dataincubator-wqu.s3.amazonaws.com/dwdata/201606scripts_sample.csv.gz -nc -P ./dw-data/
!wget http://dataincubator-wqu.s3.amazonaws.com/dwdata/practices.csv.gz -nc -P ./dw-data/
!wget http://dataincubator-wqu.s3.amazonaws.com/dwdata/chem.csv.gz -nc -P ./dw-data/
import pandas as pd
import numpy as np
import gzip
pd.__version__
# load the 2017 data
scripts = pd.read_csv("./dw-data/201701scripts_sample.csv.gz", compression = 'gzip')
scripts.head()
# load the 2017 data
scripts = pd.read_csv("./dw-data/201701scripts_sample.csv.gz", compression = 'gzip')
scripts.head()
col_names = [ 'code', 'name', 'addr_1', 'addr_2', 'borough', 'village', 'post_code']
practices = pd.read_csv("./dw-data/practices.csv.gz", names = col_names, compression = 'gzip')
practices.head()
chem = pd.read_csv("./dw-data/chem.csv.gz", compression = 'gzip')
chem.head()
opioids = ['morphine', 'oxycodone', 'methadone', 'fentanyl', 'pethidine', 'buprenorphine', 'propoxyphene', 'codeine']
#Detect drug brand names that contain opioids with 'is_opioid'
chem['is_opioid'] = chem['NAME'].str.contains('|'.join(opioids), case=False).astype(int)

#Flag scripts that correspond to an opioid prescription by adding 'is_opioid' column to scripts
scripts = pd.merge(scripts, chem, left_on='bnf_code', right_on='CHEM SUB', how='left')[scripts.columns.tolist()+['is_opioid']]
scripts['is_opioid'] = scripts['is_opioid'].fillna(0).astype(int)
scripts.head()
opioids_per_practice = scripts.groupby('practice')['is_opioid'].mean()
relative_opioids_per_practice = opioids_per_practice - scripts['is_opioid'].mean() 
standard_error_per_practice = scripts['is_opioid'].std()/np.sqrt(scripts.groupby('practice')['is_opioid'].count())

opioid_scores = (relative_opioids_per_practice/standard_error_per_practice).rename('opioid_score')
opioid_scores.head()
#We can notice that some codes are associated with multiple names
practices.groupby('code')['name'].nunique().sort_values(ascending=False).head()
#Retrieve the first alphabetically name for each practice code
practice_names = practices.groupby('code')['name'].apply(lambda group: sorted([row for row in group])[0])
#Compute the number of scripts for each practice
scripts_per_practice = scripts.groupby('practice').size().rename('scripts_number')
#Combine each practice name with its opioid score and number of scripts
practice_results = pd.concat([practice_names, opioid_scores, scripts_per_practice], axis=1, join='inner')
practice_results.head()
anomalies = sorted([(row[1],row[2],row[3]) for row in practice_results.itertuples()], key=lambda x:x[1], reverse=True)[:100]  
#anomalies = [("NATIONAL ENHANCED SERVICE", 11.6958178629, 7)] * 100
anomalies[:5]
grader.score.dw__script_anomalies(anomalies)
anomalies = sorted([(row[1],row[2],row[3]) for row in practice_results.itertuples()], key=lambda x:x[1], reverse=True)[:100]  
anomalies = [("NATIONAL ENHANCED SERVICE", 11.6958178629, 7)] * 100
anomalies[:5]
grader.score.dw__script_anomalies(anomalies)
anomalies = sorted([(row[1],row[2],row[3]) for row in practice_results.itertuples()], key=lambda x:x[1], reverse=True)[:100]  
anomalies[:5]
grader.score.dw__script_anomalies(anomalies)
%logstop
%logstart -rtq ~/.logs/dw.py append
%matplotlib inline
import matplotlib
import seaborn as sns
sns.set()
matplotlib.rcParams['figure.dpi'] = 144
%logstop
%logstart -rtq ~/.logs/dw.py append
%matplotlib inline
import matplotlib
import seaborn as sns
sns.set()
matplotlib.rcParams['figure.dpi'] = 144
%logstop
%logstart -rtq ~/.logs/dw.py append
%matplotlib inline
import matplotlib
import seaborn as sns
sns.set()
matplotlib.rcParams['figure.dpi'] = 144
opioids = ['morphine', 'oxycodone', 'methadone', 'fentanyl', 'pethidine', 'buprenorphine', 'propoxyphene', 'codeine']
import pandas as pd
import numpy as np
import gzip
pd.__version__
# load the 2017 data
scripts = pd.read_csv("./dw-data/201701scripts_sample.csv.gz", compression = 'gzip')
scripts.head()
col_names = [ 'code', 'name', 'addr_1', 'addr_2', 'borough', 'village', 'post_code']
practices = pd.read_csv("./dw-data/practices.csv.gz", names = col_names, compression = 'gzip')
practices.head()
chem = pd.read_csv("./dw-data/chem.csv.gz", compression = 'gzip')
chem.head()
'|'.join(opioids)
scripts.head()
%logstop
%logstart -rtq ~/.logs/dw.py append
%matplotlib inline
import matplotlib
import seaborn as sns
sns.set()
matplotlib.rcParams['figure.dpi'] = 144
# Wed, 17 Nov 2021 08:30:53
opioid_codes = chem[chem['NAME'].str.contains('|'.join(opioids), case=False)]['CHEM SUB'].unique()# Wed, 17 Nov 2021 08:31:13
opioid_codes# Wed, 17 Nov 2021 08:32:34
scripts['bnf_code'].isin(opioid_codes)# Wed, 17 Nov 2021 08:33:11
scripts['opioid'] = scripts['bnf_code'].isin(opioid_codes)# Wed, 17 Nov 2021 08:33:20
scripts.head()# Wed, 17 Nov 2021 08:33:48
%logstop
%logstart -rtq ~/.logs/dw.py append
%matplotlib inline
import matplotlib
import seaborn as sns
sns.set()
matplotlib.rcParams['figure.dpi'] = 144%logstop
%logstart -rtq ~/.logs/dw.py append
%matplotlib inline
import matplotlib
import seaborn as sns
sns.set()
matplotlib.rcParams['figure.dpi'] = 144
%logstop
%logstart -rtq ~/.logs/dw.py append
%matplotlib inline
import matplotlib
import seaborn as sns
sns.set()
matplotlib.rcParams['figure.dpi'] = 144
from static_grader import grader
!mkdir dw-data
!wget http://dataincubator-wqu.s3.amazonaws.com/dwdata/201701scripts_sample.csv.gz -nc -P ./dw-data/
!wget http://dataincubator-wqu.s3.amazonaws.com/dwdata/201606scripts_sample.csv.gz -nc -P ./dw-data/
!wget http://dataincubator-wqu.s3.amazonaws.com/dwdata/practices.csv.gz -nc -P ./dw-data/
!wget http://dataincubator-wqu.s3.amazonaws.com/dwdata/chem.csv.gz -nc -P ./dw-data/
import pandas as pd
import numpy as np
import gzip
pd.__version__
# load the 2017 data
scripts = pd.read_csv("./dw-data/201701scripts_sample.csv.gz", compression = 'gzip')
scripts.head()
# load the 2017 data
scripts = pd.read_csv("./dw-data/201701scripts_sample.csv.gz", compression = 'gzip')
scripts.head()
col_names = [ 'code', 'name', 'addr_1', 'addr_2', 'borough', 'village', 'post_code']
practices = pd.read_csv("./dw-data/practices.csv.gz", names = col_names, compression = 'gzip')
practices.head()
chem = pd.read_csv("./dw-data/chem.csv.gz", compression = 'gzip')
chem.head()
opioids = ['morphine', 'oxycodone', 'methadone', 'fentanyl', 'pethidine', 'buprenorphine', 'propoxyphene', 'codeine']
#Detect drug brand names that contain opioids with 'is_opioid'
chem['is_opioid'] = chem['NAME'].str.contains('|'.join(opioids), case=False).astype(int)

#Flag scripts that correspond to an opioid prescription by adding 'is_opioid' column to scripts
scripts = pd.merge(scripts, chem, left_on='bnf_code', right_on='CHEM SUB', how='left')[scripts.columns.tolist()+['is_opioid']]
scripts['is_opioid'] = scripts['is_opioid'].fillna(0).astype(int)
scripts.head()
opioids_per_practice = scripts.groupby('practice')['is_opioid'].mean()
relative_opioids_per_practice = opioids_per_practice - scripts['is_opioid'].mean() 
standard_error_per_practice = scripts['is_opioid'].std()/np.sqrt(scripts.groupby('practice')['is_opioid'].count())

opioid_scores = (relative_opioids_per_practice/standard_error_per_practice).rename('opioid_score')
opioid_scores.head()
#We can notice that some codes are associated with multiple names
practices.groupby('code')['name'].nunique().sort_values(ascending=False).head()
#Retrieve the first alphabetically name for each practice code
practice_names = practices.groupby('code')['name'].apply(lambda group: sorted([row for row in group])[0])
#Compute the number of scripts for each practice
scripts_per_practice = scripts.groupby('practice').size().rename('scripts_number')
#Combine each practice name with its opioid score and number of scripts
practice_results = pd.concat([practice_names, opioid_scores, scripts_per_practice], axis=1, join='inner')
practice_results.head()
anomalies = sorted([(row[1],row[2],row[3]) for row in practice_results.itertuples()], key=lambda x:x[1], reverse=True)[:100]  
#anomalies = [("NATIONAL ENHANCED SERVICE", 11.6958178629, 7)] * 100
anomalies[:5]
grader.score.dw__script_anomalies(anomalies)
anomalies = sorted([(row[1],row[2],row[3]) for row in practice_results.itertuples()], key=lambda x:x[1], reverse=True)[:100]  
anomalies = [("NATIONAL ENHANCED SERVICE", 11.6958178629, 7)] * 100
anomalies[:5]
grader.score.dw__script_anomalies(anomalies)
anomalies = sorted([(row[1],row[2],row[3]) for row in practice_results.itertuples()], key=lambda x:x[1], reverse=True)[:100]  
anomalies[:5]
grader.score.dw__script_anomalies(anomalies)
%logstop
%logstart -rtq ~/.logs/dw.py append
%matplotlib inline
import matplotlib
import seaborn as sns
sns.set()
matplotlib.rcParams['figure.dpi'] = 144
%logstop
%logstart -rtq ~/.logs/dw.py append
%matplotlib inline
import matplotlib
import seaborn as sns
sns.set()
matplotlib.rcParams['figure.dpi'] = 144
%logstop
%logstart -rtq ~/.logs/dw.py append
%matplotlib inline
import matplotlib
import seaborn as sns
sns.set()
matplotlib.rcParams['figure.dpi'] = 144
opioids = ['morphine', 'oxycodone', 'methadone', 'fentanyl', 'pethidine', 'buprenorphine', 'propoxyphene', 'codeine']
import pandas as pd
import numpy as np
import gzip
pd.__version__
# load the 2017 data
scripts = pd.read_csv("./dw-data/201701scripts_sample.csv.gz", compression = 'gzip')
scripts.head()
col_names = [ 'code', 'name', 'addr_1', 'addr_2', 'borough', 'village', 'post_code']
practices = pd.read_csv("./dw-data/practices.csv.gz", names = col_names, compression = 'gzip')
practices.head()
chem = pd.read_csv("./dw-data/chem.csv.gz", compression = 'gzip')
chem.head()
'|'.join(opioids)
scripts.head()
%logstop
%logstart -rtq ~/.logs/dw.py append
%matplotlib inline
import matplotlib
import seaborn as sns
sns.set()
matplotlib.rcParams['figure.dpi'] = 144
opioid_codes = chem[chem['NAME'].str.contains('|'.join(opioids), case=False)]['CHEM SUB'].unique()
opioid_codes
scripts['bnf_code'].isin(opioid_codes)
scripts['opioid'] = scripts['bnf_code'].isin(opioid_codes)
scripts.head()
%logstop
%logstart -rtq ~/.logs/dw.py append
%matplotlib inline
import matplotlib
import seaborn as sns
sns.set()
matplotlib.rcParams['figure.dpi'] = 144
# Wed, 17 Nov 2021 08:33:55
scripts['opioid'].value_counts()# Wed, 17 Nov 2021 08:34:43
scripts.head(15)# Wed, 17 Nov 2021 08:35:58
scripts['opioid'].mean()# Wed, 17 Nov 2021 08:36:16
scripts['opioid'].mean() # False = 0, True = 1# Wed, 17 Nov 2021 08:36:16
%logstop
%logstart -rtq ~/.logs/dw.py append
%matplotlib inline
import matplotlib
import seaborn as sns
sns.set()
matplotlib.rcParams['figure.dpi'] = 144%logstop
%logstart -rtq ~/.logs/dw.py append
%matplotlib inline
import matplotlib
import seaborn as sns
sns.set()
matplotlib.rcParams['figure.dpi'] = 144
%logstop
%logstart -rtq ~/.logs/dw.py append
%matplotlib inline
import matplotlib
import seaborn as sns
sns.set()
matplotlib.rcParams['figure.dpi'] = 144
from static_grader import grader
!mkdir dw-data
!wget http://dataincubator-wqu.s3.amazonaws.com/dwdata/201701scripts_sample.csv.gz -nc -P ./dw-data/
!wget http://dataincubator-wqu.s3.amazonaws.com/dwdata/201606scripts_sample.csv.gz -nc -P ./dw-data/
!wget http://dataincubator-wqu.s3.amazonaws.com/dwdata/practices.csv.gz -nc -P ./dw-data/
!wget http://dataincubator-wqu.s3.amazonaws.com/dwdata/chem.csv.gz -nc -P ./dw-data/
import pandas as pd
import numpy as np
import gzip
pd.__version__
# load the 2017 data
scripts = pd.read_csv("./dw-data/201701scripts_sample.csv.gz", compression = 'gzip')
scripts.head()
# load the 2017 data
scripts = pd.read_csv("./dw-data/201701scripts_sample.csv.gz", compression = 'gzip')
scripts.head()
col_names = [ 'code', 'name', 'addr_1', 'addr_2', 'borough', 'village', 'post_code']
practices = pd.read_csv("./dw-data/practices.csv.gz", names = col_names, compression = 'gzip')
practices.head()
chem = pd.read_csv("./dw-data/chem.csv.gz", compression = 'gzip')
chem.head()
opioids = ['morphine', 'oxycodone', 'methadone', 'fentanyl', 'pethidine', 'buprenorphine', 'propoxyphene', 'codeine']
#Detect drug brand names that contain opioids with 'is_opioid'
chem['is_opioid'] = chem['NAME'].str.contains('|'.join(opioids), case=False).astype(int)

#Flag scripts that correspond to an opioid prescription by adding 'is_opioid' column to scripts
scripts = pd.merge(scripts, chem, left_on='bnf_code', right_on='CHEM SUB', how='left')[scripts.columns.tolist()+['is_opioid']]
scripts['is_opioid'] = scripts['is_opioid'].fillna(0).astype(int)
scripts.head()
opioids_per_practice = scripts.groupby('practice')['is_opioid'].mean()
relative_opioids_per_practice = opioids_per_practice - scripts['is_opioid'].mean() 
standard_error_per_practice = scripts['is_opioid'].std()/np.sqrt(scripts.groupby('practice')['is_opioid'].count())

opioid_scores = (relative_opioids_per_practice/standard_error_per_practice).rename('opioid_score')
opioid_scores.head()
#We can notice that some codes are associated with multiple names
practices.groupby('code')['name'].nunique().sort_values(ascending=False).head()
#Retrieve the first alphabetically name for each practice code
practice_names = practices.groupby('code')['name'].apply(lambda group: sorted([row for row in group])[0])
#Compute the number of scripts for each practice
scripts_per_practice = scripts.groupby('practice').size().rename('scripts_number')
#Combine each practice name with its opioid score and number of scripts
practice_results = pd.concat([practice_names, opioid_scores, scripts_per_practice], axis=1, join='inner')
practice_results.head()
anomalies = sorted([(row[1],row[2],row[3]) for row in practice_results.itertuples()], key=lambda x:x[1], reverse=True)[:100]  
#anomalies = [("NATIONAL ENHANCED SERVICE", 11.6958178629, 7)] * 100
anomalies[:5]
grader.score.dw__script_anomalies(anomalies)
anomalies = sorted([(row[1],row[2],row[3]) for row in practice_results.itertuples()], key=lambda x:x[1], reverse=True)[:100]  
anomalies = [("NATIONAL ENHANCED SERVICE", 11.6958178629, 7)] * 100
anomalies[:5]
grader.score.dw__script_anomalies(anomalies)
anomalies = sorted([(row[1],row[2],row[3]) for row in practice_results.itertuples()], key=lambda x:x[1], reverse=True)[:100]  
anomalies[:5]
grader.score.dw__script_anomalies(anomalies)
%logstop
%logstart -rtq ~/.logs/dw.py append
%matplotlib inline
import matplotlib
import seaborn as sns
sns.set()
matplotlib.rcParams['figure.dpi'] = 144
%logstop
%logstart -rtq ~/.logs/dw.py append
%matplotlib inline
import matplotlib
import seaborn as sns
sns.set()
matplotlib.rcParams['figure.dpi'] = 144
%logstop
%logstart -rtq ~/.logs/dw.py append
%matplotlib inline
import matplotlib
import seaborn as sns
sns.set()
matplotlib.rcParams['figure.dpi'] = 144
opioids = ['morphine', 'oxycodone', 'methadone', 'fentanyl', 'pethidine', 'buprenorphine', 'propoxyphene', 'codeine']
import pandas as pd
import numpy as np
import gzip
pd.__version__
# load the 2017 data
scripts = pd.read_csv("./dw-data/201701scripts_sample.csv.gz", compression = 'gzip')
scripts.head()
col_names = [ 'code', 'name', 'addr_1', 'addr_2', 'borough', 'village', 'post_code']
practices = pd.read_csv("./dw-data/practices.csv.gz", names = col_names, compression = 'gzip')
practices.head()
chem = pd.read_csv("./dw-data/chem.csv.gz", compression = 'gzip')
chem.head()
'|'.join(opioids)
scripts.head()
%logstop
%logstart -rtq ~/.logs/dw.py append
%matplotlib inline
import matplotlib
import seaborn as sns
sns.set()
matplotlib.rcParams['figure.dpi'] = 144
opioid_codes = chem[chem['NAME'].str.contains('|'.join(opioids), case=False)]['CHEM SUB'].unique()
opioid_codes
scripts['bnf_code'].isin(opioid_codes)
scripts['opioid'] = scripts['bnf_code'].isin(opioid_codes)
scripts.head()
%logstop
%logstart -rtq ~/.logs/dw.py append
%matplotlib inline
import matplotlib
import seaborn as sns
sns.set()
matplotlib.rcParams['figure.dpi'] = 144
scripts['opioid'].value_counts()
scripts.head(15)
scripts['opioid'].mean()
scripts['opioid'].mean() # False = 0, True = 1
%logstop
%logstart -rtq ~/.logs/dw.py append
%matplotlib inline
import matplotlib
import seaborn as sns
sns.set()
matplotlib.rcParams['figure.dpi'] = 144
# Wed, 17 Nov 2021 08:37:10
scripts['opioid'].mean()# Wed, 17 Nov 2021 08:37:40
opioids_per_practice = scripts.groupby('practice').mean()# Wed, 17 Nov 2021 08:37:52
opioids_per_practice.head()# Wed, 17 Nov 2021 08:38:08
opioids_per_practice = scripts.groupby('practice')['opioid'].mean()# Wed, 17 Nov 2021 08:38:12
opioids_per_practice.head()# Wed, 17 Nov 2021 08:39:22
relative_opioids_per_practice = opioids_per_practice - scripts['opioids'].mean()# Wed, 17 Nov 2021 08:39:32
relative_opioids_per_practice = opioids_per_practice - scripts['opioid'].mean()# Wed, 17 Nov 2021 08:40:12
scripts['practice'].value_counts()# Wed, 17 Nov 2021 08:41:04
%logstop
%logstart -rtq ~/.logs/dw.py append
%matplotlib inline
import matplotlib
import seaborn as sns
sns.set()
matplotlib.rcParams['figure.dpi'] = 144%logstop
%logstart -rtq ~/.logs/dw.py append
%matplotlib inline
import matplotlib
import seaborn as sns
sns.set()
matplotlib.rcParams['figure.dpi'] = 144
%logstop
%logstart -rtq ~/.logs/dw.py append
%matplotlib inline
import matplotlib
import seaborn as sns
sns.set()
matplotlib.rcParams['figure.dpi'] = 144
from static_grader import grader
!mkdir dw-data
!wget http://dataincubator-wqu.s3.amazonaws.com/dwdata/201701scripts_sample.csv.gz -nc -P ./dw-data/
!wget http://dataincubator-wqu.s3.amazonaws.com/dwdata/201606scripts_sample.csv.gz -nc -P ./dw-data/
!wget http://dataincubator-wqu.s3.amazonaws.com/dwdata/practices.csv.gz -nc -P ./dw-data/
!wget http://dataincubator-wqu.s3.amazonaws.com/dwdata/chem.csv.gz -nc -P ./dw-data/
import pandas as pd
import numpy as np
import gzip
pd.__version__
# load the 2017 data
scripts = pd.read_csv("./dw-data/201701scripts_sample.csv.gz", compression = 'gzip')
scripts.head()
# load the 2017 data
scripts = pd.read_csv("./dw-data/201701scripts_sample.csv.gz", compression = 'gzip')
scripts.head()
col_names = [ 'code', 'name', 'addr_1', 'addr_2', 'borough', 'village', 'post_code']
practices = pd.read_csv("./dw-data/practices.csv.gz", names = col_names, compression = 'gzip')
practices.head()
chem = pd.read_csv("./dw-data/chem.csv.gz", compression = 'gzip')
chem.head()
opioids = ['morphine', 'oxycodone', 'methadone', 'fentanyl', 'pethidine', 'buprenorphine', 'propoxyphene', 'codeine']
#Detect drug brand names that contain opioids with 'is_opioid'
chem['is_opioid'] = chem['NAME'].str.contains('|'.join(opioids), case=False).astype(int)

#Flag scripts that correspond to an opioid prescription by adding 'is_opioid' column to scripts
scripts = pd.merge(scripts, chem, left_on='bnf_code', right_on='CHEM SUB', how='left')[scripts.columns.tolist()+['is_opioid']]
scripts['is_opioid'] = scripts['is_opioid'].fillna(0).astype(int)
scripts.head()
opioids_per_practice = scripts.groupby('practice')['is_opioid'].mean()
relative_opioids_per_practice = opioids_per_practice - scripts['is_opioid'].mean() 
standard_error_per_practice = scripts['is_opioid'].std()/np.sqrt(scripts.groupby('practice')['is_opioid'].count())

opioid_scores = (relative_opioids_per_practice/standard_error_per_practice).rename('opioid_score')
opioid_scores.head()
#We can notice that some codes are associated with multiple names
practices.groupby('code')['name'].nunique().sort_values(ascending=False).head()
#Retrieve the first alphabetically name for each practice code
practice_names = practices.groupby('code')['name'].apply(lambda group: sorted([row for row in group])[0])
#Compute the number of scripts for each practice
scripts_per_practice = scripts.groupby('practice').size().rename('scripts_number')
#Combine each practice name with its opioid score and number of scripts
practice_results = pd.concat([practice_names, opioid_scores, scripts_per_practice], axis=1, join='inner')
practice_results.head()
anomalies = sorted([(row[1],row[2],row[3]) for row in practice_results.itertuples()], key=lambda x:x[1], reverse=True)[:100]  
#anomalies = [("NATIONAL ENHANCED SERVICE", 11.6958178629, 7)] * 100
anomalies[:5]
grader.score.dw__script_anomalies(anomalies)
anomalies = sorted([(row[1],row[2],row[3]) for row in practice_results.itertuples()], key=lambda x:x[1], reverse=True)[:100]  
anomalies = [("NATIONAL ENHANCED SERVICE", 11.6958178629, 7)] * 100
anomalies[:5]
grader.score.dw__script_anomalies(anomalies)
anomalies = sorted([(row[1],row[2],row[3]) for row in practice_results.itertuples()], key=lambda x:x[1], reverse=True)[:100]  
anomalies[:5]
grader.score.dw__script_anomalies(anomalies)
%logstop
%logstart -rtq ~/.logs/dw.py append
%matplotlib inline
import matplotlib
import seaborn as sns
sns.set()
matplotlib.rcParams['figure.dpi'] = 144
%logstop
%logstart -rtq ~/.logs/dw.py append
%matplotlib inline
import matplotlib
import seaborn as sns
sns.set()
matplotlib.rcParams['figure.dpi'] = 144
%logstop
%logstart -rtq ~/.logs/dw.py append
%matplotlib inline
import matplotlib
import seaborn as sns
sns.set()
matplotlib.rcParams['figure.dpi'] = 144
opioids = ['morphine', 'oxycodone', 'methadone', 'fentanyl', 'pethidine', 'buprenorphine', 'propoxyphene', 'codeine']
import pandas as pd
import numpy as np
import gzip
pd.__version__
# load the 2017 data
scripts = pd.read_csv("./dw-data/201701scripts_sample.csv.gz", compression = 'gzip')
scripts.head()
col_names = [ 'code', 'name', 'addr_1', 'addr_2', 'borough', 'village', 'post_code']
practices = pd.read_csv("./dw-data/practices.csv.gz", names = col_names, compression = 'gzip')
practices.head()
chem = pd.read_csv("./dw-data/chem.csv.gz", compression = 'gzip')
chem.head()
'|'.join(opioids)
scripts.head()
%logstop
%logstart -rtq ~/.logs/dw.py append
%matplotlib inline
import matplotlib
import seaborn as sns
sns.set()
matplotlib.rcParams['figure.dpi'] = 144
opioid_codes = chem[chem['NAME'].str.contains('|'.join(opioids), case=False)]['CHEM SUB'].unique()
opioid_codes
scripts['bnf_code'].isin(opioid_codes)
scripts['opioid'] = scripts['bnf_code'].isin(opioid_codes)
scripts.head()
%logstop
%logstart -rtq ~/.logs/dw.py append
%matplotlib inline
import matplotlib
import seaborn as sns
sns.set()
matplotlib.rcParams['figure.dpi'] = 144
scripts['opioid'].value_counts()
scripts.head(15)
scripts['opioid'].mean()
scripts['opioid'].mean() # False = 0, True = 1
%logstop
%logstart -rtq ~/.logs/dw.py append
%matplotlib inline
import matplotlib
import seaborn as sns
sns.set()
matplotlib.rcParams['figure.dpi'] = 144
scripts['opioid'].mean()
opioids_per_practice = scripts.groupby('practice').mean()
opioids_per_practice.head()
opioids_per_practice = scripts.groupby('practice')['opioid'].mean()
opioids_per_practice.head()
relative_opioids_per_practice = opioids_per_practice - scripts['opioids'].mean()
relative_opioids_per_practice = opioids_per_practice - scripts['opioid'].mean()
scripts['practice'].value_counts()
%logstop
%logstart -rtq ~/.logs/dw.py append
%matplotlib inline
import matplotlib
import seaborn as sns
sns.set()
matplotlib.rcParams['figure.dpi'] = 144
# Wed, 17 Nov 2021 08:41:27
standard_error_per_practice = np.sqrt(scripts['opioid'].var() / scripts['practice'].value_counts())# Wed, 17 Nov 2021 08:42:22
scripts['practice'].value_counts()# Wed, 17 Nov 2021 08:43:36
standard_error_per_practice = np.sqrt(scripts['opioid'].var() / scripts['practice'].value_counts())
opioid_scores = relative_opioids_per_practice / standard_error_per_practice# Wed, 17 Nov 2021 08:43:58
standard_error_per_practice = np.sqrt(scripts['opioid'].var() / scripts['practice'].value_counts())
opioid_scores = relative_opioids_per_practice / standard_error_per_practice# Wed, 17 Nov 2021 08:44:09
opioid_scores.head()# Wed, 17 Nov 2021 08:45:14
practices.head()# Wed, 17 Nov 2021 08:45:40
%logstop
%logstart -rtq ~/.logs/dw.py append
%matplotlib inline
import matplotlib
import seaborn as sns
sns.set()
matplotlib.rcParams['figure.dpi'] = 144%logstop
%logstart -rtq ~/.logs/dw.py append
%matplotlib inline
import matplotlib
import seaborn as sns
sns.set()
matplotlib.rcParams['figure.dpi'] = 144
%logstop
%logstart -rtq ~/.logs/dw.py append
%matplotlib inline
import matplotlib
import seaborn as sns
sns.set()
matplotlib.rcParams['figure.dpi'] = 144
from static_grader import grader
!mkdir dw-data
!wget http://dataincubator-wqu.s3.amazonaws.com/dwdata/201701scripts_sample.csv.gz -nc -P ./dw-data/
!wget http://dataincubator-wqu.s3.amazonaws.com/dwdata/201606scripts_sample.csv.gz -nc -P ./dw-data/
!wget http://dataincubator-wqu.s3.amazonaws.com/dwdata/practices.csv.gz -nc -P ./dw-data/
!wget http://dataincubator-wqu.s3.amazonaws.com/dwdata/chem.csv.gz -nc -P ./dw-data/
import pandas as pd
import numpy as np
import gzip
pd.__version__
# load the 2017 data
scripts = pd.read_csv("./dw-data/201701scripts_sample.csv.gz", compression = 'gzip')
scripts.head()
# load the 2017 data
scripts = pd.read_csv("./dw-data/201701scripts_sample.csv.gz", compression = 'gzip')
scripts.head()
col_names = [ 'code', 'name', 'addr_1', 'addr_2', 'borough', 'village', 'post_code']
practices = pd.read_csv("./dw-data/practices.csv.gz", names = col_names, compression = 'gzip')
practices.head()
chem = pd.read_csv("./dw-data/chem.csv.gz", compression = 'gzip')
chem.head()
opioids = ['morphine', 'oxycodone', 'methadone', 'fentanyl', 'pethidine', 'buprenorphine', 'propoxyphene', 'codeine']
#Detect drug brand names that contain opioids with 'is_opioid'
chem['is_opioid'] = chem['NAME'].str.contains('|'.join(opioids), case=False).astype(int)

#Flag scripts that correspond to an opioid prescription by adding 'is_opioid' column to scripts
scripts = pd.merge(scripts, chem, left_on='bnf_code', right_on='CHEM SUB', how='left')[scripts.columns.tolist()+['is_opioid']]
scripts['is_opioid'] = scripts['is_opioid'].fillna(0).astype(int)
scripts.head()
opioids_per_practice = scripts.groupby('practice')['is_opioid'].mean()
relative_opioids_per_practice = opioids_per_practice - scripts['is_opioid'].mean() 
standard_error_per_practice = scripts['is_opioid'].std()/np.sqrt(scripts.groupby('practice')['is_opioid'].count())

opioid_scores = (relative_opioids_per_practice/standard_error_per_practice).rename('opioid_score')
opioid_scores.head()
#We can notice that some codes are associated with multiple names
practices.groupby('code')['name'].nunique().sort_values(ascending=False).head()
#Retrieve the first alphabetically name for each practice code
practice_names = practices.groupby('code')['name'].apply(lambda group: sorted([row for row in group])[0])
#Compute the number of scripts for each practice
scripts_per_practice = scripts.groupby('practice').size().rename('scripts_number')
#Combine each practice name with its opioid score and number of scripts
practice_results = pd.concat([practice_names, opioid_scores, scripts_per_practice], axis=1, join='inner')
practice_results.head()
anomalies = sorted([(row[1],row[2],row[3]) for row in practice_results.itertuples()], key=lambda x:x[1], reverse=True)[:100]  
#anomalies = [("NATIONAL ENHANCED SERVICE", 11.6958178629, 7)] * 100
anomalies[:5]
grader.score.dw__script_anomalies(anomalies)
anomalies = sorted([(row[1],row[2],row[3]) for row in practice_results.itertuples()], key=lambda x:x[1], reverse=True)[:100]  
anomalies = [("NATIONAL ENHANCED SERVICE", 11.6958178629, 7)] * 100
anomalies[:5]
grader.score.dw__script_anomalies(anomalies)
anomalies = sorted([(row[1],row[2],row[3]) for row in practice_results.itertuples()], key=lambda x:x[1], reverse=True)[:100]  
anomalies[:5]
grader.score.dw__script_anomalies(anomalies)
%logstop
%logstart -rtq ~/.logs/dw.py append
%matplotlib inline
import matplotlib
import seaborn as sns
sns.set()
matplotlib.rcParams['figure.dpi'] = 144
%logstop
%logstart -rtq ~/.logs/dw.py append
%matplotlib inline
import matplotlib
import seaborn as sns
sns.set()
matplotlib.rcParams['figure.dpi'] = 144
%logstop
%logstart -rtq ~/.logs/dw.py append
%matplotlib inline
import matplotlib
import seaborn as sns
sns.set()
matplotlib.rcParams['figure.dpi'] = 144
opioids = ['morphine', 'oxycodone', 'methadone', 'fentanyl', 'pethidine', 'buprenorphine', 'propoxyphene', 'codeine']
import pandas as pd
import numpy as np
import gzip
pd.__version__
# load the 2017 data
scripts = pd.read_csv("./dw-data/201701scripts_sample.csv.gz", compression = 'gzip')
scripts.head()
col_names = [ 'code', 'name', 'addr_1', 'addr_2', 'borough', 'village', 'post_code']
practices = pd.read_csv("./dw-data/practices.csv.gz", names = col_names, compression = 'gzip')
practices.head()
chem = pd.read_csv("./dw-data/chem.csv.gz", compression = 'gzip')
chem.head()
'|'.join(opioids)
scripts.head()
%logstop
%logstart -rtq ~/.logs/dw.py append
%matplotlib inline
import matplotlib
import seaborn as sns
sns.set()
matplotlib.rcParams['figure.dpi'] = 144
opioid_codes = chem[chem['NAME'].str.contains('|'.join(opioids), case=False)]['CHEM SUB'].unique()
opioid_codes
scripts['bnf_code'].isin(opioid_codes)
scripts['opioid'] = scripts['bnf_code'].isin(opioid_codes)
scripts.head()
%logstop
%logstart -rtq ~/.logs/dw.py append
%matplotlib inline
import matplotlib
import seaborn as sns
sns.set()
matplotlib.rcParams['figure.dpi'] = 144
scripts['opioid'].value_counts()
scripts.head(15)
scripts['opioid'].mean()
scripts['opioid'].mean() # False = 0, True = 1
%logstop
%logstart -rtq ~/.logs/dw.py append
%matplotlib inline
import matplotlib
import seaborn as sns
sns.set()
matplotlib.rcParams['figure.dpi'] = 144
scripts['opioid'].mean()
opioids_per_practice = scripts.groupby('practice').mean()
opioids_per_practice.head()
opioids_per_practice = scripts.groupby('practice')['opioid'].mean()
opioids_per_practice.head()
relative_opioids_per_practice = opioids_per_practice - scripts['opioids'].mean()
relative_opioids_per_practice = opioids_per_practice - scripts['opioid'].mean()
scripts['practice'].value_counts()
%logstop
%logstart -rtq ~/.logs/dw.py append
%matplotlib inline
import matplotlib
import seaborn as sns
sns.set()
matplotlib.rcParams['figure.dpi'] = 144
standard_error_per_practice = np.sqrt(scripts['opioid'].var() / scripts['practice'].value_counts())
scripts['practice'].value_counts()
standard_error_per_practice = np.sqrt(scripts['opioid'].var() / scripts['practice'].value_counts())
opioid_scores = relative_opioids_per_practice / standard_error_per_practice
standard_error_per_practice = np.sqrt(scripts['opioid'].var() / scripts['practice'].value_counts())
opioid_scores = relative_opioids_per_practice / standard_error_per_practice
opioid_scores.head()
practices.head()
%logstop
%logstart -rtq ~/.logs/dw.py append
%matplotlib inline
import matplotlib
import seaborn as sns
sns.set()
matplotlib.rcParams['figure.dpi'] = 144
# Wed, 17 Nov 2021 08:45:54
unique_practices = practices.groupby('code')['name'].min()# Wed, 17 Nov 2021 08:46:03
unique_practices# Wed, 17 Nov 2021 08:49:11
pd.concat([opioid_scores.rename('score'), scripts['practice'].value_counts()], axis = 1)# Wed, 17 Nov 2021 08:49:33
pd.concat([opioid_scores.rename('score'), scripts['practice'].value_counts().rename('counts')], axis = 1)# Wed, 17 Nov 2021 08:49:40
pd.concat([opioid_scores.rename('score'), scripts['practice'].value_counts().rename('count')], axis = 1)# Wed, 17 Nov 2021 08:50:32
pd.concat([unique_practices.rename('practice_name'), opioid_scores.rename('score'), scripts['practice'].value_counts().rename('count')], axis = 1)# Wed, 17 Nov 2021 08:50:56
pd.concat([unique_practices.rename('practice_name'), opioid_scores.rename('score'), scripts['practice'].value_counts().rename('count')], axis = 1).reset_index()# Wed, 17 Nov 2021 08:51:21
pd.concat([unique_practices.rename('practice_name'), opioid_scores.rename('score'), scripts['practice'].value_counts().rename('count')], axis = 1).reset_index().sort_values('score', ascending = False)# Wed, 17 Nov 2021 08:51:55
pd.concat([unique_practices.rename('practice_name'), opioid_scores.rename('score'), scripts['practice'].value_counts().rename('count')], axis = 1).reset_index().sort_values('score', ascending = False)[:100]# Wed, 17 Nov 2021 08:52:20
top100 = pd.concat([unique_practices.rename('practice_name'), opioid_scores.rename('score'), scripts['practice'].value_counts().rename('count')], axis = 1).reset_index().sort_values('score', ascending = False)[:100]# Wed, 17 Nov 2021 08:52:40
top100# Wed, 17 Nov 2021 08:53:25
top100 = pd.concat([unique_practices.rename('practice_name'), opioid_scores.rename('score'), scripts['practice'].value_counts().rename('count')], axis = 1).reset_index()rename(columns={'index': 'practice_code'}).sort_values('score', ascending = False)[:100]# Wed, 17 Nov 2021 08:53:35
top100 = pd.concat([unique_practices.rename('practice_name'), opioid_scores.rename('score'), scripts['practice'].value_counts().rename('count')], axis = 1).reset_index().rename(columns={'index': 'practice_code'}).sort_values('score', ascending = False)[:100]# Wed, 17 Nov 2021 08:53:38
top100# Wed, 17 Nov 2021 08:54:09
%logstop
%logstart -rtq ~/.logs/dw.py append
%matplotlib inline
import matplotlib
import seaborn as sns
sns.set()
matplotlib.rcParams['figure.dpi'] = 144%logstop
%logstart -rtq ~/.logs/dw.py append
%matplotlib inline
import matplotlib
import seaborn as sns
sns.set()
matplotlib.rcParams['figure.dpi'] = 144
%logstop
%logstart -rtq ~/.logs/dw.py append
%matplotlib inline
import matplotlib
import seaborn as sns
sns.set()
matplotlib.rcParams['figure.dpi'] = 144
from static_grader import grader
!mkdir dw-data
!wget http://dataincubator-wqu.s3.amazonaws.com/dwdata/201701scripts_sample.csv.gz -nc -P ./dw-data/
!wget http://dataincubator-wqu.s3.amazonaws.com/dwdata/201606scripts_sample.csv.gz -nc -P ./dw-data/
!wget http://dataincubator-wqu.s3.amazonaws.com/dwdata/practices.csv.gz -nc -P ./dw-data/
!wget http://dataincubator-wqu.s3.amazonaws.com/dwdata/chem.csv.gz -nc -P ./dw-data/
import pandas as pd
import numpy as np
import gzip
pd.__version__
# load the 2017 data
scripts = pd.read_csv("./dw-data/201701scripts_sample.csv.gz", compression = 'gzip')
scripts.head()
# load the 2017 data
scripts = pd.read_csv("./dw-data/201701scripts_sample.csv.gz", compression = 'gzip')
scripts.head()
col_names = [ 'code', 'name', 'addr_1', 'addr_2', 'borough', 'village', 'post_code']
practices = pd.read_csv("./dw-data/practices.csv.gz", names = col_names, compression = 'gzip')
practices.head()
chem = pd.read_csv("./dw-data/chem.csv.gz", compression = 'gzip')
chem.head()
opioids = ['morphine', 'oxycodone', 'methadone', 'fentanyl', 'pethidine', 'buprenorphine', 'propoxyphene', 'codeine']
#Detect drug brand names that contain opioids with 'is_opioid'
chem['is_opioid'] = chem['NAME'].str.contains('|'.join(opioids), case=False).astype(int)

#Flag scripts that correspond to an opioid prescription by adding 'is_opioid' column to scripts
scripts = pd.merge(scripts, chem, left_on='bnf_code', right_on='CHEM SUB', how='left')[scripts.columns.tolist()+['is_opioid']]
scripts['is_opioid'] = scripts['is_opioid'].fillna(0).astype(int)
scripts.head()
opioids_per_practice = scripts.groupby('practice')['is_opioid'].mean()
relative_opioids_per_practice = opioids_per_practice - scripts['is_opioid'].mean() 
standard_error_per_practice = scripts['is_opioid'].std()/np.sqrt(scripts.groupby('practice')['is_opioid'].count())

opioid_scores = (relative_opioids_per_practice/standard_error_per_practice).rename('opioid_score')
opioid_scores.head()
#We can notice that some codes are associated with multiple names
practices.groupby('code')['name'].nunique().sort_values(ascending=False).head()
#Retrieve the first alphabetically name for each practice code
practice_names = practices.groupby('code')['name'].apply(lambda group: sorted([row for row in group])[0])
#Compute the number of scripts for each practice
scripts_per_practice = scripts.groupby('practice').size().rename('scripts_number')
#Combine each practice name with its opioid score and number of scripts
practice_results = pd.concat([practice_names, opioid_scores, scripts_per_practice], axis=1, join='inner')
practice_results.head()
anomalies = sorted([(row[1],row[2],row[3]) for row in practice_results.itertuples()], key=lambda x:x[1], reverse=True)[:100]  
#anomalies = [("NATIONAL ENHANCED SERVICE", 11.6958178629, 7)] * 100
anomalies[:5]
grader.score.dw__script_anomalies(anomalies)
anomalies = sorted([(row[1],row[2],row[3]) for row in practice_results.itertuples()], key=lambda x:x[1], reverse=True)[:100]  
anomalies = [("NATIONAL ENHANCED SERVICE", 11.6958178629, 7)] * 100
anomalies[:5]
grader.score.dw__script_anomalies(anomalies)
anomalies = sorted([(row[1],row[2],row[3]) for row in practice_results.itertuples()], key=lambda x:x[1], reverse=True)[:100]  
anomalies[:5]
grader.score.dw__script_anomalies(anomalies)
%logstop
%logstart -rtq ~/.logs/dw.py append
%matplotlib inline
import matplotlib
import seaborn as sns
sns.set()
matplotlib.rcParams['figure.dpi'] = 144
%logstop
%logstart -rtq ~/.logs/dw.py append
%matplotlib inline
import matplotlib
import seaborn as sns
sns.set()
matplotlib.rcParams['figure.dpi'] = 144
%logstop
%logstart -rtq ~/.logs/dw.py append
%matplotlib inline
import matplotlib
import seaborn as sns
sns.set()
matplotlib.rcParams['figure.dpi'] = 144
opioids = ['morphine', 'oxycodone', 'methadone', 'fentanyl', 'pethidine', 'buprenorphine', 'propoxyphene', 'codeine']
import pandas as pd
import numpy as np
import gzip
pd.__version__
# load the 2017 data
scripts = pd.read_csv("./dw-data/201701scripts_sample.csv.gz", compression = 'gzip')
scripts.head()
col_names = [ 'code', 'name', 'addr_1', 'addr_2', 'borough', 'village', 'post_code']
practices = pd.read_csv("./dw-data/practices.csv.gz", names = col_names, compression = 'gzip')
practices.head()
chem = pd.read_csv("./dw-data/chem.csv.gz", compression = 'gzip')
chem.head()
'|'.join(opioids)
scripts.head()
%logstop
%logstart -rtq ~/.logs/dw.py append
%matplotlib inline
import matplotlib
import seaborn as sns
sns.set()
matplotlib.rcParams['figure.dpi'] = 144
opioid_codes = chem[chem['NAME'].str.contains('|'.join(opioids), case=False)]['CHEM SUB'].unique()
opioid_codes
scripts['bnf_code'].isin(opioid_codes)
scripts['opioid'] = scripts['bnf_code'].isin(opioid_codes)
scripts.head()
%logstop
%logstart -rtq ~/.logs/dw.py append
%matplotlib inline
import matplotlib
import seaborn as sns
sns.set()
matplotlib.rcParams['figure.dpi'] = 144
scripts['opioid'].value_counts()
scripts.head(15)
scripts['opioid'].mean()
scripts['opioid'].mean() # False = 0, True = 1
%logstop
%logstart -rtq ~/.logs/dw.py append
%matplotlib inline
import matplotlib
import seaborn as sns
sns.set()
matplotlib.rcParams['figure.dpi'] = 144
scripts['opioid'].mean()
opioids_per_practice = scripts.groupby('practice').mean()
opioids_per_practice.head()
opioids_per_practice = scripts.groupby('practice')['opioid'].mean()
opioids_per_practice.head()
relative_opioids_per_practice = opioids_per_practice - scripts['opioids'].mean()
relative_opioids_per_practice = opioids_per_practice - scripts['opioid'].mean()
scripts['practice'].value_counts()
%logstop
%logstart -rtq ~/.logs/dw.py append
%matplotlib inline
import matplotlib
import seaborn as sns
sns.set()
matplotlib.rcParams['figure.dpi'] = 144
standard_error_per_practice = np.sqrt(scripts['opioid'].var() / scripts['practice'].value_counts())
scripts['practice'].value_counts()
standard_error_per_practice = np.sqrt(scripts['opioid'].var() / scripts['practice'].value_counts())
opioid_scores = relative_opioids_per_practice / standard_error_per_practice
standard_error_per_practice = np.sqrt(scripts['opioid'].var() / scripts['practice'].value_counts())
opioid_scores = relative_opioids_per_practice / standard_error_per_practice
opioid_scores.head()
practices.head()
%logstop
%logstart -rtq ~/.logs/dw.py append
%matplotlib inline
import matplotlib
import seaborn as sns
sns.set()
matplotlib.rcParams['figure.dpi'] = 144
unique_practices = practices.groupby('code')['name'].min()
unique_practices
pd.concat([opioid_scores.rename('score'), scripts['practice'].value_counts()], axis = 1)
pd.concat([opioid_scores.rename('score'), scripts['practice'].value_counts().rename('counts')], axis = 1)
pd.concat([opioid_scores.rename('score'), scripts['practice'].value_counts().rename('count')], axis = 1)
pd.concat([unique_practices.rename('practice_name'), opioid_scores.rename('score'), scripts['practice'].value_counts().rename('count')], axis = 1)
pd.concat([unique_practices.rename('practice_name'), opioid_scores.rename('score'), scripts['practice'].value_counts().rename('count')], axis = 1).reset_index()
pd.concat([unique_practices.rename('practice_name'), opioid_scores.rename('score'), scripts['practice'].value_counts().rename('count')], axis = 1).reset_index().sort_values('score', ascending = False)
pd.concat([unique_practices.rename('practice_name'), opioid_scores.rename('score'), scripts['practice'].value_counts().rename('count')], axis = 1).reset_index().sort_values('score', ascending = False)[:100]
top100 = pd.concat([unique_practices.rename('practice_name'), opioid_scores.rename('score'), scripts['practice'].value_counts().rename('count')], axis = 1).reset_index().sort_values('score', ascending = False)[:100]
top100
top100 = pd.concat([unique_practices.rename('practice_name'), opioid_scores.rename('score'), scripts['practice'].value_counts().rename('count')], axis = 1).reset_index()rename(columns={'index': 'practice_code'}).sort_values('score', ascending = False)[:100]
top100 = pd.concat([unique_practices.rename('practice_name'), opioid_scores.rename('score'), scripts['practice'].value_counts().rename('count')], axis = 1).reset_index().rename(columns={'index': 'practice_code'}).sort_values('score', ascending = False)[:100]
top100
%logstop
%logstart -rtq ~/.logs/dw.py append
%matplotlib inline
import matplotlib
import seaborn as sns
sns.set()
matplotlib.rcParams['figure.dpi'] = 144
# Wed, 17 Nov 2021 08:54:22
anomalies = list(top100.itertuples(index=False))# Wed, 17 Nov 2021 08:54:41
grader.score.dw__script_anomalies(anomalies)# Wed, 17 Nov 2021 08:55:28
scripts16 = pd.read_csv('./dw-data/201606scripts_sample.csv.gz', compression='gzip')# Wed, 17 Nov 2021 08:55:29
scripts16.head(3)# Wed, 17 Nov 2021 08:55:30
#Compute both 2016 and 2017 prescription count for each bnf_name
bnf16 = scripts16.groupby('bnf_name').size().rename('bnf16_count')
bnf17 = scripts.groupby('bnf_name').size().rename('bnf17_count')# Wed, 17 Nov 2021 08:55:30
#Merge bnf16 and bnf17 data and eliminate occurences with no prescriptions in 2016 or in 2017
bnf = pd.concat([bnf16, bnf17], axis=1, sort=True).dropna(axis=0, how='any')

#Compute the percent growth in prescription rate from 2016 to 2017
bnf['growth_rate'] = (bnf['bnf17_count']-bnf['bnf16_count'])/bnf['bnf16_count']# Wed, 17 Nov 2021 08:55:30
#Filter out drugs items with less than 50 prescriptions in 2016 and sort items by growth rate
bnf_high_count = bnf[bnf['bnf16_count'] >= 50].sort_values(by='growth_rate', ascending=False)# Wed, 17 Nov 2021 08:55:31
bnf_high_count.head(3)# Wed, 17 Nov 2021 08:55:32
#Retrieve 50 items with largest growth and 50 items with largest shrinkage (high negative growth)
largest_growth = bnf_high_count.head(50)
largest_shrinkage = bnf_high_count.tail(50)

#Combine results into a new DataFrame
growth_anomalies = pd.concat([largest_growth, largest_shrinkage])# Wed, 17 Nov 2021 08:55:33
#Retrieve results as a list of tuples in format ('bnf_name', 'growth_rate', 'bnf16_count')
script_growth = [(row[0], row[3], row[1]) for row in growth_anomalies.itertuples()]# Wed, 17 Nov 2021 08:55:34
grader.score.dw__script_growth(script_growth)# Wed, 17 Nov 2021 08:56:20
%logstop
%logstart -rtq ~/.logs/dw.py append
%matplotlib inline
import matplotlib
import seaborn as sns
sns.set()
matplotlib.rcParams['figure.dpi'] = 144%logstop
%logstart -rtq ~/.logs/dw.py append
%matplotlib inline
import matplotlib
import seaborn as sns
sns.set()
matplotlib.rcParams['figure.dpi'] = 144
%logstop
%logstart -rtq ~/.logs/dw.py append
%matplotlib inline
import matplotlib
import seaborn as sns
sns.set()
matplotlib.rcParams['figure.dpi'] = 144
from static_grader import grader
!mkdir dw-data
!wget http://dataincubator-wqu.s3.amazonaws.com/dwdata/201701scripts_sample.csv.gz -nc -P ./dw-data/
!wget http://dataincubator-wqu.s3.amazonaws.com/dwdata/201606scripts_sample.csv.gz -nc -P ./dw-data/
!wget http://dataincubator-wqu.s3.amazonaws.com/dwdata/practices.csv.gz -nc -P ./dw-data/
!wget http://dataincubator-wqu.s3.amazonaws.com/dwdata/chem.csv.gz -nc -P ./dw-data/
import pandas as pd
import numpy as np
import gzip
pd.__version__
# load the 2017 data
scripts = pd.read_csv("./dw-data/201701scripts_sample.csv.gz", compression = 'gzip')
scripts.head()
# load the 2017 data
scripts = pd.read_csv("./dw-data/201701scripts_sample.csv.gz", compression = 'gzip')
scripts.head()
col_names = [ 'code', 'name', 'addr_1', 'addr_2', 'borough', 'village', 'post_code']
practices = pd.read_csv("./dw-data/practices.csv.gz", names = col_names, compression = 'gzip')
practices.head()
chem = pd.read_csv("./dw-data/chem.csv.gz", compression = 'gzip')
chem.head()
opioids = ['morphine', 'oxycodone', 'methadone', 'fentanyl', 'pethidine', 'buprenorphine', 'propoxyphene', 'codeine']
#Detect drug brand names that contain opioids with 'is_opioid'
chem['is_opioid'] = chem['NAME'].str.contains('|'.join(opioids), case=False).astype(int)

#Flag scripts that correspond to an opioid prescription by adding 'is_opioid' column to scripts
scripts = pd.merge(scripts, chem, left_on='bnf_code', right_on='CHEM SUB', how='left')[scripts.columns.tolist()+['is_opioid']]
scripts['is_opioid'] = scripts['is_opioid'].fillna(0).astype(int)
scripts.head()
opioids_per_practice = scripts.groupby('practice')['is_opioid'].mean()
relative_opioids_per_practice = opioids_per_practice - scripts['is_opioid'].mean() 
standard_error_per_practice = scripts['is_opioid'].std()/np.sqrt(scripts.groupby('practice')['is_opioid'].count())

opioid_scores = (relative_opioids_per_practice/standard_error_per_practice).rename('opioid_score')
opioid_scores.head()
#We can notice that some codes are associated with multiple names
practices.groupby('code')['name'].nunique().sort_values(ascending=False).head()
#Retrieve the first alphabetically name for each practice code
practice_names = practices.groupby('code')['name'].apply(lambda group: sorted([row for row in group])[0])
#Compute the number of scripts for each practice
scripts_per_practice = scripts.groupby('practice').size().rename('scripts_number')
#Combine each practice name with its opioid score and number of scripts
practice_results = pd.concat([practice_names, opioid_scores, scripts_per_practice], axis=1, join='inner')
practice_results.head()
anomalies = sorted([(row[1],row[2],row[3]) for row in practice_results.itertuples()], key=lambda x:x[1], reverse=True)[:100]  
#anomalies = [("NATIONAL ENHANCED SERVICE", 11.6958178629, 7)] * 100
anomalies[:5]
grader.score.dw__script_anomalies(anomalies)
anomalies = sorted([(row[1],row[2],row[3]) for row in practice_results.itertuples()], key=lambda x:x[1], reverse=True)[:100]  
anomalies = [("NATIONAL ENHANCED SERVICE", 11.6958178629, 7)] * 100
anomalies[:5]
grader.score.dw__script_anomalies(anomalies)
anomalies = sorted([(row[1],row[2],row[3]) for row in practice_results.itertuples()], key=lambda x:x[1], reverse=True)[:100]  
anomalies[:5]
grader.score.dw__script_anomalies(anomalies)
%logstop
%logstart -rtq ~/.logs/dw.py append
%matplotlib inline
import matplotlib
import seaborn as sns
sns.set()
matplotlib.rcParams['figure.dpi'] = 144
%logstop
%logstart -rtq ~/.logs/dw.py append
%matplotlib inline
import matplotlib
import seaborn as sns
sns.set()
matplotlib.rcParams['figure.dpi'] = 144
%logstop
%logstart -rtq ~/.logs/dw.py append
%matplotlib inline
import matplotlib
import seaborn as sns
sns.set()
matplotlib.rcParams['figure.dpi'] = 144
opioids = ['morphine', 'oxycodone', 'methadone', 'fentanyl', 'pethidine', 'buprenorphine', 'propoxyphene', 'codeine']
import pandas as pd
import numpy as np
import gzip
pd.__version__
# load the 2017 data
scripts = pd.read_csv("./dw-data/201701scripts_sample.csv.gz", compression = 'gzip')
scripts.head()
col_names = [ 'code', 'name', 'addr_1', 'addr_2', 'borough', 'village', 'post_code']
practices = pd.read_csv("./dw-data/practices.csv.gz", names = col_names, compression = 'gzip')
practices.head()
chem = pd.read_csv("./dw-data/chem.csv.gz", compression = 'gzip')
chem.head()
'|'.join(opioids)
scripts.head()
%logstop
%logstart -rtq ~/.logs/dw.py append
%matplotlib inline
import matplotlib
import seaborn as sns
sns.set()
matplotlib.rcParams['figure.dpi'] = 144
opioid_codes = chem[chem['NAME'].str.contains('|'.join(opioids), case=False)]['CHEM SUB'].unique()
opioid_codes
scripts['bnf_code'].isin(opioid_codes)
scripts['opioid'] = scripts['bnf_code'].isin(opioid_codes)
scripts.head()
%logstop
%logstart -rtq ~/.logs/dw.py append
%matplotlib inline
import matplotlib
import seaborn as sns
sns.set()
matplotlib.rcParams['figure.dpi'] = 144
scripts['opioid'].value_counts()
scripts.head(15)
scripts['opioid'].mean()
scripts['opioid'].mean() # False = 0, True = 1
%logstop
%logstart -rtq ~/.logs/dw.py append
%matplotlib inline
import matplotlib
import seaborn as sns
sns.set()
matplotlib.rcParams['figure.dpi'] = 144
scripts['opioid'].mean()
opioids_per_practice = scripts.groupby('practice').mean()
opioids_per_practice.head()
opioids_per_practice = scripts.groupby('practice')['opioid'].mean()
opioids_per_practice.head()
relative_opioids_per_practice = opioids_per_practice - scripts['opioids'].mean()
relative_opioids_per_practice = opioids_per_practice - scripts['opioid'].mean()
scripts['practice'].value_counts()
%logstop
%logstart -rtq ~/.logs/dw.py append
%matplotlib inline
import matplotlib
import seaborn as sns
sns.set()
matplotlib.rcParams['figure.dpi'] = 144
standard_error_per_practice = np.sqrt(scripts['opioid'].var() / scripts['practice'].value_counts())
scripts['practice'].value_counts()
standard_error_per_practice = np.sqrt(scripts['opioid'].var() / scripts['practice'].value_counts())
opioid_scores = relative_opioids_per_practice / standard_error_per_practice
standard_error_per_practice = np.sqrt(scripts['opioid'].var() / scripts['practice'].value_counts())
opioid_scores = relative_opioids_per_practice / standard_error_per_practice
opioid_scores.head()
practices.head()
%logstop
%logstart -rtq ~/.logs/dw.py append
%matplotlib inline
import matplotlib
import seaborn as sns
sns.set()
matplotlib.rcParams['figure.dpi'] = 144
unique_practices = practices.groupby('code')['name'].min()
unique_practices
pd.concat([opioid_scores.rename('score'), scripts['practice'].value_counts()], axis = 1)
pd.concat([opioid_scores.rename('score'), scripts['practice'].value_counts().rename('counts')], axis = 1)
pd.concat([opioid_scores.rename('score'), scripts['practice'].value_counts().rename('count')], axis = 1)
pd.concat([unique_practices.rename('practice_name'), opioid_scores.rename('score'), scripts['practice'].value_counts().rename('count')], axis = 1)
pd.concat([unique_practices.rename('practice_name'), opioid_scores.rename('score'), scripts['practice'].value_counts().rename('count')], axis = 1).reset_index()
pd.concat([unique_practices.rename('practice_name'), opioid_scores.rename('score'), scripts['practice'].value_counts().rename('count')], axis = 1).reset_index().sort_values('score', ascending = False)
pd.concat([unique_practices.rename('practice_name'), opioid_scores.rename('score'), scripts['practice'].value_counts().rename('count')], axis = 1).reset_index().sort_values('score', ascending = False)[:100]
top100 = pd.concat([unique_practices.rename('practice_name'), opioid_scores.rename('score'), scripts['practice'].value_counts().rename('count')], axis = 1).reset_index().sort_values('score', ascending = False)[:100]
top100
top100 = pd.concat([unique_practices.rename('practice_name'), opioid_scores.rename('score'), scripts['practice'].value_counts().rename('count')], axis = 1).reset_index()rename(columns={'index': 'practice_code'}).sort_values('score', ascending = False)[:100]
top100 = pd.concat([unique_practices.rename('practice_name'), opioid_scores.rename('score'), scripts['practice'].value_counts().rename('count')], axis = 1).reset_index().rename(columns={'index': 'practice_code'}).sort_values('score', ascending = False)[:100]
top100
%logstop
%logstart -rtq ~/.logs/dw.py append
%matplotlib inline
import matplotlib
import seaborn as sns
sns.set()
matplotlib.rcParams['figure.dpi'] = 144
anomalies = list(top100.itertuples(index=False))
grader.score.dw__script_anomalies(anomalies)
scripts16 = pd.read_csv('./dw-data/201606scripts_sample.csv.gz', compression='gzip')
scripts16.head(3)
#Compute both 2016 and 2017 prescription count for each bnf_name
bnf16 = scripts16.groupby('bnf_name').size().rename('bnf16_count')
bnf17 = scripts.groupby('bnf_name').size().rename('bnf17_count')
#Merge bnf16 and bnf17 data and eliminate occurences with no prescriptions in 2016 or in 2017
bnf = pd.concat([bnf16, bnf17], axis=1, sort=True).dropna(axis=0, how='any')

#Compute the percent growth in prescription rate from 2016 to 2017
bnf['growth_rate'] = (bnf['bnf17_count']-bnf['bnf16_count'])/bnf['bnf16_count']
#Filter out drugs items with less than 50 prescriptions in 2016 and sort items by growth rate
bnf_high_count = bnf[bnf['bnf16_count'] >= 50].sort_values(by='growth_rate', ascending=False)
bnf_high_count.head(3)
#Retrieve 50 items with largest growth and 50 items with largest shrinkage (high negative growth)
largest_growth = bnf_high_count.head(50)
largest_shrinkage = bnf_high_count.tail(50)

#Combine results into a new DataFrame
growth_anomalies = pd.concat([largest_growth, largest_shrinkage])
#Retrieve results as a list of tuples in format ('bnf_name', 'growth_rate', 'bnf16_count')
script_growth = [(row[0], row[3], row[1]) for row in growth_anomalies.itertuples()]
grader.score.dw__script_growth(script_growth)
%logstop
%logstart -rtq ~/.logs/dw.py append
%matplotlib inline
import matplotlib
import seaborn as sns
sns.set()
matplotlib.rcParams['figure.dpi'] = 144
