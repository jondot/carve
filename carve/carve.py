# todo:
# add table / proof / fuzzy testing incl. benchmarks
# add docs
# add helper functions as premade lambda funcs (test for nulls, etc)
# showcase composing a mapper func


from cytoolz import itemmap, map, keyfilter, identity, reduce


def xform(key, tree, mapfn, path):
    if not key:
        return tree

    (xkey, xtree) = mapfn(key, tree, path)
    if key:
        return (xkey, xtree)
    return xtree


def on_key(key, f):
    return lambda k, v, p: f(k, v, p) if (key in p) else (k, v)


def remove_empty(k, v, p):
    return (None, None) if not v else (k, v)


def mapkey(f):
    return lambda k, v, p: (f(k, v, p), v)


def mapval(f):
    return lambda k, v, p: (k, f(k, v, p))


def remove(f):
    return lambda k, v, p: (None, None) if f(k, v, p) else (k, v)


def flow(*args):
    return lambda k, v, p: reduce(
        lambda tup, f: f(tup[0], tup[1], tup[2]) + (tup[2],), args, (k, v, p)
    )[0:2]


def treemap(tree, mapfn, key=None, path=()):
    res = tree
    if isinstance(tree, dict):
        res = keyfilter(
            identity,
            itemmap(
                lambda item: treemap(item[1], mapfn, item[0], path + (item[0],)), tree
            ),
        )

    elif isinstance(tree, list):
        res = list(map(lambda t: treemap(t, mapfn, None, path), tree))

    return xform(key, res, mapfn, path)

