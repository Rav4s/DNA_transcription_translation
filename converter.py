#This program turns a strand of DNA into mRNA, which is then converted into amino acids using a codon chart
#MIT License as usual
#Ravi Shah 2020
from amino_acids import codons_to_acids

stop_index = "NaN"

def find_stop(mrna):
    if "UAA" in mrna:
        print("UAA STOP codon found")
        stop_index = mrna.index("UAA")
    elif "UAG" in mrna:
        print("UAG STOP codon found")
        stop_index = mrna.index("UAG")
    elif "UGA" in mrna:
        print("UGA STOP codon found")
        stop_index = mrna.index("UGA")
    else:
        print("No STOP codon found. Exiting...")
        quit()
    return stop_index

def transcription(dna):
    res = []
    newlist = []
    res[:] = dna

    for i in res:
        if i == "G":
            newlist.append("C")
        elif i == "C":
            newlist.append("G")
        elif i == "A":
            newlist.append("U")
        elif i == "T":
            newlist.append("A")

    mrna_strand = ''.join(newlist)
    return mrna_strand

def start_to_stop(mrna):
    global stop_index
    try:
        start_index = mrna.index("AUG")
        inter_rna = mrna[start_index:]
        stop_index = find_stop(inter_rna)
        final_rna = inter_rna[0:stop_index+3]
        return(final_rna)
    except:
        print("Please enter a valid DNA strand")
        quit()

def translation(final_rna):
    print("The mRNA strand is:", final_rna)
    n = 3
    res = [final_rna[i:i+n] for i in range(0, len(final_rna), n)]
    print("The codons are:", res)
    list_of_amino_acids = codons_to_acids(res)
    print("There are", len(list_of_amino_acids), "amino acids translated from this mRNA strand.")
    return list_of_amino_acids

strand = input("Enter the DNA strand to be transcribed and translated: ")
strand = strand.upper()
messenger_rna = transcription(strand)
thing = start_to_stop(messenger_rna)
print("Here are the amino acids:")
print(translation(thing))
