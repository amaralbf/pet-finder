from setuptools import setup

setup(
    name='pet-finder',
    version='0.1.0',
    packages=['app'],
    package_dir={'': 'src'},
    include_package_data=True,
    install_requires=[
        'Flask~=2.0.1',
    ],
)
