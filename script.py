import os
import pandas as pd
import matplotlib.patches as mpatches

from proc import plot_fig, plot_clustered_fig

# ----------------------------------------
# Import data
# ----------------------------------------
project_path = '.'
os.chdir(project_path)
path_raw = os.path.join('.', 'data', 'raw')
path_proc = os.path.join('.', 'data', 'proc')
file_name = 'Codesofconductreview_DATA_2021-08-26_0940.csv'
file_labels = 'Codesofconductreview_DATA_LABELS_2021-03-08_1401.csv'

file = os.path.join(path_raw, file_name)
df = pd.read_csv(file)

labels = os.path.join(path_raw, file_labels)
df_labs = pd.read_csv(labels, nrows=0)

# ----------------------------------------
# Clean data
# ----------------------------------------
universities = list(df.university.values)
universities = [uni.strip() for uni in universities]

outcomes_all = list(df.columns[2:])
outcome_labels = list(df_labs.columns[2:])
comments = ['university',
            'def_res_integrity_text',
            'def_res_quality_text',
            'def_res_misconduct_text',
            'comment_definitions',
            'comment_ethics',
            'comment_protocol_rct',
            'comment_protocol_other',
            'comment_protocol_analy',
            'comment_open_data',
            'comment_open_code',
            'comment_open_publish',
            'comment_report_guide',
            'comment_coi',
            'comment_training',
            'comment_misbehaviours',
            'codes_of_conduct_review_final_complete']

# get numeric outcomes scores, separate into df's with different scoring
num_outcomes, num_outcome_labels = [], []
for outcome, label in zip(outcomes_all, outcome_labels):
    if outcome not in comments:
        num_outcomes.append(outcome)
        num_outcome_labels.append(label)

df_num = df[num_outcomes]
df_def = df_num.iloc[:, 1:4] # scores: no, default, specific
df_eth = df_num.iloc[:, 4:6] # scores: no, yes
df_out = df_num.iloc[:, 6:] # scores: no, default, advised, required

labels2 = {0: 'no', 1: 'yes'}
labels3 = {0: 'no', 1: 'default', 2: 'specific'}
labels4 = {0: 'no', 1: 'default', 2: 'advised', 3: 'required'}

df_num['ethics_human'].apply(lambda label: labels2[label])

"""
# get median (IQR) of scores binarised to No = 0, Default/Advised/Required = 1
df_ = pd.concat([df_def, df_eth, df_out], axis=1)
df_.to_csv(os.path.join(path_proc, 'data_R2_init.csv'))

vars = list(df_.columns)
vars.remove('funding_open_access')
for var in vars:
    df_.loc[df_[var] != 0, var] = 1
df_.to_csv(os.path.join(path_proc, 'data_R2_v1.csv'))  # median (IQR) is calculated manually in Excel file
"""

# ----------------------------------------
# Analyse
# ----------------------------------------
file = os.path.join(path_proc, 'results.txt')
open(file, 'w').close()
outfile = open(file, 'w')
with open(file, 'a') as file:
    for outcome, label in zip(num_outcomes, num_outcome_labels):
        file.write('\n[{}]: {}'.format(outcome, label[:80]))

    file.write('\n\n\nDEFINITIONS')
    qstart = 1
    for outcome, label in zip(list(df_def.columns), num_outcome_labels[1:4]):
        file.write('\n\nQ{}. Does the code define {}\n'.format(qstart, label))
        file.write('\nNon-Group of Eight\n')
        file.write(df_num[df['go8'] == 0][outcome].apply(lambda label: labels3[label]).value_counts().sort_index().to_string())
        file.write('\n\n')
        file.write(df_num[df['go8'] == 0][outcome].apply(lambda label: labels3[label]).value_counts(normalize=True).mul(100).round(1).sort_index().to_string())
        file.write('\n\nGroup of Eight\n')
        file.write(df_num[df['go8'] == 1][outcome].apply(lambda label: labels3[label]).value_counts().sort_index().to_string())
        file.write('\n\n')
        file.write(df_num[df['go8'] == 1][outcome].apply(lambda label: labels3[label]).value_counts(normalize=True).mul(100).round(1).sort_index().to_string())
        qstart += 1

    file.write('\n\n\nETHICS')
    for outcome, label in zip(list(df_eth.columns), num_outcome_labels[4:6]):
        file.write('\n\nQ{}. Does the code state that {}\n'.format(qstart, label))
        file.write('\nNon-Group of Eight\n')
        file.write(df_num[df['go8'] == 0][outcome].apply(lambda label: labels2[label]).value_counts().sort_index().to_string())
        file.write('\n\n')
        file.write(df_num[df['go8'] == 0][outcome].apply(lambda label: labels2[label]).value_counts(normalize=True).mul(100).round(1).sort_index().to_string())
        file.write('\n\nGroup of Eight\n')
        file.write(df_num[df['go8'] == 1][outcome].apply(lambda label: labels2[label]).value_counts().sort_index().to_string())
        file.write('\n\n')
        file.write(df_num[df['go8'] == 1][outcome].apply(lambda label: labels2[label]).value_counts(normalize=True).mul(100).round(1).sort_index().to_string())
        qstart += 1

    file.write('\n\n\nRESPONSIBLE PRACTICES AND MISBEHAVIOURS')
    for outcome, label in zip(list(df_out.columns), num_outcome_labels[6:]):
        if outcome not in ['fabricate_data', 'select_data', 'select_results', 'p_hacking', 'harking']:
            if label != 'Is there University funding to support open access publication?':
                file.write('\n\nQ{}. Does the code state that {}\n'.format(qstart, label))
                file.write('\nNon-Group of Eight\n')
                qstart += 1
        else:
            file.write('\n\nQ{}. Does the code state that {} should be discouraged\n'.format(qstart, label))
            file.write('\nNon-Group of Eight\n')
            qstart += 1

        if label != 'Is there University funding to support open access publication?':
            file.write(df_num[df['go8'] == 0][outcome].dropna().apply(lambda label: labels4[label]).value_counts().sort_index().to_string())
            file.write('\n\n')
            file.write(df_num[df['go8'] == 0][outcome].dropna().apply(lambda label: labels4[label]).value_counts(normalize=True).mul(100).round(1).sort_index().to_string())
            file.write('\n\nGroup of Eight\n')
            file.write(df_num[df['go8'] == 1][outcome].dropna().apply(lambda label: labels4[label]).value_counts().sort_index().to_string())
            file.write('\n\n')
            file.write(df_num[df['go8'] == 1][outcome].dropna().apply(lambda label: labels4[label]).value_counts(normalize=True).mul(100).round(1).sort_index().to_string())

# ----------------------------------------
# Graph
# ----------------------------------------
# colors2 = {0: 'red', 1: 'green'}
# colors3 = {0: 'red', 1: 'orange', 2: 'green'}
# colors4 = {0: 'red', 1: 'orange', 2: 'gold', 3: 'green'}
#
# patch_r = mpatches.Patch(color='red', label='No')
# patch_o = mpatches.Patch(color='orange', label='Default')
# patch_y = mpatches.Patch(color='gold', label='Advised')
# patch_g_y = mpatches.Patch(color='green', label='Yes')
# patch_g_s = mpatches.Patch(color='green', label='Specific')
# patch_g_r = mpatches.Patch(color='green', label='Required')

colors2 = {0: '#e41a1c', 1: '#4daf4a'}
colors3 = {0: '#e41a1c', 1: '#ff7f00', 2: '#4daf4a'}
colors4 = {0: '#e41a1c', 1: '#ff7f00', 2: '#dede00', 3: '#4daf4a'}

patch_r = mpatches.Patch(color='#e41a1c', label='No')
patch_o = mpatches.Patch(color='#ff7f00', label='Default')
patch_y = mpatches.Patch(color='#dede00', label='Advised')
patch_g_y = mpatches.Patch(color='#4daf4a', label='Yes')
patch_g_s = mpatches.Patch(color='#4daf4a', label='Specific')
patch_g_r = mpatches.Patch(color='#4daf4a', label='Required')

plot_fig(df_def,
         ['Research\nintegrity', 'Research\nquality', 'Research\nmisconduct'],
         [patch_r, patch_o, patch_g_s],
         colors3,
         'definitions')

plot_fig(df_eth,
         ['Human', 'Animal'],
         [patch_r, patch_g_y],
         colors2,
         'ethics')

plot_fig(df_out.loc[:, list(df_out.columns[:6]) + list(df_out.columns[7:10])],
         ['Register\ntrial\nprotocol', 'Register\nother\nprotocol', 'Register\nanalysis\nprotocol', 'Open\ndata',
          'Open\ncode', 'Open\npublishing', 'Reporting\nguidelines', 'Conflicts\nof\ninterest',
          'Researcher\ntraining'],
         [patch_r, patch_o, patch_y, patch_g_r],
         colors4,
         'outcomes')

plot_fig(df_out.iloc[:, 10:],
         ['Fabricate\ndata', 'Select\ndata', 'Select\nresults', 'P-hacking', 'Harking'],
         [patch_r, patch_o, patch_y, patch_g_r],
         colors4,
         'misbehaviours')

# ----------------------------------------
# Graph: by Group of Eight
# ----------------------------------------

plot_clustered_fig(df_def,
                   df['go8'],
                   ['Research\nintegrity', 'Research\nquality', 'Research\nmisconduct'],
                   [patch_r, patch_o, patch_g_s],
                   colors3,
                   'definitions_')

plot_clustered_fig(df_eth,
                   df['go8'],
                   ['Human', 'Animal'],
                   [patch_r, patch_g_y],
                   colors2,
                   'ethics_')

plot_clustered_fig(df_out.loc[:, list(df_out.columns[:6]) + list(df_out.columns[7:10])],
                   df['go8'],
                   ['Register\ntrial\nprotocol', 'Register\nother\nprotocol', 'Register\nanalysis\nprotocol', 'Open\ndata',
                    'Open\ncode', 'Open\npublishing', 'Reporting\nguidelines', 'Conflicts\nof\ninterest',
                    'Researcher\ntraining'],
                   [patch_r, patch_o, patch_y, patch_g_r],
                   colors4,
                   'outcomes_')

plot_clustered_fig(df_out.iloc[:, 10:],
                   df['go8'],
                   ['Fabricate\ndata', 'Select\ndata', 'Select\nresults', 'P-hacking', 'Harking'],
                   [patch_r, patch_o, patch_y, patch_g_r],
                   colors4,
                   'misbehaviours_')