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
df_A = pd.read_csv('partitioned_data/by_band/band_A.csv', dtype=dtypes)

df_12_7 = df_A.loc[df_A['pellet_type'] == '1/2" steel']
# display(df_12_7)

df_test = pd.DataFrame(df_12_7, columns=['velocity_mps'])
# display(df_test)

np_mps = df_test.transpose().to_numpy()[0]

print(np_mps)
print(type(np_mps))


fig, ax = plt.subplots()
ax.boxplot(np_mps)
ax.set_ylim([0, 60])
plt.show()