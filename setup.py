from setuptools import setup, find_packages

setup(
    name='umLabeller',
    version='1.0.0',
    packages=find_packages(),
    include_package_data=True,
    package_data={'umLabeller': ['data/eng.word.full.230613.r7.tsv']},
    description='Morphological inspection tool for subword compositions of tokenizers',
    author='Khuyagbaatar Batsuren',
    url='https://github.com/unimorph/umLabeller',
    python_requires='>=3.6',
)
