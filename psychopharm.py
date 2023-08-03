#!/usr/bin/env python
# coding: utf-8

# In[3]:


import pandas as pd
pharm = pd.read_csv(r"C:\Users\kspen\OneDrive\Documents\pychopharmacology_python.csv")


# In[2]:


diagnosis = input('''Enter a diagnosis category: addiction, adhd, agitation, anxiety, bipolar, depression, eating, 
            insomnia, mania, movement, brain, or psychosis: ''')

weight = input('''Do you want to view medications with weight gain side effects of unusual, not unusual, common,
         problematic, or not well characterized:  ''')

sedation = input('''Do you want to view medications with sedation side effects of unusual, not unusual, common,
           or problematic: ''')

renal = input('Does the patient have renal impairment? Answer by stage: ren1, ren2, ren3, ren4, or no: ')

hepatic = input('Does the patient have hepatic impairment? Answer by stage: hep1, hep2, hep3, hep4, or no: ')


dx_list = ['addiction', 'adhd', 'agitation', 'anxiety', 'bipolar', 'depression', 'eating', 'insomnia',
           'mania', 'movement', 'brain', 'psychosis']

wt_list = ['unusual', 'not unusual', 'common','problematic', 'not well characterized']

sed_list = ['unusual', 'not unusual', 'common', 'problematic']

ren_list = ['ren1', 'ren2', 'ren3', 'ren4']

hep_list = ['hep1', 'hep2', 'hep3', 'hep4']
        

pharm[(pharm.loc[:,'bipolar']==1) & (pharm.loc[:,'weight'] == 'unusual') & 
      (pharm.loc[:,'sedation'] == 'unusual')][['medication', 'brand', 'class', 
                                               renal]].sort_values(by='medication', ignore_index=True)

   
    
def prescribe(diagnosis, weight, sedation, renal, hepatic):
    for dx in dx_list:
        if dx == diagnosis:
            for wt in wt_list:
                if wt == weight:
                    for sed in sed_list:
                        if sed == sedation:
                            for ren in ren_list:
                                if ren == renal:
                                    for hep in hep_list:
                                        if hep == hepatic:
                                            return(pharm[(pharm[diagnosis]==1) &
                                                  (pharm['weight'] == weight) & 
                                                  (pharm['sedation']== sedation) &
                                                  (pharm[renal]!='contraindicated') &
                                                  (pharm[hepatic]!='contraindicated')][['medication','brand','class', 
                                                                                       renal, hepatic]].sort_values(by='medication', 
                                                                                                                    ignore_index=True))
                                                                                                                   
            
                                        elif hepatic == 'no':
                                            return(pharm[(pharm[diagnosis]==1) &
                                                  (pharm['weight'] == weight) & 
                                                  (pharm['sedation']== sedation) &
                                                  (pharm[renal]!='contraindicated')][['medication','brand','class',
                                                                                     renal]].sort_values(by='medication',
                                                                                                        ignore_index=True))
                                        else:
                                            continue
                                elif renal == 'no':
                                        for hep in hep_list:
                                            if hep == hepatic:
                                                return(pharm[(pharm[diagnosis]==1) &
                                                  (pharm['weight'] == weight) & 
                                                  (pharm['sedation']== sedation) &
                                                  (pharm[hepatic]!='contraindicated')][['medication','brand','class',
                                                                                       hepatic]].sort_values(by='medication',
                                                                                                            ignore_index=True))
                                            elif hepatic == 'no':
                                                return(pharm[(pharm[diagnosis]==1) &
                                                  (pharm['weight'] == weight) & 
                                                  (pharm['sedation']== sedation)][['medication','brand','class']].sort_values(by='medication',
                                                                                                                             ignore_index=True))    
                                        else:
                                            continue
                                else:
                                    continue
                        else:
                            continue
                else:
                    continue
        else:
            continue
        
                            
                       
prescribe(diagnosis, weight, sedation, renal, hepatic)

