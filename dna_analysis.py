sequence = "ATGCGTACGTTAGC"

print("DNA Sequence:", sequence)
print("Length:", len(sequence))

print("A:",sequence.count("A"))
print("T:",sequence.count("T"))
print("G:",sequence.count("G"))
print("C:",sequence.count("C"))

gc_content = (sequence.count("G") + sequence.count("C")) / len(sequence) * 100
print("GC Content:", round(gc_content, 2),"%")