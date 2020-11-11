#This program turns a strand of DNA into mRNA, which is then converted into amino acids using a codon chart
#MIT License as usual
#Ravi Shah 2020
from amino_acids import codons_to_acids

stop_index = "NaN"

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

def find_start(mrna):
    try:
        start_index = mrna.index("AUG")
        inter_rna = mrna[start_index:]
        return inter_rna
    except:
        print("Please enter a valid DNA strand with a start codon.")
        quit()

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

def break_into_codons(mrna):
    n = 3
    res = [mrna[i:i+n] for i in range(0, len(mrna), n)]
    return res

def truncate(codons, stop_index):
    codons = codons[0:stop_index+1]
    return codons

def translation(final_codons):
    print("The codons are:", final_codons)
    list_of_amino_acids = codons_to_acids(final_codons)
    print("There are", len(list_of_amino_acids), "amino acids translated from this mRNA strand.")
    return list_of_amino_acids

strand = input("Enter the DNA strand to be transcribed and translated: ")
strand = strand.upper()
messenger_rna = transcription(strand)
with_start = find_start(messenger_rna)
into_codons = break_into_codons(with_start)
stop_index = find_stop(into_codons)
final_codons = truncate(into_codons, stop_index)
amino_acids_list = translation(final_codons)
print(amino_acids_list)
