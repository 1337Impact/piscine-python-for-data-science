def ft_tqdm(lst: range) -> None:
    """
    A custom progress bar generator function.

    This function emulates a progress bar similar to the one provided by `tqdm`

    Parameters:
    -----------
    lst : range
        The range or iterable over which the progress bar will iterate.

    Yields:
    """
    size = len(lst)
    tmp = 100 / size
    for (i, e) in enumerate(lst):
        done = int((i+1) * tmp)
        progress = 100 - done

        print(f"{done}% | [{'=' * done}{' ' *
              progress}>] | {i+1}/{size}", end="\r")
        yield e
