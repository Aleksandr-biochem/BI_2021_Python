class RNA:
    
    def __init__(self, sequence):
        if set(sequence) <= set('acguACGU'):
            self.sequence = sequence.upper()
        else:
            raise Exception("Check the sequence, the alphabet does not match RNA sequence")
            
    def gc_content(self):
        return (self.sequence.count('C') + self.sequence.count('G')) / len(self.sequence) * 100
    
    def reverse_complement(self):
        return self.sequence.translate(str.maketrans("ACGU", "UGCA"))[::-1]
    
    def __iterator(self):
        for el in self.sequence:
            yield el
    
    def __iter__(self):
        return self.__iterator()
    
    def __eq__(self, other):
        if not isinstance(other, DNA):
            return NotImplemented
        return self.sequence == other.sequence
    
    def __hash__(self):
        return hash(repr(self))
    
    def __repr__(self):
        return self.sequence

class DNA:
 
    def __init__(self, sequence):
        if set(sequence) <= set('acgtACGT'):
            self.sequence = sequence.upper()
        else:
            raise Exception("Check the sequence, the alphabet does not match DNA sequence")
        
    def gc_content(self):
        return (self.sequence.count('C') + self.sequence.count('G')) / len(self.sequence) * 100
    
    def reverse_complement(self):
        return self.sequence.translate(str.maketrans("ACGT", "TGCA"))[::-1]
        
    def transcribe(self):
        return RNA(self.sequence.translate(str.maketrans("T", "U")))
    
    def __iterator(self):
        for el in self.sequence:
            yield el
    
    def __iter__(self):
        return self.__iterator()
    
    def __eq__(self, other):
        if not isinstance(other, DNA):
            return NotImplemented
        return self.sequence == other.sequence
    
    def __hash__(self):
        return hash(repr(self))
    
    def __repr__(self):
        return self.sequence
