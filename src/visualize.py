import numpy as np
import pandas as pd
import seaborn as sns
from scipy.stats import pearsonr
import matplotlib.pyplot as plt

def corrfunc(x,y, ax=None, **kws):
    """Plot the correlation coefficient in the top right hand corner of a plot."""
    r, _ = pearsonr(x, y)
    ax = ax or plt.gca()
    ax.annotate(f'{r:.2f}', xy=(.85, .9), xycoords=ax.transAxes, fontsize=14)

def plot_scatter_grid(dataframe, kde=False, alpha=0.2, upper_color='black', diag_color='black', lower_color='viridis'):
    numeric_vars = dataframe.select_dtypes([np.number]).columns.tolist()
    grid = sns.PairGrid(data=dataframe, vars=numeric_vars)
    grid = grid.map_upper(sns.regplot, color=upper_color, scatter_kws={'alpha': alpha})
    grid = grid.map_upper(corrfunc)
    grid = grid.map_lower(sns.kdeplot, cmap=lower_color)
    grid = grid.map_diag(sns.distplot, kde=kde, color=upper_color)
    plt.tight_layout()
