from .carve import treemap as _treemap_noncurried


def treemap(fn):
    return lambda tree: _treemap_noncurried(tree, fn)
