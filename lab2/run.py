import subprocess
import os
solution = "lab2.py"

num_tests = 8

passed = 0

for i in range(1, num_tests + 1):
    in_file = f"test{i}.in"
    out_file = f"test{i}.out"

    if not os.path.exists(in_file) or not os.path.exists(out_file):
        print(f"test {i}: file not fund")
        continue
    with open(in_file, "r") as f:
        result = subprocess.run(["python", solution], stdin=f, capture_output=True, text=True, timeout=5)
    actual = result.stdout.strip()

    expected_nums = expected.split()
    actual_nums = actual.split()

    if expected_nums == actual.nums:
        print(f"test {i: done}")
        passed += 1
    else:
        print(f"test {i}: error")
        print(f"expected: {expected[:80]}...")
        print(f"received: {actual[:80]}...")
print(f"\n at end: {passed}/{num_tests} tests completed")
