#!/usr/bin/env python
# coding: utf-8

# In[221]:


import datetime
import pandas as pd
import pickle
import os

# 여태까지 작업한 데이터가 담기는 곳
dict_df = {}
cnt = 0
trial = str(cnt)+'_trial'

# 업로드한 데이터가 담기는곳
pkl_data = None





class data_save():
    def __init__(self,train_df = pd.DataFrame() ,test_df = pd.DataFrame() ,all_df = pd.DataFrame()):
        
        global dict_df
        global cnt
        global trial
        global pkl_data

        self.train_df = train_df
        self.test_df = test_df
        self.all_df = all_df
        
        if pkl_data == None :
            # 현재 데이터 받기용
            print('저장된 pickle파일 없음')
            
        
        else : 
            print('저장된 pickle파일 load')
            # load할 pkl파일이 있으면 해당 데이터 load
            dict_df = pkl_data
            cnt = int(list(pkl_data.keys())[-1].split('_')[0])
            trial = list(pkl_data.keys())[-1]

        
        # 데이터 history용 
        if not self.all_df.empty :
            cnt+=1
            trial = str(cnt)+'_trial'
            dict_df[trial] = self.all_df

            
            
        elif not self.train_df.empty and not self.test_df.empty :
            self.train_df['data_set'] = 'train'
            self.test_df['data_set'] = 'test'
            
            for i in self.train_df.columns.difference(self.test_df.columns):
                self.test_df[str(i)] = 0
            
            self.all_df = pd.concat([self.train_df,self.test_df])
            
            cnt+=1
            trial = str(cnt)+'_trial'
            dict_df[trial] = self.all_df

            
        
    def return_train_df(self):
        return self.train_df
        
    def return_test_df(self):
        return self.test_df
    
    def return_all_df(self):
        return self.all_df
    
    def return_dict_df(self):
        return dict_df

    def save_pkl(self):
        with open('pkl_file/hist_df_'+datetime.datetime.now().strftime('%Y%m%d_%H%M')+'.pkl', 'wb') as f:
            pickle.dump(dict_df, f)
        
    
    def del_last_hist_df(self):
        del dict_df[trial]
        print('마지막 trial 데이터 제거')
        print('제거된 trial : ', trial)
        
        cnt -= 1
        trial = str(cnt-1)+'_trial'
        


# pkl파일 있으면 불러오는부분 ~
r = [s for s in os.listdir('pkl_file') if ".pkl" in s]

if len(r)>=1:
    print("통과")
    with open('pkl_file/'+r[-1], 'rb') as fr:
        pkl_data = pickle.load(fr)
        
