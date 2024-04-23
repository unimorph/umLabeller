from setuptools import setup, find_packages

setup(
    name='umLabeller',
    version='1.0.0',
    py_modules=['umLabeller'],
    data_files=[('data', ['eng.word.full.230613.r7.tsv'])],
    description='Morphological inspection tool for subword compositions of tokenizers',
    author='Khuyagbaatar Batsuren',
    url='https://github.com/unimorph/umLabeller',
    python_requires='>=3.6',
)
