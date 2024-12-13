import pandas as pd
import numpy as np
import scipy.stats
from slugify import slugify
from IPython.display import display

# data load
dtypes = {
    'band_type':            'string', #0
    'pellet_type':          'string', #1
    'trial_num':            'int',    #2
    'mass_gn':              'float',  #3
    'calc_mass_g':          'float',  #4
    'velocity_mps':         'float',  #5
    'draw_length_m':        'float',  #6 
    'slack_length_m':       'float',  #7
    'draw_weight_kg':       'float',  #8
    'calc_draw_force_N':    'float',  #9
    'note':                 'string', #10
    'calc_momentum':        'float',  #11
    'calc_power_stroke_m':  'float',  #12
    'calc_PE':              'float',  #13
    'calc_KE':              'float',  #14
    'calc_efficiency':      'float',  #15
}
df = pd.read_csv('data/data_with_calcs.csv', dtype=dtypes)
unused_cols = [
    'trial_num', 'draw_length_m', 'slack_length_m', 'draw_weight_kg', 
    'calc_draw_force_N', 'note', 'calc_power_stroke_m', 'calc_PE'
]
df.drop(labels=unused_cols, axis='columns', inplace=True)

# Mean
df_mean = df.groupby(['band_type', 'pellet_type']).agg(func="mean").round(3)
df_mean['sort_key'] = '0'
df_mean['stat'] = 'Mean'

# Median
df_median = df.groupby(['band_type', 'pellet_type']).agg(func="median").round(3)
df_median['sort_key'] = '1'
df_median['stat'] = 'Median'

# Standard Deviation
df_std = df.groupby(['band_type', 'pellet_type']).agg(func=np.std, ddof=1).round(3)
df_std['sort_key'] = '2'
df_std['stat'] = 'Std. Dev.'

def conf_interval(data, confidence=0.95, mean_round=3, tail_round=3):
    a = 1.0 * np.array(data)
    n = len(a)
    m, se = np.mean(a), scipy.stats.sem(a)
    h = se * scipy.stats.t.ppf((1 + confidence) / 2., n-1)
    return str(f"{round(m, mean_round)} ±{round(h, tail_round)}")

df_ci_95 = df.groupby(['band_type', 'pellet_type']).agg(
    mass_gn=pd.NamedAgg(column='mass_gn', aggfunc=lambda x: conf_interval(x, 0.95)),
    calc_mass_g=pd.NamedAgg(column='calc_mass_g', aggfunc=lambda x: conf_interval(x, 0.95)),
    velocity_mps=pd.NamedAgg(column='velocity_mps', aggfunc=lambda x: conf_interval(x, 0.95)),
    calc_momentum=pd.NamedAgg(column='calc_momentum', aggfunc=lambda x: conf_interval(x, 0.95)),
    calc_KE=pd.NamedAgg(column='calc_KE', aggfunc=lambda x: conf_interval(x, 0.95)),
    calc_efficiency=pd.NamedAgg(column='calc_efficiency', aggfunc=lambda x: conf_interval(x, 0.95)),
)
df_ci_95['sort_key'] = '3'
df_ci_95['stat'] = '95% C.I.'

df_ci_99 = df.groupby(['band_type', 'pellet_type']).agg(
    mass_gn=pd.NamedAgg(column='mass_gn', aggfunc=lambda x: conf_interval(x, 0.99)),
    calc_mass_g=pd.NamedAgg(column='calc_mass_g', aggfunc=lambda x: conf_interval(x, 0.99)),
    velocity_mps=pd.NamedAgg(column='velocity_mps', aggfunc=lambda x: conf_interval(x, 0.99)),
    calc_momentum=pd.NamedAgg(column='calc_momentum', aggfunc=lambda x: conf_interval(x, 0.99)),
    calc_KE=pd.NamedAgg(column='calc_KE', aggfunc=lambda x: conf_interval(x, 0.99)),
    calc_efficiency=pd.NamedAgg(column='calc_efficiency', aggfunc=lambda x: conf_interval(x, 0.99)),
)
df_ci_99['sort_key'] = '4'
df_ci_99['stat'] = '99% C.I.'

df_final = pd.concat([df_mean, df_median, df_std, df_ci_95, df_ci_99])
df_final.sort_index(axis='index', inplace=True)

band_names = df[['band_type']].drop_duplicates().to_numpy().flatten()
pellet_types = df[['pellet_type']].drop_duplicates().to_numpy().flatten()

# prepare for final output
# re-order the columns
col_order = [
    'stat', 'mass_gn', 'calc_mass_g', 'velocity_mps', 'calc_momentum', 
    'calc_KE', 'calc_efficiency', 
]
df_final = df_final.reindex(columns=col_order)

# create the tables
for i, band_name in enumerate(band_names):
    for j, pellet_type in enumerate(pellet_types):
        tmp_df = df_final.query(f"band_type == '{band_name}' and pellet_type == '{pellet_type}'")
        
        # print(f'{band_name}, {pellet_type}: {tmp_df.shape}')
        
        # don't create empty tables:
        if tmp_df.shape[0] == 0:
            print(f'skipping {band_name}, {pellet_type}')
        else:            
            col_map = {
                'stat':             'Statistic',
                'mass_gn':          'Mass (grains)',
                'calc_mass_g':      'Mass (g)',
                'velocity_mps':     'Velocity (m/s)',
                'calc_momentum':    'Momentum (kg⋅m/s)',
                'calc_KE':          'Kinetic Energy (J)',
                'calc_efficiency':  'Efficiency',
            }
            tmp_df = tmp_df.rename(columns=col_map)
            
            # massage the file names
            base_name = f"{band_name}_{pellet_type}_stats"
            base_name = base_name.replace('1/2"', '½ inch')
            base_name = base_name.replace('3/8"', '⅜ inch')
            base_name = base_name.replace(' ', '_')
            table_name = slugify(base_name)
            # print(table_name)
            table_md = tmp_df.to_markdown(buf=f"tables/{table_name}.md", index=False)
