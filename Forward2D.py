#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 31 14:57:58 2018

@author: nephilim
"""
from multiprocessing import Pool
import numpy as np
import Add_CPML
import Time_loop
import Wavelet
# import shutil
# import os

def Forward2D(parameter,value_source,value_receiver,index):
    t=np.arange(parameter['NewModel']['k_max'])*parameter['NewModel']['dt']
    f=Wavelet.ricker(t,parameter['NewModel']['Freq'])
    CPML_Params=Add_CPML.Add_CPML(parameter['NewModel']['xl'],parameter['NewModel']['zl'],parameter['All_sigma'],\
                                  parameter['All_epsilon'],parameter['All_mu'],parameter['NewModel']['dx'],\
                                  parameter['NewModel']['dz'],parameter['NewModel']['dt'])
    Forward_data=Time_loop.time_loop(parameter['NewModel']['xl'],parameter['NewModel']['zl'],\
                                     parameter['NewModel']['dx'],parameter['NewModel']['dz'],\
                                     parameter['NewModel']['dt'],parameter['All_sigma'],\
                                     parameter['All_epsilon'],parameter['All_mu'],CPML_Params,\
                                     f,parameter['NewModel']['k_max'],value_source,value_receiver)
    Profile=np.empty((parameter['NewModel']['k_max']))
    for i in range(parameter['NewModel']['k_max']):
        tmp=Forward_data.__next__()
        Profile[i]=tmp[0]
    return index,Profile
    
def Forward_2D(parameter):
    pool=Pool(processes=8)
    Profile=np.empty((parameter['NewModel']['k_max'],len(parameter['NewModel']['SourcePosition_idx'])))
    res_l=[]
    for idx,data_position in enumerate(zip(parameter['NewModel']['SourcePosition_idx'],parameter['NewModel']['ReceiverPosition_idx'])):
        print(data_position[0])
        print(data_position[1])
        res=pool.apply_async(Forward2D,args=(parameter,data_position[0],data_position[1],idx))
        res_l.append(res)
    pool.close()
    pool.join()
    for res in res_l:
        result=res.get()
        Profile[:,result[0]]=result[1]
        del result
    del res_l
    pool.terminate()
    return Profile
    
    
    
    
if __name__=='__main__':
    parameter=dict()
    parameter['NewModel']=dict()
    parameter['NewModel']['xl']=101
    parameter['NewModel']['zl']=51
    parameter['NewModel']['dx']=0.025
    parameter['NewModel']['dz']=0.025
    parameter['NewModel']['dt']=1e-11
    parameter['NewModel']['k_max']=750
    parameter['NewModel']['Freq']=4e8
    parameter['All_epsilon']=4*np.ones((201,201))
    parameter['All_epsilon'][0:20,10:20]=10
    parameter['All_sigma']=1e-5*np.ones((201,201))
    parameter['All_mu']=np.ones((201,201))
    # x_=np.arange(10,110)
    # z_=[10,]*len(x_)
    parameter['NewModel']['SourcePosition_idx']=[(10, 10), (10, 11), (10, 12), (10, 13), (10, 14), (10, 15), (10, 16), (10, 17), (10, 18), (10, 19)]

    parameter['NewModel']['ReceiverPosition_idx']=[(10, 12), (10, 13), (10, 14), (10, 15), (10, 16), (10, 17), (10, 18), (10, 19), (10, 20), (10, 21)]
    Profile=Forward_2D(parameter)
    from matplotlib import pyplot
    pyplot.imshow(Profile,vmin=0.1*np.min(Profile),vmax=0.1*np.max(Profile),extent=(0,1,0,1))
    