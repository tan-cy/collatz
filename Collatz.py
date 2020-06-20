#!/usr/bin/env python3

# ---------------------------
# projects/collatz/Collatz.py
# Copyright (C) 2016
# Glenn P. Downing
# ---------------------------

# ---------------------------------
# cache of collatz values 1 to 1000
# ---------------------------------


cache = [1,2,8,3,6,9,17,4,20,7,
        15,10,10,18,18,5,13,21,21,8,
        8,16,16,11,24,11,112,19,19,19,
        107,6,27,14,14,22,22,22,35,9,
        110,9,30,17,17,17,105,12,25,25,
        25,12,12,113,113,20,33,20,33,20,
        20,108,108,7,28,28,28,15,15,15,
        103,23,116,23,15,23,23,36,36,10,
        23,111,111,10,10,31,31,18,31,18,
        93,18,18,106,106,13,119,26,26,26,
        26,26,88,13,39,13,101,114,114,114,
        70,21,13,34,34,21,21,34,34,21,
        96,21,47,109,109,109,47,8,122,29,
        29,29,29,29,42,16,91,16,42,16,
        16,104,104,24,117,117,117,24,24,16,
        16,24,37,24,86,37,37,37,55,11,
        99,24,24,112,112,112,68,11,50,11,
        125,32,32,32,81,19,32,32,32,19,
        19,94,94,19,45,19,45,107,107,107,
        45,14,120,120,120,27,27,27,120,27,
        19,27,40,27,27,89,89,14,40,40,
        40,14,14,102,102,115,27,115,53,115,
        115,71,71,22,53,14,14,35,35,35,
        128,22,84,22,128,35,35,35,53,22,
        22,97,97,22,22,48,48,110,48,110,
        66,110,110,48,48,9,123,123,123,30,
        30,30,79,30,123,30,22,30,30,43,
        43,17,30,92,92,17,17,43,43,17,
        43,17,61,105,105,105,43,25,30,118,
        118,118,118,118,56,25,74,25,118,17,
        17,17,43,25,38,38,38,25,25,87,
        87,38,131,38,38,38,38,56,56,12,
        25,100,100,25,25,25,144,113,51,113,
        25,113,113,69,69,12,113,51,51,12,
        12,126,126,33,126,33,126,33,33,82,
        82,20,126,33,33,33,33,33,51,20,
        46,20,46,95,95,95,46,20,20,46,
        46,20,20,46,46,108,64,108,59,108,
        108,46,46,15,33,121,121,121,121,121,
        121,28,59,28,77,28,28,121,121,28,
        20,20,20,28,28,41,41,28,41,28,
        134,90,90,90,134,15,134,41,41,41,
        41,41,33,15,59,15,54,103,103,103,
        41,116,28,28,28,116,116,54,54,116,
        28,116,54,72,72,72,98,23,116,54,
        54,15,15,15,41,36,129,36,129,36,
        36,129,129,23,36,85,85,23,23,129,
        129,36,36,36,28,36,36,54,54,23,
        49,23,23,98,98,98,142,23,49,23,
        142,49,49,49,98,111,23,49,49,111,
        111,67,67,111,62,111,36,49,49,49,
        62,10,36,124,124,124,124,124,62,31,
        124,31,124,31,31,80,80,31,31,124,
        124,31,31,23,23,31,23,31,49,44,
        44,44,137,18,44,31,31,93,93,93,
        44,18,137,18,31,44,44,44,88,18,
        44,44,44,18,18,62,62,106,57,106,
        31,106,106,44,44,26,31,31,31,119,
        119,119,31,119,57,119,119,119,119,57,
        57,26,75,75,75,26,26,119,119,18,
        57,18,70,18,18,44,44,26,132,39,
        39,39,39,39,70,26,132,26,132,88,
        88,88,132,39,26,132,132,39,39,39,
        39,39,31,39,31,57,57,57,132,13,
        52,26,26,101,101,101,39,26,145,26,
        101,26,26,145,145,114,52,52,52,114,
        114,26,26,114,52,114,145,70,70,70,
        96,13,65,114,114,52,52,52,65,13,
        65,13,39,127,127,127,39,34,127,127,
        127,34,34,127,127,34,127,34,65,83,
        83,83,171,21,34,127,127,34,34,34,
        65,34,26,34,26,34,34,52,52,21,
        47,47,47,21,21,47,47,96,34,96,
        140,96,96,47,47,21,140,21,21,47,
        47,47,96,21,91,21,47,47,47,47,
        140,109,21,65,65,109,109,60,60,109,
        34,109,153,47,47,47,60,16,34,34,
        34,122,122,122,153,122,34,122,60,122,
        122,122,122,29,122,60,60,29,29,78,
        78,29,78,29,104,122,122,122,73,29,
        60,21,21,21,21,21,73,29,47,29,
        135,42,42,42,135,29,42,42,42,29,
        29,135,135,91,135,91,42,91,91,135,
        135,16,29,135,135,42,42,42,86,42,
        42,42,42,42,42,34,34,16,60,60,
        60,16,16,55,55,104,29,104,148,104,
        104,42,42,117,148,29,29,29,29,29,
        179,117,148,117,29,55,55,55,148,117,
        117,29,29,117,117,55,55,73,148,73,
        47,73,73,99,99,24,68,117,117,55,
        55,55,117,16,68,16,55,16,16,42,
        42,37,130,130,130,37,37,130,130,37,
        130,37,68,130,130,130,117,24,130,37,
        37,86,86,86,130,24,174,24,86,130,
        130,130,37,37,37,37,37,37,37,29,
        29,37,29,37,29,55,55,55,130,24,
        50,50,50,24,24,24,143,99,50,99,
        37,99,99,143,143,24,99,50,50,24,
        24,143,143,50,24,50,37,50,50,99,
        99,112,94,24,24,50,50,50,50,112]


# ------------
# collatz_read
# ------------


def collatz_read(s):
    """
    read two ints
    s a string
    return a list of two ints, representing the beginning and end of a range, [i, j]
    """
    a = s.split()
    return [int(a[0]), int(a[1])]


# -------------------
# collatz_eval_helper
# -------------------

def collatz_eval_helper(s):
    count = 1
    if s>0:
        if s <= 1000:
            return cache[s-1]
        else:
            while s != 1:
                if s%2 == 0:
                    s = s//2
                else:
                    s = 3*s+1
                count+=1
    else:
        count = 0
    return count


# ------------
# collatz_eval
# ------------


def collatz_eval(i, j):
    """
    i the beginning of the range, inclusive
    j the end       of the range, inclusive
    return the max cycle length of the range [i, j]
    """
    # <your code>
    l = []
    if i > j:
        i, j = j, i
    for x in range(i, j+1):
        l.append(collatz_eval_helper(x))
    return max(l)

# -------------
# collatz_print
# -------------


def collatz_print(w, i, j, v):
    """
    print three ints
    w a writer
    i the beginning of the range, inclusive
    j the end       of the range, inclusive
    v the max cycle length
    """
    w.write(str(i) + " " + str(j) + " " + str(v) + "\n")

# -------------
# collatz_solve
# -------------


def collatz_solve(r, w):
    """
    r a reader
    w a writer
    """
    for s in r:
        i, j = collatz_read(s)
        v = collatz_eval(i, j)
        collatz_print(w, i, j, v)

