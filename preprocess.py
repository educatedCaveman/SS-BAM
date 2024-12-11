from IPython.display import display
from unitpy import U, Q , Unit, Quantity
import pandas as pd

# unit conversions
# grains to kg
grains = 1.0 * U("grain")
gn_to_kg = grains.to('kg').value

# kg to N
# equates kg with kg-force


# data load
dtypes = {
    'band_type':        'string', 
    'pellet_type':      'string', 
    'trial_num':        'int', 
    'mass_gn':          'float', 
    'velocity_mps':     'float',
    'draw_length_m':    'float', 
    'slack_length_m':   'float', 
    'draw_weight_kg':   'float', 
    'note':             'string'
}
df = pd.read_csv('SS-BAM - data.csv', dtype=dtypes)
df['calc_mass_kg'] = df['mass_gn'] * gn_to_kg

display(df)
# print(df.columns)

# df1 = df['note']

# display(df1)