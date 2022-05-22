import pandas as pd
import os
path = '/Users/edwu/Desktop/UCI/LexisNexis Interview Project/'
folders_name = ['dest history data','dest test data','origin data']
dir_list = os.listdir(path+folders_name[-1])

#['JFK.csv', 'LGA.csv', 'EWR.csv']
dest_his = pd.DataFrame()
dest_tes = pd.DataFrame()
origin = pd.DataFrame()
data = ['dest_his','dest_tes','origin']
for index,name in enumerate(folders_name):
    temp = pd.DataFrame()
    path2folder = path + name
    dir_list = os.listdir(path2folder)
    for file in dir_list:
        file_path = path2folder + '/' + file
        temp_data = pd.read_csv(file_path, index_col = 0)
        temp = pd.concat([temp,temp_data])
    temp.to_csv(path+data[index]+'.csv')






