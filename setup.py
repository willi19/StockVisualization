from setuptools import setup, find_packages
from distutils.util import convert_path

main_ns = {}
with open(ver_path) as ver_file:
    exec(ver_file.read(), main_ns)

setup(
    name            = 'website',
    version         = main_ns['__version__'],
    description     = 'StockData Visualization',
    url             = 'https://github.com/willi19/StockVisualization',
    author          = 'Mingi Choi, Dongjin Shin',
    author_email    = 'willi19@snu.ac.kr, djshin1015@snu.ac.kr',
    install_requires= ['requests', 'pandas', 'datetime', 'numpy', 'xlrd'],
    license         = 'MIT',
    packages        = find_packages(include=['website','website.*']),
    python_requires = '>=3',
    zip_safe        = False
)