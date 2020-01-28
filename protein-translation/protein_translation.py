def proteins(strand):
    codons_to_protein = {
        "AUG": "Methionine",
        "UUU": "Phenylalanine",
        "UUC": "Phenylalanine",
        "UUA": "Leucine",
        "UUG": "Leucine",
        "UCU": "Serine",
        "UCC": "Serine",
        "UCA": "Serine",
        "UCG": "Serine",
        "UAU": "Tyrosine",
        "UAC": "Tyrosine",
        "UGU": "Cysteine",
        "UGC": "Cysteine",
        "UGG": "Tryptophan",
    }
    if len(strand) % 3 != 0:
        raise Exception("Wrong size of RNA sequence")
    result = []
    for i in range(len(strand) // 3):
        if strand[i * 3 : i * 3 + 3] in "UAA.UAG.UGA":
            return result
        else:
            try:
                result.append(codons_to_protein[strand[i * 3 : i * 3 + 3]])
            except KeyError:
                raise Exception("Invalid codon")
    return result

