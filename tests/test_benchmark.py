from carve import __version__
from carve import treemap

from boltons.iterutils import remap

target = {
    "system": {
        "planets": [
            {"name": "earth", "foo": None},
            {"name": "earth", "foo": None},
            {"name": "earth", "foo": None},
            {"name": "earth", "foo": None},
            {"name": "earth", "foo": None},
            {"name": "earth", "foo": None},
            {"name": "earth", "foo": None},
            {"name": "earth", "foo": None},
            {"name": "earth", "foo": None},
            {"name": "earth", "foo": None},
            {"name": "earth", "foo": None},
            {"name": "earth", "foo": None},
            {"name": "earth", "foo": None},
            {"name": "jupiter"},
            {"name": "jupiter"},
            {"name": "jupiter"},
            {"name": "jupiter"},
            {"name": "jupiter"},
            {"name": "jupiter"},
            {"name": "jupiter"},
            {"name": "jupiter"},
            {"name": "jupiter"},
            {"name": "jupiter"},
            {"name": "jupiter"},
            {"name": "jupiter"},
            {
                "nested": [
                    {
                        "nested": [
                            {"name": "earth", "foo": None},
                            {"name": "earth", "foo": None},
                            {"name": "earth", "foo": None},
                            {"name": "earth", "foo": None},
                            {"name": "earth", "foo": None},
                            {"name": "earth", "foo": None},
                            {"name": "earth", "foo": None},
                            {"name": "earth", "foo": None},
                            {"name": "earth", "foo": None},
                            {"name": "earth", "foo": None},
                            {"name": "earth", "foo": None},
                            {"name": "earth", "foo": None},
                            {"name": "earth", "foo": None},
                            {"name": "jupiter"},
                            {"name": "jupiter"},
                            {"name": "jupiter"},
                            {"name": "jupiter"},
                            {"name": "jupiter"},
                            {"name": "jupiter"},
                            {"name": "jupiter"},
                            {"name": "jupiter"},
                            {"name": "jupiter"},
                            {"name": "jupiter"},
                            {"name": "jupiter"},
                            {"name": "jupiter"},
                        ]
                    },
                    {"name": "earth", "foo": None},
                    {"name": "earth", "foo": None},
                    {"name": "earth", "foo": None},
                    {"name": "earth", "foo": None},
                    {"name": "earth", "foo": None},
                    {"name": "earth", "foo": None},
                    {"name": "earth", "foo": None},
                    {"name": "earth", "foo": None},
                    {"name": "earth", "foo": None},
                    {"name": "earth", "foo": None},
                    {"name": "earth", "foo": None},
                    {"name": "earth", "foo": None},
                    {"name": "earth", "foo": None},
                    {"name": "jupiter"},
                    {"name": "jupiter"},
                    {"name": "jupiter"},
                    {"name": "jupiter"},
                    {"name": "jupiter"},
                    {"name": "jupiter"},
                    {"name": "jupiter"},
                    {"name": "jupiter"},
                    {"name": "jupiter"},
                    {"name": "jupiter"},
                    {"name": "jupiter"},
                    {"name": "jupiter"},
                ]
            },
        ]
    }
}
target_b = {"system": {"planets": {"name": "earth"}}}


def test_uit(benchmark):
    def with_uit():
        treemap(target, lambda k, v, p: (None, None) if not v else (k, v))

    benchmark(with_uit)


def test_remap(benchmark):
    def with_remap():
        remap(target, lambda p, k, v: v is not None)

    benchmark(with_remap)

