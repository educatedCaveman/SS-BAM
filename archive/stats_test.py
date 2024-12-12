from IPython.display import display
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# data load
dtypes = {
    'band_type':            'string',   #0
    'pellet_type':          'string',   #1
    'trial_num':            'int',      #2
    'mass_gn':              'float',    #3
    'calc_mass_g':          'float',    #4
    'velocity_mps':         'float',    #5
    'draw_length_m':        'float',    #6 
    'slack_length_m':       'float',    #7
    'draw_weight_kg':       'float',    #8
    'calc_draw_force_N':    'float',    #9
    'note':                 'string',   #10
    'calc_momentum':        'float',    #11
    'calc_power_stroke_m':  'float',    #12
    'calc_PE':              'float',    #13
    'calc_KE':              'float',    #14
    'calc_efficiency':      'float',    #15
}
df = pd.read_csv('partitioned_data/by_band/band_A.csv', dtype=dtypes)

df = df.loc[df['pellet_type'] == '1/2" steel']

df_mean = df.groupby(['band_type', 'pellet_type']).agg(
    mass_gn=pd.NamedAgg(column="mass_gn", aggfunc="mean"),
    calc_mass_g=pd.NamedAgg(column="calc_mass_g", aggfunc="mean"),
    velocity_mps=pd.NamedAgg(column="velocity_mps", aggfunc="mean"),
    calc_momentum=pd.NamedAgg(column="calc_momentum", aggfunc="mean"),
    calc_KE=pd.NamedAgg(column="calc_KE", aggfunc="mean"),
    calc_efficiency=pd.NamedAgg(column="calc_efficiency", aggfunc="mean"),
)
df_mean['stat'] = 'mean'
neworder = ['stat','mass_gn','calc_mass_g','velocity_mps','calc_momentum','calc_KE','calc_efficiency',]
df_mean=df_mean.reindex(columns=neworder)
# display(df_mean)

df_median = df.groupby(['band_type', 'pellet_type']).agg(
    mass_gn=pd.NamedAgg(column="mass_gn", aggfunc="median"),
    calc_mass_g=pd.NamedAgg(column="calc_mass_g", aggfunc="median"),
    velocity_mps=pd.NamedAgg(column="velocity_mps", aggfunc="median"),
    calc_momentum=pd.NamedAgg(column="calc_momentum", aggfunc="median"),
    calc_KE=pd.NamedAgg(column="calc_KE", aggfunc="median"),
    calc_efficiency=pd.NamedAgg(column="calc_efficiency", aggfunc="median"),
)
df_median['stat'] = 'median'
df_median=df_median.reindex(columns=neworder)
# display(df_median)

df_stdev = df.groupby(['band_type', 'pellet_type']).agg(
    mass_gn=pd.NamedAgg(column="mass_gn", aggfunc="std"),
    calc_mass_g=pd.NamedAgg(column="calc_mass_g", aggfunc="std"),
    velocity_mps=pd.NamedAgg(column="velocity_mps", aggfunc="std"),
    calc_momentum=pd.NamedAgg(column="calc_momentum", aggfunc="std"),
    calc_KE=pd.NamedAgg(column="calc_KE", aggfunc="std"),
    calc_efficiency=pd.NamedAgg(column="calc_efficiency", aggfunc="std"),
)
df_stdev['stat'] = 'std. dev.'
df_stdev=df_stdev.reindex(columns=neworder)
# # display(df_stdev)


frames = [df_mean, df_median, df_stdev]

df_concat = pd.concat(frames)
display(df_concat)


# display(df_stat)