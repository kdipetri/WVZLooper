#!/bin/env python

###########################################
#
# Main plotting script for the WVZ analysis
#
###########################################

#____________________________________________________________________________________
def main_analysis_make_plot_userfilter():

    import plottery_wrapper as p
    import argparse
    import sys
    
    parser = argparse.ArgumentParser(description="Plotter for the WVZ analysis")
    parser.add_argument('-s' , '--sample_set_name' , dest='sample_set_name' , help='Sample set name (e.g. WVZ2016_v0.0.9 or even the combined ones like WVZ2016_v0.0.9_WVZ2017_v0.0.9_WVZ2018_v0.0.9' , required=True)
    parser.add_argument('-t' , '--tag'             , dest='tag'             , help='Tag of the looper output'                                                                                         , required=True)
    parser.add_argument('-d' , '--dirname'         , dest='dirname'         , help='karri_plots/<sample_set_name>/<tag>/<dirname> for plot output'                                                          , required=True)
    parser.add_argument('-p' , '--filter_pattern'  , dest='filter_pattern'  , help='To filter out plot'                                                                                               , required=True)
    parser.add_argument('-u' , '--unblind'         , dest='unblind'         , help='To unblind data'     , default=True, action='store_true'                                                                        )
    # parser.add_argument('-f' , '--fake_rate_study' , dest='fake_rate_study' , help='Use MC bkg grouping intended for fake rate study ', default=False, action='store_true'                                           )
    parser.add_argument('-n' , '--nbins'           , dest='nbins'           , help='# of bins'           , default=15                                                                                                )
    parser.add_argument('-y' , '--yaxis_log'       , dest='yaxis_log'       , help='yaxis log'           , default=False, action='store_true'                                                                        )
    parser.add_argument('-c' , '--one_signal'      , dest='one_signal'      , help='one signal hist'     , default=False, action='store_true'                                                                        )
    parser.add_argument('-x' , '--xaxis_label'     , dest='xaxis_label'     , help='xaxis title'         , default=""                                                                                                )
    parser.add_argument('-r' , '--yaxis_range'     , dest='yaxis_range'     , help='yaxis range'         , default=[]                                                                                                )
    parser.add_argument('-i' , '--stack_signal'    , dest='stack_signal'    , help='stack signal'        , default=False, action='store_true'                                                                        )
    
    args = parser.parse_args()


    # Make plot function of the main analysis
    # The main thing is that this plotting script runs over the output files
    # that was ran with "WVZ201*_v*" ntuples
    # This means that it assumes specific histogram files to exists

    ntuple_version = args.sample_set_name
    tag = args.tag
    dirname = args.dirname
    filter_pattern = args.filter_pattern
    unblind = args.unblind

    #KARRI ggZH tmp 
    #bkgfiles = ["outputs/{}/{}/mad_zh_wwz.root".format(ntuple_version, tag)]
    #bkgnames = [ "ZH_WWZ_mad" ]
    #sigfiles_detail = [
    #        #"outputs/{}/{}/nonh_wwz.root".format(ntuple_version, tag),
    #        "outputs/{}/{}/zh_wwz.root".format(ntuple_version, tag),
    #        "outputs/{}/{}/ggzh_wwz.root".format(ntuple_version, tag),
    #        ]
    #signames = [ "ZH_WWZ", "ggZH_WWZ" ]


    # Comparing All things together
    bkgfiles = [
            #"outputs/{}/{}/nonh_wwz.root".format(ntuple_version, tag),
            "outputs/{}/{}/zh_wwz.root".format(ntuple_version, tag),
            "outputs/{}/{}/ggzh_wwz.root".format(ntuple_version, tag),
            ]
    bkgnames = [ "Powheg ZH_WWZ", "Powheg ggZH_WWZ" ]
    sigfiles_detail = []
    signames = [ ]
    #sigfiles_detail = ["outputs/{}/{}/mad_zh_wwz.root".format(ntuple_version, tag)]
    #signames = ["Madgraph ZH_WWZ" ]

    colors = [2005, 2007, 2003, 2011, 920, 2012, 2011, 2002]
    #colors = [2001, 2005, 2007, 2003, 2011, 920, 2012, 2011, 2002]

    if "2016" in ntuple_version: lumi = 35.9
    if "2017" in ntuple_version: lumi = 41.3
    if "2018" in ntuple_version: lumi = 59.74
    if "2016" in ntuple_version and "2017" in ntuple_version and "2018" in ntuple_version: lumi = 137

    p.dump_plot(fnames=bkgfiles,
            #KARRI ggZH tmp 
            sig_fnames=sigfiles_detail,
            data_fname="outputs/{}/{}/mad_zh_wwz.root".format(ntuple_version, tag),
            #data_fname=None,
            usercolors=colors,
            legend_labels=bkgnames,
            signal_labels=signames, 
            dirname="karri_plots/{}/{}/{}".format(ntuple_version, tag, dirname),
            filter_pattern=filter_pattern,
            dogrep=True,
	    #donorm=False if "Yield" in filter_pattern else True, 
            extraoptions={
                "print_yield":True,
                "nbins":int(args.nbins),
                "signal_scale": 1,
                # "signal_scale": 20,
                # "signal_scale": 10,
                # "signal_scale": "auto",
                "legend_scalex":2.0 if "PlusX" in filter_pattern else 1.3,
                "legend_scaley":0.7 if "PlusX" in filter_pattern else 1.2,
                "legend_ncolumns": 1,
                # "legend_smart": False if args.yaxis_log else True,
                "legend_smart": True,
                "yaxis_log":args.yaxis_log,
                "ymax_scale": 1.5,
                "lumi_value":lumi,
                # "no_overflow": True,
                "remove_underflow": True,
                "xaxis_ndivisions":505,
                "ratio_range":[0.,2.],
                "xaxis_label":args.xaxis_label,
                "ratio_xaxis_title":args.xaxis_label,
                "yaxis_range":[float(x) for x in args.yaxis_range.split(",")] if isinstance(args.yaxis_range, basestring) and len(args.yaxis_range) > 0 else [],
                "no_ratio": False if unblind else True,
                },
            # _plotter=p.plot_cut_scan,
            )


if __name__ == "__main__":

    # Run different make plot script based on what dataset the looper ran on
    main_analysis_make_plot_userfilter()
