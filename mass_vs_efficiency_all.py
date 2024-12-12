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
np_A_mass_gn            = np_A[:, 3]
np_A_velocity           = np_A[:, 5]
np_A_draw_weight        = np_A[:, 9]
np_A_draw_force         = np_A[:, 10]
np_A_calc_momentum      = np_A[:, 11]
np_A_calc_PE            = np_A[:, 13]
np_A_calc_KE            = np_A[:, 14]
np_A_calc_efficiency    = np_A[:, 15]

# band B
np_B_mass_gn            = np_B[:, 3]
np_B_velocity           = np_B[:, 5]
np_B_draw_weight        = np_B[:, 9]
np_B_draw_force         = np_B[:, 10]
np_B_calc_momentum      = np_B[:, 11]
np_B_calc_PE            = np_B[:, 13]
np_B_calc_KE            = np_B[:, 14]
np_B_calc_efficiency    = np_B[:, 15]

# band C
np_C_mass_gn            = np_C[:, 3]
np_C_velocity           = np_C[:, 5]
np_C_draw_weight        = np_C[:, 9]
np_C_draw_force         = np_C[:, 10]
np_C_calc_momentum      = np_C[:, 11]
np_C_calc_PE            = np_C[:, 13]
np_C_calc_KE            = np_C[:, 14]
np_C_calc_efficiency    = np_C[:, 15]

# band D
np_D_mass_gn            = np_D[:, 3]
np_D_velocity           = np_D[:, 5]
np_D_draw_weight        = np_D[:, 9]
np_D_draw_force         = np_D[:, 10]
np_D_calc_momentum      = np_D[:, 11]
np_D_calc_PE            = np_D[:, 13]
np_D_calc_KE            = np_D[:, 14]
np_D_calc_efficiency    = np_D[:, 15]

# band E
np_E_mass_gn            = np_E[:, 3]
np_E_velocity           = np_E[:, 5]
np_E_draw_weight        = np_E[:, 9]
np_E_draw_force         = np_E[:, 10]
np_E_calc_momentum      = np_E[:, 11]
np_E_calc_PE            = np_E[:, 13]
np_E_calc_KE            = np_E[:, 14]
np_E_calc_efficiency    = np_E[:, 15]

# band F
np_F_mass_gn            = np_F[:, 3]
np_F_velocity           = np_F[:, 5]
np_F_draw_weight        = np_F[:, 9]
np_F_draw_force         = np_F[:, 10]
np_F_calc_momentum      = np_F[:, 11]
np_F_calc_PE            = np_F[:, 13]
np_F_calc_KE            = np_F[:, 14]
np_F_calc_efficiency    = np_F[:, 15]


fig, ax = plt.subplots()
ax.scatter(np_A_mass_gn, np_A_calc_efficiency, label='Band A')
ax.scatter(np_B_mass_gn, np_B_calc_efficiency, label='Band B')
ax.scatter(np_C_mass_gn, np_C_calc_efficiency, label='Band C')
ax.scatter(np_D_mass_gn, np_D_calc_efficiency, label='Band D')
ax.scatter(np_E_mass_gn, np_E_calc_efficiency, label='Band E')
ax.scatter(np_F_mass_gn, np_F_calc_efficiency, label='Band F')

ax.legend()
ax.grid(True)

plt.show()