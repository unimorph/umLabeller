# umLabeller

## Installation

To install from source, please use the following commands:

```
git clone https://github.com/unimorph/umLabeller.git
cd umLabeller
pip install .
```

## Usage

```
from umLabeller import UniMorphLabeller

uml = umLabeller()
print(uml.auto_classify('stepstones',['Ġsteps','tones']))

```