from setuptools import setup, Extension
import subprocess
import os

subprocess.check_call(['cmake', '.'], cwd='feaplusplus')
subprocess.check_call(['make'], cwd='feaplusplus')

feaplusplus_include = os.path.abspath('feaplusplus/feaplusplus/include')
feaplusplus_lib = os.path.abspath('feaplusplus/feaplusplus/build')

ext_modules = [
    Extension(
        'structurax',
        sources=[],
        include_dirs=[feaplusplus_include],
        library_dirs=[feaplusplus_lib],
        libraries=['feaplusplus']
    )
]

setup(
    name='structurax',
    version='0.1',
    packages=['structurax'],
    ext_modules=ext_modules,
    install_requires=[
        'numpy',
    ],
)

