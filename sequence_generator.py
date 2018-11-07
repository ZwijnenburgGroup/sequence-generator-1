import itertools
import sys

'''
Script to generate two-component sequences of specified length.

Use
---
python sequence_generator.py <length>

where `length` is an integer, specifying the length
of the sequences to be generated.

Output
------
File `sequences.txt` containing a list of all sequences. Sequence strings
can be used in conjunction with the Supramolecular Toolkit
(stk, https://github.com/JelfsMaterialsGroup/stk) to produce oligomer models
with a particular sequence.
'''

def generate_sequences(length):
    sequences = []
    for seq in itertools.product(['A', 'B'], repeat=length):
        if seq not in sequences and seq[::-1] not in sequences:
            sequences.append(seq)
    return sequences

def write_sequences(sequences):
    with open('sequences.txt', 'w') as f:
        [f.write(''.join(seq)+'\n') for seq in sequences]

def main():
    length = int(sys.argv[-1])
    sequences = generate_sequences(length)
    write_sequences(sequences)
    print('{} sequences generated'.format(len(sequences)))

if __name__ == '__main__':
    main()
