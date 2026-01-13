import datetime
import uuid
import time

def main():
    while True:
        curr_time = datetime.datetime.now().isoformat()
        output_str = uuid.uuid8()
        print(f"{curr_time}: {output_str}")
        time.sleep(5)


if __name__ == "__main__":
    main()
