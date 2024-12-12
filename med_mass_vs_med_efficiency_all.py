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
input_df = pd.read_csv('data_with_calcs.csv', dtype=dtypes)
# display(input_df)

# split into different bands
df_A = input_df.loc[input_df['band_type'] == 'band_A']
df_B = input_df.loc[input_df['band_type'] == 'band_B']
df_C = input_df.loc[input_df['band_type'] == 'band_C']
df_D = input_df.loc[input_df['band_type'] == 'band_D']
df_E = input_df.loc[input_df['band_type'] == 'band_E']
df_F = input_df.loc[input_df['band_type'] == 'band_F']

# aggregate the dataframes and collect the data into a plottable form
band_df = [df_A, df_B, df_C, df_D, df_E, df_F]
mass_med = []
efficiency_med = []

for df in band_df:
    df_med = df.groupby('pellet_type').agg(
        mass_gn=pd.NamedAgg(column='mass_gn', aggfunc="median"),
        calc_efficiency=pd.NamedAgg(column='calc_efficiency', aggfunc="median"),
    )    
    df_med.sort_values(by='mass_gn', inplace=True)    
    np_med = df_med.to_numpy()
    mass_med.append(np_med[:, 0])
    efficiency_med.append(np_med[:, 1])       

# set up the plot
plt.style.use('bmh')
fig, ax = plt.subplots()
ax.set_title('Median Pellet Mass vs. Median Efficiency')

# create each of the band's plots
labels = ['Band A', 'Band B', 'Band C', 'Band D', 'Band E', 'Band F']
point_fmt = ['o', '^', 'v', '<', '>', 's']
for i in range(0, len(mass_med)):
    ax.plot(mass_med[i], efficiency_med[i], f'{point_fmt[i]}:', label=labels[i])

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
ax.set_ylabel('Velocity (m/s)')

# gridlines
plt.grid(visible=True, which='major', axis='both')
plt.grid(visible=True, which='minor', axis='both', alpha=0.3)

# legend
ax.legend(loc='lower right')

# final plot
# plt.show()
plt.savefig('median_mass_vs_efficiency.svg', format='svg')