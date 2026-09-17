import subprocess
import os

solution = "lab3.py"           
test_folder = "tests"          
num_tests = 8
passed = 0

for i in range(1, num_tests + 1):
    test_path = os.path.join(test_folder, str(i))
    
    if not os.path.exists(in_file) or not os.path.exists(out_file):
        print(f"тест {i}: файл не найден в папке {test_path}")
        continue
    with open(out_file, "r", encoding="utf-8") as f:
        expected = f.read().strip()
    with open(in_file, "r", encoding="utf-8") as f:
        result = subprocess.run(
            ["python", solution],
            stdin=f,
            capture_output=True,
            text=True,
            timeout=5
        )

    actual = result.stdout.strip()

    if expected.split() == actual.split():
        print(f"тест {i}: пройден")
        passed += 1
    else:
        print(f"тест {i}: ошибка")
        print(f"   ожидалось: {expected[:80]}")
        print(f"   получено:  {actual[:80]}")

print(f"\n Итого: {passed}/{num_tests} тестов пройдено") 