# umLabeller

umLabeller is an inspection tool for characterizing the semantic compositionality of subword tokenization,
based on the morphological information retrieved from UniMorph.

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

uml = UniMorphLabeller()
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
|   stepstones   |   _steps tones          |   alien         |
|   swappiness   |   _sw appiness          |   alien         |
|   swappiness   |   _swap pi ness         |   morph         |
|   jogging      |   _jogging              |   vocab         |

## References
More details can be read in the following article:

Khuyagbaatar Batsuren, Ekaterina Vylomova, Verna Dankers, Tsetsuukhei Delgerbaatar, Omri Uzan, Yuval Pinter, Gábor Bella – Evaluating Subword Tokenization: Alien Subword Composition and OOV Generalization Challenge. [https://arxiv.org/abs/2404.13292](https://arxiv.org/abs/2404.13292)
