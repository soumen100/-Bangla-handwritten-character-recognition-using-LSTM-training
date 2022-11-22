# -*- coding: utf-8 -*-
"""
Created on Tue Nov 22 18:30:12 2022

@author: System Administrator
"""

# pip inastall splitfolders
import splitfolders # or import splitfolders
input_folder = "D:\\soumen_halder\\working\\EKUES_RAW_DATA\\male"
output = "D:\\soumen_halder\\EKUES_TEST_TRAIN_DATA" #where you want the split datasets saved. one will be created if it does not exist or none is set

splitfolders.ratio(input_folder, output=output, seed=42, ratio=(.8, .1, .1)) # ratio of split are in order of train/val/test. You can change to whatever you want. For train/val sets only, you could do .75, .25 for example.