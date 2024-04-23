from setuptools import setup, find_packages
import os

# Get all data files
data_files = []
for (root, _, files) in os.walk('data'):
    data_files.append((root, [os.path.join(root, f) for f in files]))

setup(
    name='umLabeller',
    version='1.0.0',
    packages=find_packages(),
    description='Morphological inspection tool for subword compositions of tokenizers',
    author='Khuyagbaatar Batsuren',
    url='https://github.com/unimorph/umLabeller',
    python_requires='>=3.6',
    data_files=data_files,
)