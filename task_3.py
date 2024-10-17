import sys
import re
from collections import defaultdict

# Function for parsing a log string
def parse_log_line(line: str) -> dict:
    # Divide string into parts using regular expression
    re_pattern = r'(\d{4}-\d{2}-\d{2}) (\d{2}:\d{2}:\d{2}) (\w+) (.*)'
    match = re.match(re_pattern, line)
    if match:
        return {
            'date': match.group(1),
            'time': match.group(2),
            'level': match.group(3),
            'message': match.group(4)
        }
    return None

# Function for downloading logs from a file
def load_logs(file_path: str) -> list:
    logs = []
    try:
        with open(file_path, 'r') as file:
            for line in file:
                parsed_line = parse_log_line(line.strip())
                if parsed_line:
                    logs.append(parsed_line)
    except FileNotFoundError:
        print(f"Файл {file_path} не знайдено.")
        sys.exit(1)
    return logs

# Function for filtering logs by logging level
def filter_logs_by_level(logs: list, level: str) -> list:
    return [log for log in logs if log['level'].upper() == level.upper()]

# Function for counting number of records by logging levels
def count_logs_by_level(logs: list) -> dict:
    counts = defaultdict(int)
    for log in logs:
        counts[log['level'].upper()] += 1
    return counts

# Function for displaying statistics
def display_log_counts(counts: dict):
    print(f"{'Рівень логування':<15} | {'Кількість':<7}")
    print("-" * 25)
    for level, count in counts.items():
        print(f"{level:<16} | {count:<7}")

# Main function
def main():
    if len(sys.argv) < 2:
        print("Використання: python main.py <шлях до файлу логу> [рівень логування]")
        sys.exit(1)

    file_path = sys.argv[1]
    logs = load_logs(file_path)

    # If second argument is passed (check logging level)
    if len(sys.argv) == 3:
        level = sys.argv[2]
        filtered_logs = filter_logs_by_level(logs, level)
        if not filtered_logs:
            print(f"Записів рівня {level.upper()} не знайдено.")
        else:
            counts = count_logs_by_level(logs)
            display_log_counts(counts)
            print(f"\nДеталі логів для рівня '{level.upper()}':")
            for log in filtered_logs:
                print(f"{log['date']} {log['time']} - {log['message']}")
    else:
        counts = count_logs_by_level(logs)
        display_log_counts(counts)


# Запуск головної функції
if __name__ == "__main__":
    main()

# Приклад запуску скрипта з додатковим аргументом
# python task_3.py path/to/logfile.log error
