from IPython.display import display
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

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
df = pd.read_csv('data_with_calcs.csv', dtype=dtypes)

np_A = df.loc[df['band_type'] == 'band_A'].to_numpy()
np_B = df.loc[df['band_type'] == 'band_B'].to_numpy()
np_C = df.loc[df['band_type'] == 'band_C'].to_numpy()
np_D = df.loc[df['band_type'] == 'band_D'].to_numpy()
np_E = df.loc[df['band_type'] == 'band_E'].to_numpy()
np_F = df.loc[df['band_type'] == 'band_F'].to_numpy()

# band A
np_A_drawforce  = np_A[:, 9]
np_A_calc_KE    = np_A[:, 14]
# band B
np_B_drawforce  = np_B[:, 9]
np_B_calc_KE    = np_B[:, 14]
# band C
np_C_drawforce  = np_C[:, 9]
np_C_calc_KE    = np_C[:, 14]
# band D
np_D_drawforce  = np_D[:, 9]
np_D_calc_KE    = np_D[:, 14]
# band E
np_E_drawforce  = np_E[:, 9]
np_E_calc_KE    = np_E[:, 14]
# band F
np_F_drawforce  = np_F[:, 9]
np_F_calc_KE    = np_F[:, 14]

fig, ax = plt.subplots()
ax.scatter(np_A_drawforce, np_A_calc_KE, label='Band A')
ax.scatter(np_B_drawforce, np_B_calc_KE, label='Band B')
ax.scatter(np_C_drawforce, np_C_calc_KE, label='Band C')
ax.scatter(np_D_drawforce, np_D_calc_KE, label='Band D')
ax.scatter(np_E_drawforce, np_E_calc_KE, label='Band E')
ax.scatter(np_F_drawforce, np_F_calc_KE, label='Band F')

ax.legend()
ax.grid(True)

plt.show()