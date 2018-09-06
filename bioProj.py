

#opens file name entered by user
o1 = input("Please Enter Your DNA Sequence File Name: " )
o1 = open(o1)
o1_contents = o1.read()
#translates to upper case
operator = o1_contents.upper()

#table for decoding
map = {"UUU":"F", "UUC":"F", "UUA":"L", "UUG":"L",
    "UCU":"S", "UCC":"S", "UCA":"S", "UCG":"S",
    "UAU":"Y", "UAC":"Y", "UAA":"STOP**", "UAG":"STOP**",
    "UGU":"C", "UGC":"C", "UGA":"STOP**", "UGG":"W",
    "CUU":"L", "CUC":"L", "CUA":"L", "CUG":"L",
    "CCU":"P", "CCC":"P", "CCA":"P", "CCG":"P",
    "CAU":"H", "CAC":"H", "CAA":"Q", "CAG":"Q",
    "CGU":"R", "CGC":"R", "CGA":"R", "CGG":"R",
    "AUU":"I", "AUC":"I", "AUA":"I", "AUG":"**M",
    "ACU":"T", "ACC":"T", "ACA":"T", "ACG":"T",
    "AAU":"N", "AAC":"N", "AAA":"K", "AAG":"K",
    "AGU":"S", "AGC":"S", "AGA":"R", "AGG":"R",
    "GUU":"V", "GUC":"V", "GUA":"V", "GUG":"V",
    "GCU":"A", "GCC":"A", "GCA":"A", "GCG":"A",
    "GAU":"D", "GAC":"D", "GAA":"E", "GAG":"E",
    "GGU":"G", "GGC":"G", "GGA":"G", "GGG":"G",}
#transer complement
def rc(my_sequence):
    my_dictionary = {'A': 'T', 'T': 'A', 'C': 'G', 'G': 'C'}
    return "".join([my_dictionary[base] for base in my_sequence])
#reverse complement
def rfc(my_sequence):
    my_dictionary = {'A': 'T', 'T': 'A', 'C': 'G', 'G': 'C'}
    return "".join([my_dictionary[base] for base in reversed(my_sequence)])
# mRNA trnaslation
def D_2_R(str):

    before = 'T'
    after = 'U'
    trans_table = str.maketrans(before,after)
    return str.translate(trans_table)
#convers them using the list and entered sequence
def codons2protien(x, unit, map):
    protein = ''
    #gets rid of any of the last chrs if not in a multiplayer
    for i in range(x, (len(unit)-x)-((len(unit)-x)%3), 3):
        # defines the three chrs and iterates by 3 from the starting point
        codon = unit[i:i + 3]
        #puts together all the codons
        protein += map[codon]
#returns the list
    return protein
# all of my conversions so i can print them
replaced = D_2_R(operator)
complement = rc(operator)
reverse_comp = rfc(operator)
translated_revercomp = D_2_R(reverse_comp)
atry = codons2protien(0,replaced,map)
atry1 = codons2protien(1,replaced,map)
atry2 = codons2protien(2,replaced,map)
atr = codons2protien(0,translated_revercomp, map)
atr1 = codons2protien(1,translated_revercomp, map)
atr2 = codons2protien(2,translated_revercomp, map)

print("ORIGINAL :", operator)
print("RNA from org :",replaced)
print ("COMPLEMENT", complement)
print ("Reverse Complement", reverse_comp)
print("translated reverse comp", translated_revercomp)
print("*****************************************************************************")
print("**_____** indicates a highlighted area ")
print("Reading frame 1 ",atry,)
print("Reading frame 2 ",atry1)
print("Reading frame 3 ",atry2)
print("Reading frame 4 ",atr)
print("Reading frame 5 ",atr1)
print("Reading frame 6 ",atr2)