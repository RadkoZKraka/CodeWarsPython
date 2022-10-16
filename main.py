# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

def pipe_fix(nums):
    result = [*range(nums[0], nums[len(nums) - 1] + 1)]
    return result


def hoop_count(n):
    if n >= 10:
        return 'Great, now move on to tricks'
    return 'Keep at it until you get it'


def get_char(c):
    # Your code goes here ^_^
    return chr(c)


res = pipe_fix([-1, 4])
for x in res:
    print(x)


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


la_liga_goals = 43
champions_league_goals = 10
copa_del_rey_goals = 5

total_goals = la_liga_goals + champions_league_goals + copa_del_rey_goals


def goals(laLiga, copaDelRey, championsLeague):
    total_goals_func = laLiga + copaDelRey + championsLeague
    return total_goals_func


def find_average(numbers):
    length = len(numbers)
    if length == 0:
        return 0
    return sum(numbers) / length

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
