def DNA_strand(dna):
    """
    other way:
    return dna.translate(string.maketrans("ATCG","TAGC"))
    #2.7 need to import string
    """
    dic = {"A":"T","T":"A","C":"G","G":"C"}
    result = ""
    for i in dna:
        result += dic[i]
    return result

print DNA_strand ("ATTGC")
