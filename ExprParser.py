# Generated from ./Expr.g4 by ANTLR 4.13.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,91,560,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,2,19,7,19,2,20,
        7,20,2,21,7,21,2,22,7,22,2,23,7,23,2,24,7,24,1,0,1,0,1,0,5,0,54,
        8,0,10,0,12,0,57,9,0,1,0,3,0,60,8,0,1,0,1,0,1,1,1,1,1,1,1,1,1,1,
        5,1,69,8,1,10,1,12,1,72,9,1,1,1,3,1,75,8,1,3,1,77,8,1,1,1,1,1,1,
        1,1,1,1,1,3,1,84,8,1,1,1,1,1,1,1,1,1,3,1,90,8,1,5,1,92,8,1,10,1,
        12,1,95,9,1,1,1,3,1,98,8,1,1,1,1,1,1,1,1,1,3,1,104,8,1,1,1,1,1,1,
        1,1,1,1,1,5,1,111,8,1,10,1,12,1,114,9,1,1,1,3,1,117,8,1,3,1,119,
        8,1,1,1,1,1,3,1,123,8,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,3,1,133,
        8,1,1,1,1,1,5,1,137,8,1,10,1,12,1,140,9,1,1,1,1,1,1,1,1,1,1,1,1,
        1,1,1,1,1,3,1,150,8,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,
        1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,3,1,171,8,1,1,1,1,1,1,1,1,1,1,
        1,1,1,1,1,1,1,1,1,1,1,1,1,3,1,184,8,1,1,1,1,1,1,1,1,1,1,1,1,1,1,
        1,1,1,3,1,194,8,1,1,1,1,1,3,1,198,8,1,1,1,1,1,3,1,202,8,1,1,1,1,
        1,1,1,1,1,1,1,1,1,1,1,1,1,5,1,212,8,1,10,1,12,1,215,9,1,1,1,3,1,
        218,8,1,1,1,5,1,221,8,1,10,1,12,1,224,9,1,1,1,1,1,1,1,1,1,1,1,1,
        1,1,1,1,1,3,1,234,8,1,1,1,3,1,237,8,1,1,1,1,1,3,1,241,8,1,1,1,1,
        1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,3,1,254,8,1,1,1,1,1,1,1,1,
        1,1,1,1,1,1,1,1,1,5,1,264,8,1,10,1,12,1,267,9,1,1,1,3,1,270,8,1,
        1,1,1,1,1,1,1,1,3,1,276,8,1,1,1,1,1,1,1,3,1,281,8,1,1,1,1,1,1,1,
        1,1,1,1,1,1,1,1,1,1,1,1,3,1,292,8,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,
        1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,
        1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,
        1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,3,1,341,8,1,1,1,1,1,1,1,1,1,1,1,
        3,1,348,8,1,1,1,1,1,1,1,3,1,353,8,1,1,1,1,1,1,1,5,1,358,8,1,10,1,
        12,1,361,9,1,1,2,1,2,1,3,1,3,1,4,1,4,1,4,1,4,1,4,5,4,372,8,4,10,
        4,12,4,375,9,4,3,4,377,8,4,1,4,3,4,380,8,4,1,5,1,5,1,5,5,5,385,8,
        5,10,5,12,5,388,9,5,1,6,3,6,391,8,6,1,6,1,6,1,6,3,6,396,8,6,1,7,
        3,7,399,8,7,1,7,1,7,3,7,403,8,7,1,7,3,7,406,8,7,1,8,3,8,409,8,8,
        1,8,1,8,1,8,3,8,414,8,8,1,8,1,8,1,8,1,8,1,8,5,8,421,8,8,10,8,12,
        8,424,9,8,1,8,3,8,427,8,8,3,8,429,8,8,1,8,1,8,1,9,1,9,1,9,3,9,436,
        8,9,1,10,1,10,1,11,1,11,1,11,1,11,1,11,3,11,445,8,11,5,11,447,8,
        11,10,11,12,11,450,9,11,1,12,1,12,1,12,1,12,3,12,456,8,12,5,12,458,
        8,12,10,12,12,12,461,9,12,1,13,1,13,1,13,1,13,3,13,467,8,13,1,13,
        1,13,1,13,1,13,3,13,473,8,13,5,13,475,8,13,10,13,12,13,478,9,13,
        1,13,3,13,481,8,13,1,14,1,14,1,14,5,14,486,8,14,10,14,12,14,489,
        9,14,1,15,1,15,1,15,5,15,494,8,15,10,15,12,15,497,9,15,1,16,3,16,
        500,8,16,1,16,1,16,1,17,1,17,1,17,1,17,1,17,1,17,1,17,1,17,1,17,
        1,17,3,17,514,8,17,1,18,1,18,1,19,1,19,3,19,520,8,19,1,19,1,19,1,
        20,1,20,1,20,5,20,527,8,20,10,20,12,20,530,9,20,1,21,3,21,533,8,
        21,1,21,1,21,1,22,1,22,3,22,539,8,22,1,22,1,22,1,23,1,23,1,23,5,
        23,546,8,23,10,23,12,23,549,9,23,1,24,1,24,1,24,1,24,1,24,1,24,1,
        24,3,24,558,8,24,1,24,0,1,2,25,0,2,4,6,8,10,12,14,16,18,20,22,24,
        26,28,30,32,34,36,38,40,42,44,46,48,0,10,1,0,53,54,4,0,34,34,36,
        37,56,57,73,73,1,0,58,60,1,0,56,57,3,0,35,35,38,38,65,68,1,0,61,
        64,1,0,1,3,1,0,46,52,2,0,11,11,86,88,2,0,31,33,86,87,650,0,50,1,
        0,0,0,2,291,1,0,0,0,4,362,1,0,0,0,6,364,1,0,0,0,8,379,1,0,0,0,10,
        381,1,0,0,0,12,390,1,0,0,0,14,405,1,0,0,0,16,408,1,0,0,0,18,432,
        1,0,0,0,20,437,1,0,0,0,22,439,1,0,0,0,24,451,1,0,0,0,26,480,1,0,
        0,0,28,482,1,0,0,0,30,490,1,0,0,0,32,499,1,0,0,0,34,513,1,0,0,0,
        36,515,1,0,0,0,38,517,1,0,0,0,40,523,1,0,0,0,42,532,1,0,0,0,44,536,
        1,0,0,0,46,542,1,0,0,0,48,557,1,0,0,0,50,55,3,2,1,0,51,52,5,81,0,
        0,52,54,3,2,1,0,53,51,1,0,0,0,54,57,1,0,0,0,55,53,1,0,0,0,55,56,
        1,0,0,0,56,59,1,0,0,0,57,55,1,0,0,0,58,60,5,81,0,0,59,58,1,0,0,0,
        59,60,1,0,0,0,60,61,1,0,0,0,61,62,5,0,0,1,62,1,1,0,0,0,63,64,6,1,
        -1,0,64,76,5,77,0,0,65,70,3,2,1,0,66,67,5,81,0,0,67,69,3,2,1,0,68,
        66,1,0,0,0,69,72,1,0,0,0,70,68,1,0,0,0,70,71,1,0,0,0,71,74,1,0,0,
        0,72,70,1,0,0,0,73,75,5,81,0,0,74,73,1,0,0,0,74,75,1,0,0,0,75,77,
        1,0,0,0,76,65,1,0,0,0,76,77,1,0,0,0,77,78,1,0,0,0,78,292,5,78,0,
        0,79,80,3,4,2,0,80,83,5,88,0,0,81,82,5,52,0,0,82,84,3,2,1,0,83,81,
        1,0,0,0,83,84,1,0,0,0,84,93,1,0,0,0,85,86,5,82,0,0,86,89,5,88,0,
        0,87,88,5,52,0,0,88,90,3,2,1,0,89,87,1,0,0,0,89,90,1,0,0,0,90,92,
        1,0,0,0,91,85,1,0,0,0,92,95,1,0,0,0,93,91,1,0,0,0,93,94,1,0,0,0,
        94,292,1,0,0,0,95,93,1,0,0,0,96,98,5,5,0,0,97,96,1,0,0,0,97,98,1,
        0,0,0,98,99,1,0,0,0,99,100,5,4,0,0,100,101,5,88,0,0,101,103,5,75,
        0,0,102,104,3,10,5,0,103,102,1,0,0,0,103,104,1,0,0,0,104,105,1,0,
        0,0,105,106,5,76,0,0,106,118,5,77,0,0,107,112,3,2,1,0,108,109,5,
        81,0,0,109,111,3,2,1,0,110,108,1,0,0,0,111,114,1,0,0,0,112,110,1,
        0,0,0,112,113,1,0,0,0,113,116,1,0,0,0,114,112,1,0,0,0,115,117,5,
        81,0,0,116,115,1,0,0,0,116,117,1,0,0,0,117,119,1,0,0,0,118,107,1,
        0,0,0,118,119,1,0,0,0,119,120,1,0,0,0,120,292,5,78,0,0,121,123,5,
        5,0,0,122,121,1,0,0,0,122,123,1,0,0,0,123,124,1,0,0,0,124,125,3,
        8,4,0,125,126,5,45,0,0,126,127,3,2,1,38,127,292,1,0,0,0,128,129,
        5,9,0,0,129,132,5,88,0,0,130,131,5,10,0,0,131,133,3,2,1,0,132,130,
        1,0,0,0,132,133,1,0,0,0,133,134,1,0,0,0,134,138,5,77,0,0,135,137,
        3,14,7,0,136,135,1,0,0,0,137,140,1,0,0,0,138,136,1,0,0,0,138,139,
        1,0,0,0,139,141,1,0,0,0,140,138,1,0,0,0,141,292,5,78,0,0,142,143,
        5,16,0,0,143,144,5,75,0,0,144,145,3,2,1,0,145,146,5,76,0,0,146,149,
        3,2,1,0,147,148,5,17,0,0,148,150,3,2,1,0,149,147,1,0,0,0,149,150,
        1,0,0,0,150,292,1,0,0,0,151,152,5,19,0,0,152,153,5,75,0,0,153,154,
        3,2,1,0,154,155,5,76,0,0,155,156,3,2,1,35,156,292,1,0,0,0,157,158,
        5,20,0,0,158,159,3,2,1,0,159,160,5,19,0,0,160,161,5,75,0,0,161,162,
        3,2,1,0,162,163,5,76,0,0,163,292,1,0,0,0,164,165,5,18,0,0,165,170,
        5,75,0,0,166,167,3,4,2,0,167,168,5,88,0,0,168,171,1,0,0,0,169,171,
        5,88,0,0,170,166,1,0,0,0,170,169,1,0,0,0,171,172,1,0,0,0,172,173,
        5,38,0,0,173,174,3,2,1,0,174,175,5,76,0,0,175,176,3,2,1,33,176,292,
        1,0,0,0,177,178,5,18,0,0,178,183,5,75,0,0,179,180,3,4,2,0,180,181,
        5,88,0,0,181,184,1,0,0,0,182,184,5,88,0,0,183,179,1,0,0,0,183,182,
        1,0,0,0,184,185,1,0,0,0,185,186,5,44,0,0,186,187,3,2,1,0,187,188,
        5,76,0,0,188,189,3,2,1,32,189,292,1,0,0,0,190,191,5,18,0,0,191,193,
        5,75,0,0,192,194,3,26,13,0,193,192,1,0,0,0,193,194,1,0,0,0,194,195,
        1,0,0,0,195,197,5,81,0,0,196,198,3,2,1,0,197,196,1,0,0,0,197,198,
        1,0,0,0,198,199,1,0,0,0,199,201,5,81,0,0,200,202,3,28,14,0,201,200,
        1,0,0,0,201,202,1,0,0,0,202,203,1,0,0,0,203,204,5,76,0,0,204,292,
        3,2,1,31,205,206,5,21,0,0,206,207,5,75,0,0,207,208,3,2,1,0,208,209,
        5,76,0,0,209,213,5,77,0,0,210,212,3,22,11,0,211,210,1,0,0,0,212,
        215,1,0,0,0,213,211,1,0,0,0,213,214,1,0,0,0,214,217,1,0,0,0,215,
        213,1,0,0,0,216,218,3,24,12,0,217,216,1,0,0,0,217,218,1,0,0,0,218,
        222,1,0,0,0,219,221,3,22,11,0,220,219,1,0,0,0,221,224,1,0,0,0,222,
        220,1,0,0,0,222,223,1,0,0,0,223,225,1,0,0,0,224,222,1,0,0,0,225,
        226,5,78,0,0,226,292,1,0,0,0,227,228,5,27,0,0,228,236,3,2,1,0,229,
        233,5,28,0,0,230,231,5,75,0,0,231,232,5,88,0,0,232,234,5,76,0,0,
        233,230,1,0,0,0,233,234,1,0,0,0,234,235,1,0,0,0,235,237,3,2,1,0,
        236,229,1,0,0,0,236,237,1,0,0,0,237,240,1,0,0,0,238,239,5,29,0,0,
        239,241,3,2,1,0,240,238,1,0,0,0,240,241,1,0,0,0,241,292,1,0,0,0,
        242,243,5,39,0,0,243,244,5,75,0,0,244,245,3,2,1,0,245,246,5,76,0,
        0,246,247,3,2,1,28,247,292,1,0,0,0,248,292,5,41,0,0,249,250,5,30,
        0,0,250,292,3,2,1,26,251,253,5,26,0,0,252,254,3,2,1,0,253,252,1,
        0,0,0,253,254,1,0,0,0,254,292,1,0,0,0,255,292,5,24,0,0,256,292,5,
        25,0,0,257,269,5,7,0,0,258,270,5,88,0,0,259,260,5,77,0,0,260,265,
        5,88,0,0,261,262,5,82,0,0,262,264,5,88,0,0,263,261,1,0,0,0,264,267,
        1,0,0,0,265,263,1,0,0,0,265,266,1,0,0,0,266,268,1,0,0,0,267,265,
        1,0,0,0,268,270,5,78,0,0,269,258,1,0,0,0,269,259,1,0,0,0,270,271,
        1,0,0,0,271,272,5,42,0,0,272,292,5,87,0,0,273,275,5,8,0,0,274,276,
        5,23,0,0,275,274,1,0,0,0,275,276,1,0,0,0,276,277,1,0,0,0,277,280,
        3,2,1,0,278,279,5,43,0,0,279,281,5,88,0,0,280,278,1,0,0,0,280,281,
        1,0,0,0,281,292,1,0,0,0,282,283,5,14,0,0,283,292,3,2,1,16,284,285,
        7,0,0,0,285,292,3,2,1,14,286,287,7,1,0,0,287,292,3,2,1,13,288,289,
        5,6,0,0,289,292,3,2,1,12,290,292,3,34,17,0,291,63,1,0,0,0,291,79,
        1,0,0,0,291,97,1,0,0,0,291,122,1,0,0,0,291,128,1,0,0,0,291,142,1,
        0,0,0,291,151,1,0,0,0,291,157,1,0,0,0,291,164,1,0,0,0,291,177,1,
        0,0,0,291,190,1,0,0,0,291,205,1,0,0,0,291,227,1,0,0,0,291,242,1,
        0,0,0,291,248,1,0,0,0,291,249,1,0,0,0,291,251,1,0,0,0,291,255,1,
        0,0,0,291,256,1,0,0,0,291,257,1,0,0,0,291,273,1,0,0,0,291,282,1,
        0,0,0,291,284,1,0,0,0,291,286,1,0,0,0,291,288,1,0,0,0,291,290,1,
        0,0,0,292,359,1,0,0,0,293,294,10,11,0,0,294,295,5,55,0,0,295,358,
        3,2,1,11,296,297,10,10,0,0,297,298,7,2,0,0,298,358,3,2,1,11,299,
        300,10,9,0,0,300,301,7,3,0,0,301,358,3,2,1,10,302,303,10,8,0,0,303,
        304,7,4,0,0,304,358,3,2,1,9,305,306,10,7,0,0,306,307,7,5,0,0,307,
        358,3,2,1,8,308,309,10,6,0,0,309,310,5,71,0,0,310,358,3,2,1,7,311,
        312,10,5,0,0,312,313,5,72,0,0,313,358,3,2,1,6,314,315,10,4,0,0,315,
        316,5,70,0,0,316,358,3,2,1,5,317,318,10,3,0,0,318,319,5,85,0,0,319,
        320,3,2,1,0,320,321,5,84,0,0,321,322,3,2,1,3,322,358,1,0,0,0,323,
        324,10,2,0,0,324,325,3,6,3,0,325,326,3,2,1,2,326,358,1,0,0,0,327,
        328,10,20,0,0,328,329,5,83,0,0,329,358,5,88,0,0,330,331,10,19,0,
        0,331,332,5,79,0,0,332,333,3,2,1,0,333,334,5,80,0,0,334,358,1,0,
        0,0,335,336,10,18,0,0,336,347,5,69,0,0,337,348,5,88,0,0,338,340,
        5,75,0,0,339,341,3,30,15,0,340,339,1,0,0,0,340,341,1,0,0,0,341,342,
        1,0,0,0,342,348,5,76,0,0,343,344,5,79,0,0,344,345,3,2,1,0,345,346,
        5,80,0,0,346,348,1,0,0,0,347,337,1,0,0,0,347,338,1,0,0,0,347,343,
        1,0,0,0,348,358,1,0,0,0,349,350,10,17,0,0,350,352,5,75,0,0,351,353,
        3,30,15,0,352,351,1,0,0,0,352,353,1,0,0,0,353,354,1,0,0,0,354,358,
        5,76,0,0,355,356,10,15,0,0,356,358,7,0,0,0,357,293,1,0,0,0,357,296,
        1,0,0,0,357,299,1,0,0,0,357,302,1,0,0,0,357,305,1,0,0,0,357,308,
        1,0,0,0,357,311,1,0,0,0,357,314,1,0,0,0,357,317,1,0,0,0,357,323,
        1,0,0,0,357,327,1,0,0,0,357,330,1,0,0,0,357,335,1,0,0,0,357,349,
        1,0,0,0,357,355,1,0,0,0,358,361,1,0,0,0,359,357,1,0,0,0,359,360,
        1,0,0,0,360,3,1,0,0,0,361,359,1,0,0,0,362,363,7,6,0,0,363,5,1,0,
        0,0,364,365,7,7,0,0,365,7,1,0,0,0,366,380,5,88,0,0,367,376,5,75,
        0,0,368,373,3,12,6,0,369,370,5,82,0,0,370,372,3,12,6,0,371,369,1,
        0,0,0,372,375,1,0,0,0,373,371,1,0,0,0,373,374,1,0,0,0,374,377,1,
        0,0,0,375,373,1,0,0,0,376,368,1,0,0,0,376,377,1,0,0,0,377,378,1,
        0,0,0,378,380,5,76,0,0,379,366,1,0,0,0,379,367,1,0,0,0,380,9,1,0,
        0,0,381,386,3,12,6,0,382,383,5,82,0,0,383,385,3,12,6,0,384,382,1,
        0,0,0,385,388,1,0,0,0,386,384,1,0,0,0,386,387,1,0,0,0,387,11,1,0,
        0,0,388,386,1,0,0,0,389,391,5,74,0,0,390,389,1,0,0,0,390,391,1,0,
        0,0,391,392,1,0,0,0,392,395,5,88,0,0,393,394,5,52,0,0,394,396,3,
        2,1,0,395,393,1,0,0,0,395,396,1,0,0,0,396,13,1,0,0,0,397,399,5,15,
        0,0,398,397,1,0,0,0,398,399,1,0,0,0,399,400,1,0,0,0,400,406,3,16,
        8,0,401,403,5,15,0,0,402,401,1,0,0,0,402,403,1,0,0,0,403,404,1,0,
        0,0,404,406,3,18,9,0,405,398,1,0,0,0,405,402,1,0,0,0,406,15,1,0,
        0,0,407,409,5,5,0,0,408,407,1,0,0,0,408,409,1,0,0,0,409,410,1,0,
        0,0,410,411,3,20,10,0,411,413,5,75,0,0,412,414,3,10,5,0,413,412,
        1,0,0,0,413,414,1,0,0,0,414,415,1,0,0,0,415,416,5,76,0,0,416,428,
        5,77,0,0,417,422,3,2,1,0,418,419,5,81,0,0,419,421,3,2,1,0,420,418,
        1,0,0,0,421,424,1,0,0,0,422,420,1,0,0,0,422,423,1,0,0,0,423,426,
        1,0,0,0,424,422,1,0,0,0,425,427,5,81,0,0,426,425,1,0,0,0,426,427,
        1,0,0,0,427,429,1,0,0,0,428,417,1,0,0,0,428,429,1,0,0,0,429,430,
        1,0,0,0,430,431,5,78,0,0,431,17,1,0,0,0,432,435,3,20,10,0,433,434,
        5,52,0,0,434,436,3,2,1,0,435,433,1,0,0,0,435,436,1,0,0,0,436,19,
        1,0,0,0,437,438,7,8,0,0,438,21,1,0,0,0,439,440,5,22,0,0,440,441,
        3,2,1,0,441,448,5,84,0,0,442,444,3,2,1,0,443,445,5,81,0,0,444,443,
        1,0,0,0,444,445,1,0,0,0,445,447,1,0,0,0,446,442,1,0,0,0,447,450,
        1,0,0,0,448,446,1,0,0,0,448,449,1,0,0,0,449,23,1,0,0,0,450,448,1,
        0,0,0,451,452,5,23,0,0,452,459,5,84,0,0,453,455,3,2,1,0,454,456,
        5,81,0,0,455,454,1,0,0,0,455,456,1,0,0,0,456,458,1,0,0,0,457,453,
        1,0,0,0,458,461,1,0,0,0,459,457,1,0,0,0,459,460,1,0,0,0,460,25,1,
        0,0,0,461,459,1,0,0,0,462,463,3,4,2,0,463,466,5,88,0,0,464,465,5,
        52,0,0,465,467,3,2,1,0,466,464,1,0,0,0,466,467,1,0,0,0,467,476,1,
        0,0,0,468,469,5,82,0,0,469,472,5,88,0,0,470,471,5,52,0,0,471,473,
        3,2,1,0,472,470,1,0,0,0,472,473,1,0,0,0,473,475,1,0,0,0,474,468,
        1,0,0,0,475,478,1,0,0,0,476,474,1,0,0,0,476,477,1,0,0,0,477,481,
        1,0,0,0,478,476,1,0,0,0,479,481,3,2,1,0,480,462,1,0,0,0,480,479,
        1,0,0,0,481,27,1,0,0,0,482,487,3,2,1,0,483,484,5,82,0,0,484,486,
        3,2,1,0,485,483,1,0,0,0,486,489,1,0,0,0,487,485,1,0,0,0,487,488,
        1,0,0,0,488,29,1,0,0,0,489,487,1,0,0,0,490,495,3,32,16,0,491,492,
        5,82,0,0,492,494,3,32,16,0,493,491,1,0,0,0,494,497,1,0,0,0,495,493,
        1,0,0,0,495,496,1,0,0,0,496,31,1,0,0,0,497,495,1,0,0,0,498,500,5,
        74,0,0,499,498,1,0,0,0,499,500,1,0,0,0,500,501,1,0,0,0,501,502,3,
        2,1,0,502,33,1,0,0,0,503,514,5,12,0,0,504,514,5,13,0,0,505,514,5,
        88,0,0,506,514,3,36,18,0,507,514,3,38,19,0,508,514,3,44,22,0,509,
        510,5,75,0,0,510,511,3,2,1,0,511,512,5,76,0,0,512,514,1,0,0,0,513,
        503,1,0,0,0,513,504,1,0,0,0,513,505,1,0,0,0,513,506,1,0,0,0,513,
        507,1,0,0,0,513,508,1,0,0,0,513,509,1,0,0,0,514,35,1,0,0,0,515,516,
        7,9,0,0,516,37,1,0,0,0,517,519,5,79,0,0,518,520,3,40,20,0,519,518,
        1,0,0,0,519,520,1,0,0,0,520,521,1,0,0,0,521,522,5,80,0,0,522,39,
        1,0,0,0,523,528,3,42,21,0,524,525,5,82,0,0,525,527,3,42,21,0,526,
        524,1,0,0,0,527,530,1,0,0,0,528,526,1,0,0,0,528,529,1,0,0,0,529,
        41,1,0,0,0,530,528,1,0,0,0,531,533,5,74,0,0,532,531,1,0,0,0,532,
        533,1,0,0,0,533,534,1,0,0,0,534,535,3,2,1,0,535,43,1,0,0,0,536,538,
        5,77,0,0,537,539,3,46,23,0,538,537,1,0,0,0,538,539,1,0,0,0,539,540,
        1,0,0,0,540,541,5,78,0,0,541,45,1,0,0,0,542,547,3,48,24,0,543,544,
        5,82,0,0,544,546,3,48,24,0,545,543,1,0,0,0,546,549,1,0,0,0,547,545,
        1,0,0,0,547,548,1,0,0,0,548,47,1,0,0,0,549,547,1,0,0,0,550,551,3,
        20,10,0,551,552,5,84,0,0,552,553,3,2,1,0,553,558,1,0,0,0,554,555,
        5,74,0,0,555,558,3,2,1,0,556,558,5,88,0,0,557,550,1,0,0,0,557,554,
        1,0,0,0,557,556,1,0,0,0,558,49,1,0,0,0,72,55,59,70,74,76,83,89,93,
        97,103,112,116,118,122,132,138,149,170,183,193,197,201,213,217,222,
        233,236,240,253,265,269,275,280,291,340,347,352,357,359,373,376,
        379,386,390,395,398,402,405,408,413,422,426,428,435,444,448,455,
        459,466,472,476,480,487,495,499,513,519,528,532,538,547,557
    ]

class ExprParser ( Parser ):

    grammarFileName = "Expr.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'var'", "'let'", "'const'", "'function'", 
                     "'async'", "'await'", "'import'", "'export'", "'class'", 
                     "'extends'", "'constructor'", "'this'", "'super'", 
                     "'new'", "'static'", "'if'", "'else'", "'for'", "'while'", 
                     "'do'", "'switch'", "'case'", "'default'", "'break'", 
                     "'continue'", "'return'", "'try'", "'catch'", "'finally'", 
                     "'throw'", "'true'", "'false'", "'null'", "'typeof'", 
                     "'instanceof'", "'delete'", "'void'", "'in'", "'with'", 
                     "'enum'", "'debugger'", "'from'", "'as'", "'of'", "'=>'", 
                     "'+='", "'-='", "'*='", "'/='", "'%='", "'**='", "'='", 
                     "'++'", "'--'", "'**'", "'+'", "'-'", "'*'", "'/'", 
                     "'%'", "'==='", "'!=='", "'=='", "'!='", "'>='", "'<='", 
                     "'>'", "'<'", "'?.'", "'??'", "'&&'", "'||'", "'!'", 
                     "'...'", "'('", "')'", "'{'", "'}'", "'['", "']'", 
                     "';'", "','", "'.'", "':'", "'?'" ]

    symbolicNames = [ "<INVALID>", "VAR", "LET", "CONST", "FUNCTION", "ASYNC", 
                      "AWAIT", "IMPORT", "EXPORT", "CLASS", "EXTENDS", "CONSTRUCTOR", 
                      "THIS", "SUPER", "NEW", "STATIC", "IF", "ELSE", "FOR", 
                      "WHILE", "DO", "SWITCH", "CASE", "DEFAULT", "BREAK", 
                      "CONTINUE", "RETURN", "TRY", "CATCH", "FINALLY", "THROW", 
                      "TRUE", "FALSE", "NULL", "TYPEOF", "INSTANCEOF", "DELETE", 
                      "VOID", "IN", "WITH", "ENUM", "DEBUGGER", "FROM", 
                      "AS", "OF", "ARROW", "ASSIGN_ADD", "ASSIGN_SUB", "ASSIGN_MUL", 
                      "ASSIGN_DIV", "ASSIGN_MOD", "ASSIGN_EXP", "ASIG", 
                      "INC", "DEC", "EXP", "MAS", "MENOS", "MULT", "DIV", 
                      "MOD", "STRICT_EQ", "STRICT_NE", "EQU", "NEQ", "BE", 
                      "LE", "BIG", "LESS", "OPTIONAL_CHAIN", "NULLISH", 
                      "AND", "OR", "NOT", "ELLIPSIS", "PI", "PD", "LI", 
                      "LD", "CI", "CD", "PC", "C", "P", "DP", "Q", "NUM", 
                      "CADENA", "ID", "WS", "LINE_COMMENT", "BLOCK_COMMENT" ]

    RULE_root = 0
    RULE_expr = 1
    RULE_variableModifier = 2
    RULE_assignmentOperator = 3
    RULE_arrowParams = 4
    RULE_paramList = 5
    RULE_param = 6
    RULE_classMember = 7
    RULE_methodDefinition = 8
    RULE_fieldDefinition = 9
    RULE_propertyName = 10
    RULE_caseClause = 11
    RULE_defaultClause = 12
    RULE_forInit = 13
    RULE_forUpdate = 14
    RULE_argumentList = 15
    RULE_argument = 16
    RULE_primaryExpr = 17
    RULE_literal = 18
    RULE_arrayLiteral = 19
    RULE_elementList = 20
    RULE_elementItem = 21
    RULE_objectLiteral = 22
    RULE_propertyList = 23
    RULE_property = 24

    ruleNames =  [ "root", "expr", "variableModifier", "assignmentOperator", 
                   "arrowParams", "paramList", "param", "classMember", "methodDefinition", 
                   "fieldDefinition", "propertyName", "caseClause", "defaultClause", 
                   "forInit", "forUpdate", "argumentList", "argument", "primaryExpr", 
                   "literal", "arrayLiteral", "elementList", "elementItem", 
                   "objectLiteral", "propertyList", "property" ]

    EOF = Token.EOF
    VAR=1
    LET=2
    CONST=3
    FUNCTION=4
    ASYNC=5
    AWAIT=6
    IMPORT=7
    EXPORT=8
    CLASS=9
    EXTENDS=10
    CONSTRUCTOR=11
    THIS=12
    SUPER=13
    NEW=14
    STATIC=15
    IF=16
    ELSE=17
    FOR=18
    WHILE=19
    DO=20
    SWITCH=21
    CASE=22
    DEFAULT=23
    BREAK=24
    CONTINUE=25
    RETURN=26
    TRY=27
    CATCH=28
    FINALLY=29
    THROW=30
    TRUE=31
    FALSE=32
    NULL=33
    TYPEOF=34
    INSTANCEOF=35
    DELETE=36
    VOID=37
    IN=38
    WITH=39
    ENUM=40
    DEBUGGER=41
    FROM=42
    AS=43
    OF=44
    ARROW=45
    ASSIGN_ADD=46
    ASSIGN_SUB=47
    ASSIGN_MUL=48
    ASSIGN_DIV=49
    ASSIGN_MOD=50
    ASSIGN_EXP=51
    ASIG=52
    INC=53
    DEC=54
    EXP=55
    MAS=56
    MENOS=57
    MULT=58
    DIV=59
    MOD=60
    STRICT_EQ=61
    STRICT_NE=62
    EQU=63
    NEQ=64
    BE=65
    LE=66
    BIG=67
    LESS=68
    OPTIONAL_CHAIN=69
    NULLISH=70
    AND=71
    OR=72
    NOT=73
    ELLIPSIS=74
    PI=75
    PD=76
    LI=77
    LD=78
    CI=79
    CD=80
    PC=81
    C=82
    P=83
    DP=84
    Q=85
    NUM=86
    CADENA=87
    ID=88
    WS=89
    LINE_COMMENT=90
    BLOCK_COMMENT=91

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class RootContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ExprParser.ExprContext)
            else:
                return self.getTypedRuleContext(ExprParser.ExprContext,i)


        def EOF(self):
            return self.getToken(ExprParser.EOF, 0)

        def PC(self, i:int=None):
            if i is None:
                return self.getTokens(ExprParser.PC)
            else:
                return self.getToken(ExprParser.PC, i)

        def getRuleIndex(self):
            return ExprParser.RULE_root




    def root(self):

        localctx = ExprParser.RootContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_root)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 50
            self.expr(0)
            self.state = 55
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,0,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 51
                    self.match(ExprParser.PC)
                    self.state = 52
                    self.expr(0) 
                self.state = 57
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,0,self._ctx)

            self.state = 59
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==81:
                self.state = 58
                self.match(ExprParser.PC)


            self.state = 61
            self.match(ExprParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return ExprParser.RULE_expr

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)


    class FunctionDeclContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ExprParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def FUNCTION(self):
            return self.getToken(ExprParser.FUNCTION, 0)
        def ID(self):
            return self.getToken(ExprParser.ID, 0)
        def PI(self):
            return self.getToken(ExprParser.PI, 0)
        def PD(self):
            return self.getToken(ExprParser.PD, 0)
        def LI(self):
            return self.getToken(ExprParser.LI, 0)
        def LD(self):
            return self.getToken(ExprParser.LD, 0)
        def ASYNC(self):
            return self.getToken(ExprParser.ASYNC, 0)
        def paramList(self):
            return self.getTypedRuleContext(ExprParser.ParamListContext,0)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ExprParser.ExprContext)
            else:
                return self.getTypedRuleContext(ExprParser.ExprContext,i)

        def PC(self, i:int=None):
            if i is None:
                return self.getTokens(ExprParser.PC)
            else:
                return self.getToken(ExprParser.PC, i)


    class NewExprContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ExprParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def NEW(self):
            return self.getToken(ExprParser.NEW, 0)
        def expr(self):
            return self.getTypedRuleContext(ExprParser.ExprContext,0)



    class AssignmentExprContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ExprParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ExprParser.ExprContext)
            else:
                return self.getTypedRuleContext(ExprParser.ExprContext,i)

        def assignmentOperator(self):
            return self.getTypedRuleContext(ExprParser.AssignmentOperatorContext,0)



    class DebuggerExprContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ExprParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def DEBUGGER(self):
            return self.getToken(ExprParser.DEBUGGER, 0)


    class MultiplicativeContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ExprParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ExprParser.ExprContext)
            else:
                return self.getTypedRuleContext(ExprParser.ExprContext,i)

        def MULT(self):
            return self.getToken(ExprParser.MULT, 0)
        def DIV(self):
            return self.getToken(ExprParser.DIV, 0)
        def MOD(self):
            return self.getToken(ExprParser.MOD, 0)


    class BreakExprContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ExprParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def BREAK(self):
            return self.getToken(ExprParser.BREAK, 0)


    class ForInExprContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ExprParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def FOR(self):
            return self.getToken(ExprParser.FOR, 0)
        def PI(self):
            return self.getToken(ExprParser.PI, 0)
        def IN(self):
            return self.getToken(ExprParser.IN, 0)
        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ExprParser.ExprContext)
            else:
                return self.getTypedRuleContext(ExprParser.ExprContext,i)

        def PD(self):
            return self.getToken(ExprParser.PD, 0)
        def variableModifier(self):
            return self.getTypedRuleContext(ExprParser.VariableModifierContext,0)

        def ID(self):
            return self.getToken(ExprParser.ID, 0)


    class SwitchExprContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ExprParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def SWITCH(self):
            return self.getToken(ExprParser.SWITCH, 0)
        def PI(self):
            return self.getToken(ExprParser.PI, 0)
        def expr(self):
            return self.getTypedRuleContext(ExprParser.ExprContext,0)

        def PD(self):
            return self.getToken(ExprParser.PD, 0)
        def LI(self):
            return self.getToken(ExprParser.LI, 0)
        def LD(self):
            return self.getToken(ExprParser.LD, 0)
        def caseClause(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ExprParser.CaseClauseContext)
            else:
                return self.getTypedRuleContext(ExprParser.CaseClauseContext,i)

        def defaultClause(self):
            return self.getTypedRuleContext(ExprParser.DefaultClauseContext,0)



    class PostIncDecContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ExprParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self):
            return self.getTypedRuleContext(ExprParser.ExprContext,0)

        def INC(self):
            return self.getToken(ExprParser.INC, 0)
        def DEC(self):
            return self.getToken(ExprParser.DEC, 0)


    class ForExprContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ExprParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def FOR(self):
            return self.getToken(ExprParser.FOR, 0)
        def PI(self):
            return self.getToken(ExprParser.PI, 0)
        def PC(self, i:int=None):
            if i is None:
                return self.getTokens(ExprParser.PC)
            else:
                return self.getToken(ExprParser.PC, i)
        def PD(self):
            return self.getToken(ExprParser.PD, 0)
        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ExprParser.ExprContext)
            else:
                return self.getTypedRuleContext(ExprParser.ExprContext,i)

        def forInit(self):
            return self.getTypedRuleContext(ExprParser.ForInitContext,0)

        def forUpdate(self):
            return self.getTypedRuleContext(ExprParser.ForUpdateContext,0)



    class UnaryExprContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ExprParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self):
            return self.getTypedRuleContext(ExprParser.ExprContext,0)

        def NOT(self):
            return self.getToken(ExprParser.NOT, 0)
        def MENOS(self):
            return self.getToken(ExprParser.MENOS, 0)
        def MAS(self):
            return self.getToken(ExprParser.MAS, 0)
        def TYPEOF(self):
            return self.getToken(ExprParser.TYPEOF, 0)
        def VOID(self):
            return self.getToken(ExprParser.VOID, 0)
        def DELETE(self):
            return self.getToken(ExprParser.DELETE, 0)


    class NullishExprContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ExprParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ExprParser.ExprContext)
            else:
                return self.getTypedRuleContext(ExprParser.ExprContext,i)

        def NULLISH(self):
            return self.getToken(ExprParser.NULLISH, 0)


    class IfExprContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ExprParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def IF(self):
            return self.getToken(ExprParser.IF, 0)
        def PI(self):
            return self.getToken(ExprParser.PI, 0)
        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ExprParser.ExprContext)
            else:
                return self.getTypedRuleContext(ExprParser.ExprContext,i)

        def PD(self):
            return self.getToken(ExprParser.PD, 0)
        def ELSE(self):
            return self.getToken(ExprParser.ELSE, 0)


    class BlockExprContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ExprParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def LI(self):
            return self.getToken(ExprParser.LI, 0)
        def LD(self):
            return self.getToken(ExprParser.LD, 0)
        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ExprParser.ExprContext)
            else:
                return self.getTypedRuleContext(ExprParser.ExprContext,i)

        def PC(self, i:int=None):
            if i is None:
                return self.getTokens(ExprParser.PC)
            else:
                return self.getToken(ExprParser.PC, i)


    class ImportExprContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ExprParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def IMPORT(self):
            return self.getToken(ExprParser.IMPORT, 0)
        def FROM(self):
            return self.getToken(ExprParser.FROM, 0)
        def CADENA(self):
            return self.getToken(ExprParser.CADENA, 0)
        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(ExprParser.ID)
            else:
                return self.getToken(ExprParser.ID, i)
        def LI(self):
            return self.getToken(ExprParser.LI, 0)
        def LD(self):
            return self.getToken(ExprParser.LD, 0)
        def C(self, i:int=None):
            if i is None:
                return self.getTokens(ExprParser.C)
            else:
                return self.getToken(ExprParser.C, i)


    class CallExprContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ExprParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self):
            return self.getTypedRuleContext(ExprParser.ExprContext,0)

        def PI(self):
            return self.getToken(ExprParser.PI, 0)
        def PD(self):
            return self.getToken(ExprParser.PD, 0)
        def argumentList(self):
            return self.getTypedRuleContext(ExprParser.ArgumentListContext,0)



    class EqualityContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ExprParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ExprParser.ExprContext)
            else:
                return self.getTypedRuleContext(ExprParser.ExprContext,i)

        def EQU(self):
            return self.getToken(ExprParser.EQU, 0)
        def NEQ(self):
            return self.getToken(ExprParser.NEQ, 0)
        def STRICT_EQ(self):
            return self.getToken(ExprParser.STRICT_EQ, 0)
        def STRICT_NE(self):
            return self.getToken(ExprParser.STRICT_NE, 0)


    class PreIncDecContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ExprParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self):
            return self.getTypedRuleContext(ExprParser.ExprContext,0)

        def INC(self):
            return self.getToken(ExprParser.INC, 0)
        def DEC(self):
            return self.getToken(ExprParser.DEC, 0)


    class ConditionalExprContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ExprParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ExprParser.ExprContext)
            else:
                return self.getTypedRuleContext(ExprParser.ExprContext,i)

        def Q(self):
            return self.getToken(ExprParser.Q, 0)
        def DP(self):
            return self.getToken(ExprParser.DP, 0)


    class ThrowExprContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ExprParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def THROW(self):
            return self.getToken(ExprParser.THROW, 0)
        def expr(self):
            return self.getTypedRuleContext(ExprParser.ExprContext,0)



    class MemberAccessContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ExprParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self):
            return self.getTypedRuleContext(ExprParser.ExprContext,0)

        def P(self):
            return self.getToken(ExprParser.P, 0)
        def ID(self):
            return self.getToken(ExprParser.ID, 0)


    class ExponentExprContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ExprParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ExprParser.ExprContext)
            else:
                return self.getTypedRuleContext(ExprParser.ExprContext,i)

        def EXP(self):
            return self.getToken(ExprParser.EXP, 0)


    class ClassDeclContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ExprParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def CLASS(self):
            return self.getToken(ExprParser.CLASS, 0)
        def ID(self):
            return self.getToken(ExprParser.ID, 0)
        def LI(self):
            return self.getToken(ExprParser.LI, 0)
        def LD(self):
            return self.getToken(ExprParser.LD, 0)
        def EXTENDS(self):
            return self.getToken(ExprParser.EXTENDS, 0)
        def expr(self):
            return self.getTypedRuleContext(ExprParser.ExprContext,0)

        def classMember(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ExprParser.ClassMemberContext)
            else:
                return self.getTypedRuleContext(ExprParser.ClassMemberContext,i)



    class DoWhileExprContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ExprParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def DO(self):
            return self.getToken(ExprParser.DO, 0)
        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ExprParser.ExprContext)
            else:
                return self.getTypedRuleContext(ExprParser.ExprContext,i)

        def WHILE(self):
            return self.getToken(ExprParser.WHILE, 0)
        def PI(self):
            return self.getToken(ExprParser.PI, 0)
        def PD(self):
            return self.getToken(ExprParser.PD, 0)


    class ReturnExprContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ExprParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def RETURN(self):
            return self.getToken(ExprParser.RETURN, 0)
        def expr(self):
            return self.getTypedRuleContext(ExprParser.ExprContext,0)



    class LogicalAndContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ExprParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ExprParser.ExprContext)
            else:
                return self.getTypedRuleContext(ExprParser.ExprContext,i)

        def AND(self):
            return self.getToken(ExprParser.AND, 0)


    class ArrowFunctionContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ExprParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def arrowParams(self):
            return self.getTypedRuleContext(ExprParser.ArrowParamsContext,0)

        def ARROW(self):
            return self.getToken(ExprParser.ARROW, 0)
        def expr(self):
            return self.getTypedRuleContext(ExprParser.ExprContext,0)

        def ASYNC(self):
            return self.getToken(ExprParser.ASYNC, 0)


    class AwaitExprContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ExprParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def AWAIT(self):
            return self.getToken(ExprParser.AWAIT, 0)
        def expr(self):
            return self.getTypedRuleContext(ExprParser.ExprContext,0)



    class ForOfExprContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ExprParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def FOR(self):
            return self.getToken(ExprParser.FOR, 0)
        def PI(self):
            return self.getToken(ExprParser.PI, 0)
        def OF(self):
            return self.getToken(ExprParser.OF, 0)
        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ExprParser.ExprContext)
            else:
                return self.getTypedRuleContext(ExprParser.ExprContext,i)

        def PD(self):
            return self.getToken(ExprParser.PD, 0)
        def variableModifier(self):
            return self.getTypedRuleContext(ExprParser.VariableModifierContext,0)

        def ID(self):
            return self.getToken(ExprParser.ID, 0)


    class AdditiveContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ExprParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ExprParser.ExprContext)
            else:
                return self.getTypedRuleContext(ExprParser.ExprContext,i)

        def MAS(self):
            return self.getToken(ExprParser.MAS, 0)
        def MENOS(self):
            return self.getToken(ExprParser.MENOS, 0)


    class IndexAccessContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ExprParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ExprParser.ExprContext)
            else:
                return self.getTypedRuleContext(ExprParser.ExprContext,i)

        def CI(self):
            return self.getToken(ExprParser.CI, 0)
        def CD(self):
            return self.getToken(ExprParser.CD, 0)


    class ContinueExprContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ExprParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def CONTINUE(self):
            return self.getToken(ExprParser.CONTINUE, 0)


    class WhileExprContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ExprParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def WHILE(self):
            return self.getToken(ExprParser.WHILE, 0)
        def PI(self):
            return self.getToken(ExprParser.PI, 0)
        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ExprParser.ExprContext)
            else:
                return self.getTypedRuleContext(ExprParser.ExprContext,i)

        def PD(self):
            return self.getToken(ExprParser.PD, 0)


    class TryExprContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ExprParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def TRY(self):
            return self.getToken(ExprParser.TRY, 0)
        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ExprParser.ExprContext)
            else:
                return self.getTypedRuleContext(ExprParser.ExprContext,i)

        def CATCH(self):
            return self.getToken(ExprParser.CATCH, 0)
        def FINALLY(self):
            return self.getToken(ExprParser.FINALLY, 0)
        def PI(self):
            return self.getToken(ExprParser.PI, 0)
        def ID(self):
            return self.getToken(ExprParser.ID, 0)
        def PD(self):
            return self.getToken(ExprParser.PD, 0)


    class PrimarySContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ExprParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def primaryExpr(self):
            return self.getTypedRuleContext(ExprParser.PrimaryExprContext,0)



    class OptionalChainExprContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ExprParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ExprParser.ExprContext)
            else:
                return self.getTypedRuleContext(ExprParser.ExprContext,i)

        def OPTIONAL_CHAIN(self):
            return self.getToken(ExprParser.OPTIONAL_CHAIN, 0)
        def ID(self):
            return self.getToken(ExprParser.ID, 0)
        def PI(self):
            return self.getToken(ExprParser.PI, 0)
        def PD(self):
            return self.getToken(ExprParser.PD, 0)
        def CI(self):
            return self.getToken(ExprParser.CI, 0)
        def CD(self):
            return self.getToken(ExprParser.CD, 0)
        def argumentList(self):
            return self.getTypedRuleContext(ExprParser.ArgumentListContext,0)



    class ExportExprContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ExprParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def EXPORT(self):
            return self.getToken(ExprParser.EXPORT, 0)
        def expr(self):
            return self.getTypedRuleContext(ExprParser.ExprContext,0)

        def DEFAULT(self):
            return self.getToken(ExprParser.DEFAULT, 0)
        def AS(self):
            return self.getToken(ExprParser.AS, 0)
        def ID(self):
            return self.getToken(ExprParser.ID, 0)


    class VariableDeclContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ExprParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def variableModifier(self):
            return self.getTypedRuleContext(ExprParser.VariableModifierContext,0)

        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(ExprParser.ID)
            else:
                return self.getToken(ExprParser.ID, i)
        def ASIG(self, i:int=None):
            if i is None:
                return self.getTokens(ExprParser.ASIG)
            else:
                return self.getToken(ExprParser.ASIG, i)
        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ExprParser.ExprContext)
            else:
                return self.getTypedRuleContext(ExprParser.ExprContext,i)

        def C(self, i:int=None):
            if i is None:
                return self.getTokens(ExprParser.C)
            else:
                return self.getToken(ExprParser.C, i)


    class RelationalContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ExprParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ExprParser.ExprContext)
            else:
                return self.getTypedRuleContext(ExprParser.ExprContext,i)

        def LESS(self):
            return self.getToken(ExprParser.LESS, 0)
        def BIG(self):
            return self.getToken(ExprParser.BIG, 0)
        def LE(self):
            return self.getToken(ExprParser.LE, 0)
        def BE(self):
            return self.getToken(ExprParser.BE, 0)
        def INSTANCEOF(self):
            return self.getToken(ExprParser.INSTANCEOF, 0)
        def IN(self):
            return self.getToken(ExprParser.IN, 0)


    class WithExprContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ExprParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def WITH(self):
            return self.getToken(ExprParser.WITH, 0)
        def PI(self):
            return self.getToken(ExprParser.PI, 0)
        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ExprParser.ExprContext)
            else:
                return self.getTypedRuleContext(ExprParser.ExprContext,i)

        def PD(self):
            return self.getToken(ExprParser.PD, 0)


    class LogicalOrContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ExprParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ExprParser.ExprContext)
            else:
                return self.getTypedRuleContext(ExprParser.ExprContext,i)

        def OR(self):
            return self.getToken(ExprParser.OR, 0)



    def expr(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = ExprParser.ExprContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 2
        self.enterRecursionRule(localctx, 2, self.RULE_expr, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 291
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,33,self._ctx)
            if la_ == 1:
                localctx = ExprParser.BlockExprContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx

                self.state = 64
                self.match(ExprParser.LI)
                self.state = 76
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & 243197368357188606) != 0) or ((((_la - 73)) & ~0x3f) == 0 and ((1 << (_la - 73)) & 57429) != 0):
                    self.state = 65
                    self.expr(0)
                    self.state = 70
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,2,self._ctx)
                    while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                        if _alt==1:
                            self.state = 66
                            self.match(ExprParser.PC)
                            self.state = 67
                            self.expr(0) 
                        self.state = 72
                        self._errHandler.sync(self)
                        _alt = self._interp.adaptivePredict(self._input,2,self._ctx)

                    self.state = 74
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if _la==81:
                        self.state = 73
                        self.match(ExprParser.PC)




                self.state = 78
                self.match(ExprParser.LD)
                pass

            elif la_ == 2:
                localctx = ExprParser.VariableDeclContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 79
                self.variableModifier()
                self.state = 80
                self.match(ExprParser.ID)
                self.state = 83
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,5,self._ctx)
                if la_ == 1:
                    self.state = 81
                    self.match(ExprParser.ASIG)
                    self.state = 82
                    self.expr(0)


                self.state = 93
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,7,self._ctx)
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt==1:
                        self.state = 85
                        self.match(ExprParser.C)
                        self.state = 86
                        self.match(ExprParser.ID)
                        self.state = 89
                        self._errHandler.sync(self)
                        la_ = self._interp.adaptivePredict(self._input,6,self._ctx)
                        if la_ == 1:
                            self.state = 87
                            self.match(ExprParser.ASIG)
                            self.state = 88
                            self.expr(0)

                 
                    self.state = 95
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,7,self._ctx)

                pass

            elif la_ == 3:
                localctx = ExprParser.FunctionDeclContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 97
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==5:
                    self.state = 96
                    self.match(ExprParser.ASYNC)


                self.state = 99
                self.match(ExprParser.FUNCTION)
                self.state = 100
                self.match(ExprParser.ID)
                self.state = 101
                self.match(ExprParser.PI)
                self.state = 103
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==74 or _la==88:
                    self.state = 102
                    self.paramList()


                self.state = 105
                self.match(ExprParser.PD)
                self.state = 106
                self.match(ExprParser.LI)
                self.state = 118
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & 243197368357188606) != 0) or ((((_la - 73)) & ~0x3f) == 0 and ((1 << (_la - 73)) & 57429) != 0):
                    self.state = 107
                    self.expr(0)
                    self.state = 112
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,10,self._ctx)
                    while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                        if _alt==1:
                            self.state = 108
                            self.match(ExprParser.PC)
                            self.state = 109
                            self.expr(0) 
                        self.state = 114
                        self._errHandler.sync(self)
                        _alt = self._interp.adaptivePredict(self._input,10,self._ctx)

                    self.state = 116
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if _la==81:
                        self.state = 115
                        self.match(ExprParser.PC)




                self.state = 120
                self.match(ExprParser.LD)
                pass

            elif la_ == 4:
                localctx = ExprParser.ArrowFunctionContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 122
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==5:
                    self.state = 121
                    self.match(ExprParser.ASYNC)


                self.state = 124
                self.arrowParams()
                self.state = 125
                self.match(ExprParser.ARROW)
                self.state = 126
                self.expr(38)
                pass

            elif la_ == 5:
                localctx = ExprParser.ClassDeclContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 128
                self.match(ExprParser.CLASS)
                self.state = 129
                self.match(ExprParser.ID)
                self.state = 132
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==10:
                    self.state = 130
                    self.match(ExprParser.EXTENDS)
                    self.state = 131
                    self.expr(0)


                self.state = 134
                self.match(ExprParser.LI)
                self.state = 138
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while (((_la) & ~0x3f) == 0 and ((1 << _la) & 34848) != 0) or ((((_la - 86)) & ~0x3f) == 0 and ((1 << (_la - 86)) & 7) != 0):
                    self.state = 135
                    self.classMember()
                    self.state = 140
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 141
                self.match(ExprParser.LD)
                pass

            elif la_ == 6:
                localctx = ExprParser.IfExprContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 142
                self.match(ExprParser.IF)
                self.state = 143
                self.match(ExprParser.PI)
                self.state = 144
                self.expr(0)
                self.state = 145
                self.match(ExprParser.PD)
                self.state = 146
                self.expr(0)
                self.state = 149
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,16,self._ctx)
                if la_ == 1:
                    self.state = 147
                    self.match(ExprParser.ELSE)
                    self.state = 148
                    self.expr(0)


                pass

            elif la_ == 7:
                localctx = ExprParser.WhileExprContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 151
                self.match(ExprParser.WHILE)
                self.state = 152
                self.match(ExprParser.PI)
                self.state = 153
                self.expr(0)
                self.state = 154
                self.match(ExprParser.PD)
                self.state = 155
                self.expr(35)
                pass

            elif la_ == 8:
                localctx = ExprParser.DoWhileExprContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 157
                self.match(ExprParser.DO)
                self.state = 158
                self.expr(0)
                self.state = 159
                self.match(ExprParser.WHILE)
                self.state = 160
                self.match(ExprParser.PI)
                self.state = 161
                self.expr(0)
                self.state = 162
                self.match(ExprParser.PD)
                pass

            elif la_ == 9:
                localctx = ExprParser.ForInExprContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 164
                self.match(ExprParser.FOR)
                self.state = 165
                self.match(ExprParser.PI)
                self.state = 170
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [1, 2, 3]:
                    self.state = 166
                    self.variableModifier()
                    self.state = 167
                    self.match(ExprParser.ID)
                    pass
                elif token in [88]:
                    self.state = 169
                    self.match(ExprParser.ID)
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 172
                self.match(ExprParser.IN)
                self.state = 173
                self.expr(0)
                self.state = 174
                self.match(ExprParser.PD)
                self.state = 175
                self.expr(33)
                pass

            elif la_ == 10:
                localctx = ExprParser.ForOfExprContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 177
                self.match(ExprParser.FOR)
                self.state = 178
                self.match(ExprParser.PI)
                self.state = 183
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [1, 2, 3]:
                    self.state = 179
                    self.variableModifier()
                    self.state = 180
                    self.match(ExprParser.ID)
                    pass
                elif token in [88]:
                    self.state = 182
                    self.match(ExprParser.ID)
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 185
                self.match(ExprParser.OF)
                self.state = 186
                self.expr(0)
                self.state = 187
                self.match(ExprParser.PD)
                self.state = 188
                self.expr(32)
                pass

            elif la_ == 11:
                localctx = ExprParser.ForExprContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 190
                self.match(ExprParser.FOR)
                self.state = 191
                self.match(ExprParser.PI)
                self.state = 193
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & 243197368357188606) != 0) or ((((_la - 73)) & ~0x3f) == 0 and ((1 << (_la - 73)) & 57429) != 0):
                    self.state = 192
                    self.forInit()


                self.state = 195
                self.match(ExprParser.PC)
                self.state = 197
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & 243197368357188606) != 0) or ((((_la - 73)) & ~0x3f) == 0 and ((1 << (_la - 73)) & 57429) != 0):
                    self.state = 196
                    self.expr(0)


                self.state = 199
                self.match(ExprParser.PC)
                self.state = 201
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & 243197368357188606) != 0) or ((((_la - 73)) & ~0x3f) == 0 and ((1 << (_la - 73)) & 57429) != 0):
                    self.state = 200
                    self.forUpdate()


                self.state = 203
                self.match(ExprParser.PD)
                self.state = 204
                self.expr(31)
                pass

            elif la_ == 12:
                localctx = ExprParser.SwitchExprContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 205
                self.match(ExprParser.SWITCH)
                self.state = 206
                self.match(ExprParser.PI)
                self.state = 207
                self.expr(0)
                self.state = 208
                self.match(ExprParser.PD)
                self.state = 209
                self.match(ExprParser.LI)
                self.state = 213
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,22,self._ctx)
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt==1:
                        self.state = 210
                        self.caseClause() 
                    self.state = 215
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,22,self._ctx)

                self.state = 217
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==23:
                    self.state = 216
                    self.defaultClause()


                self.state = 222
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==22:
                    self.state = 219
                    self.caseClause()
                    self.state = 224
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 225
                self.match(ExprParser.LD)
                pass

            elif la_ == 13:
                localctx = ExprParser.TryExprContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 227
                self.match(ExprParser.TRY)
                self.state = 228
                self.expr(0)
                self.state = 236
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,26,self._ctx)
                if la_ == 1:
                    self.state = 229
                    self.match(ExprParser.CATCH)
                    self.state = 233
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,25,self._ctx)
                    if la_ == 1:
                        self.state = 230
                        self.match(ExprParser.PI)
                        self.state = 231
                        self.match(ExprParser.ID)
                        self.state = 232
                        self.match(ExprParser.PD)


                    self.state = 235
                    self.expr(0)


                self.state = 240
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,27,self._ctx)
                if la_ == 1:
                    self.state = 238
                    self.match(ExprParser.FINALLY)
                    self.state = 239
                    self.expr(0)


                pass

            elif la_ == 14:
                localctx = ExprParser.WithExprContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 242
                self.match(ExprParser.WITH)
                self.state = 243
                self.match(ExprParser.PI)
                self.state = 244
                self.expr(0)
                self.state = 245
                self.match(ExprParser.PD)
                self.state = 246
                self.expr(28)
                pass

            elif la_ == 15:
                localctx = ExprParser.DebuggerExprContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 248
                self.match(ExprParser.DEBUGGER)
                pass

            elif la_ == 16:
                localctx = ExprParser.ThrowExprContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 249
                self.match(ExprParser.THROW)
                self.state = 250
                self.expr(26)
                pass

            elif la_ == 17:
                localctx = ExprParser.ReturnExprContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 251
                self.match(ExprParser.RETURN)
                self.state = 253
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,28,self._ctx)
                if la_ == 1:
                    self.state = 252
                    self.expr(0)


                pass

            elif la_ == 18:
                localctx = ExprParser.BreakExprContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 255
                self.match(ExprParser.BREAK)
                pass

            elif la_ == 19:
                localctx = ExprParser.ContinueExprContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 256
                self.match(ExprParser.CONTINUE)
                pass

            elif la_ == 20:
                localctx = ExprParser.ImportExprContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 257
                self.match(ExprParser.IMPORT)
                self.state = 269
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [88]:
                    self.state = 258
                    self.match(ExprParser.ID)
                    pass
                elif token in [77]:
                    self.state = 259
                    self.match(ExprParser.LI)
                    self.state = 260
                    self.match(ExprParser.ID)
                    self.state = 265
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    while _la==82:
                        self.state = 261
                        self.match(ExprParser.C)
                        self.state = 262
                        self.match(ExprParser.ID)
                        self.state = 267
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)

                    self.state = 268
                    self.match(ExprParser.LD)
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 271
                self.match(ExprParser.FROM)
                self.state = 272
                self.match(ExprParser.CADENA)
                pass

            elif la_ == 21:
                localctx = ExprParser.ExportExprContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 273
                self.match(ExprParser.EXPORT)
                self.state = 275
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==23:
                    self.state = 274
                    self.match(ExprParser.DEFAULT)


                self.state = 277
                self.expr(0)
                self.state = 280
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,32,self._ctx)
                if la_ == 1:
                    self.state = 278
                    self.match(ExprParser.AS)
                    self.state = 279
                    self.match(ExprParser.ID)


                pass

            elif la_ == 22:
                localctx = ExprParser.NewExprContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 282
                self.match(ExprParser.NEW)
                self.state = 283
                self.expr(16)
                pass

            elif la_ == 23:
                localctx = ExprParser.PreIncDecContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 284
                _la = self._input.LA(1)
                if not(_la==53 or _la==54):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 285
                self.expr(14)
                pass

            elif la_ == 24:
                localctx = ExprParser.UnaryExprContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 286
                _la = self._input.LA(1)
                if not(((((_la - 34)) & ~0x3f) == 0 and ((1 << (_la - 34)) & 549768396813) != 0)):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 287
                self.expr(13)
                pass

            elif la_ == 25:
                localctx = ExprParser.AwaitExprContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 288
                self.match(ExprParser.AWAIT)
                self.state = 289
                self.expr(12)
                pass

            elif la_ == 26:
                localctx = ExprParser.PrimarySContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 290
                self.primaryExpr()
                pass


            self._ctx.stop = self._input.LT(-1)
            self.state = 359
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,38,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 357
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,37,self._ctx)
                    if la_ == 1:
                        localctx = ExprParser.ExponentExprContext(self, ExprParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 293
                        if not self.precpred(self._ctx, 11):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 11)")
                        self.state = 294
                        self.match(ExprParser.EXP)
                        self.state = 295
                        self.expr(11)
                        pass

                    elif la_ == 2:
                        localctx = ExprParser.MultiplicativeContext(self, ExprParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 296
                        if not self.precpred(self._ctx, 10):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 10)")
                        self.state = 297
                        _la = self._input.LA(1)
                        if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 2017612633061982208) != 0)):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 298
                        self.expr(11)
                        pass

                    elif la_ == 3:
                        localctx = ExprParser.AdditiveContext(self, ExprParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 299
                        if not self.precpred(self._ctx, 9):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 9)")
                        self.state = 300
                        _la = self._input.LA(1)
                        if not(_la==56 or _la==57):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 301
                        self.expr(10)
                        pass

                    elif la_ == 4:
                        localctx = ExprParser.RelationalContext(self, ExprParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 302
                        if not self.precpred(self._ctx, 8):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 8)")
                        self.state = 303
                        _la = self._input.LA(1)
                        if not(((((_la - 35)) & ~0x3f) == 0 and ((1 << (_la - 35)) & 16106127369) != 0)):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 304
                        self.expr(9)
                        pass

                    elif la_ == 5:
                        localctx = ExprParser.EqualityContext(self, ExprParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 305
                        if not self.precpred(self._ctx, 7):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 7)")
                        self.state = 306
                        _la = self._input.LA(1)
                        if not(((((_la - 61)) & ~0x3f) == 0 and ((1 << (_la - 61)) & 15) != 0)):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 307
                        self.expr(8)
                        pass

                    elif la_ == 6:
                        localctx = ExprParser.LogicalAndContext(self, ExprParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 308
                        if not self.precpred(self._ctx, 6):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 6)")
                        self.state = 309
                        self.match(ExprParser.AND)
                        self.state = 310
                        self.expr(7)
                        pass

                    elif la_ == 7:
                        localctx = ExprParser.LogicalOrContext(self, ExprParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 311
                        if not self.precpred(self._ctx, 5):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 5)")
                        self.state = 312
                        self.match(ExprParser.OR)
                        self.state = 313
                        self.expr(6)
                        pass

                    elif la_ == 8:
                        localctx = ExprParser.NullishExprContext(self, ExprParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 314
                        if not self.precpred(self._ctx, 4):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 4)")
                        self.state = 315
                        self.match(ExprParser.NULLISH)
                        self.state = 316
                        self.expr(5)
                        pass

                    elif la_ == 9:
                        localctx = ExprParser.ConditionalExprContext(self, ExprParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 317
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 318
                        self.match(ExprParser.Q)
                        self.state = 319
                        self.expr(0)
                        self.state = 320
                        self.match(ExprParser.DP)
                        self.state = 321
                        self.expr(3)
                        pass

                    elif la_ == 10:
                        localctx = ExprParser.AssignmentExprContext(self, ExprParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 323
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 324
                        self.assignmentOperator()
                        self.state = 325
                        self.expr(2)
                        pass

                    elif la_ == 11:
                        localctx = ExprParser.MemberAccessContext(self, ExprParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 327
                        if not self.precpred(self._ctx, 20):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 20)")
                        self.state = 328
                        self.match(ExprParser.P)
                        self.state = 329
                        self.match(ExprParser.ID)
                        pass

                    elif la_ == 12:
                        localctx = ExprParser.IndexAccessContext(self, ExprParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 330
                        if not self.precpred(self._ctx, 19):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 19)")
                        self.state = 331
                        self.match(ExprParser.CI)
                        self.state = 332
                        self.expr(0)
                        self.state = 333
                        self.match(ExprParser.CD)
                        pass

                    elif la_ == 13:
                        localctx = ExprParser.OptionalChainExprContext(self, ExprParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 335
                        if not self.precpred(self._ctx, 18):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 18)")
                        self.state = 336
                        self.match(ExprParser.OPTIONAL_CHAIN)
                        self.state = 347
                        self._errHandler.sync(self)
                        token = self._input.LA(1)
                        if token in [88]:
                            self.state = 337
                            self.match(ExprParser.ID)
                            pass
                        elif token in [75]:
                            self.state = 338
                            self.match(ExprParser.PI)
                            self.state = 340
                            self._errHandler.sync(self)
                            _la = self._input.LA(1)
                            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 243197368357188606) != 0) or ((((_la - 73)) & ~0x3f) == 0 and ((1 << (_la - 73)) & 57431) != 0):
                                self.state = 339
                                self.argumentList()


                            self.state = 342
                            self.match(ExprParser.PD)
                            pass
                        elif token in [79]:
                            self.state = 343
                            self.match(ExprParser.CI)
                            self.state = 344
                            self.expr(0)
                            self.state = 345
                            self.match(ExprParser.CD)
                            pass
                        else:
                            raise NoViableAltException(self)

                        pass

                    elif la_ == 14:
                        localctx = ExprParser.CallExprContext(self, ExprParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 349
                        if not self.precpred(self._ctx, 17):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 17)")
                        self.state = 350
                        self.match(ExprParser.PI)
                        self.state = 352
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)
                        if (((_la) & ~0x3f) == 0 and ((1 << _la) & 243197368357188606) != 0) or ((((_la - 73)) & ~0x3f) == 0 and ((1 << (_la - 73)) & 57431) != 0):
                            self.state = 351
                            self.argumentList()


                        self.state = 354
                        self.match(ExprParser.PD)
                        pass

                    elif la_ == 15:
                        localctx = ExprParser.PostIncDecContext(self, ExprParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 355
                        if not self.precpred(self._ctx, 15):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 15)")
                        self.state = 356
                        _la = self._input.LA(1)
                        if not(_la==53 or _la==54):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        pass

             
                self.state = 361
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,38,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class VariableModifierContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def VAR(self):
            return self.getToken(ExprParser.VAR, 0)

        def LET(self):
            return self.getToken(ExprParser.LET, 0)

        def CONST(self):
            return self.getToken(ExprParser.CONST, 0)

        def getRuleIndex(self):
            return ExprParser.RULE_variableModifier




    def variableModifier(self):

        localctx = ExprParser.VariableModifierContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_variableModifier)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 362
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 14) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AssignmentOperatorContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ASIG(self):
            return self.getToken(ExprParser.ASIG, 0)

        def ASSIGN_ADD(self):
            return self.getToken(ExprParser.ASSIGN_ADD, 0)

        def ASSIGN_SUB(self):
            return self.getToken(ExprParser.ASSIGN_SUB, 0)

        def ASSIGN_MUL(self):
            return self.getToken(ExprParser.ASSIGN_MUL, 0)

        def ASSIGN_DIV(self):
            return self.getToken(ExprParser.ASSIGN_DIV, 0)

        def ASSIGN_MOD(self):
            return self.getToken(ExprParser.ASSIGN_MOD, 0)

        def ASSIGN_EXP(self):
            return self.getToken(ExprParser.ASSIGN_EXP, 0)

        def getRuleIndex(self):
            return ExprParser.RULE_assignmentOperator




    def assignmentOperator(self):

        localctx = ExprParser.AssignmentOperatorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_assignmentOperator)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 364
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 8936830510563328) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ArrowParamsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(ExprParser.ID, 0)

        def PI(self):
            return self.getToken(ExprParser.PI, 0)

        def PD(self):
            return self.getToken(ExprParser.PD, 0)

        def param(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ExprParser.ParamContext)
            else:
                return self.getTypedRuleContext(ExprParser.ParamContext,i)


        def C(self, i:int=None):
            if i is None:
                return self.getTokens(ExprParser.C)
            else:
                return self.getToken(ExprParser.C, i)

        def getRuleIndex(self):
            return ExprParser.RULE_arrowParams




    def arrowParams(self):

        localctx = ExprParser.ArrowParamsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_arrowParams)
        self._la = 0 # Token type
        try:
            self.state = 379
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [88]:
                self.enterOuterAlt(localctx, 1)
                self.state = 366
                self.match(ExprParser.ID)
                pass
            elif token in [75]:
                self.enterOuterAlt(localctx, 2)
                self.state = 367
                self.match(ExprParser.PI)
                self.state = 376
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==74 or _la==88:
                    self.state = 368
                    self.param()
                    self.state = 373
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    while _la==82:
                        self.state = 369
                        self.match(ExprParser.C)
                        self.state = 370
                        self.param()
                        self.state = 375
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)



                self.state = 378
                self.match(ExprParser.PD)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ParamListContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def param(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ExprParser.ParamContext)
            else:
                return self.getTypedRuleContext(ExprParser.ParamContext,i)


        def C(self, i:int=None):
            if i is None:
                return self.getTokens(ExprParser.C)
            else:
                return self.getToken(ExprParser.C, i)

        def getRuleIndex(self):
            return ExprParser.RULE_paramList




    def paramList(self):

        localctx = ExprParser.ParamListContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_paramList)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 381
            self.param()
            self.state = 386
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==82:
                self.state = 382
                self.match(ExprParser.C)
                self.state = 383
                self.param()
                self.state = 388
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ParamContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(ExprParser.ID, 0)

        def ELLIPSIS(self):
            return self.getToken(ExprParser.ELLIPSIS, 0)

        def ASIG(self):
            return self.getToken(ExprParser.ASIG, 0)

        def expr(self):
            return self.getTypedRuleContext(ExprParser.ExprContext,0)


        def getRuleIndex(self):
            return ExprParser.RULE_param




    def param(self):

        localctx = ExprParser.ParamContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_param)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 390
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==74:
                self.state = 389
                self.match(ExprParser.ELLIPSIS)


            self.state = 392
            self.match(ExprParser.ID)
            self.state = 395
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==52:
                self.state = 393
                self.match(ExprParser.ASIG)
                self.state = 394
                self.expr(0)


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ClassMemberContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def methodDefinition(self):
            return self.getTypedRuleContext(ExprParser.MethodDefinitionContext,0)


        def STATIC(self):
            return self.getToken(ExprParser.STATIC, 0)

        def fieldDefinition(self):
            return self.getTypedRuleContext(ExprParser.FieldDefinitionContext,0)


        def getRuleIndex(self):
            return ExprParser.RULE_classMember




    def classMember(self):

        localctx = ExprParser.ClassMemberContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_classMember)
        self._la = 0 # Token type
        try:
            self.state = 405
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,47,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 398
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==15:
                    self.state = 397
                    self.match(ExprParser.STATIC)


                self.state = 400
                self.methodDefinition()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 402
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==15:
                    self.state = 401
                    self.match(ExprParser.STATIC)


                self.state = 404
                self.fieldDefinition()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class MethodDefinitionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def propertyName(self):
            return self.getTypedRuleContext(ExprParser.PropertyNameContext,0)


        def PI(self):
            return self.getToken(ExprParser.PI, 0)

        def PD(self):
            return self.getToken(ExprParser.PD, 0)

        def LI(self):
            return self.getToken(ExprParser.LI, 0)

        def LD(self):
            return self.getToken(ExprParser.LD, 0)

        def ASYNC(self):
            return self.getToken(ExprParser.ASYNC, 0)

        def paramList(self):
            return self.getTypedRuleContext(ExprParser.ParamListContext,0)


        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ExprParser.ExprContext)
            else:
                return self.getTypedRuleContext(ExprParser.ExprContext,i)


        def PC(self, i:int=None):
            if i is None:
                return self.getTokens(ExprParser.PC)
            else:
                return self.getToken(ExprParser.PC, i)

        def getRuleIndex(self):
            return ExprParser.RULE_methodDefinition




    def methodDefinition(self):

        localctx = ExprParser.MethodDefinitionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_methodDefinition)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 408
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==5:
                self.state = 407
                self.match(ExprParser.ASYNC)


            self.state = 410
            self.propertyName()
            self.state = 411
            self.match(ExprParser.PI)
            self.state = 413
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==74 or _la==88:
                self.state = 412
                self.paramList()


            self.state = 415
            self.match(ExprParser.PD)
            self.state = 416
            self.match(ExprParser.LI)
            self.state = 428
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 243197368357188606) != 0) or ((((_la - 73)) & ~0x3f) == 0 and ((1 << (_la - 73)) & 57429) != 0):
                self.state = 417
                self.expr(0)
                self.state = 422
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,50,self._ctx)
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt==1:
                        self.state = 418
                        self.match(ExprParser.PC)
                        self.state = 419
                        self.expr(0) 
                    self.state = 424
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,50,self._ctx)

                self.state = 426
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==81:
                    self.state = 425
                    self.match(ExprParser.PC)




            self.state = 430
            self.match(ExprParser.LD)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FieldDefinitionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def propertyName(self):
            return self.getTypedRuleContext(ExprParser.PropertyNameContext,0)


        def ASIG(self):
            return self.getToken(ExprParser.ASIG, 0)

        def expr(self):
            return self.getTypedRuleContext(ExprParser.ExprContext,0)


        def getRuleIndex(self):
            return ExprParser.RULE_fieldDefinition




    def fieldDefinition(self):

        localctx = ExprParser.FieldDefinitionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_fieldDefinition)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 432
            self.propertyName()
            self.state = 435
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==52:
                self.state = 433
                self.match(ExprParser.ASIG)
                self.state = 434
                self.expr(0)


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class PropertyNameContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(ExprParser.ID, 0)

        def CADENA(self):
            return self.getToken(ExprParser.CADENA, 0)

        def NUM(self):
            return self.getToken(ExprParser.NUM, 0)

        def CONSTRUCTOR(self):
            return self.getToken(ExprParser.CONSTRUCTOR, 0)

        def getRuleIndex(self):
            return ExprParser.RULE_propertyName




    def propertyName(self):

        localctx = ExprParser.PropertyNameContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_propertyName)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 437
            _la = self._input.LA(1)
            if not(_la==11 or ((((_la - 86)) & ~0x3f) == 0 and ((1 << (_la - 86)) & 7) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CaseClauseContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CASE(self):
            return self.getToken(ExprParser.CASE, 0)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ExprParser.ExprContext)
            else:
                return self.getTypedRuleContext(ExprParser.ExprContext,i)


        def DP(self):
            return self.getToken(ExprParser.DP, 0)

        def PC(self, i:int=None):
            if i is None:
                return self.getTokens(ExprParser.PC)
            else:
                return self.getToken(ExprParser.PC, i)

        def getRuleIndex(self):
            return ExprParser.RULE_caseClause




    def caseClause(self):

        localctx = ExprParser.CaseClauseContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_caseClause)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 439
            self.match(ExprParser.CASE)
            self.state = 440
            self.expr(0)
            self.state = 441
            self.match(ExprParser.DP)
            self.state = 448
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 243197368357188606) != 0) or ((((_la - 73)) & ~0x3f) == 0 and ((1 << (_la - 73)) & 57429) != 0):
                self.state = 442
                self.expr(0)
                self.state = 444
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==81:
                    self.state = 443
                    self.match(ExprParser.PC)


                self.state = 450
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DefaultClauseContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def DEFAULT(self):
            return self.getToken(ExprParser.DEFAULT, 0)

        def DP(self):
            return self.getToken(ExprParser.DP, 0)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ExprParser.ExprContext)
            else:
                return self.getTypedRuleContext(ExprParser.ExprContext,i)


        def PC(self, i:int=None):
            if i is None:
                return self.getTokens(ExprParser.PC)
            else:
                return self.getToken(ExprParser.PC, i)

        def getRuleIndex(self):
            return ExprParser.RULE_defaultClause




    def defaultClause(self):

        localctx = ExprParser.DefaultClauseContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_defaultClause)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 451
            self.match(ExprParser.DEFAULT)
            self.state = 452
            self.match(ExprParser.DP)
            self.state = 459
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 243197368357188606) != 0) or ((((_la - 73)) & ~0x3f) == 0 and ((1 << (_la - 73)) & 57429) != 0):
                self.state = 453
                self.expr(0)
                self.state = 455
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==81:
                    self.state = 454
                    self.match(ExprParser.PC)


                self.state = 461
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ForInitContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def variableModifier(self):
            return self.getTypedRuleContext(ExprParser.VariableModifierContext,0)


        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(ExprParser.ID)
            else:
                return self.getToken(ExprParser.ID, i)

        def ASIG(self, i:int=None):
            if i is None:
                return self.getTokens(ExprParser.ASIG)
            else:
                return self.getToken(ExprParser.ASIG, i)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ExprParser.ExprContext)
            else:
                return self.getTypedRuleContext(ExprParser.ExprContext,i)


        def C(self, i:int=None):
            if i is None:
                return self.getTokens(ExprParser.C)
            else:
                return self.getToken(ExprParser.C, i)

        def getRuleIndex(self):
            return ExprParser.RULE_forInit




    def forInit(self):

        localctx = ExprParser.ForInitContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_forInit)
        self._la = 0 # Token type
        try:
            self.state = 480
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,61,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 462
                self.variableModifier()
                self.state = 463
                self.match(ExprParser.ID)
                self.state = 466
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==52:
                    self.state = 464
                    self.match(ExprParser.ASIG)
                    self.state = 465
                    self.expr(0)


                self.state = 476
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==82:
                    self.state = 468
                    self.match(ExprParser.C)
                    self.state = 469
                    self.match(ExprParser.ID)
                    self.state = 472
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if _la==52:
                        self.state = 470
                        self.match(ExprParser.ASIG)
                        self.state = 471
                        self.expr(0)


                    self.state = 478
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 479
                self.expr(0)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ForUpdateContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ExprParser.ExprContext)
            else:
                return self.getTypedRuleContext(ExprParser.ExprContext,i)


        def C(self, i:int=None):
            if i is None:
                return self.getTokens(ExprParser.C)
            else:
                return self.getToken(ExprParser.C, i)

        def getRuleIndex(self):
            return ExprParser.RULE_forUpdate




    def forUpdate(self):

        localctx = ExprParser.ForUpdateContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_forUpdate)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 482
            self.expr(0)
            self.state = 487
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==82:
                self.state = 483
                self.match(ExprParser.C)
                self.state = 484
                self.expr(0)
                self.state = 489
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ArgumentListContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def argument(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ExprParser.ArgumentContext)
            else:
                return self.getTypedRuleContext(ExprParser.ArgumentContext,i)


        def C(self, i:int=None):
            if i is None:
                return self.getTokens(ExprParser.C)
            else:
                return self.getToken(ExprParser.C, i)

        def getRuleIndex(self):
            return ExprParser.RULE_argumentList




    def argumentList(self):

        localctx = ExprParser.ArgumentListContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_argumentList)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 490
            self.argument()
            self.state = 495
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==82:
                self.state = 491
                self.match(ExprParser.C)
                self.state = 492
                self.argument()
                self.state = 497
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ArgumentContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr(self):
            return self.getTypedRuleContext(ExprParser.ExprContext,0)


        def ELLIPSIS(self):
            return self.getToken(ExprParser.ELLIPSIS, 0)

        def getRuleIndex(self):
            return ExprParser.RULE_argument




    def argument(self):

        localctx = ExprParser.ArgumentContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_argument)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 499
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==74:
                self.state = 498
                self.match(ExprParser.ELLIPSIS)


            self.state = 501
            self.expr(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class PrimaryExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def THIS(self):
            return self.getToken(ExprParser.THIS, 0)

        def SUPER(self):
            return self.getToken(ExprParser.SUPER, 0)

        def ID(self):
            return self.getToken(ExprParser.ID, 0)

        def literal(self):
            return self.getTypedRuleContext(ExprParser.LiteralContext,0)


        def arrayLiteral(self):
            return self.getTypedRuleContext(ExprParser.ArrayLiteralContext,0)


        def objectLiteral(self):
            return self.getTypedRuleContext(ExprParser.ObjectLiteralContext,0)


        def PI(self):
            return self.getToken(ExprParser.PI, 0)

        def expr(self):
            return self.getTypedRuleContext(ExprParser.ExprContext,0)


        def PD(self):
            return self.getToken(ExprParser.PD, 0)

        def getRuleIndex(self):
            return ExprParser.RULE_primaryExpr




    def primaryExpr(self):

        localctx = ExprParser.PrimaryExprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_primaryExpr)
        try:
            self.state = 513
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [12]:
                self.enterOuterAlt(localctx, 1)
                self.state = 503
                self.match(ExprParser.THIS)
                pass
            elif token in [13]:
                self.enterOuterAlt(localctx, 2)
                self.state = 504
                self.match(ExprParser.SUPER)
                pass
            elif token in [88]:
                self.enterOuterAlt(localctx, 3)
                self.state = 505
                self.match(ExprParser.ID)
                pass
            elif token in [31, 32, 33, 86, 87]:
                self.enterOuterAlt(localctx, 4)
                self.state = 506
                self.literal()
                pass
            elif token in [79]:
                self.enterOuterAlt(localctx, 5)
                self.state = 507
                self.arrayLiteral()
                pass
            elif token in [77]:
                self.enterOuterAlt(localctx, 6)
                self.state = 508
                self.objectLiteral()
                pass
            elif token in [75]:
                self.enterOuterAlt(localctx, 7)
                self.state = 509
                self.match(ExprParser.PI)
                self.state = 510
                self.expr(0)
                self.state = 511
                self.match(ExprParser.PD)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LiteralContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NUM(self):
            return self.getToken(ExprParser.NUM, 0)

        def CADENA(self):
            return self.getToken(ExprParser.CADENA, 0)

        def TRUE(self):
            return self.getToken(ExprParser.TRUE, 0)

        def FALSE(self):
            return self.getToken(ExprParser.FALSE, 0)

        def NULL(self):
            return self.getToken(ExprParser.NULL, 0)

        def getRuleIndex(self):
            return ExprParser.RULE_literal




    def literal(self):

        localctx = ExprParser.LiteralContext(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_literal)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 515
            _la = self._input.LA(1)
            if not(((((_la - 31)) & ~0x3f) == 0 and ((1 << (_la - 31)) & 108086391056891911) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ArrayLiteralContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CI(self):
            return self.getToken(ExprParser.CI, 0)

        def CD(self):
            return self.getToken(ExprParser.CD, 0)

        def elementList(self):
            return self.getTypedRuleContext(ExprParser.ElementListContext,0)


        def getRuleIndex(self):
            return ExprParser.RULE_arrayLiteral




    def arrayLiteral(self):

        localctx = ExprParser.ArrayLiteralContext(self, self._ctx, self.state)
        self.enterRule(localctx, 38, self.RULE_arrayLiteral)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 517
            self.match(ExprParser.CI)
            self.state = 519
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 243197368357188606) != 0) or ((((_la - 73)) & ~0x3f) == 0 and ((1 << (_la - 73)) & 57431) != 0):
                self.state = 518
                self.elementList()


            self.state = 521
            self.match(ExprParser.CD)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ElementListContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def elementItem(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ExprParser.ElementItemContext)
            else:
                return self.getTypedRuleContext(ExprParser.ElementItemContext,i)


        def C(self, i:int=None):
            if i is None:
                return self.getTokens(ExprParser.C)
            else:
                return self.getToken(ExprParser.C, i)

        def getRuleIndex(self):
            return ExprParser.RULE_elementList




    def elementList(self):

        localctx = ExprParser.ElementListContext(self, self._ctx, self.state)
        self.enterRule(localctx, 40, self.RULE_elementList)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 523
            self.elementItem()
            self.state = 528
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==82:
                self.state = 524
                self.match(ExprParser.C)
                self.state = 525
                self.elementItem()
                self.state = 530
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ElementItemContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr(self):
            return self.getTypedRuleContext(ExprParser.ExprContext,0)


        def ELLIPSIS(self):
            return self.getToken(ExprParser.ELLIPSIS, 0)

        def getRuleIndex(self):
            return ExprParser.RULE_elementItem




    def elementItem(self):

        localctx = ExprParser.ElementItemContext(self, self._ctx, self.state)
        self.enterRule(localctx, 42, self.RULE_elementItem)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 532
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==74:
                self.state = 531
                self.match(ExprParser.ELLIPSIS)


            self.state = 534
            self.expr(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ObjectLiteralContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LI(self):
            return self.getToken(ExprParser.LI, 0)

        def LD(self):
            return self.getToken(ExprParser.LD, 0)

        def propertyList(self):
            return self.getTypedRuleContext(ExprParser.PropertyListContext,0)


        def getRuleIndex(self):
            return ExprParser.RULE_objectLiteral




    def objectLiteral(self):

        localctx = ExprParser.ObjectLiteralContext(self, self._ctx, self.state)
        self.enterRule(localctx, 44, self.RULE_objectLiteral)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 536
            self.match(ExprParser.LI)
            self.state = 538
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==11 or ((((_la - 74)) & ~0x3f) == 0 and ((1 << (_la - 74)) & 28673) != 0):
                self.state = 537
                self.propertyList()


            self.state = 540
            self.match(ExprParser.LD)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class PropertyListContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def property_(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ExprParser.PropertyContext)
            else:
                return self.getTypedRuleContext(ExprParser.PropertyContext,i)


        def C(self, i:int=None):
            if i is None:
                return self.getTokens(ExprParser.C)
            else:
                return self.getToken(ExprParser.C, i)

        def getRuleIndex(self):
            return ExprParser.RULE_propertyList




    def propertyList(self):

        localctx = ExprParser.PropertyListContext(self, self._ctx, self.state)
        self.enterRule(localctx, 46, self.RULE_propertyList)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 542
            self.property_()
            self.state = 547
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==82:
                self.state = 543
                self.match(ExprParser.C)
                self.state = 544
                self.property_()
                self.state = 549
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class PropertyContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def propertyName(self):
            return self.getTypedRuleContext(ExprParser.PropertyNameContext,0)


        def DP(self):
            return self.getToken(ExprParser.DP, 0)

        def expr(self):
            return self.getTypedRuleContext(ExprParser.ExprContext,0)


        def ELLIPSIS(self):
            return self.getToken(ExprParser.ELLIPSIS, 0)

        def ID(self):
            return self.getToken(ExprParser.ID, 0)

        def getRuleIndex(self):
            return ExprParser.RULE_property




    def property_(self):

        localctx = ExprParser.PropertyContext(self, self._ctx, self.state)
        self.enterRule(localctx, 48, self.RULE_property)
        try:
            self.state = 557
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,71,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 550
                self.propertyName()
                self.state = 551
                self.match(ExprParser.DP)
                self.state = 552
                self.expr(0)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 554
                self.match(ExprParser.ELLIPSIS)
                self.state = 555
                self.expr(0)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 556
                self.match(ExprParser.ID)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[1] = self.expr_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def expr_sempred(self, localctx:ExprContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 11)
         

            if predIndex == 1:
                return self.precpred(self._ctx, 10)
         

            if predIndex == 2:
                return self.precpred(self._ctx, 9)
         

            if predIndex == 3:
                return self.precpred(self._ctx, 8)
         

            if predIndex == 4:
                return self.precpred(self._ctx, 7)
         

            if predIndex == 5:
                return self.precpred(self._ctx, 6)
         

            if predIndex == 6:
                return self.precpred(self._ctx, 5)
         

            if predIndex == 7:
                return self.precpred(self._ctx, 4)
         

            if predIndex == 8:
                return self.precpred(self._ctx, 3)
         

            if predIndex == 9:
                return self.precpred(self._ctx, 2)
         

            if predIndex == 10:
                return self.precpred(self._ctx, 20)
         

            if predIndex == 11:
                return self.precpred(self._ctx, 19)
         

            if predIndex == 12:
                return self.precpred(self._ctx, 18)
         

            if predIndex == 13:
                return self.precpred(self._ctx, 17)
         

            if predIndex == 14:
                return self.precpred(self._ctx, 15)
         




