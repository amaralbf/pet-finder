import app


def test_version():
    getattr(app, '__version__')
