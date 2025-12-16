import sys
import os

CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
SRC_CODE_EX00 = os.path.abspath(
    os.path.join(CURRENT_DIR, '../../ex00')
)

sys.path.insert(0, SRC_CODE_EX00)

print(SRC_CODE_EX00)

from give_bmi import give_bmi, apply_limit

height = [2.71, 1.15]
weight = [165.3, 38.4]

bmi = give_bmi(height, weight)

print(bmi, type(bmi))
print(apply_limit(bmi, 26))

