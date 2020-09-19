#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jul  5 17:32:32 2019

@author: nephilim
"""
import struct
from numpy import fromfile
import datetime


def dzt_headers_datetime(date_bytes):
    binary_array = format(struct.unpack("=I", date_bytes)[0], "b").zfill(32)[::-1]
    sec2=int(binary_array[0:5][::-1], base=2)  # 5-bits 00-04  0-29 (second/2)
    minutes=int(binary_array[5:11][::-1], base=2)  # 6-bits 05-10  0-59
    hour=int(binary_array[11:16][::-1], base=2)  # 5-bits 11-15  0-23
    day=int(binary_array[16:21][::-1], base=2)  # 5-bits 16-20  1-31
    month=int(binary_array[21:25][::-1], base=2)  # 4-bits 21-24  1-12, 1=Jan, 2=Feb, etc.
    year=int(binary_array[25:32][::-1], base=2)  # 7-bits 25-31  0-127 (0-127 = 1980-2107)
    value_range_pairs=((sec2,(0,30)),(minutes,(0,60)),(hour,(0,24)),(day, (1,32)),(month,(1,13)),(year,(0,128)))

    if all((v >= lb) & (v < ub) for v, (lb, ub) in value_range_pairs):
        return datetime.datetime(1980 + year, month, day, hour, minutes, sec2 * 2)
    else:
        return '%s-%s-%s %s:%s:%s'%(year+1980,month,day,hour,minutes,sec2*2)

def dzt_headers(fileobject):
    DZT_HEADER_BYTES=1024
    header=fileobject.read(DZT_HEADER_BYTES)
    DZT_HEADER_STRUCT='=4Hh5fH4s4s7H3f18s2H4hcc14sH12sh896s'
    (rh_tag,
     rh_data,
     rh_nsamp,
     rh_bits,
     rh_zero,
     rh_sps,
     rh_spm,
     rh_mpm,
     rh_position,
     rh_range,
     rh_npass,
     rh_create,
     rh_modif,
     rh_rgain,
     rh_nrgain,
     rh_text,
     rh_ntext,
     rh_proc,
     rh_nproc,
     rh_nchan,
     rh_epsr,
     rh_top,
     rh_depth,
     rh_reserved,
     rh_spp,
     rh_linemun,
     rh_start_x,
     rh_start_y,
     rh_end_x,
     rh_end_y,
     rh_lineorder,
     rh_dtype,
     rh_antname,
     rh_chanmask,
     rh_name,
     rh_chksum,
     rh_variable)=struct.unpack(DZT_HEADER_STRUCT,header)

    rh_tag_bits=hex(rh_tag)
    rh_tag_bytes=struct.pack("H",rh_tag).decode('ascii','ignore').replace("\x00", " ").strip()
    rh_create_time=dzt_headers_datetime(rh_create)
    rh_modif_time=dzt_headers_datetime(rh_modif)
    rh_reserved=rh_reserved.decode('ascii','ignore').replace("\x00", " ").strip()
    rh_lineorder=rh_lineorder.decode('ascii','ignore').replace("\x00", " ").strip()
    rh_dtype=rh_dtype.decode('ascii','ignore').replace("\x00", " ").strip()
    rh_antname=rh_antname.decode('ascii','ignore').replace("\x00", " ").strip()
    rh_name=rh_name.decode('ascii','ignore').replace("\x00", " ").strip()
    rh_variable=rh_variable.decode('ascii','ignore').replace("\x00", " ").strip()
    
    header_dict={"rh_tag": rh_tag,
                 "rh_tag_bits": rh_tag_bits,
                 "rh_tag_bytes": rh_tag_bytes,
                 "rh_data": rh_data,
                 "rh_nsamp": rh_nsamp,
                 "rh_nsamp": rh_nsamp,
                 "rh_bits": rh_bits,
                 "rh_zero": rh_zero,
                 "rh_sps": rh_sps,
                 "rh_spm": rh_spm,
                 "rh_mpm": rh_mpm,
                 "rh_position": rh_position,
                 "rh_range": rh_range,
                 "rh_npass": rh_npass,
                 "rh_create": rh_create_time,
                 "rh_modif": rh_modif_time,
                 "rh_rgain": rh_rgain,
                 "rh_nrgain": rh_nrgain,
                 "rh_text": rh_text,
                 "rh_ntext": rh_ntext,
                 "rh_proc": rh_proc,
                 "rh_nproc": rh_nproc,
                 "rh_nchan": rh_nchan,
                 "rh_epsr": rh_epsr,
                 "rh_top": rh_top,
                 "rh_depth": rh_depth,
                 "rh_reserved": rh_reserved,
                 "rh_spp": rh_spp,
                 "rh_linemun": rh_linemun,
                 "rh_start_x": rh_start_x,
                 "rh_start_y": rh_start_y,
                 "rh_end_x": rh_end_x,
                 "rh_end_y": rh_end_y,
                 "rh_lineorder": rh_lineorder,
                 "rh_dtype": rh_dtype,
                 "rh_antname": rh_antname,
                 "rh_chanmask": rh_chanmask,
                 "rh_name": rh_name,
                 "rh_chksum": rh_chksum,
                 "rh_variable": rh_variable,
                 }
    if rh_data!=1024:
        fileobject.read(DZT_HEADER_BYTES*(rh_data-1))
    else:
        fileobject.read(DZT_HEADER_BYTES*(rh_nchan-1))
    return header_dict

def DZT_read(fileobject):    
    # fileobject=open('./CSU1215__002.DZT','rb')
    headers=dzt_headers(fileobject)
    dtype_dict={8:"uint8",16:"uint16",32:"int32",64:"int64"}
    dtype_=headers['rh_bits']
    dtype=dtype_dict[dtype_]
    data_array=fromfile(fileobject, count=-1, dtype=dtype)
    N=headers['rh_nsamp']
    D=data_array.size//N
    data_array=data_array.reshape((N,D),order='F')
    data_array[:2,:]=0
    return headers,data_array