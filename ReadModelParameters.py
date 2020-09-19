#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jan 18 01:26:03 2020

@author: nephilim
"""
class FileOpen_Read(object):
    def __init__(self,filename):
        self.filename=filename
    def ReadModelParameters(self):
        with open(self.filename, 'r') as fileobj:
            ParameterName=fileobj.readline()
            # X_Range & Z_Range
            NextLine=fileobj.readline()
            NL_data=NextLine.split(';')
            X_Range_=NL_data[0].split(':')
            self.X_Range=float(X_Range_[1])
            Z_Range_=NL_data[1].split(':')
            self.Z_Range=float(Z_Range_[1])
            # dx & dz
            NextLine=fileobj.readline()
            NL_data=NextLine.split(';')
            dx_=NL_data[0].split(':')
            self.dx=float(dx_[1])
            dz_=NL_data[1].split(':')
            self.dz=float(dz_[1])
            # dt & SimulationTime & Frequence
            NextLine=fileobj.readline()
            NL_data=NextLine.split(';')
            dt_=NL_data[0].split(':')
            self.dt=float(dt_[1])
            SimulationTime_=NL_data[1].split(':')
            self.SimulationTime=float(SimulationTime_[1])
            Frequence_=NL_data[2].split(':')
            self.Frequence=float(Frequence_[1])
            # SourceStart & ReceierStart & Step & Scan
            NextLine=fileobj.readline()
            NL_data=NextLine.split(';')
            SourceStart_=NL_data[0].split(':')
            self.SourceStart=eval(SourceStart_[1])
            ReceierStart_=NL_data[1].split(':')
            self.ReceierStart=eval(ReceierStart_[1])
            Step_=NL_data[2].split(':')
            self.Step=float(Step_[1])
            Scan_=NL_data[3].split(':')
            self.Scan=int(Scan_[1])
            # Conductivity & DielectricConstant & MagneticPermeability
            NextLine=fileobj.readline()
            NL_data=NextLine.split(';')
            NM_Conductivity_=NL_data[0].split(':')
            self.NM_Conductivity=float(NM_Conductivity_[1])
            NM_DielectricConstant_=NL_data[1].split(':')
            self.NM_DielectricConstant=float(NM_DielectricConstant_[1])
            NM_MagneticPermeability_=NL_data[2].split(':')
            self.NM_MagneticPermeability=float(NM_MagneticPermeability_[1])
            while True:
                fileobj.readline()
                ParameterName=fileobj.readline()
                if ParameterName:
                    self.ReadNextModel(ParameterName,fileobj)
                else:
                    break

    def ReadNextModel(self,ParameterName,fileobj):
        if 'Rectangle' in str(ParameterName):
            # Left & Bottom & Width & High
            self.Rectangle=True
            NextLine=fileobj.readline()
            NL_data=NextLine.split(';')
            Left_=NL_data[0].split(':')
            self.Left=float(Left_[1])
            Bottom_=NL_data[1].split(':')
            self.Bottom=float(Bottom_[1])
            Width_=NL_data[2].split(':')
            self.Width=float(Width_[1])
            High_=NL_data[3].split(':')
            self.High=float(High_[1])
            # Conductivity & DielectricConstant & MagneticPermeability
            NextLine=fileobj.readline()
            NL_data=NextLine.split(';')
            Re_Conductivity_=NL_data[0].split(':')
            self.Re_Conductivity=float(Re_Conductivity_[1])
            Re_DielectricConstant_=NL_data[1].split(':')
            self.Re_DielectricConstant=float(Re_DielectricConstant_[1])
            Re_MagneticPermeability_=NL_data[2].split(':')
            self.Re_MagneticPermeability=float(Re_MagneticPermeability_[1])
        if 'Ellipse' in str(ParameterName):
            # Center & LongAxis & ShortAxis
            self.Ellipse=True
            NextLine=fileobj.readline()
            NL_data=NextLine.split(';')
            Center_=NL_data[0].split(':')
            self.Center=eval(Center_[1])
            self.Center_x=self.Center[0]
            self.Center_z=self.Center[1]
            LongAxis_=NL_data[1].split(':')
            self.LongAxis=float(LongAxis_[1])
            ShortAxis_=NL_data[2].split(':')
            self.ShortAxis=float(ShortAxis_[1])
            # Conductivity & DielectricConstant & MagneticPermeability
            NextLine=fileobj.readline()
            NL_data=NextLine.split(';')
            El_Conductivity_=NL_data[0].split(':')
            self.El_Conductivity=float(El_Conductivity_[1])
            El_DielectricConstant_=NL_data[1].split(':')
            self.El_DielectricConstant=float(El_DielectricConstant_[1])
            El_MagneticPermeability_=NL_data[2].split(':')
            self.El_MagneticPermeability=float(El_MagneticPermeability_[1])
        if 'Polygon' in str(ParameterName):
            # xc & zc
            self.Polygon=True
            NextLine=fileobj.readline()
            NL_data=NextLine.split(';')
            xc_=NL_data[0].split(':')
            self.xc=eval(xc_[1])
            zc_=NL_data[1].split(':')
            self.zc=eval(zc_[1])
            # Conductivity & DielectricConstant & MagneticPermeability
            NextLine=fileobj.readline()
            NL_data=NextLine.split(';')
            Po_Conductivity_=NL_data[0].split(':')
            self.Po_Conductivity=float(Po_Conductivity_[1])
            Po_DielectricConstant_=NL_data[1].split(':')
            self.Po_DielectricConstant=float(Po_DielectricConstant_[1])
            Po_MagneticPermeability_=NL_data[2].split(':')
            self.Po_MagneticPermeability=float(Po_MagneticPermeability_[1])
            
if __name__=='__main__':
    FileRead=FileOpen_Read('./re0.csu')
    FileRead.ReadModelParameters()
