from carve import treemap, mapkey, mapval, remove, on_key, remove_empty, flow
from carve.curried import treemap as treemapfn
from toolz import pipe


def test_fun_stuff():
    target = {"john": {"doe": 1}}
    res = treemap(target, lambda k, v, p: (len(k), v))
    assert res == {4: {3: 1}}

    target = {"john": {"doe": [{"puma": "yes", "adidas": "no"}]}}
    res = treemap(target, lambda k, v, p: (len(k), "maybe" if v == "no" else v))
    assert res == {4: {3: [{4: "yes", 6: "maybe"}]}}


def test_mappers():
    target = {"john": {"doe": [{"puma": "yes", "adidas": "no"}]}}
    assert treemap(target, remove(lambda k, v, p: k == "adidas")) == {
        "john": {"doe": [{"puma": "yes"}]}
    }

    assert treemap(target, mapval(lambda k, v, p: "X" if len(p) > 2 else v)) == {
        "john": {"doe": [{"adidas": "X", "puma": "X"}]}
    }
    assert treemap(target, mapkey(lambda k, v, p: "X" + v if len(p) > 2 else k)) == {
        "john": {"doe": [{"Xyes": "yes", "Xno": "no"}]}
    }

    assert treemap(target, on_key("puma", lambda k, v, p: (k, "X"))) == {
        "john": {"doe": [{"adidas": "no", "puma": "X"}]}
    }
    assert treemap(
        {
            "a": "b",
            "c": None,
            "arr": [{"hi": {"ho": {"hi": None}, "hi": "ho"}}, None, {"hiho": None}],
        },
        remove_empty,
    ) == {"a": "b", "arr": [{"hi": {"hi": "ho"}}, None, {}]}


def test_compose():
    target = {"john": {"doe": [{"adidas": None, "puma": "X"}]}}
    scream = lambda k, v, p: ("PUMA", v) if k == "puma" else (k, v)
    assert treemap(target, flow(scream, remove_empty)) == {
        "john": {"doe": [{"PUMA": "X"}]}
    }


def test_curried():
    assert pipe(
        {
            "a": "b",
            "c": None,
            "arr": [{"hi": {"ho": {"hi": None}, "hi": "ho"}}, None, {"hiho": None}],
        },
        treemapfn(remove_empty),
    ) == {"a": "b", "arr": [{"hi": {"hi": "ho"}}, None, {}]}
