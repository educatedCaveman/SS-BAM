"""
this creates plots for my slingshot experiment
"""

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
# from IPython.display import display

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

# efficiency x velocity: this might be garbage
input_df['vel_adj'] = input_df['velocity_mps'] * input_df['calc_efficiency']

# split into different bands
df_A = input_df.loc[input_df['band_type'] == 'band_A']
df_B = input_df.loc[input_df['band_type'] == 'band_B']
df_C = input_df.loc[input_df['band_type'] == 'band_C']
df_D = input_df.loc[input_df['band_type'] == 'band_D']
df_E = input_df.loc[input_df['band_type'] == 'band_E']
df_F = input_df.loc[input_df['band_type'] == 'band_F']

# aggregate the dataframes and collect the data into a plottable form
band_df = [df_A, df_B, df_C, df_D, df_E, df_F]
band_names = ['Band A', 'Band B', 'Band C', 'Band D', 'Band E', 'Band F']

# for i in range(0, len(band_df)):
for i, df in enumerate(band_df):
    df_med = df.groupby('pellet_type').agg(
        mass=pd.NamedAgg(column='mass_gn', aggfunc="median"),
        efficiency=pd.NamedAgg(column='calc_efficiency', aggfunc="median"),
        velocity=pd.NamedAgg(column='velocity_mps', aggfunc="median"),
        vel_adj=pd.NamedAgg(column='vel_adj', aggfunc="median"),
    )
    df_med.sort_values(by='mass', inplace=True)
    np_med = df_med.to_numpy()
    mass = np_med[:, 0]
    efficiency = np_med[:, 1]
    velocity = np_med[:, 2]
    vel_adj = np_med[:, 3]

    # set up the plot
    plt.style.use('bmh')
    fig, ax1 = plt.subplots()
    ax2 = ax1.twinx()
    ax1.set_title(f'{band_names[i]} - Adjusted Velocity')

    ax1.plot(mass, efficiency, 'o:', label='Efficiency', color='red')
    ax2.plot(mass, velocity, '^:', label='Velocity', color='green')
    ax2.plot(mass, vel_adj, 'v:', label='Velocity, adjusted', color='blue')

    # x-axis
    X_MAX = 140
    X_MAJ_INT = 20
    X_MIN_INT = 5
    ax1.set_xlim([0, X_MAX])
    plt.xticks(np.arange(0, X_MAX+X_MIN_INT, X_MAJ_INT))
    plt.xticks(np.arange(0, X_MAX, X_MIN_INT), minor=True)
    ax1.set_xlabel('Pellet Mass (grains)')

    # y1-axis
    Y1_MAX = 1.0
    Y1_MAJ_INT = 0.1
    Y1_MIN_INT = 0.02
    ax1.set_ylim([0.0, Y1_MAX])
    plt.yticks(np.arange(0.0, Y1_MAX + Y1_MIN_INT, Y1_MAJ_INT,))
    plt.yticks(np.arange(0.0, Y1_MAX, Y1_MIN_INT), minor=True)
    ax1.set_ylabel('Efficiency')

    # y2-axis
    Y2_MAJ_INT = 10
    Y2_MAX = int((int(np.max(velocity) / 10) + 1) * 10)
    Y2_MIN_INT = 1
    ax2.set_ylim([0.0, Y2_MAX])
    plt.yticks(np.arange(0.0, Y2_MAX + Y2_MIN_INT, Y2_MAJ_INT,))
    plt.yticks(np.arange(0.0, Y2_MAX, Y2_MIN_INT), minor=True)
    ax2.set_ylabel('Velocity (m/s)')

    # gridlines
    plt.grid(visible=False)

    # legend
    lines1, labels1 = ax1.get_legend_handles_labels()
    lines2, labels2 = ax2.get_legend_handles_labels()
    ax2.legend(lines1 + lines2, labels1 + labels2, loc='lower right')

    # final plot
    # plt.show()
    plt.savefig(f'charts/{band_names[i]}_adjusted_velocity_efficiency.svg', format='svg')
    plt.savefig(f'charts/{band_names[i]}_adjusted_velocity_efficiency.png', format='png')
    # ax1.clear()
    # ax2.clear()
