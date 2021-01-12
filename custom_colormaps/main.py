from . import return_colormap


def main(name="Dark_rainbow", gamma=1.0, reverse=False):

    """
    Highest interface of the custom-colormap

    Parameters
    ----------
    name : str
        Colormap name. Currently, ``Dark_rainbow``, ``rainbow2``, ``sls_SAOImage``,
        ``rainbow3``, ``rainbow_SAOImage``, ``b_SAOImage``, ``spectrum_Starlink``,
        and ``Hue_sat_value2`` are supported.

    gamma : float
        gamma corrections for the selected colormap.

    reverse : bool
        Choose if you use reversed colormap or not.

    Examples
    --------
    >>> from custom_colormap import main
    >>> cmap = main(name="Dark_rainbow", gamma=1.0, reverse=False)
    """
    color_numbers = return_colormap.get_colordata(name)
    cmap = return_colormap.get_colormap(color_numbers, gamma=1.0, reverse=False)

    return cmap
