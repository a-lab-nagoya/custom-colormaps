import matplotlib as mpl
import numpy as np
import toml


def get_colordata(name="Dark_rainbow"):
    color = toml.load(open("../colordata/cmapdata.toml"))
    color_numbers = color["Table"][name]
    return color_numbers


def get_colormap(color_numbers, gamma=1.0, reverse=False):
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
