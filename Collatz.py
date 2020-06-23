#!/usr/bin/env python3

# ---------------------------
# projects/collatz/Collatz.py
# Copyright (C) 2016
# Glenn P. Downing
# ---------------------------


# ---------------------------------
# cache of collatz values 1 to 1000
# ---------------------------------
cache = {1: 1, 2: 2, 3: 8, 4: 3, 5: 6, 6: 9, 7: 17, 8: 4, 9: 20, 10: 7,
         11: 15, 12: 10, 13: 10, 14: 18, 15: 18, 16: 5, 17: 13, 18: 21, 19: 21, 20: 8,
         21: 8, 22: 16, 23: 16, 24: 11, 25: 24, 26: 11, 27: 112, 28: 19, 29: 19, 30: 19,
         31: 107, 32: 6, 33: 27, 34: 14, 35: 14, 36: 22, 37: 22, 38: 22, 39: 35, 40: 9,
         41: 110, 42: 9, 43: 30, 44: 17, 45: 17, 46: 17, 47: 105, 48: 12, 49: 25, 50: 25,
         51: 25, 52: 12, 53: 12, 54: 113, 55: 113, 56: 20, 57: 33, 58: 20, 59: 33, 60: 20,
         61: 20, 62: 108, 63: 108, 64: 7, 65: 28, 66: 28, 67: 28, 68: 15, 69: 15, 70: 15,
         71: 103, 72: 23, 73: 116, 74: 23, 75: 15, 76: 23, 77: 23, 78: 36, 79: 36, 80: 10,
         81: 23, 82: 111, 83: 111, 84: 10, 85: 10, 86: 31, 87: 31, 88: 18, 89: 31, 90: 18,
         91: 93, 92: 18, 93: 18, 94: 106, 95: 106, 96: 13, 97: 119, 98: 26, 99: 26, 100: 26,
         101: 26, 102: 26, 103: 88, 104: 13, 105: 39, 106: 13, 107: 101, 108: 114, 109: 114, 110: 114,
         111: 70, 112: 21, 113: 13, 114: 34, 115: 34, 116: 21, 117: 21, 118: 34, 119: 34, 120: 21,
         121: 96, 122: 21, 123: 47, 124: 109, 125: 109, 126: 109, 127: 47, 128: 8, 129: 122, 130: 29,
         131: 29, 132: 29, 133: 29, 134: 29, 135: 42, 136: 16, 137: 91, 138: 16, 139: 42, 140: 16,
         141: 16, 142: 104, 143: 104, 144: 24, 145: 117, 146: 117, 147: 117, 148: 24, 149: 24, 150: 16,
         151: 16, 152: 24, 153: 37, 154: 24, 155: 86, 156: 37, 157: 37, 158: 37, 159: 55, 160: 11,
         161: 99, 162: 24, 163: 24, 164: 112, 165: 112, 166: 112, 167: 68, 168: 11, 169: 50, 170: 11,
         171: 125, 172: 32, 173: 32, 174: 32, 175: 81, 176: 19, 177: 32, 178: 32, 179: 32, 180: 19,
         181: 19, 182: 94, 183: 94, 184: 19, 185: 45, 186: 19, 187: 45, 188: 107, 189: 107, 190: 107,
         191: 45, 192: 14, 193: 120, 194: 120, 195: 120, 196: 27, 197: 27, 198: 27, 199: 120, 200: 27,
         201: 19, 202: 27, 203: 40, 204: 27, 205: 27, 206: 89, 207: 89, 208: 14, 209: 40, 210: 40,
         211: 40, 212: 14, 213: 14, 214: 102, 215: 102, 216: 115, 217: 27, 218: 115, 219: 53, 220: 115,
         221: 115, 222: 71, 223: 71, 224: 22, 225: 53, 226: 14, 227: 14, 228: 35, 229: 35, 230: 35,
         231: 128, 232: 22, 233: 84, 234: 22, 235: 128, 236: 35, 237: 35, 238: 35, 239: 53, 240: 22,
         241: 22, 242: 97, 243: 97, 244: 22, 245: 22, 246: 48, 247: 48, 248: 110, 249: 48, 250: 110,
         251: 66, 252: 110, 253: 110, 254: 48, 255: 48, 256: 9, 257: 123, 258: 123, 259: 123, 260: 30,
         261: 30, 262: 30, 263: 79, 264: 30, 265: 123, 266: 30, 267: 22, 268: 30, 269: 30, 270: 43,
         271: 43, 272: 17, 273: 30, 274: 92, 275: 92, 276: 17, 277: 17, 278: 43, 279: 43, 280: 17,
         281: 43, 282: 17, 283: 61, 284: 105, 285: 105, 286: 105, 287: 43, 288: 25, 289: 30, 290: 118,
         291: 118, 292: 118, 293: 118, 294: 118, 295: 56, 296: 25, 297: 74, 298: 25, 299: 118, 300: 17,
         301: 17, 302: 17, 303: 43, 304: 25, 305: 38, 306: 38, 307: 38, 308: 25, 309: 25, 310: 87,
         311: 87, 312: 38, 313: 131, 314: 38, 315: 38, 316: 38, 317: 38, 318: 56, 319: 56, 320: 12,
         321: 25, 322: 100, 323: 100, 324: 25, 325: 25, 326: 25, 327: 144, 328: 113, 329: 51, 330: 113,
         331: 25, 332: 113, 333: 113, 334: 69, 335: 69, 336: 12, 337: 113, 338: 51, 339: 51, 340: 12,
         341: 12, 342: 126, 343: 126, 344: 33, 345: 126, 346: 33, 347: 126, 348: 33, 349: 33, 350: 82,
         351: 82, 352: 20, 353: 126, 354: 33, 355: 33, 356: 33, 357: 33, 358: 33, 359: 51, 360: 20,
         361: 46, 362: 20, 363: 46, 364: 95, 365: 95, 366: 95, 367: 46, 368: 20, 369: 20, 370: 46,
         371: 46, 372: 20, 373: 20, 374: 46, 375: 46, 376: 108, 377: 64, 378: 108, 379: 59, 380: 108,
         381: 108, 382: 46, 383: 46, 384: 15, 385: 33, 386: 121, 387: 121, 388: 121, 389: 121, 390: 121,
         391: 121, 392: 28, 393: 59, 394: 28, 395: 77, 396: 28, 397: 28, 398: 121, 399: 121, 400: 28,
         401: 20, 402: 20, 403: 20, 404: 28, 405: 28, 406: 41, 407: 41, 408: 28, 409: 41, 410: 28,
         411: 134, 412: 90, 413: 90, 414: 90, 415: 134, 416: 15, 417: 134, 418: 41, 419: 41, 420: 41,
         421: 41, 422: 41, 423: 33, 424: 15, 425: 59, 426: 15, 427: 54, 428: 103, 429: 103, 430: 103,
         431: 41, 432: 116, 433: 28, 434: 28, 435: 28, 436: 116, 437: 116, 438: 54, 439: 54, 440: 116,
         441: 28, 442: 116, 443: 54, 444: 72, 445: 72, 446: 72, 447: 98, 448: 23, 449: 116, 450: 54,
         451: 54, 452: 15, 453: 15, 454: 15, 455: 41, 456: 36, 457: 129, 458: 36, 459: 129, 460: 36,
         461: 36, 462: 129, 463: 129, 464: 23, 465: 36, 466: 85, 467: 85, 468: 23, 469: 23, 470: 129,
         471: 129, 472: 36, 473: 36, 474: 36, 475: 28, 476: 36, 477: 36, 478: 54, 479: 54, 480: 23,
         481: 49, 482: 23, 483: 23, 484: 98, 485: 98, 486: 98, 487: 142, 488: 23, 489: 49, 490: 23,
         491: 142, 492: 49, 493: 49, 494: 49, 495: 98, 496: 111, 497: 23, 498: 49, 499: 49, 500: 111,
         501: 111, 502: 67, 503: 67, 504: 111, 505: 62, 506: 111, 507: 36, 508: 49, 509: 49, 510: 49,
         511: 62, 512: 10, 513: 36, 514: 124, 515: 124, 516: 124, 517: 124, 518: 124, 519: 62, 520: 31,
         521: 124, 522: 31, 523: 124, 524: 31, 525: 31, 526: 80, 527: 80, 528: 31, 529: 31, 530: 124,
         531: 124, 532: 31, 533: 31, 534: 23, 535: 23, 536: 31, 537: 23, 538: 31, 539: 49, 540: 44,
         541: 44, 542: 44, 543: 137, 544: 18, 545: 44, 546: 31, 547: 31, 548: 93, 549: 93, 550: 93,
         551: 44, 552: 18, 553: 137, 554: 18, 555: 31, 556: 44, 557: 44, 558: 44, 559: 88, 560: 18,
         561: 44, 562: 44, 563: 44, 564: 18, 565: 18, 566: 62, 567: 62, 568: 106, 569: 57, 570: 106,
         571: 31, 572: 106, 573: 106, 574: 44, 575: 44, 576: 26, 577: 31, 578: 31, 579: 31, 580: 119,
         581: 119, 582: 119, 583: 31, 584: 119, 585: 57, 586: 119, 587: 119, 588: 119, 589: 119, 590: 57,
         591: 57, 592: 26, 593: 75, 594: 75, 595: 75, 596: 26, 597: 26, 598: 119, 599: 119, 600: 18,
         601: 57, 602: 18, 603: 70, 604: 18, 605: 18, 606: 44, 607: 44, 608: 26, 609: 132, 610: 39,
         611: 39, 612: 39, 613: 39, 614: 39, 615: 70, 616: 26, 617: 132, 618: 26, 619: 132, 620: 88,
         621: 88, 622: 88, 623: 132, 624: 39, 625: 26, 626: 132, 627: 132, 628: 39, 629: 39, 630: 39,
         631: 39, 632: 39, 633: 31, 634: 39, 635: 31, 636: 57, 637: 57, 638: 57, 639: 132, 640: 13,
         641: 52, 642: 26, 643: 26, 644: 101, 645: 101, 646: 101, 647: 39, 648: 26, 649: 145, 650: 26,
         651: 101, 652: 26, 653: 26, 654: 145, 655: 145, 656: 114, 657: 52, 658: 52, 659: 52, 660: 114,
         661: 114, 662: 26, 663: 26, 664: 114, 665: 52, 666: 114, 667: 145, 668: 70, 669: 70, 670: 70,
         671: 96, 672: 13, 673: 65, 674: 114, 675: 114, 676: 52, 677: 52, 678: 52, 679: 65, 680: 13,
         681: 65, 682: 13, 683: 39, 684: 127, 685: 127, 686: 127, 687: 39, 688: 34, 689: 127, 690: 127,
         691: 127, 692: 34, 693: 34, 694: 127, 695: 127, 696: 34, 697: 127, 698: 34, 699: 65, 700: 83,
         701: 83, 702: 83, 703: 171, 704: 21, 705: 34, 706: 127, 707: 127, 708: 34, 709: 34, 710: 34,
         711: 65, 712: 34, 713: 26, 714: 34, 715: 26, 716: 34, 717: 34, 718: 52, 719: 52, 720: 21,
         721: 47, 722: 47, 723: 47, 724: 21, 725: 21, 726: 47, 727: 47, 728: 96, 729: 34, 730: 96,
         731: 140, 732: 96, 733: 96, 734: 47, 735: 47, 736: 21, 737: 140, 738: 21, 739: 21, 740: 47,
         741: 47, 742: 47, 743: 96, 744: 21, 745: 91, 746: 21, 747: 47, 748: 47, 749: 47, 750: 47,
         751: 140, 752: 109, 753: 21, 754: 65, 755: 65, 756: 109, 757: 109, 758: 60, 759: 60, 760: 109,
         761: 34, 762: 109, 763: 153, 764: 47, 765: 47, 766: 47, 767: 60, 768: 16, 769: 34, 770: 34,
         771: 34, 772: 122, 773: 122, 774: 122, 775: 153, 776: 122, 777: 34, 778: 122, 779: 60, 780: 122,
         781: 122, 782: 122, 783: 122, 784: 29, 785: 122, 786: 60, 787: 60, 788: 29, 789: 29, 790: 78,
         791: 78, 792: 29, 793: 78, 794: 29, 795: 104, 796: 122, 797: 122, 798: 122, 799: 73, 800: 29,
         801: 60, 802: 21, 803: 21, 804: 21, 805: 21, 806: 21, 807: 73, 808: 29, 809: 47, 810: 29,
         811: 135, 812: 42, 813: 42, 814: 42, 815: 135, 816: 29, 817: 42, 818: 42, 819: 42, 820: 29,
         821: 29, 822: 135, 823: 135, 824: 91, 825: 135, 826: 91, 827: 42, 828: 91, 829: 91, 830: 135,
         831: 135, 832: 16, 833: 29, 834: 135, 835: 135, 836: 42, 837: 42, 838: 42, 839: 86, 840: 42,
         841: 42, 842: 42, 843: 42, 844: 42, 845: 42, 846: 34, 847: 34, 848: 16, 849: 60, 850: 60,
         851: 60, 852: 16, 853: 16, 854: 55, 855: 55, 856: 104, 857: 29, 858: 104, 859: 148, 860: 104,
         861: 104, 862: 42, 863: 42, 864: 117, 865: 148, 866: 29, 867: 29, 868: 29, 869: 29, 870: 29,
         871: 179, 872: 117, 873: 148, 874: 117, 875: 29, 876: 55, 877: 55, 878: 55, 879: 148, 880: 117,
         881: 117, 882: 29, 883: 29, 884: 117, 885: 117, 886: 55, 887: 55, 888: 73, 889: 148, 890: 73,
         891: 47, 892: 73, 893: 73, 894: 99, 895: 99, 896: 24, 897: 68, 898: 117, 899: 117, 900: 55,
         901: 55, 902: 55, 903: 117, 904: 16, 905: 68, 906: 16, 907: 55, 908: 16, 909: 16, 910: 42,
         911: 42, 912: 37, 913: 130, 914: 130, 915: 130, 916: 37, 917: 37, 918: 130, 919: 130, 920: 37,
         921: 130, 922: 37, 923: 68, 924: 130, 925: 130, 926: 130, 927: 117, 928: 24, 929: 130, 930: 37,
         931: 37, 932: 86, 933: 86, 934: 86, 935: 130, 936: 24, 937: 174, 938: 24, 939: 86, 940: 130,
         941: 130, 942: 130, 943: 37, 944: 37, 945: 37, 946: 37, 947: 37, 948: 37, 949: 37, 950: 29,
         951: 29, 952: 37, 953: 29, 954: 37, 955: 29, 956: 55, 957: 55, 958: 55, 959: 130, 960: 24,
         961: 50, 962: 50, 963: 50, 964: 24, 965: 24, 966: 24, 967: 143, 968: 99, 969: 50, 970: 99,
         971: 37, 972: 99, 973: 99, 974: 143, 975: 143, 976: 24, 977: 99, 978: 50, 979: 50, 980: 24,
         981: 24, 982: 143, 983: 143, 984: 50, 985: 24, 986: 50, 987: 37, 988: 50, 989: 50, 990: 99,
         991: 99, 992: 112, 993: 94, 994: 24, 995: 24, 996: 50, 997: 50, 998: 50, 999: 50, 1000: 112}

# -------------------------------------------------------
# cache of collatz values 1 to 10000 in intervals of 1000
# key represents first number of the interval
# -------------------------------------------------------
interval_cache = {1: 179, 1001: 182, 2001: 217, 3001: 238,
                  4001: 215, 5001: 236, 6001: 262, 7001: 252, 8001: 247, 9001: 260}


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
    try:
        return [int(a[0]), int(a[1])]
    except:
        sys.exit()


# -------------------
# collatz_eval_helper
# -------------------

def collatz_eval_helper(s):
    """
    s is an integer
    returns cycle length of s
    """
    count = 0
    x = s
    if s == 1:
        return 1
    elif s > 0:
        while s != 1:
            if s in cache:
                cache.update({x: count+cache[s]})
                return cache[s]+count
            elif s % 2 == 0:
                s = s//2
            else:
                s = 3*s+1
            count += 1
        cache.update({x: count})
        return count
    else:
        return count


def collatz_interval(i, j):
    """
    i the beginning of the range, inclusive
    j the end       of the range, inclusive
    updates interval_cache after finding max cycle length of 1000 integers
    return the max cycle length of the range [i, j]
    """
    l = []
    for x in range(i, j+1):
        l.append(collatz_eval_helper(x))
    interval_cache.update({i: max(l)})
    return max(l)

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
    assert 0 <= i < 1000000
    assert 0 <= j < 1000000
    l = []
    if i > j:
        i, j = j, i
    if i == j:
        l.append(collatz_eval_helper(i))
    while i < j:
        if i > 1 and i % 1000 == 1:
            if i in interval_cache and j >= i+999:
                l.append(interval_cache[i])
            elif j > i+999:
                l.append(collatz_interval(i, i+999))
            i = i + 1000
        elif i == 1 and j >= i+999:
            l.append(interval_cache[i])
            i = i+1000
        else:
            l.append(collatz_eval_helper(i))
            i += 1
    assert max(l) >= 0
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
