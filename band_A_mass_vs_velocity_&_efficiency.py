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
# band_df = [df_A, df_B, df_C, df_D, df_E, df_F]
band_df = [df_A, df_B]
band_names = ['Band A', 'Band B', 'Band C', 'Band D', 'Band E', 'Band F']

for i in range(0, len(band_df)):
    df_med = band_df[i].groupby('pellet_type').agg(
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
    ax1.set_title(f'{band_names[i]} - Pellet Mass vs. Efficiency & Velocity')

    ax1.plot(mass, efficiency, f'o:', label='Efficiency', color='red')
    ax2.plot(mass, velocity, f'^:', label='Velocity', color='green')
    ax2.plot(mass, vel_adj, f'v:', label='Velocity, adjusted', color='blue')

    # x-axis
    x_max = 140
    x_maj_int = 20
    x_min_int = 5
    ax1.set_xlim([0, x_max])
    plt.xticks(np.arange(0, x_max+x_min_int, x_maj_int))
    plt.xticks(np.arange(0, x_max, x_min_int), minor=True)
    ax1.set_xlabel('Pellet Mass (grains)')

    # y1-axis
    y1_max = 1.0
    y1_maj_int = 0.1
    y1_min_int = 0.02
    ax1.set_ylim([0.0, y1_max])
    plt.yticks(np.arange(0.0, y1_max + y1_min_int, y1_maj_int,))
    plt.yticks(np.arange(0.0, y1_max, y1_min_int), minor=True)
    ax1.set_ylabel('Efficiency')

    # y2-axis
    y2_maj_int = 10
    y2_max = int(int(np.max(velocity) / 10) * 10)
    y2_min_int = 1
    ax2.set_ylim([0.0, y2_max])
    plt.yticks(np.arange(0.0, y2_max + y2_min_int, y2_maj_int,))
    plt.yticks(np.arange(0.0, y2_max, y2_min_int), minor=True)    
    ax2.set_ylabel('Velocity (m/s)')

    # gridlines
    # plt.grid(visible=True, which='major', axis='both')
    # plt.grid(visible=True, which='minor', axis='both', alpha=0.3)
    plt.grid(visible=False)

    # legend
    lines1, labels1 = ax1.get_legend_handles_labels()
    lines2, labels2 = ax2.get_legend_handles_labels()
    ax2.legend(lines1 + lines2, labels1 + labels2, loc='lower right')

    # final plot
    plt.show()
    # ax1.clear()
    # ax2.clear()
    # plt.savefig('median_mass_vs_efficiency.svg', format='svg')
    # plt.savefig('median_mass_vs_efficiency.png', format='png')