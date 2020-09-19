#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan 17 23:37:53 2020

@author: nephilim
"""
def WriteModelData(ParametersData,FileName):
    X_Range=ParametersData['NewModel']['xlim']
    Z_Range=ParametersData['NewModel']['xlim']
    dx=ParametersData['NewModel']['dx']
    dz=ParametersData['NewModel']['dz']
    dt=ParametersData['NewModel']['dt']
    t=ParametersData['NewModel']['t']
    Freq=ParametersData['NewModel']['Freq']
    Step=ParametersData['NewModel']['Step']
    Scan=int(ParametersData['NewModel']['Scan'])
    SourceStart=ParametersData['NewModel']['SourcePosition'][0]
    ReceiverStart=ParametersData['NewModel']['ReceiverPosition'][0]
    NM_sigma=ParametersData['NewModel']['Single_sigma']
    NM_epsilon=ParametersData['NewModel']['Single_epsilon']
    NM_mu=ParametersData['NewModel']['Single_mu']
    if 'AddRectangle' in ParametersData.keys():
        Left=ParametersData['AddRectangle']['Left']
        Bottom=ParametersData['AddRectangle']['Bottom']
        Width=ParametersData['AddRectangle']['Width']
        High=ParametersData['AddRectangle']['High']
        Re_sigma=ParametersData['AddRectangle']['Single_sigma']
        Re_epsilon=ParametersData['AddRectangle']['Single_epsilon']
        Re_mu=ParametersData['AddRectangle']['Single_mu']
    if 'AddEllipse' in ParametersData.keys():
        Center_x=ParametersData['AddEllipse']['Center_x']
        Center_z=ParametersData['AddEllipse']['Center_z']
        LongAxis=ParametersData['AddEllipse']['LongAxis_']
        ShortAxis=ParametersData['AddEllipse']['ShortAxis_']
        El_sigma=ParametersData['AddEllipse']['Single_sigma']
        El_epsilon=ParametersData['AddEllipse']['Single_epsilon']
        El_mu=ParametersData['AddEllipse']['Single_mu']
    if 'AddPolygon' in ParametersData.keys():
        xc=ParametersData['AddPolygon']['xc']
        zc=ParametersData['AddPolygon']['zc']
        Po_sigma=ParametersData['AddPolygon']['Single_sigma']
        Po_epsilon=ParametersData['AddPolygon']['Single_epsilon']
        Po_mu=ParametersData['AddPolygon']['Single_mu']
        
    with open(FileName, 'w+') as f:
        # NewModel
        f.write('#NewModel:\n')
        f.write('X_Range:%f;Z_Range:%f\n'%(X_Range,Z_Range))
        f.write('dx:%f;dz:%f\n'%(dx,dz))
        f.write('dt:%e;SimulationTime:%e;Frequence:%e\n'%(dt,t,Freq))
        f.write('SourceStart:(%f,%f);ReceierStart:(%f,%f);Step:%f;Scan:%d\n'%(SourceStart[0],SourceStart[1],ReceiverStart[0],ReceiverStart[1],Step,Scan))
        f.write('Conductivity:%e;DielectricConstant:%f;MagneticPermeability:%f\n'%(NM_sigma,NM_epsilon,NM_mu))
        if 'AddRectangle' in ParametersData.keys():
            # Rectangle
            f.write('\n#AddRectangle:\n')
            f.write('Left:%f;Bottom:%f;Width:%f;High:%f\n'%(Left,Bottom,Width,High))
            f.write('Conductivity:%e;DielectricConstant:%f;MagneticPermeability:%f\n'%(Re_sigma,Re_epsilon,Re_mu))
        if 'AddEllipse' in ParametersData.keys():
            # Ellipse
            f.write('\n#AddEllipse:\n')
            f.write('Center:(%f,%f);LongAxis:%f;ShortAxis:%f\n'%(Center_x,Center_z,LongAxis,ShortAxis))
            f.write('Conductivity:%e;DielectricConstant:%f;MagneticPermeability:%f\n'%(El_sigma,El_epsilon,El_mu))
        if 'AddPolygon' in ParametersData.keys():
            # Polygon
            f.write('\n#AddPolygon:\n')
            f.write('xc:(')
            for idx,xc_ in enumerate(xc):
                f.write('%f'%xc_)
                if idx != len(xc)-1:
                    f.write(',')
            f.write(');zc:(')
            for idx,zc_ in enumerate(zc):
                f.write('%f'%zc_)
                if idx != len(zc)-1:
                    f.write(',')
            f.write(')\n')
            f.write('Conductivity:%e;DielectricConstant:%f;MagneticPermeability:%f\n'%(Po_sigma,Po_epsilon,Po_mu))