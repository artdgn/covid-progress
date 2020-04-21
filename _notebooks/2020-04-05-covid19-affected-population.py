# -*- coding: utf-8 -*-
# ---
# jupyter:
#   jupytext:
#     formats: ipynb,py:light
#     text_representation:
#       extension: .py
#       format_name: light
#       format_version: '1.5'
#       jupytext_version: 1.4.2
#   kernelspec:
#     display_name: Python 3
#     language: python
#     name: python3
# ---

# + [markdown] papermill={"duration": 0.013695, "end_time": "2020-03-27T06:31:15.895652", "exception": false, "start_time": "2020-03-27T06:31:15.881957", "status": "completed"} tags=[]
# # Affected Population by Country (full table, updated daily)
# > Displaying the full table of projections of affected populations.
#
# - categories: [overview]
# - comments: true
# - author: <a href=https://github.com/artdgn/>artdgn</a>
# - image: images/affected-pop.png
# - permalink: /covid-affected-population/
# - toc: true
# - hide: false
# -

# > Important: This dashboard contains the results of a predictive model that was not built by an epidimiologist.

# + papermill={"duration": 0.330834, "end_time": "2020-03-27T06:31:16.261108", "exception": false, "start_time": "2020-03-27T06:31:15.930274", "status": "completed"} tags=[]
#hide
import pandas as pd
import covid_helpers

helper = covid_helpers.OverviewData
stylers = covid_helpers.PandasStyling
df = helper.filter_df(helper.table_with_projections())
# -

#hide_input
from IPython.display import display, Markdown
Markdown(f"***Based on data up to: {pd.to_datetime(helper.dt_today).date().isoformat()}***")

# ## For other details and projections see [main notebook](/notebook-posts/covid-progress-projections/)

# ## Projected Affected Population percentage
#
# > Countries sorted by number of new cases in last 5 days
#
# - Details of estimation and prediction calculations are in [Appendix](#appendix).
# - Column definitions:
#     - <font size=2><b>Estimated <i>new</i> cases in last 5 days</b>: self explanatory.</font>
#     - <font size=2><b>Estimated <i>total</i> affected population percentage</b>: estimated percentage of total population already affected (infected, recovered, or dead).</font>
#     - <font size=2><b>Estimated daily infection rate</b>: daily percentage rate of new infections relative to active infections during last 5 days.</font>
#     - <font size=2><b>Projected total affected percentage in 14 days</b>: of population.</font>
#     - <font size=2><b>Projected total affected percentage in 30 days</b>: of population.</font>        
#     - <font size=2><b>Lagged fatality rate</b>: reported total deaths divided by total cases 8 days ago.</font>

# +
#hide_input
df_data = df.sort_values('Cases.new.est', ascending=False)
df_pretty = df_data.copy()
df_pretty['affected_ratio.est.+14d'] = stylers.with_errs_ratio(
    df_pretty, 'affected_ratio.est.+14d', 'affected_ratio.est.+14d.err')
df_pretty['affected_ratio.est.+30d'] = stylers.with_errs_ratio(
    df_pretty, 'affected_ratio.est.+30d', 'affected_ratio.est.+30d.err')
df_pretty['infection_rate'] = stylers.with_errs_ratio(df_pretty, 'infection_rate', 'growth_rate_std')

cols = {'Cases.new.est': 'Estimated <br> <i>new</i> cases <br> in last 5 days',        
       'affected_ratio.est': 'Estimated <br><i>total</i><br>affected<br>population<br>percentage',
       'infection_rate': 'Estimated <br>daily infection<br>rate',
       'affected_ratio.est.+14d': 'Projected<br><i>total</i><br>affected<br>percentage<br>In 14 days',
       'affected_ratio.est.+30d': 'Projected<br><i>total</i><br>affected<br>percentage<br>In 30 days',       
       'lagged_fatality_rate': 'Lagged<br>fatality<br>rate',
      }

df_pretty[cols.keys()].rename(cols, axis=1).style\
    .apply(stylers.add_bar, color='#719974',
           s_v=df_data['affected_ratio.est.+14d'], subset=cols['affected_ratio.est.+14d'])\
    .apply(stylers.add_bar, color='#a1afa3',
           s_v=df_data['affected_ratio.est.+30d'], subset=cols['affected_ratio.est.+30d'])\
    .apply(stylers.add_bar, color='#f49d5a',
           s_v=df_data['infection_rate']/0.33, subset=cols['infection_rate'])\
    .bar(subset=cols['Cases.new.est'], color='#b57b17')\
    .bar(subset=cols['affected_ratio.est'], color='#5dad64', vmin=0, vmax=1.0)\
    .bar(subset=cols['lagged_fatality_rate'], color='#420412', vmin=0, vmax=0.2)\
    .applymap(lambda _: 'color: red', subset=cols['lagged_fatality_rate'])\
    .format('<b>{:,.0f}</b>', subset=cols['Cases.new.est'])\
    .format('<b>{:.1%}</b>', subset=[cols['lagged_fatality_rate'], cols['affected_ratio.est']])
# -

# ## Appendix
# <a id='appendix'></a>
# [See appendix in main notebook](/notebook-posts/covid-progress-projections/#appendix)
