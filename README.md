![](media/carve.png)

# 🌲Carve

A minimalist Python library for manipulating nested data structures with ease and performance.

Take a look:

```
>>> from carve import treemap
>>> obj = {"john": {"doe": [{"puma": "yes", "adidas": None}]}}
>>> treemap(obj, remove_empty)
{"john": {"doe": [{"puma": "yes"}]}}
>>> treemap(obj, lambda k,v,p: ("PUMA", "puma") if k == "puma" else (k,v))
{"john": {"doe": [{"PUMA": "puma", "adidas": None}]}}
```

## Quick Start

Install using pip/pipenv/etc. (we recommend [poetry](https://github.com/sdispater/poetry) for sane dependency management):

```
$ poetry add carve
```

Transform your dictionary using a `k,v,p` context for each operation:

* k - key.
* v - value.
* p - path, in the form of a tuple: ("john", "doe") means the nested key "john.doe".

And return a key-value tuple: `(key, value)`. You can:

* Return a custom value to change both key and value `("foo", "bar")`
* Just modify a key: `("foo", v)`
* Just modify a value: `(k, "bar")`
* Remove the current entry: `(None, None)`
* Decide what to do based on your current path: `(None, None) if "secret" in p else (k,v)`

## Builtins

You can use the following builtins for shortcut operations:

```python
from carve import treemap, mapkey, mapval, remove, on_key, remove_empty, flow

treemap(target, remove(lambda k, v, p: k == "adidas"))
treemap(target, mapval(lambda k, v, p: "X" if len(p) > 2 else v))
treemap(target, mapkey(lambda k, v, p: "X" + v if len(p) > 2 else k))
treemap(target, on_key("puma", lambda k, v, p: (k, "X")))
treemap(target, remove_empty)

# multiple builtins, left-to-right with 'flow'
assert treemap(target, flow(scream, remove_empty))
```


### Thanks:

To all [Contributors](https://github.com/jondot/carve/graphs/contributors) - you make this happen, thanks!

# Copyright

Copyright (c) 2018 [@jondot](http://twitter.com/jondot). See [LICENSE](LICENSE.txt) for further details.