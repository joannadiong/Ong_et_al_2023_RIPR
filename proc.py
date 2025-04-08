import os
import pandas as pd
import matplotlib
import matplotlib.pyplot as plt

matplotlib.rcParams.update({'font.size': 7})
# matplotlib.rcParams.update({'font.size': 10}) # SVG: Figs 1, 3 in font 10, Fig 2 in font 7

path_proc = os.path.join('.', 'data', 'proc')

# function to plot stacked barplots
def plot_fig(df: pd.DataFrame, xlabels: list, legend_handles: list, colors: dict, figname: str):
    """Plot Pandas stacked bar plots showing breakdown """
    ax = df.apply(lambda count: count.value_counts(normalize=True)).transpose().\
        plot(kind='bar', color=colors, alpha=1, stacked=True, rot=0) # colormap='RdYlGn'
    plt.legend(handles=legend_handles, bbox_to_anchor=(1.05, 1))

    ax.set_xticklabels(xlabels)
    ax.set_yticklabels(['0', '20', '40', '60', '80', '100'])
    plt.ylabel('Percentage (%)')
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)

    plt.tight_layout()
    # file = os.path.join(path_proc, figname + '.png')
    file = os.path.join(path_proc, figname + '.svg')
    plt.savefig(file, dpi=300)
    plt.close()

# function to plot clustered stacked barplots
def plot_clustered_fig(df: pd.DataFrame, go8: pd.Series, xlabels: list, legend_handles: list, colors: dict, figname: str):
    """Plot Pandas stacked bar plots showing breakdown """
    vars = df.columns.values
    df = pd.concat([df, go8], axis=1)

    ax = df[vars][df['go8'] == 0].apply(lambda count: count.value_counts()).transpose().\
        plot(kind='bar', position=1.1, width=0.2, color=colors, alpha=1, stacked=True, rot=0)
    df[vars][df['go8'] == 1].apply(lambda count: count.value_counts()).transpose().\
        plot(ax=ax, kind='bar', position=-0.1, width=0.2, color=colors, alpha=1, stacked=True, rot=0)
    plt.legend(handles=legend_handles, bbox_to_anchor=(1.05, 1))

    ax.set_xticklabels(xlabels)
    # ax.set_yticklabels(['0', '5', '10', '15', '20'])
    plt.ylabel('No. of codes')
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)

    plt.tight_layout()
    # file = os.path.join(path_proc + '/go8', figname + '.png')
    file = os.path.join(path_proc + '/go8', figname + '.svg')
    plt.savefig(file, dpi=300)
    plt.close()