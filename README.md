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

Output:

```
alien
```
## Examples

|   input word   |   subword tokenization  |   output label  |
|----------------|-------------------------|-----------------|
|   jogging      |   _j ogging             |   alien         |
|   neutralised  |   _neutral ised         |   morph         |
|   stepstones   |   _steps _tones         |   alien         |
|   swappiness   |   _sw appiness          |   alien         |
|   swappiness   |   _swap pi ness         |   morph         |
|   jogging      |   _jogging              |   vocab         |

