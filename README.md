# umLabeller

umLabeller is an inspection tool for characterizing the semantic compositionality of subword tokenization,
based on the morphological information retrieved from UniMorph. 
Given a word _w_ and its subword tokenization, _s_ = (_s1_, ..., _sn_) | ∀i _si_ ∈ V, umLabeller assigns one of four categories: _vocab, alien, morph, or n/a_:

- **vocabulary subword**: the given word _w_ is a subword in the vocabulary as _w_ ∈ _V_;
- **alien composition**: the given subword sequence _s_ is an alien subword composition if we find at least two subwords _si_ and _sj_ in s that are not meaningful with respect to the meaning of _w_;
- **morphological composition**: the subword sequence _s_ is morphological if it is neither a vocabulary nor an alien subword composition;
- **n/a**: UniMorph has no information on the word.

umLabeller can characterize over half a million English words and is compatible with most modern tokenizers.

## Installation

To install from the source, please use the following commands:

```
!git clone https://github.com/unimorph/umLabeller.git
```

```
cd umLabeller
```

```
!pip install .
```

Note: The instructions above have been tested on Google Colab.

## Usage

```
from umLabeller.umLabeller import UniMorphLabeller

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
