import pandas as pd
import matplotlib.pyplot as plt
from IPython import display
plt.rcParams.update({'font.size': 42})
df = pd.read_csv("../scratch_dataset/metadata.csv")
primary_key='p_ID'
columns=['total-views', 'total-remixes', 'total-favorites', 'total-loves', 'is-remix', 'Remixed-from', 'Abstraction', 'Parallelism', 'Logic', 'Synchronization', 'FlowControl', 'UserInteractivity', 'DataRepresentation', 'Mastery', 'Clones', 'CustomBlocks', 'InstancesSprites']
count=1
for col in columns:
    df_grouped = df.groupby([primary_key]).sum().sort_values(col, ascending=False).head(10)
    df_col = df_grouped[col]
    fig = df_col.plot(kind='bar', xlabel=primary_key, ylabel=col, title=col + " vs " + primary_key, figsize=(20, 20), fontsize=18).get_figure()
    fig.savefig('trial1/images/vis' + str(count) + '.png')
    count+=1
    plt.close()