import os
import pkg_resources

class UniMorphLabeller:
    def __init__(self):
      self.segmentations, self.morpheme_merges = self.initiate_labeller_data()
      self.key = 'Ġ'
    
    def setKey(self, key):
        self.key = key
    
    #normalized (lowercases) reader
    def read_unimorph_csv_normalized(self, path):
        data = {}
        with open(path, encoding='utf-8') as f:
            for line in f:
                fields = line.rstrip("\n").split("\t")
                data[fields[0]] = fields[1].lower().split(' @@')
        return data

    def findMorph(self, merges, morphs):
      if len(morphs) == 1:
        return morphs[0]
      if morphs in merges:
        return merges[morphs]
      head_morph = morphs[0]
      second_morph = self.findMorph(merges, tuple(morphs[1:]))
      if (head_morph, second_morph) in merges:
        return merges[head_morph, second_morph]
      return None

    def updateMerges(self, merges, word, morphs):
      for i in range(1,len(morphs)):
        #print('duudlaa ', word, morphs[:i], morphs[i:])
        # if word =='Ġunhappiness':
        #     print('duudlaa ', word, i, morphs[:i], morphs[i:])
        head_morph = self.findMorph(merges, morphs[:i])
        if head_morph == None:
          if word.startswith(''.join(morphs[:i])):
            head_morph = ''.join(morphs[:i])
          else:
            return None
        tail_morph = self.findMorph(merges, morphs[i:])
        #print('surlaa ', word, head_morph, tail_morph)
        if tail_morph == None:
          # if word =='Ġunhappiness':
          #   print(head_morph, tail_morph)
          if word.startswith(head_morph+morphs[i][0]):
            tail_morph = word[len(head_morph):]
            merges[tuple(morphs[i:])] = tail_morph
            merges[head_morph, tail_morph] = word
          elif word.endswith(''.join(morphs[i:])):
            tail_morph = ''.join(morphs[i:])
            merges[tuple(morphs[i:])] = tail_morph
            merges[head_morph, tail_morph] = word
          elif word.startswith(head_morph) and head_morph[-1] == morphs[i][0]:
            tail_morph = word[len(head_morph)-1:]
            merges[tuple(morphs[i:])] = tail_morph
            merges[head_morph, tail_morph] = word
          else:
            return None
        else:
          # if word =='Ġunhappiness':
          #   print(head_morph, tail_morph)
          merges[head_morph, tail_morph] = word
      return merges

    def read_morphological_merges_from_unimorph(self, path):
        data = {}
        max_len = 0
        with open(path, encoding='utf-8') as f:
            for line in f:
                fields = line.rstrip("\n").lower().split("\t")
                if fields[2] == '000':
                    continue
                subwords = fields[1].split(' @@')
                data[tuple(subwords)] = fields[0]
                data[('Ġ'+subwords[0],)+tuple(subwords[1:])] = 'Ġ'+fields[0]
                if len(subwords)==3:
                    try:
                        if fields[0].startswith(subwords[0]+subwords[1][0]):
                            if ((subwords[1],subwords[2]) in data) is False:
                                data[subwords[1],subwords[2]] = fields[0][len(subwords[0]):]
                                data['Ġ'+subwords[1],subwords[2]] = 'Ġ'+fields[0][len(subwords[0]):]
                            data[subwords[0],data[subwords[1],subwords[2]]] = fields[0]
                            data['Ġ'+subwords[0],data[subwords[1],subwords[2]]] = 'Ġ'+fields[0]
                        if fields[0].endswith(subwords[2]):
                            if ((subwords[0],subwords[1]) in data) is False:
                                data[subwords[0],subwords[1]] = fields[0][:-len(subwords[2])]
                                data['Ġ'+subwords[0],subwords[1]] = 'Ġ'+fields[0][:-len(subwords[2])]
                            data[data[subwords[0],subwords[1]],subwords[2]] = fields[0]
                            data['Ġ'+data[subwords[0],subwords[1]],subwords[2]] = 'Ġ'+fields[0]
                    except:
                        print(fields[0], subwords)
                max_len = len(subwords) if len(subwords) > max_len else max_len
        #print(max_len)
        for i in range(3, max_len):
          focus_list = []
          for k,v in data.items():
            if len(k) == i:
              focus_list.append((k,v))
          for (k,v) in focus_list:
            copy_data = self.updateMerges(data, v, k)
        return data

    def initiate_labeller_data(self):
      #data_file_path = os.path.join(os.path.dirname(__file__), 'data', 'eng.word.full.230613.r7.tsv')
      data_file_path = pkg_resources.resource_filename('umLabeller', 'data/eng.word.full.230613.r7.tsv')
      #data_file_path = pkg_resources.resource_filename(__name__, 'data/eng.word.full.230613.r7.tsv')
      segments = self.read_unimorph_csv_normalized(data_file_path)
      #merges = read_unimorph_merges(path)
      merges = self.read_morphological_merges_from_unimorph(data_file_path)
      return segments, merges

    def rec_labeller(self, subw, morp):
      if len(subw) > len(morp):
        return 'alien'
      if len(subw) == 2:
        if subw[0] == morp[0] or subw[1] == morp[len(morp)-1] or (subw[0] + 'e' == morp[0] and len(subw[0])>2):
          return 'morph'
        else:
          if len(morp) > 2:
            for ix in range(len(morp)-1):
              try:
                morp_begin = morp[:ix+1]
                morp_end = morp[ix+1:]
                if len(morp_begin) > 1:
                  m_beg = self.morpheme_merges[tuple(morp_begin)]
                else:
                  m_beg = morp_begin[0]
                if len(morp_end) > 1:
                  m_end = self.morpheme_merges[tuple(morp_end)]
                else:
                  m_end = morp_end[0]
                can_label = self.rec_labeller(subw, [m_beg, m_end])
                if can_label == 'morph':
                  return can_label
              except:
                continue
          return 'alien'
      else:
        if subw[0] == morp[0] or (subw[0] + 'e' == morp[0] and len(subw[0])>2):
          return self.rec_labeller(subw[1:], morp[1:])
        elif subw[len(subw)-1] == morp[len(morp)-1]:
          return self.rec_labeller(subw[:len(subw)-1], morp[:len(morp)-1])
        else:
          if len(subw) == len(morp):
            return 'alien'
          else:
            #key = morp[len(morp)-2] +'_'+morp[len(morp)-1]
            key = (morp[len(morp)-2], morp[len(morp)-1])
            if key in self.morpheme_merges:
              return self.rec_labeller(subw, morp[:len(morp)-2]+[self.morpheme_merges[key]])
            return 'alien'

    def normalize(self, tokens, key):
      if key == '#' or key == '@':
        return self.normalizeBERT(tokens)
      else:
        if tokens[0].startswith(key):
            tokens[0] = tokens[0][1:]
      return tokens

    def normalizeBERT(self, tokens):
      for i in range(len(tokens)):
        if i == 0: continue
        if tokens[i].startswith('##') or tokens[i].startswith('@@'):
            tokens[i] = tokens[i][2:]
      return tokens

    def classify(self, word, subwords):
      if subwords[0] == '':
        subwords = subwords[1:]
      if len(subwords) == 1:
        return 'vocab'
      if (word in self.segmentations) is False:
        return 'n.a'
      if subwords == self.segmentations[word]:
        return 'morph'
      morphs = self.segmentations[word]
      if len(subwords) > len(morphs):
        return 'alien'
      ans = self.rec_labeller(subwords, morphs)
      #print('orloo ', ans, word, subwords, morphs)
      return ans

    def auto_classify(self, word, subwords):
      normalized_subwords = self.normalize(subwords, self.key)
      return self.classify(word, normalized_subwords)
