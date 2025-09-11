import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def ts_scatterplot(dat, dim1_, dim2_, **kwargs):
    """Making a scatterplot of a dataset.
       Args:
           dat: a numpy ndarray of shape (n_ts, n_dim) or (n_ts, length_ts)
           dim1_ and dim2_: int, the dimension id."""
    plt.plot(dat[:, dim1_], dat[:, dim2_], 'o', color='#365d8d', alpha=0.6, **kwargs)
    plt.xlabel(f'Dimension {dim1_}')
    plt.ylabel(f'Dimension {dim2_}')
    plt.show()


def plot_dataset_in_clusters(data, labels, palette='viridis', sharey_=True, **kwargs):
    """Plot the clustered dataset"""
    n_clusters = len(np.unique(labels))
    cmap = plt.get_cmap(palette)
    colors = [cmap(i) for i in np.linspace(0, 1, n_clusters)]

    _, axs = plt.subplots(ncols=1, nrows=n_clusters,
                          sharex=True, sharey=sharey_,
                          tight_layout=True, **kwargs)
    for i, ax in zip(np.unique(labels), axs.flat):
        group = data[labels==i]
        for j in range(len(group)):
            ax.plot(group[j], color=colors[i], alpha=0.5)
            ax.set_title(f"Cluster {i}")

    plt.show()
