# input = 'acedgfb cdfbe gcdfa fbcad dab cefabd cdfgeb eafb cagedb ab | cdfeb fcadb cdfeb cdbaf'

source = """
be cfbegad cbdgef fgaecd cgeb fdcge agebfd fecdb fabcd edb | fdgacbe cefdb cefbgd gcbe
edbfga begcd cbg gc gcadebf fbgde acbgfd abcde gfcbed gfec | fcgedb cgb dgebacf gc
fgaebd cg bdaec gdafb agbcfd gdcbef bgcad gfac gcb cdgabef | cg cg fdcagb cbg
fbegcd cbd adcefb dageb afcb bc aefdc ecdab fgdeca fcdbega | efabcd cedba gadfec cb
aecbfdg fbg gf bafeg dbefa fcge gcbea fcaegb dgceab fcbdga | gecf egdcabf bgf bfgea
fgeab ca afcebg bdacfeg cfaedg gcfdb baec bfadeg bafgc acf | gebdcfa ecba ca fadegcb
dbcfg fgd bdegcaf fgec aegbdf ecdfab fbedc dacgb gdcebf gf | cefg dcbef fcge gbcadfe
bdfegc cbegaf gecbf dfcage bdacg ed bedf ced adcbefg gebcd | ed bcgafe cdgba cbgef
egadfb cdbfeg cegd fecab cgb gbdefca cg fgcdab egfdb bfceg | gbdfcae bgc cg cgb
gcafb gcf dcaebfg ecagb gf abcdeg gaef cafbge fdbac fegbdc | fgae cfgab fg bagce
"""

# match patterns to corresponding digit
# 1 uses 2 segments only
# 4 uses 4 segments only
# 7 uses 3 segments only
# 8 uses 7 segments only

# segment length to digit map
seglen2digit = {
    2: 1,
    3: 7,
    4: 4,
    # 5: 2|3|5
    # 6: 0|6|9
    7: 8
}

# 0 must contain what is in 1 & 7

input = open('input')
# input = [x for x in source.splitlines() if x]
# print(input)

# part 1
digit_count = {}
for line in [x.strip() for x in input]:
    patterns, outputs = [x.strip() for x in line.strip().split('|')]
    outdigits = outputs.split()
    for digit in outdigits:
        seglen = len(digit)
        if seglen == 2:
            digit_count[seglen2digit[2]] = digit_count.get(seglen2digit[2], 0) + 1
        elif seglen == 4:
            digit_count[seglen2digit[4]] = digit_count.get(seglen2digit[4], 0) + 1
        elif seglen == 3:
            digit_count[seglen2digit[3]] = digit_count.get(seglen2digit[3], 0) + 1
        elif seglen == 7:
            digit_count[seglen2digit[7]] = digit_count.get(seglen2digit[7], 0) + 1

ans = sum(digit_count.values())
print(ans)

# part 2
# wires = { 1: None, 2: None, 3: None, 4: None, 5: None, 6: None, 7: None, 8: None, 9: None }
sum = 0
input = open('input')
for line in [x.strip() for x in input]:
    segments, outputs = [x.strip() for x in line.strip().split('|')]
    outpatterns = outputs.split()
    segpatterns = segments.split()
    wires = { 0: None, 1: None, 2: None, 3: None, 4: None, 5: None, 6: None, 7: None, 8: None, 9: None }

    for segment_pattern in outpatterns + segpatterns:
        slen = len(segment_pattern)

        if slen in [2,3,4,7]:
            wires[seglen2digit[slen]] = "".join(sorted(segment_pattern))

    candidates_069 = [x for x in outpatterns + segpatterns if len(x) == 6]
    candidates_235 = [x for x in outpatterns + segpatterns if len(x) == 5]

    for candidate in candidates_069:
        w14 = set(wires[1] + wires[4] + wires[7]) 
        w17 = set(wires[1] + wires[7])

        # 9 contains all of 1,4,7
        if all([w in candidate for w in w14]):
            wires[9] = "".join(sorted(candidate))
        # 0 contains all of 1,7
        elif all([w in candidate for w in w17]):
            wires[0] = "".join(sorted(candidate))
        # 6 contains all of 5
        else:
            wires[6] = "".join(sorted(candidate))
    
    for candidate in candidates_235:
        w17 = set(wires[1] + wires[7])

        # 3 contains all of 1,7
        if all([w in candidate for w in w17]):
            wires[3] = "".join(sorted(candidate))
        # 5 contains all of 4 except 1 segment
        elif len([x for x in [w in candidate for w in wires[4]] if x == True]) == 3:
            wires[5] = "".join(sorted(candidate))
        # 2 contains all of 
        else:
            wires[2] = "".join(sorted(candidate))

    # print(wires)

    key_list = list(wires.keys())
    val_list = list(wires.values())
    getnum = lambda p: key_list[val_list.index("".join(sorted(p)))]

    number = int("".join([str(getnum(x)) for x in outpatterns]))
    # print(test)

    sum += number

print(sum)