from IPython.display import display
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# data load
dtypes = {
    'band_type':            'string', 
    'pellet_type':          'string', 
    'trial_num':            'int', 
    'mass_gn':              'float', 
    'calc_mass_g':          'float',
    'velocity_mps':         'float',
    'draw_length_m':        'float', 
    'slack_length_m':       'float', 
    'draw_weight_kg':       'float', 
    'calc_draw_force_N':    'float', 
    'note':                 'string'
}
df = pd.read_csv('SS-BAM - data.csv', dtype=dtypes)

# add calculated fields
df['calc_momentum'] = (df['calc_mass_g'] / 1000) * df['velocity_mps']
df['calc_power_stroke_m'] = df['draw_length_m'] - df['slack_length_m']
df['calc_PE'] = 0.5 * df['calc_draw_force_N'] * df['calc_power_stroke_m']
df['calc_KE'] = 0.5 * (df['calc_mass_g'] / 1000) * df['velocity_mps']**2
df['calc_efficiency'] = df['calc_KE'] / df['calc_PE']

# save dataframe for reference
df.to_csv('data_with_calcs.csv', mode='w', index=False)

# # split the data by band type and save
df_A = df.loc[df['band_type'] == 'band_A']
df_B = df.loc[df['band_type'] == 'band_B']
df_C = df.loc[df['band_type'] == 'band_C']
df_D = df.loc[df['band_type'] == 'band_D']
df_E = df.loc[df['band_type'] == 'band_E']
df_F = df.loc[df['band_type'] == 'band_F']

df_A.to_csv('partitioned_data/by_band/band_A.csv', mode='w', index=False)
df_B.to_csv('partitioned_data/by_band/band_B.csv', mode='w', index=False)
df_C.to_csv('partitioned_data/by_band/band_C.csv', mode='w', index=False)
df_D.to_csv('partitioned_data/by_band/band_D.csv', mode='w', index=False)
df_E.to_csv('partitioned_data/by_band/band_E.csv', mode='w', index=False)
df_F.to_csv('partitioned_data/by_band/band_F.csv', mode='w', index=False)

# split the data by pellet type and save
df_12_7     = df.loc[df['pellet_type'] == '1/2" steel']
df_12       = df.loc[df['pellet_type'] == '12 mm steel']
df_11       = df.loc[df['pellet_type'] == '11 mm steel']
df_10       = df.loc[df['pellet_type'] == '10 mm steel']
df_09_525   = df.loc[df['pellet_type'] == '3/8" steel']
df_09       = df.loc[df['pellet_type'] == '9 mm steel']
df_08       = df.loc[df['pellet_type'] == '8 mm steel']
df_07       = df.loc[df['pellet_type'] == '7 mm steel']
df_06       = df.loc[df['pellet_type'] == '6 mm steel']
df_05_5     = df.loc[df['pellet_type'] == '5.5 mm steel']
df_05       = df.loc[df['pellet_type'] == '5 mm steel']
df_clay     = df.loc[df['pellet_type'] == 'clay']
df_rubber   = df.loc[df['pellet_type'] == 'rubber']

df_12_7.to_csv('partitioned_data/by_pellet/12_7_mm_steel.csv', mode='w', index=False)
df_12.to_csv('partitioned_data/by_pellet/12_mm_steel.csv', mode='w', index=False)
df_11.to_csv('partitioned_data/by_pellet/11_mm_steel.csv', mode='w', index=False)
df_10.to_csv('partitioned_data/by_pellet/10_mm_steel.csv', mode='w', index=False)
df_09_525.to_csv('partitioned_data/by_pellet/9_525_mm_steel.csv', mode='w', index=False)
df_09.to_csv('partitioned_data/by_pellet/09_mm_steel.csv', mode='w', index=False)
df_08.to_csv('partitioned_data/by_pellet/08_mm_steel.csv', mode='w', index=False)
df_07.to_csv('partitioned_data/by_pellet/07_mm_steel.csv', mode='w', index=False)
df_06.to_csv('partitioned_data/by_pellet/06_mm_steel.csv', mode='w', index=False)
df_05_5.to_csv('partitioned_data/by_pellet/05_5_mm_steel.csv', mode='w', index=False)
df_05.to_csv('partitioned_data/by_pellet/05_mm_steel.csv', mode='w', index=False)
df_clay.to_csv('partitioned_data/by_pellet/clay.csv', mode='w', index=False)
df_rubber.to_csv('partitioned_data/by_pellet/rubber.csv', mode='w', index=False)
