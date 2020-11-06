def codons_to_acids(list_of_codons):
    newlist = []
    for i in list_of_codons:
        if i == "GUU":
            newlist.append("Valine")
        if i == "GUC":
            newlist.append("Valine")
        if i == "GUA":
            newlist.append("Valine")
        if i == "GUG":
            newlist.append("Valine")
        if i == "GCU":
            newlist.append("Alanine")
        if i == "GCC":
            newlist.append("Alanine")
        if i == "GCA":
            newlist.append("Alanine")
        if i == "GCG":
            newlist.append("Alanine")
        if i == "GAU":
            newlist.append("Aspartic Acid")
        if i == "GAC":
            newlist.append("Aspartic Acid")
        if i == "GAA":
            newlist.append("Glutamic Acid")
        if i == "GAG":
            newlist.append("Glutamic Acid")
        if i == "GGU":
            newlist.append("Glycine")
        if i == "GGC":
            newlist.append("Glycine")
        if i == "GGA":
            newlist.append("Glycine")
        if i == "GGG":
            newlist.append("Glycine")
        if i == "UUU":
            newlist.append("Phenylalanine")
        if i == "UUC":
            newlist.append("Phenylalanine")
        if i == "UUA":
            newlist.append("Leucine")
        if i == "UUG":
            newlist.append("Leucine")
        if i == "UCU":
            newlist.append("Serine")
        if i == "UCC":
            newlist.append("Serine")
        if i == "UCA":
            newlist.append("Serine")
        if i == "UCG":
            newlist.append("Serine")
        if i == "UAU":
            newlist.append("Tyrosine")
        if i == "UAC":
            newlist.append("Tyrosine")
        if i == "UAA":
            newlist.append("STOP")
        if i == "UAG":
            newlist.append("STOP")
        if i == "UGU":
            newlist.append("Cysteine")
        if i == "UGC":
            newlist.append("Cysteine")
        if i == "UGA":
            newlist.append("STOP")
        if i == "UGG":
            newlist.append("Tryptophan")
        if i == "CUU":
            newlist.append("Leucine")
        if i == "CUC":
            newlist.append("Leucine")
        if i == "CUA":
            newlist.append("Leucine")
        if i == "CUG":
            newlist.append("Leucine")
        if i == "CCU":
            newlist.append("Proline")
        if i == "CCC":
            newlist.append("Proline")
        if i == "CCA":
            newlist.append("Proline")
        if i == "CCG":
            newlist.append("Proline")
        if i == "CAU":
            newlist.append("Histidine")
        if i == "CAC":
            newlist.append("Histidine")
        if i == "CAA":
            newlist.append("Glutamine")
        if i == "CAG":
            newlist.append("Glutamine")
        if i == "CGU":
            newlist.append("Arginine")
        if i == "CGC":
            newlist.append("Arginine")
        if i == "CGA":
            newlist.append("Arginine")
        if i == "CGG":
            newlist.append("Arginine")
        if i == "AUU":
            newlist.append("Isoleucine")
        if i == "AUC":
            newlist.append("Isoleucine")
        if i == "AUA":
            newlist.append("Isoleucine")
        if i == "AUG":
            newlist.append("Methionine")
        if i == "ACU":
            newlist.append("Threonine")
        if i == "ACC":
            newlist.append("Threonine")
        if i == "ACA":
            newlist.append("Threonine")
        if i == "ACG":
            newlist.append("Threonine")
        if i == "AAU":
            newlist.append("Asparagine")
        if i == "AAC":
            newlist.append("Asparagine")
        if i == "AAA":
            newlist.append("Lysine")
        if i == "AAG":
            newlist.append("Lysine")
        if i == "AGU":
            newlist.append("Serine")
        if i == "AGC":
            newlist.append("Serine")
        if i == "AGA":
            newlist.append("Arginine")
        if i == "AGG":
            newlist.append("Arginine")
    return newlist
