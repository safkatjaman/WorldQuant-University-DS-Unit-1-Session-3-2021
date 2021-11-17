# Wed, 17 Nov 2021 05:05:11
%logstop
%logstart -rtq ~/.logs/PY_Intro.py append
import seaborn as sns
sns.set()# Wed, 17 Nov 2021 05:06:43
%logstop
%logstart -rtq ~/.logs/in.py append
import seaborn as sns
sns.set()# Wed, 17 Nov 2021 05:09:46
%logstop
%logstart -rtq ~/.logs/ip.py append
import seaborn as sns
sns.set()# Wed, 17 Nov 2021 05:18:01
%logstop
%logstart -rtq ~/.logs/vc.py append
import seaborn as sns
sns.set()# Wed, 17 Nov 2021 05:21:14
%logstop
%logstart -rtq ~/.logs/dw.py append
import seaborn as sns
sns.set()# Wed, 17 Nov 2021 05:31:31
%logstop
%logstart -ortq ~/.logs/in.py append
%matplotlib inline
import matplotlib
import seaborn as sns
sns.set()
matplotlib.rcParams['figure.dpi'] = 144# Wed, 17 Nov 2021 05:31:35
%logstop
%logstart -rtq ~/.logs/pw.py append
import seaborn as sns
sns.set()# Wed, 17 Nov 2021 05:32:52
%logstop
%logstart -ortq ~/.logs/pw.py append
%matplotlib inline
import matplotlib
import seaborn as sns
sns.set()
matplotlib.rcParams['figure.dpi'] = 144# Wed, 17 Nov 2021 05:40:43
%logstop
%logstart -rtq ~/.logs/vc.py append
import seaborn as sns
sns.set()# Wed, 17 Nov 2021 05:40:58
%logstop
%logstart -rtq ~/.logs/ip.py append
import seaborn as sns
sns.set()# Wed, 17 Nov 2021 05:42:11
%logstop
%logstart -rtq ~/.logs/vc.py append
import seaborn as sns
sns.set()# Wed, 17 Nov 2021 05:42:29
%logstop
%logstart -rtq ~/.logs/in.py append
import seaborn as sns
sns.set()# Wed, 17 Nov 2021 05:42:44
%logstop
%logstart -rtq ~/.logs/ip.py append
import seaborn as sns
sns.set()# Wed, 17 Nov 2021 05:43:15
%logstop
%logstart -rtq ~/.logs/dw.py append
import seaborn as sns
sns.set()# Wed, 17 Nov 2021 06:02:22
%matplotlib inline
import matplotlib
import seaborn as sns
matplotlib.rcParams['savefig.dpi'] = 144# Wed, 17 Nov 2021 06:02:23
from static_grader import grader# Wed, 17 Nov 2021 06:02:25
!mkdir dw-data
!wget http://dataincubator-wqu.s3.amazonaws.com/dwdata/201701scripts_sample.csv.gz -nc -P ./dw-data/
!wget http://dataincubator-wqu.s3.amazonaws.com/dwdata/201606scripts_sample.csv.gz -nc -P ./dw-data/
!wget http://dataincubator-wqu.s3.amazonaws.com/dwdata/practices.csv.gz -nc -P ./dw-data/
!wget http://dataincubator-wqu.s3.amazonaws.com/dwdata/chem.csv.gz -nc -P ./dw-data/# Wed, 17 Nov 2021 06:02:31
import pandas as pd
import numpy as np
import gzip# Wed, 17 Nov 2021 06:02:32
# load the 2017 data
with gzip.open('./dw-data/201701scripts_sample.csv.gz', 'rb') as f:
    scripts = pd.read_csv(f)
col_names=[ 'code', 'name', 'addr_1', 'addr_2', 'borough', 'village', 'post_code']
with gzip.open('./dw-data/practices.csv.gz', 'rb') as f:
    practices = pd.read_csv(f, names=col_names)
with gzip.open('./dw-data/chem.csv.gz', 'rb') as f:
    chem = pd.read_csv(f)# Wed, 17 Nov 2021 06:02:34
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
# Wed, 17 Nov 2021 06:02:35
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
# Wed, 17 Nov 2021 06:02:37
chem.head()#[Out]#     CHEM SUB                                NAME
#[Out]# 0  0101010A0                     Alexitol Sodium
#[Out]# 1  0101010B0                          Almasilate
#[Out]# 2  0101010C0                 Aluminium Hydroxide
#[Out]# 3  0101010D0  Aluminium Hydroxide With Magnesium
#[Out]# 4  0101010E0                        Hydrotalcite
# Wed, 17 Nov 2021 06:02:41
summary = pd.DataFrame(scripts.describe())
summary#[Out]#                items            nic       act_cost       quantity
#[Out]# count  973193.000000  973193.000000  973193.000000  973193.000000
#[Out]# mean        9.133136      73.058915      67.986613     741.329835
#[Out]# std        29.204198     188.070257     174.401703    3665.426958
#[Out]# min         1.000000       0.000000       0.040000       0.000000
#[Out]# 25%         1.000000       7.800000       7.330000      28.000000
#[Out]# 50%         2.000000      22.640000      21.220000     100.000000
#[Out]# 75%         6.000000      65.000000      60.670000     350.000000
#[Out]# max      2384.000000   16320.000000   15108.320000  577720.000000
# Wed, 17 Nov 2021 06:02:42
stats = list(summary.index)[0:3]
stats.extend(list(summary.index)[4:7])
stats#[Out]# ['count', 'mean', 'std', '25%', '50%', '75%']
# Wed, 17 Nov 2021 06:02:44
summary_stats = [(col, (summary[col][stats[0]] * summary[col][stats[1]],summary[col][stats[1]],summary[col][stats[2]],
        summary[col][stats[3]],summary[col][stats[4]],summary[col][stats[5]])) 
 for col in [list(summary.columns)[0],list(summary.columns)[3],list(summary.columns)[1],list(summary.columns)[2]]]# Wed, 17 Nov 2021 06:02:46
summary_stats = [('items', (0,) * 6), ('quantity', (0,) * 6), ('nic', (0,) * 6), ('act_cost', (0,) * 6)]# Wed, 17 Nov 2021 06:02:47
grader.score.dw__summary_statistics(summary_stats)# Wed, 17 Nov 2021 06:02:58
grader.score.dw__summary_statistics(summary_stats)# Wed, 17 Nov 2021 06:03:16
opioids = ['morphine', 'oxycodone', 'methadone', 'fentanyl', 'pethidine', 'buprenorphine', 'propoxyphene', 'codeine']# Wed, 17 Nov 2021 06:03:18
bychemsub = chem.groupby('CHEM SUB')['NAME'].unique() #take all the unique chem subs into a pd series# Wed, 17 Nov 2021 06:03:19
bychemsub.head()#[Out]# CHEM SUB
#[Out]# 010101000      [Other Antacid & Simeticone Preps]
#[Out]# 0101010A0                       [Alexitol Sodium]
#[Out]# 0101010B0                            [Almasilate]
#[Out]# 0101010C0                   [Aluminium Hydroxide]
#[Out]# 0101010D0    [Aluminium Hydroxide With Magnesium]
#[Out]# Name: NAME, dtype: object
# Wed, 17 Nov 2021 06:03:20
# for those subs that have different names join the names to single str
chemsub = bychemsub.to_frame()['NAME'].apply(lambda x: ' '.join(x)).to_frame()# Wed, 17 Nov 2021 06:03:21
chemsub.head()#[Out]#                                          NAME
#[Out]# CHEM SUB                                     
#[Out]# 010101000    Other Antacid & Simeticone Preps
#[Out]# 0101010A0                     Alexitol Sodium
#[Out]# 0101010B0                          Almasilate
#[Out]# 0101010C0                 Aluminium Hydroxide
#[Out]# 0101010D0  Aluminium Hydroxide With Magnesium
# Wed, 17 Nov 2021 06:03:24
s = pd.Series(opioids)
s.str.lower()#[Out]# 0         morphine
#[Out]# 1        oxycodone
#[Out]# 2        methadone
#[Out]# 3         fentanyl
#[Out]# 4        pethidine
#[Out]# 5    buprenorphine
#[Out]# 6     propoxyphene
#[Out]# 7          codeine
#[Out]# dtype: object
# Wed, 17 Nov 2021 06:03:25
check = '|'.join(s.str.lower())
chemsub['isOpioids'] = chemsub['NAME'].str.lower().str.contains(check)# Wed, 17 Nov 2021 06:03:26
chemsub[chemsub['isOpioids']==True].head()#[Out]#                                           NAME  isOpioids
#[Out]# CHEM SUB                                                 
#[Out]# 0104020D0  Codeine Phosphate Compound Mixtures       True
#[Out]# 0104020N0                     Opium & Morphine       True
#[Out]# 0309010C0                    Codeine Phosphate       True
#[Out]# 0309010N0            Diamorphine Hydrochloride       True
#[Out]# 0309010S0              Methadone Hydrochloride       True
# Wed, 17 Nov 2021 06:03:27
# need a dict of the subs and flags for later
dct = dict(chemsub['isOpioids'])# Wed, 17 Nov 2021 06:03:29
scripts['clsfd'] = scripts['bnf_code'].apply(lambda x: x in dct.keys())# Wed, 17 Nov 2021 06:03:30
scripts[scripts['clsfd']==True].head()#[Out]#   practice   bnf_code                              bnf_name  items   nic  \
#[Out]# 0   N85639  0106020C0                 Bisacodyl_Tab E/C 5mg      1  0.39   
#[Out]# 1   N85639  0106040M0      Movicol Plain_Paed Pdr Sach 6.9g      1  4.38   
#[Out]# 2   N85639  0301011R0    Salbutamol_Inha 100mcg (200 D) CFF      1  1.50   
#[Out]# 3   N85639  0304010G0  Chlorphenamine Mal_Oral Soln 2mg/5ml      1  2.62   
#[Out]# 4   N85639  0401020K0                      Diazepam_Tab 2mg      1  0.16   
#[Out]# 
#[Out]#    act_cost  quantity  clsfd  
#[Out]# 0      0.47        12   True  
#[Out]# 1      4.07        30   True  
#[Out]# 2      1.40         1   True  
#[Out]# 3      2.44       150   True  
#[Out]# 4      0.26         6   True  
# Wed, 17 Nov 2021 06:03:31
def flag(cols):
    code = cols[0]
    clsfd = cols[1]
    if clsfd:
        return dct[code]
    else:
        return clsfd# Wed, 17 Nov 2021 06:03:32
scripts['isOpioids'] = scripts[['bnf_code','clsfd']].apply(flag, axis=1)   # Wed, 17 Nov 2021 06:03:40
bypractice = scripts.groupby('practice')['isOpioids']# Wed, 17 Nov 2021 06:03:41
# propos: only add the practices that have opioids
opioids_per_practice = [(prac, bypractice.get_group(prac).mean()) for prac in bypractice.groups.keys() 
                        if (len(bypractice.get_group(prac).value_counts())>1)]# Wed, 17 Nov 2021 06:03:43
ops = pd.DataFrame(opioids_per_practice, columns=['code','propos'])
ops.sort_values(by=['propos'], ascending=False).head()#[Out]#        code    propos
#[Out]# 697  Y01852  0.857143
#[Out]# 676  Y00581  0.500000
#[Out]# 699  Y01943  0.333333
#[Out]# 730  Y02947  0.285714
#[Out]# 758  Y04657  0.222222
# Wed, 17 Nov 2021 06:03:44
len(ops)#[Out]# 790
# Wed, 17 Nov 2021 06:03:45
scripts['isOpioids'].mean()#[Out]# 0.03580276471367961
# Wed, 17 Nov 2021 06:03:47
# relative propos: only add the practices that have opioids
relative_opioids_per_practice = [(prac, bypractice.get_group(prac).mean() - scripts['isOpioids'].mean()) 
                       for prac in bypractice.groups.keys() 
                                 if (len(bypractice.get_group(prac).value_counts())>1)]# Wed, 17 Nov 2021 06:03:49
relops = pd.DataFrame(relative_opioids_per_practice, columns=['code','propos'])
relops.sort_values(by=['propos'], ascending=False).head()#[Out]#        code    propos
#[Out]# 697  Y01852  0.821340
#[Out]# 676  Y00581  0.464197
#[Out]# 699  Y01943  0.297531
#[Out]# 730  Y02947  0.249912
#[Out]# 758  Y04657  0.186419
# Wed, 17 Nov 2021 06:03:52
stdev = scripts['isOpioids'].std()
stdev#[Out]# 0.18579817605238425
# Wed, 17 Nov 2021 06:03:53
standard_error_per_practice = [(prac, stdev/np.sqrt(bypractice.get_group(prac).count())) 
                               for prac in bypractice.groups.keys()
                              if (len(bypractice.get_group(prac).value_counts())>1)]# Wed, 17 Nov 2021 06:03:54
stderr = pd.DataFrame(standard_error_per_practice, columns=['code','stderr'])
stderr.sort_values(by=['stderr'], ascending=False).head()#[Out]#        code    stderr
#[Out]# 676  Y00581  0.131379
#[Out]# 699  Y01943  0.107271
#[Out]# 730  Y02947  0.070225
#[Out]# 697  Y01852  0.070225
#[Out]# 776  Y05269  0.065690
# Wed, 17 Nov 2021 06:03:56
opioid_scores = [(relative_opioids_per_practice[x][0], relative_opioids_per_practice[x][1]/standard_error_per_practice[x][1]) 
                       for x in range(len(relative_opioids_per_practice))]# Wed, 17 Nov 2021 06:03:58
opscores = pd.DataFrame(opioid_scores,columns=['code','z_score'])
opscores.sort_values(by=['z_score'], ascending=False).head()#[Out]#        code    z_score
#[Out]# 697  Y01852  11.695818
#[Out]# 742  Y03668   6.150582
#[Out]# 260  G81703   5.123032
#[Out]# 769  Y04997   4.958866
#[Out]# 754  Y04585   4.888878
# Wed, 17 Nov 2021 06:04:00
bycode = practices.groupby('code')['name'].unique() #10843 unique codes in practices compared to 790 in opioid_scores# Wed, 17 Nov 2021 06:04:00
# for those codes that have different names, take alphabetically 1st one
codes = bycode.to_frame()['name'].apply(lambda x: sorted(x)[0]) #take alphabetically 1st name# Wed, 17 Nov 2021 06:04:01
codes.head()#[Out]# code
#[Out]# A81001           THE DENSHAM SURGERY
#[Out]# A81002    QUEENS PARK MEDICAL CENTRE
#[Out]# A81003     VICTORIA MEDICAL PRACTICE
#[Out]# A81004       BLUEBELL MEDICAL CENTRE
#[Out]# A81005            SPRINGWOOD SURGERY
#[Out]# Name: name, dtype: object
# Wed, 17 Nov 2021 06:04:04
# only the top 100!
topscores = list(opscores.sort_values(by=['z_score'], ascending=False)[['code','z_score']].apply(
    lambda x: (str(x[0]),x[1]), axis=1))[:100]
topscores[:5]#[Out]# [('Y01852', 11.695817862936027),
#[Out]#  ('Y03668', 6.1505817490838295),
#[Out]#  ('G81703', 5.123032414033079),
#[Out]#  ('Y04997', 4.958866438487605),
#[Out]#  ('Y04585', 4.8888781604828235)]
# Wed, 17 Nov 2021 06:04:06
anomalies = [(
    codes[topscores[x][0]], topscores[x][1], len(scripts[scripts['practice']==topscores[x][0]])) 
                       for x in range(len(topscores))]# Wed, 17 Nov 2021 06:04:13
anomalies = [("NATIONAL ENHANCED SERVICE", 11.6958178629, 7)] * 100# Wed, 17 Nov 2021 06:04:13
grader.score.dw__script_anomalies(anomalies)# Wed, 17 Nov 2021 06:05:56
%logstop
%logstart -ortq ~/.logs/dw.py append
%matplotlib inline
import matplotlib
import seaborn as sns
sns.set()
matplotlib.rcParams['figure.dpi'] = 144# Wed, 17 Nov 2021 06:12:48
%matplotlib inline
import matplotlib
import seaborn as sns
sns.set()
matplotlib.rcParams['figure.dpi'] = 144# Wed, 17 Nov 2021 06:13:05
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
anomalies = [(k[1], k[2], k[3]) for k in result.itertuples()][:100]# Wed, 17 Nov 2021 06:13:24
opioids = ['morphine', 'oxycodone', 'methadone', 'fentanyl', 'pethidine', 'buprenorphine', 'propoxyphene', 'codeine']# Wed, 17 Nov 2021 06:13:43
anomalies = [("NATIONAL ENHANCED SERVICE", 11.6958178629, 7)] * 100

grader.score.dw__script_anomalies(anomalies)# Wed, 17 Nov 2021 06:16:33
%matplotlib inline
import matplotlib
import seaborn as sns
sns.set()
matplotlib.rcParams['figure.dpi'] = 144# Wed, 17 Nov 2021 06:16:33
from static_grader import grader# Wed, 17 Nov 2021 06:16:34
!mkdir dw-data
!wget http://dataincubator-wqu.s3.amazonaws.com/dwdata/201701scripts_sample.csv.gz -nc -P ./dw-data/
!wget http://dataincubator-wqu.s3.amazonaws.com/dwdata/201606scripts_sample.csv.gz -nc -P ./dw-data/
!wget http://dataincubator-wqu.s3.amazonaws.com/dwdata/practices.csv.gz -nc -P ./dw-data/
!wget http://dataincubator-wqu.s3.amazonaws.com/dwdata/chem.csv.gz -nc -P ./dw-data/# Wed, 17 Nov 2021 06:16:38
import pandas as pd
import numpy as np
import gzip# Wed, 17 Nov 2021 06:16:38
# load the 2017 data
scripts_file = gzip.open('./dw-data/201701scripts_sample.csv.gz', 'r')
    
scripts = pd.read_csv(scripts_file)
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
# Wed, 17 Nov 2021 06:16:40
scripts_file_16 = gzip.open('./dw-data/201606scripts_sample.csv.gz', 'r')
    
scripts_16 = pd.read_csv(scripts_file_16)
scripts_16.head()#[Out]#   practice   bnf_code                                 bnf_name  items   nic  \
#[Out]# 0   N85638  0301011R0   Salamol_Inha 100mcg (200 D) CFF (Teva)      2  2.92   
#[Out]# 1   N85638  0301011R0  Easyhaler_Salbutamol Sulf 200mcg (200D)      1  6.63   
#[Out]# 2   N85638  0301020I0     Ipratrop Brom_Inh Soln 500mcg/2ml Ud      1  1.77   
#[Out]# 3   N85638  0301020I0     Ipratrop Brom_Inh Soln 250mcg/1ml Ud      1  4.47   
#[Out]# 4   N85638  0302000C0        Clenil Modulite_Inha 50mcg (200D)      1  3.70   
#[Out]# 
#[Out]#    act_cost  quantity  
#[Out]# 0      2.73         2  
#[Out]# 1      6.15         1  
#[Out]# 2      1.75        12  
#[Out]# 3      4.15        20  
#[Out]# 4      3.44         1  
# Wed, 17 Nov 2021 06:16:41
practices_file = gzip.open('./dw-data/practices.csv.gz', 'r')

col_names=[ 'code', 'name', 'addr_1', 'addr_2', 'borough', 'village', 'post_code']
practices = pd.read_csv(practices_file, names = col_names)
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
# Wed, 17 Nov 2021 06:16:42
chem = pd.read_csv(gzip.open('./dw-data/chem.csv.gz', 'r'))
chem.head()#[Out]#     CHEM SUB                                NAME
#[Out]# 0  0101010A0                     Alexitol Sodium
#[Out]# 1  0101010B0                          Almasilate
#[Out]# 2  0101010C0                 Aluminium Hydroxide
#[Out]# 3  0101010D0  Aluminium Hydroxide With Magnesium
#[Out]# 4  0101010E0                        Hydrotalcite
# Wed, 17 Nov 2021 06:16:52
opioids = ['morphine', 'oxycodone', 'methadone', 'fentanyl', 'pethidine', 'buprenorphine', 'propoxyphene', 'codeine']# Wed, 17 Nov 2021 06:16:53
opioids_join = '|'.join(opioids)
opioids_join#[Out]# 'morphine|oxycodone|methadone|fentanyl|pethidine|buprenorphine|propoxyphene|codeine'
# Wed, 17 Nov 2021 06:16:54
chem.head()#[Out]#     CHEM SUB                                NAME
#[Out]# 0  0101010A0                     Alexitol Sodium
#[Out]# 1  0101010B0                          Almasilate
#[Out]# 2  0101010C0                 Aluminium Hydroxide
#[Out]# 3  0101010D0  Aluminium Hydroxide With Magnesium
#[Out]# 4  0101010E0                        Hydrotalcite
# Wed, 17 Nov 2021 06:16:55
opioid_codes = chem.loc[chem['NAME'].str.contains(opioids_join, case=False)]['CHEM SUB'].tolist()
len(opioid_codes)#[Out]# 35
# Wed, 17 Nov 2021 06:16:57
chem_new = chem
chem_new.columns = ['bnf_code','chem_name']
chem_new.head()#[Out]#     bnf_code                           chem_name
#[Out]# 0  0101010A0                     Alexitol Sodium
#[Out]# 1  0101010B0                          Almasilate
#[Out]# 2  0101010C0                 Aluminium Hydroxide
#[Out]# 3  0101010D0  Aluminium Hydroxide With Magnesium
#[Out]# 4  0101010E0                        Hydrotalcite
# Wed, 17 Nov 2021 06:16:58
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
# Wed, 17 Nov 2021 06:16:59
scrpt = scripts
scrpt.head()#[Out]#   practice   bnf_code                              bnf_name  items   nic  \
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
# Wed, 17 Nov 2021 06:17:00
scrpt['opioid_prescription'] = scrpt['bnf_code'].isin(opioid_codes)# Wed, 17 Nov 2021 06:17:01
scrpt.head()#[Out]#   practice   bnf_code                              bnf_name  items   nic  \
#[Out]# 0   N85639  0106020C0                 Bisacodyl_Tab E/C 5mg      1  0.39   
#[Out]# 1   N85639  0106040M0      Movicol Plain_Paed Pdr Sach 6.9g      1  4.38   
#[Out]# 2   N85639  0301011R0    Salbutamol_Inha 100mcg (200 D) CFF      1  1.50   
#[Out]# 3   N85639  0304010G0  Chlorphenamine Mal_Oral Soln 2mg/5ml      1  2.62   
#[Out]# 4   N85639  0401020K0                      Diazepam_Tab 2mg      1  0.16   
#[Out]# 
#[Out]#    act_cost  quantity  opioid_prescription  
#[Out]# 0      0.47        12                False  
#[Out]# 1      4.07        30                False  
#[Out]# 2      1.40         1                False  
#[Out]# 3      2.44       150                False  
#[Out]# 4      0.26         6                False  
# Wed, 17 Nov 2021 06:17:02
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
# Wed, 17 Nov 2021 06:17:04
pract = practices[['code', 'name']]
pract.columns = ['practice', 'name']
pract.head()#[Out]#   practice                        name
#[Out]# 0   A81001         THE DENSHAM SURGERY
#[Out]# 1   A81002  QUEENS PARK MEDICAL CENTRE
#[Out]# 2   A81003   VICTORIA MEDICAL PRACTICE
#[Out]# 3   A81004      WOODLANDS ROAD SURGERY
#[Out]# 4   A81005          SPRINGWOOD SURGERY
# Wed, 17 Nov 2021 06:17:06
opioids_per_practice = scrpt.groupby('practice')['opioid_prescription'].mean().rename('frac')
opioids_per_practice.head()#[Out]# practice
#[Out]# A81005    0.033179
#[Out]# A81007    0.043329
#[Out]# A81011    0.046556
#[Out]# A81012    0.042793
#[Out]# A81017    0.038140
#[Out]# Name: frac, dtype: float64
# Wed, 17 Nov 2021 06:17:07
overall_rate = scrpt['opioid_prescription'].mean()
overall_rate#[Out]# 0.03580276471367961
# Wed, 17 Nov 2021 06:17:08
overall_rate_std = scrpt['opioid_prescription'].std()
overall_rate_std#[Out]# 0.18579817605238425
# Wed, 17 Nov 2021 06:17:09
relative_opioids_per_practice = (opioids_per_practice - overall_rate).rename('relative')
relative_opioids_per_practice.head()#[Out]# practice
#[Out]# A81005   -0.002624
#[Out]# A81007    0.007526
#[Out]# A81011    0.010753
#[Out]# A81012    0.006990
#[Out]# A81017    0.002337
#[Out]# Name: relative, dtype: float64
# Wed, 17 Nov 2021 06:17:12
opioid = scrpt.groupby('practice')['opioid_prescription'].sum().rename('opioid')
opioid.head()#[Out]# practice
#[Out]# A81005    50
#[Out]# A81007    63
#[Out]# A81011    73
#[Out]# A81012    57
#[Out]# A81017    82
#[Out]# Name: opioid, dtype: int64
# Wed, 17 Nov 2021 06:17:14
total = scrpt.groupby('practice')['bnf_code'].count().rename('total')
total.head()#[Out]# practice
#[Out]# A81005    1507
#[Out]# A81007    1454
#[Out]# A81011    1568
#[Out]# A81012    1332
#[Out]# A81017    2150
#[Out]# Name: total, dtype: int64
# Wed, 17 Nov 2021 06:17:15
standard_error_per_practice = (overall_rate_std/(total**0.5)).rename('std_err')
opioid_scores = (relative_opioids_per_practice/standard_error_per_practice).rename('opioid_scores')

standard_error_per_practice.head()
opioid_scores.head()#[Out]# practice
#[Out]# A81005   -0.548306
#[Out]# A81007    1.544557
#[Out]# A81011    2.291795
#[Out]# A81012    1.373060
#[Out]# A81017    0.583168
#[Out]# Name: opioid_scores, dtype: float64
# Wed, 17 Nov 2021 06:17:18
merged = pd.concat([opioid, total, opioids_per_practice, relative_opioids_per_practice, standard_error_per_practice,opioid_scores], axis=1)# Wed, 17 Nov 2021 06:17:19
merged = merged.reset_index()# Wed, 17 Nov 2021 06:17:19
merged.head()#[Out]#   practice  opioid  total      frac  relative   std_err  opioid_scores
#[Out]# 0   A81005      50   1507  0.033179 -0.002624  0.004786      -0.548306
#[Out]# 1   A81007      63   1454  0.043329  0.007526  0.004873       1.544557
#[Out]# 2   A81011      73   1568  0.046556  0.010753  0.004692       2.291795
#[Out]# 3   A81012      57   1332  0.042793  0.006990  0.005091       1.373060
#[Out]# 4   A81017      82   2150  0.038140  0.002337  0.004007       0.583168
# Wed, 17 Nov 2021 06:17:21
pract.reset_index().head()#[Out]#    index practice                        name
#[Out]# 0      0   A81001         THE DENSHAM SURGERY
#[Out]# 1      1   A81002  QUEENS PARK MEDICAL CENTRE
#[Out]# 2      2   A81003   VICTORIA MEDICAL PRACTICE
#[Out]# 3      3   A81004      WOODLANDS ROAD SURGERY
#[Out]# 4      4   A81005          SPRINGWOOD SURGERY
# Wed, 17 Nov 2021 06:17:22
final_df = merged.merge(pract, on='practice', how='left')# Wed, 17 Nov 2021 06:17:23
final_df.head()#[Out]#   practice  opioid  total      frac  relative   std_err  opioid_scores  \
#[Out]# 0   A81005      50   1507  0.033179 -0.002624  0.004786      -0.548306   
#[Out]# 1   A81007      63   1454  0.043329  0.007526  0.004873       1.544557   
#[Out]# 2   A81011      73   1568  0.046556  0.010753  0.004692       2.291795   
#[Out]# 3   A81012      57   1332  0.042793  0.006990  0.005091       1.373060   
#[Out]# 4   A81017      82   2150  0.038140  0.002337  0.004007       0.583168   
#[Out]# 
#[Out]#                         name  
#[Out]# 0         SPRINGWOOD SURGERY  
#[Out]# 1          BANKHOUSE SURGERY  
#[Out]# 2          CHADWICK PRACTICE  
#[Out]# 3  WESTBOURNE MEDICAL CENTRE  
#[Out]# 4        WOODBRIDGE PRACTICE  
# Wed, 17 Nov 2021 06:17:25
final_df.sort_values('opioid_scores', ascending = False , inplace=True)# Wed, 17 Nov 2021 06:17:25
final_df.head()#[Out]#     practice  opioid  total      frac  relative   std_err  opioid_scores  \
#[Out]# 829   Y01852       6      7  0.857143  0.821340  0.070225      11.695818   
#[Out]# 874   Y03006       2      2  1.000000  0.964197  0.131379       7.339043   
#[Out]# 895   Y03668      11     60  0.183333  0.147531  0.023986       6.150582   
#[Out]# 296   G81703       7     36  0.194444  0.158642  0.030966       5.123032   
#[Out]# 948   Y04997      28    321  0.087227  0.051425  0.010370       4.958866   
#[Out]# 
#[Out]#                                 name  
#[Out]# 829        NATIONAL ENHANCED SERVICE  
#[Out]# 874         OUTREACH SERVICE NH / RH  
#[Out]# 895  BRISDOC HEALTHCARE SERVICES OOH  
#[Out]# 296           H&R P C SPECIAL SCHEME  
#[Out]# 948                   HMR BARDOC OOH  
# Wed, 17 Nov 2021 06:17:26
final = final_df.drop_duplicates('name')
final.head()#[Out]#     practice  opioid  total      frac  relative   std_err  opioid_scores  \
#[Out]# 829   Y01852       6      7  0.857143  0.821340  0.070225      11.695818   
#[Out]# 874   Y03006       2      2  1.000000  0.964197  0.131379       7.339043   
#[Out]# 895   Y03668      11     60  0.183333  0.147531  0.023986       6.150582   
#[Out]# 296   G81703       7     36  0.194444  0.158642  0.030966       5.123032   
#[Out]# 948   Y04997      28    321  0.087227  0.051425  0.010370       4.958866   
#[Out]# 
#[Out]#                                 name  
#[Out]# 829        NATIONAL ENHANCED SERVICE  
#[Out]# 874         OUTREACH SERVICE NH / RH  
#[Out]# 895  BRISDOC HEALTHCARE SERVICES OOH  
#[Out]# 296           H&R P C SPECIAL SCHEME  
#[Out]# 948                   HMR BARDOC OOH  
# Wed, 17 Nov 2021 06:17:28
result = final[['name','opioid_scores','total']]
result.head()#[Out]#                                 name  opioid_scores  total
#[Out]# 829        NATIONAL ENHANCED SERVICE      11.695818      7
#[Out]# 874         OUTREACH SERVICE NH / RH       7.339043      2
#[Out]# 895  BRISDOC HEALTHCARE SERVICES OOH       6.150582     60
#[Out]# 296           H&R P C SPECIAL SCHEME       5.123032     36
#[Out]# 948                   HMR BARDOC OOH       4.958866    321
# Wed, 17 Nov 2021 06:17:29
result = result.head(100)
values = result.get_values().tolist()# Wed, 17 Nov 2021 06:17:36
answer=[]

for item in values:
    answer.append(tuple(item))# Wed, 17 Nov 2021 06:17:42
def script_anomalies():
    return answer# Wed, 17 Nov 2021 06:17:58
grader.score('dw__script_anomalies', script_anomalies)# Wed, 17 Nov 2021 06:38:55
%logstop
%logstart -rtq ~/.logs/dw.py append
%matplotlib inline
import matplotlib
import seaborn as sns
sns.set()
matplotlib.rcParams['figure.dpi'] = 144