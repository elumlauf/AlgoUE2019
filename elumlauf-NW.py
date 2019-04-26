import sys
import argparse
from Bio import SeqIO

# input must be  python3 nw_1.py --match 1 --mismatch -1 --gap -2 < filename
parser = argparse.ArgumentParser()
text="Needleman Wunsch for pairwise global sequence alignment. Enter match, mismatch, and gap integer values as shown above. \
Enter the two sequences in fasta format as a file via STDIN by adding:   < filename"
parser = argparse.ArgumentParser(description = text)
parser.add_argument("--match", type=int, help="scoring value for two matching nucleotides or aas; default value = 1")
parser.add_argument("--mismatch", type=int, help="scoring value for two mismatching nucleotides or aas; default value = -1")
parser.add_argument("--gap", type=int, help="scoring value for a gap; default value = -2")
args = parser.parse_args()

text1="If values for --match, --mismatch, --gap are not entered, default values match=1, mismatch=-1, and gap=-2 are used."

if len(sys.argv) < 7:
    print(text1)
if args.match == None:
    match =1
else:
    match_const = int(args.match)
if args.mismatch == None:
    mismatch =-1
else:
    mismatch = int(args.mismatch)
if args.gap==None:
    gap = -2
else:
    gap = int(args.gap)

def match_score(unit1,unit2):
    global match, gap
    if unit1 == unit2:
        return match_const
    elif unit1 == '-' or unit2 == '-':
          return gap
    else:
        return mismatch

if __name__ == "__main__":
    fin = sys.stdin
    if sys.stdin.isatty():
        sys.exit("You did not enter a STDIN")
    records = list(SeqIO.parse(fin, "fasta"))
    #length of sequence 0 will be number of rows
    len_seq0 = len(records[0].seq)
    #length of sequence 1 will be number of columns
    len_seq1 = len(records[1].seq)

    dict_rows = len_seq1 + 1
    dict_col = len_seq0 + 1
    score_dict = {(0,0):0}
    for i in range(0, dict_rows):
        score_dict[(i,0)]= i * gap
    for j in range(0, dict_col):
        score_dict[(0,j)]= j * gap

    for ii in range(1, dict_rows):
        for jj in range(1, dict_col):
            match = score_dict[(ii-1,jj-1)] + match_score(records[0].seq[jj-1],records[1].seq[ii-1])
            deletion = score_dict[(ii-1,jj)] + gap
            insertion = score_dict[(ii,jj-1)] + gap
            #max score
            score_dict[(ii,jj)] = max(match, deletion, insertion)

    # traceback
    seq_align0 = ""
    seq_align1 = ""
    third_line = ""

    iii = len_seq1
    jjj = len_seq0

    while iii>0 and jjj>0:
        score_now = score_dict[(iii,jjj)]
        score_diag = score_dict[(iii-1,jjj-1)]
        score_up = score_dict[(iii,jjj-1)]
        score_left = score_dict[(iii-1,jjj)]

        if score_now == score_diag + match_score(records[0].seq[jjj-1],records[1].seq[iii-1]):
            seq_align0 += records[0].seq[jjj-1]
            seq_align1 += records[1].seq[iii-1]

            if match_score(records[0].seq[jjj-1],records[1].seq[iii-1]) == match_const:
                third_line += "*"
            else:
                third_line += " "
            iii -= 1
            jjj -= 1

        elif score_now == score_up + gap:
            seq_align0 += records[0].seq[jjj-1]
            seq_align1 += '-'
            third_line += " "
            jjj -= 1
        elif score_now == score_left + gap:
            seq_align0 += '-'
            seq_align1 += records[1].seq[iii-1]
            third_line += " "
            iii -= 1

    while jjj>0:
        seq_align0 += records[0].seq[jjj-1]
        seq_align1 += '-'
        third_line += " "
        jjj -= 1
    while iii>0:
        seq_align0 += '-'
        seq_align1 += records[1].seq[iii-1]
        third_line += " "
        iii -= 1
    seq_align0 = seq_align0[::-1]
    seq_align1 = seq_align1[::-1]
    third_line = third_line[::-1]

    length_align = len(seq_align0)
    line_length = 60

    list_align0=([seq_align0[i:i+line_length] for i in range(0, len(seq_align0), line_length)])
    list_align1=([seq_align1[i:i+line_length] for i in range(0, len(seq_align1), line_length)])
    list_thirdline=([third_line[i:i+line_length] for i in range(0,len(third_line),line_length)])
    number_lines=len(list_align0)

    length_id0=len(records[0].id)
    length_id1=len(records[1].id)

    maxlength_id=max(length_id0,length_id1)
    totallength_id=maxlength_id + 3
    spaces_0=totallength_id - length_id0
    spaces_1=totallength_id - length_id1

    print ("CLUSTAL" + "\n" )

    for x in range(0,number_lines):
        print (records[0].id + ' ' * spaces_0 + list_align0[x] + "\n" + records[1].id + ' ' * spaces_1 + list_align1[x] + "\n" + ' ' * (totallength_id) + list_thirdline[x] + "\n")

    print(score_dict[(dict_rows-1,dict_col-1)], file=sys.stderr)
