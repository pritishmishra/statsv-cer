import os
import glob
import pandas as pd
original_dataset_path = '../scratch_dataset/'
target_dataset_path = '../scratch-dataset-notebook/'
extension = 'csv'
row_limit=100000

os.chdir(original_dataset_path)
csv_files = glob.glob('*.{}'.format(extension))
#print(csv_files)

for csv_file in csv_files:
    df = pd.read_csv(original_dataset_path + csv_file, error_bad_lines=False, warn_bad_lines=False, nrows=row_limit)
    #print(df.shape)
    df.to_csv(target_dataset_path + csv_file, index=False)