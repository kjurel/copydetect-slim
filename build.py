from setuptools.extension import Extension

custom_extension = Extension(
    "copydetect.winnow",
    sources=["copydetect/winnow/winnow.c"],
    define_macros=[("PY_SSIZE_T_CLEAN", )],  # type: ignore
    optional=True)


def build(setup_kwargs):
    """
    This is a callback for poetry used to hook in our extensions.
    """

    setup_kwargs.update({
        # declare the extension so that setuptools will compile it
        "ext_modules": [custom_extension],
    })
