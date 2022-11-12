"""Build optional cython modules."""

import os
from distutils.command.build_ext import build_ext


class BuildExt(build_ext):
    def build_extensions(self):
        try:
            super().build_extensions()
        except Exception:
            pass


def build(setup_kwargs):
    if os.environ.get("SKIP_CYTHON", False):
        return
    try:
        from Cython.Build import cythonize

        setup_kwargs.update(
            dict(
                ext_modules=cythonize(
                    [
                        "src/home_assistant_bluetooth/models.py",
                    ],
                    compiler_directives={"language_level": "3"},  # Python 3
                ),
                cmdclass=dict(build_ext=BuildExt),
            )
        )
    except Exception:
        if os.environ.get("REQUIRE_CYTHON"):
            raise
        pass
