

def file_opener(file_name):
    with open(file_name, "r") as file:
        temp_file = file.read()
        return temp_file


def sequence_analyser(sequence):
    seq_count = {"a": 0, "c": 0, "g": 0, "t": 0}
    for i in range(0, len(sequence)):
        if sequence[i].lower() == "a":
            seq_count["a"] += 1
        elif sequence[i].lower() == "c":
            seq_count["c"] += 1
        elif sequence[i].lower() == "g":
            seq_count["g"] += 1
        elif sequence[i].lower() == "t":
            seq_count["t"] += 1
    return seq_count


def get_compliment(sequence, reverse=False):
    compliment = ""
    if reverse:
        for j in range(len(sequence) - 1, -1, -1):
            if sequence[j].lower() == "a":
                compliment += "t"
            elif sequence[j].lower() == "t":
                compliment += "a"
            elif sequence[j].lower() == "c":
                compliment += "g"
            elif sequence[j].lower() == "g":
                compliment += "c"
        return compliment
    else:
        for i in range(0, len(sequence)):
            if sequence[i].lower() == "a":
                compliment += "t"
            elif sequence[i].lower() == "t":
                compliment += "a"
            elif sequence[i].lower() == "c":
                compliment += "g"
            elif sequence[i].lower() == "g":
                compliment += "c"
        return compliment


def gc_count_calc(seq_count):
    gc_count = (seq_count["g"] + seq_count["c"])/(seq_count["a"] + seq_count["g"] + seq_count["c"] + seq_count["t"])
    return gc_count


def detect_gc_islands(sequence, window_size, gc_threshold):
    cpg_islands = []


def test_comp():
    assert get_compliment("ATAT") == "tata"
    assert get_compliment("ATAT", True) == "atat"
    print("Compliment Functioning")


def test_gc_count():
    assert gc_count_calc(sequence_analyser("ggggaaaaaaaatttatatatcgcc")) == 0.32
    print("GC Count Functioning")


def main():
    test_comp()
    test_gc_count()
    sequence_count = sequence_analyser(file_opener("sequence.fasta"))


main()
