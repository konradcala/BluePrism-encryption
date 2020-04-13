from setuptools import setup, find_packages

setup(
    name='BluePrism-encryption',
    version='0.1',
    packages=find_packages(),
    license='',
    author='',
    author_email='',
    description='Blue Prism encryption',
    install_requires=['pycryptodomex'],
    extras_require={'test': ['pytest']}
)
