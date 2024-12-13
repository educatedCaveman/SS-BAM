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

unused_cols = [
    'band_type', 'pellet_type', 'trial_num', 'calc_mass_g', 'velocity_mps', 
    'draw_length_m', 'draw_length_m', 'slack_length_m', 'draw_weight_kg', 
    'calc_draw_force_N', 'note', 'calc_momentum', 'calc_power_stroke_m', 
    'calc_PE', 'calc_KE', 
]

df_A = df.loc[df['band_type'] == 'band_A'].drop(labels=unused_cols, axis=1)
df_B = df.loc[df['band_type'] == 'band_B'].drop(labels=unused_cols, axis=1)
df_C = df.loc[df['band_type'] == 'band_C'].drop(labels=unused_cols, axis=1)
df_D = df.loc[df['band_type'] == 'band_D'].drop(labels=unused_cols, axis=1)
df_E = df.loc[df['band_type'] == 'band_E'].drop(labels=unused_cols, axis=1)
df_F = df.loc[df['band_type'] == 'band_F'].drop(labels=unused_cols, axis=1)

band_df = [df_A, df_B, df_C, df_D, df_E, df_F]
mass = []
efficiency = []

for df in band_df: 
    np_df = df.to_numpy()    
    mass.append(np_df[:, 0])
    efficiency.append(np_df[:, 1])  

# set up the plot
plt.style.use('bmh')
fig, ax = plt.subplots()
ax.set_title('Pellet Mass vs. Efficiency')

# create each of the band's plots
labels = ['Band A', 'Band B', 'Band C', 'Band D', 'Band E', 'Band F']
point_fmt = ['o', '^', 'v', '<', '>', 's']
for i in range(0, len(mass)):
    ax.scatter(mass[i], efficiency[i], label=labels[i], marker=f'{point_fmt[i]}')

# x-axis
x_max = 140
x_maj_int = 20
x_min_int = 5
ax.set_xlim([0, x_max])
plt.xticks(np.arange(0, x_max+x_min_int, x_maj_int))
plt.xticks(np.arange(0, x_max, x_min_int), minor=True)
ax.set_xlabel('Pellet Mass (grains)')

# y-axis
y_max = 1.0
y_maj_int = 0.1
y_min_int = 0.02
ax.set_ylim([0.0, y_max])
plt.yticks(np.arange(0.0, y_max+y_min_int, y_maj_int,))
plt.yticks(np.arange(0.0, y_max, y_min_int), minor=True)
ax.set_ylabel('Efficiency')

# gridlines
plt.grid(visible=True, which='major', axis='both')
plt.grid(visible=True, which='minor', axis='both', alpha=0.3)

# legend
ax.legend(loc='lower right')

# final plot
# plt.show()
plt.savefig(f'charts/mass_vs_efficiency_all.svg', format='svg')
plt.savefig(f'charts/mass_vs_efficiency_all.png', format='png')