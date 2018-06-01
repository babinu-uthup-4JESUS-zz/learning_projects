##########################################
# Compilations of helper plotter functions
#########################################
import numpy as np
import matplotlib.pyplot as plt

# Generic method of adding a text box to a figure.
def log_relevant_metrics_text_box_top_right(data_pd_series, plot_obj):
    """Add a textbox with relevant details to a given plot (though we do not use this now)

    Usage::

        >>> import pandas as pd
        >>> import matplotlib.pyplot as plt
        >>> # Code for getting data to pandas dataframe df
        >>> # Code for plotting data present in dataframe df (to a relevant plot_obj)
        >>> log_relevant_metrics_text_box_top_right(df['column name', plot_obj) (a series object and a plot object)

    :param data_pd_series: A pandas Series object
    :param plot_obj: A matplotlib plot object
    """

    mu = data_pd_series.mean()
    median = data_pd_series.median()
    sigma = data_pd_series.std()
    max_val = data_pd_series.max()
    min_val = data_pd_series.min()
    textstr = \
        '$\mu=%.2f$\n$\mathrm{median}=%.2f$\n$\sigma=%.2f$\n$\max=%.2f$\n$\min=%.2f$' % \
        (mu, median, sigma, max_val, min_val)


    # these are matplotlib.patch.Patch properties
    props = dict(boxstyle='round', facecolor='wheat', alpha=0.5)

    # place a text box in upper left in axes coords
    plot_obj.text(0.85, 0.95, textstr, transform=plot_obj.transAxes, fontsize=14,
            verticalalignment='top', bbox=props)

# Generic method of plotting a dataframe.
def plot_rel_data_v2(multiple_states_data, 
                     x_label, 
                     y_label, 
                     title_str, 
                     x_tick=1, 
                     y_tick=0.2, 
                     fig_length=16,
                     fig_breadth=9,
                     x_label_font_size=18,
                     y_label_font_size=16):
    """Plots relevant data from the given dataframe.

    Usage::

        >>> import pandas as pd
        >>> import matplotlib.pyplot as plt
        >>> # Code for getting data to pandas dataframe df
        >>> plot_rel_data(df, column1, column2, title_name)

    :param multiple_states_data: Given pandas dataframe
    :param x_label: Label to be printed on X axis
    :param y_label: Label to be printed on Y axis    
    :param title_str: Title of the resultant graph
    :param x_tick: Minimum increment on x-values
    :param y_tick: Minimum increment on y-values
    :param fig_length: Length of output figure.
    :param fig_breadth: Breadth of output figure.
    :param x_label_font_size: Size of label on X axis.
    :param y_label_font_size: Size of label on Y axis.    
    """
    fig, ax = plt.subplots(1,1,figsize=(fig_length, fig_breadth)) 
    multiple_states_data.plot(ax=ax)
    ax.xaxis.label.set_size(x_label_font_size)
    ax.yaxis.label.set_size(y_label_font_size)
    ax.set(xlabel=x_label, ylabel=y_label)
    ax.set_title(title_str)
    ax.set_xticks(np.arange(multiple_states_data.index.min(), multiple_states_data.index.max(), x_tick))
    ax.set_yticks(np.arange(multiple_states_data.min().min(), multiple_states_data.max().max(), y_tick))
    print(multiple_states_data.describe())
    return ax


