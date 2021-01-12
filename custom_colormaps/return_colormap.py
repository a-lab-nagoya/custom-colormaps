import matplotlib as mpl
import numpy as np
import toml
from pathlib import Path


def get_colordata(name):
    """

    Load color map data from setting file.

    Parameters
    ----------
    name : str
        Colormap name. Currently, ``Dark_rainbow``, ``rainbow2``, ``sls_SAOImage``,
        ``rainbow3``, ``rainbow_SAOImage``, ``b_SAOImage``, ``spectrum_Starlink``,
        and ``Hue_sat_value2`` are supported.
    """
    color = toml.load(open(Path(__file__).parent / "colordata" / "cmapdata.toml"))
    color_numbers = color["table"][name]
    return color_numbers


def get_colormap(color_numbers, gamma=1.0, reverse=False):
    """

    Make LinearSegmentedColormap.

    Parameters
    ----------
    color_numbers : list
        Values to determin colors.

    gamma : float
        gamma corrections for the selected colormap.

    reverse : bool
        Chose if you use reversed colormap or not.
    """

    color_numbers = np.array(color_numbers)
    if reverse:
        cmap_list = color_numbers[::-1, :]
    else:
        cmap_list = color_numbers[::-1, :]

    cmap_list = np.array(cmap_list)
    cmap = mpl.colors.LinearSegmentedColormap.from_list(
        name="from_list", colors=cmap_list / 255, gamma=gamma
    )
    return cmap


if __name__ == "main":
    pass
