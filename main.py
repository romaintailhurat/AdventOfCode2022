from itertools import groupby
from heapq import nlargest
from string import ascii_letters
from io import StringIO

import re


# ----- Day 1
def day1():
  with open("day1.input") as day1in:
    raw = day1in.readlines()
    max = 0
    acc = 0

    for value in raw:
      if value == "\n":
        if acc > max:
          max = acc
        acc = 0
      else:
        calories = int(value.strip())
        acc += calories

    return (max)


def day1_2():
  with open("day1.input") as day1in:
    raw = day1in.readlines()
    groups = [list(g) for _, g in groupby(raw, key="\n".__ne__)]
    groups_without_empty = [g for g in groups if g != ["\n"]]
    calories = [sum([int(x) for x in g]) for g in groups_without_empty]
    top3 = nlargest(3, calories)
    return (sum(top3))


# ----- Day 2
def day2():
  with open("day2.input") as day2in:
    raw = day2in.readlines()
    second_hands = {"X": 1, "Y": 2, "Z": 3}
    score = 0

    for round in raw:
      fh, sh = round.strip().split(" ")
      if fh + sh in ["AX", "BY", "CZ"]:
        score += 3 + second_hands[sh]
      elif fh + sh in ["AY", "BZ", "CX"]:
        score += 6 + second_hands[sh]
      else:
        score += second_hands[sh]
    return (score)


def day2_2():
  with open("day2.input") as day2in:
    raw = day2in.readlines()
    rps = ["A", "B", "C"]
    winning_hands = {"A": "B", "B": "C", "C": "A"}
    losing_hands = {v: k for k, v in winning_hands.items()}
    score = 0

    for round in raw:
      fh, sh = round.strip().split(" ")
      if sh == "X":
        lh = losing_hands[fh]
        base_score = rps.index(lh) + 1
        score += base_score
      elif sh == "Y":
        base_score = rps.index(fh) + 1
        score += 3 + base_score
      else:
        wh = winning_hands[fh]
        base_score = rps.index(wh) + 1
        score += 6 + base_score

    return score


# ----- Day 3
def day3():
  with open("day3.input") as day3in:
    raw = day3in.readlines()
    priorities = 0

    for rucks in raw:
      mid = int(len(rucks) / 2)
      ruck1 = rucks[0:mid]
      ruck2 = rucks[mid:len(rucks)]
      inter = set(ruck1) & set(ruck2)
      element = list(inter)[0]
      priority = ascii_letters.index(element) + 1
      priorities += priority

    return priorities


def day3_2():
  with open("day3.input") as day3in:
    raw = day3in.readlines()
    priorities = 0
    rucks = [raw[i:i + 3] for i in range(0, len(raw), 3)]

    for ruck in rucks:
      sub1, sub2, sub3 = [sub.strip() for sub in ruck]
      inter = set(sub1) & set(sub2) & set(sub3)
      element = list(inter)[0]
      priority = ascii_letters.index(element) + 1
      priorities += priority

    return (priorities)


# ----- Day 4
def day4():
  with open("day4.input") as day4in:
    raw = day4in.readlines()
    assignments = [r.strip().split(",") for r in raw]
    count = 0

    for assignment in assignments:
      a1, a2 = assignment
      r1, r2 = [int(x) for x in a1.split("-")]
      r3, r4 = [int(x) for x in a2.split("-")]
      if (r1 <= r3 and r2 >= r4) or (r3 <= r1 and r4 >= r2):
        count += 1

    return (count)


# ----- Day 5


def parse_instruction(instruction):
  exp = re.compile(r"\d+")
  inst = exp.findall(instruction)
  return [int(x) for x in inst]


def day5():
  with open("day5.input") as day5in:
    raw = day5in.readlines()
    instructions = []
    stacks = [[] for _ in range(9)] # UGLY, parse it
    for line in raw:
      if line[0:4] == "move":
        instructions.append(line)
      elif "[" in line:
        thing = [line[i:i + 4] for i in range(0, len(line), 4)]
        for i, crate in enumerate(thing):
          if "[" in crate:
            stacks[i].append(crate.strip())
      else:
        pass
    
    for instruction in instructions:
      n, source, target = parse_instruction(instruction)      
      for _ in range(n):
        crate = stacks[source-1].pop(0)
        stacks[target-1].insert(0, crate)      

    res = "".join([stack[0] for stack in stacks])
    print(res.replace("[", "").replace("]", ""))

# ----- Day 6
def day6():
  with open("day6.input") as day6in:
    packet_offset = 4
    message_offset = 14
    offset = message_offset # switch for part I or II
    
    stream = day6in.readlines()[0]
    
    for i in range(len(stream)-(offset-1)):
      window = stream[i:i+offset]
      if len(set(window)) == len(window):
        print(window, i+offset)
        break
    
day6()
