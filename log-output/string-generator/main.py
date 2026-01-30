import datetime
import uuid
import time
from pathlib import Path

file_path = Path('/usr/src/app/files/logs.txt')
file_path.parent.mkdir(exist_ok=True, parents=True)

def main():
    output_str = uuid.uuid4()
    
    while True:
        curr_time = datetime.datetime.now().isoformat()
        log = f"{curr_time}: {output_str}"
        with open(file_path, "w") as f:
            f.write(log)
        time.sleep(5)

if __name__ == "__main__":
    main()
