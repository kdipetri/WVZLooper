#!/bin/env python

import ROOT as r
import sys


years = []
years.append("WVZ2016_v0.1.12.7")
years.append("WVZ2017_v0.1.12.7")
years.append("WVZ2018_v0.1.12.7")

for year in versions: 

	print("Version: ", year)
	#f = r.TFile("/nfs-7/userdata/phchang/babies/{}/karri_vh_nonbb_amcatnlo_1.root".format(year))
	f = r.TFile("/home/users/kdipetri/public_html/WVZBabyMaker/output_{}.root".format(year))

	if not f: continue
	
	t = f.Get("t")
	h = f.Get("h_neventsinfile")
	
	#f_www = r.TFile("/nfs-7/userdata/phchang/babies/{}/karri_wh_ww_amcatnlo_1.root".format(year), "recreate")
	#t_www = t.CopyTree("VHchannel==24&&Higgschannel==24")
	#t_www.Write()
	#h.Write()
	
	f_zww = r.TFile("/home/users/kdipetri/public_html/WVZBabyMaker/{}_karri_zh_ww_amcatnlo_1.root".format(year), "recreate")
	t_zww = t.CopyTree("VHchannel==23&&Higgschannel==24")
	t_zww.Write()
	h.Write()
	
	#f_wzz = r.TFile("/nfs-7/userdata/phchang/babies/{}/karri_wh_zz_amcatnlo_1.root".format(year), "recreate")
	#t_wzz = t.CopyTree("VHchannel==24&&Higgschannel==23")
	#t_wzz.Write()
	#h.Write()
	
	#f_zzz = r.TFile("/nfs-7/userdata/phchang/babies/{}/karri_zh_zz_amcatnlo_1.root".format(year), "recreate")
	#t_zzz = t.CopyTree("VHchannel==23&&Higgschannel==23")
	#t_zzz.Write()
	#h.Write()
	
	#f_rest = r.TFile("/nfs-7/userdata/phchang/babies/{}/karri_vh_nonbbwwzz_amcatnlo_1.root".format(year), "recreate")
	#t_rest = t.CopyTree("Higgschannel!=23&&Higgschannel!=24")
	#t_rest.Write()
	#h.Write()
	

print("Done!")
