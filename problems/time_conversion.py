import os


def time_conversion(time: str) -> str:
    hour, minute, second_with_period = time.split(":")
    second, period = second_with_period[:2], second_with_period[2:]
    hour = int(hour)

    if period == "PM":
        if hour != 12:
            hour += 12

    elif period == "AM" and hour == 12:
        hour = "0"

    hour = f"{hour:02}"

    return f"{hour}:{minute}:{second}"

if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()
    #test = [time_conversion(t) for t in s.split()]
    result = time_conversion(s)
    print(result)
    #fptr.write(result + "\n")
    #fptr.close()
