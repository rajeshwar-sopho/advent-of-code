"""
--- Day 2: Cube Conundrum ---
You're launched high into the atmosphere! The apex of your trajectory just barely reaches the surface of a large island floating in the sky. You gently land in a fluffy pile of leaves. It's quite cold, but you don't see much snow. An Elf runs over to greet you.

The Elf explains that you've arrived at Snow Island and apologizes for the lack of snow. He'll be happy to explain the situation, but it's a bit of a walk, so you have some time. They don't get many visitors up here; would you like to play a game in the meantime?

As you walk, the Elf shows you a small bag and some cubes which are either red, green, or blue. Each time you play this game, he will hide a secret number of cubes of each color in the bag, and your goal is to figure out information about the number of cubes.

To get information, once a bag has been loaded with cubes, the Elf will reach into the bag, grab a handful of random cubes, show them to you, and then put them back in the bag. He'll do this a few times per game.

You play several games and record the information from each game (your puzzle input). Each game is listed with its ID number (like the 11 in Game 11: ...) followed by a semicolon-separated list of subsets of cubes that were revealed from the bag (like 3 red, 5 green, 4 blue).

For example, the record of a few games might look like this:

Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue
Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red
Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red
Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green
In game 1, three sets of cubes are revealed from the bag (and then put back again). The first set is 3 blue cubes and 4 red cubes; the second set is 1 red cube, 2 green cubes, and 6 blue cubes; the third set is only 2 green cubes.

The Elf would first like to know which games would have been possible if the bag contained only 12 red cubes, 13 green cubes, and 14 blue cubes?

In the example above, games 1, 2, and 5 would have been possible if the bag had been loaded with that configuration. However, game 3 would have been impossible because at one point the Elf showed you 20 red cubes at once; similarly, game 4 would also have been impossible because the Elf showed you 15 blue cubes at once. If you add up the IDs of the games that would have been possible, you get 8.

Determine which games would have been possible if the bag had been loaded with only 12 red cubes, 13 green cubes, and 14 blue cubes. What is the sum of the IDs of those games?

--- Part Two ---
The Elf says they've stopped producing snow because they aren't getting any water! He isn't sure why the water stopped; however, he can show you how to get to the water source to check it out for yourself. It's just up ahead!

As you continue your walk, the Elf poses a second question: in each game you played, what is the fewest number of cubes of each color that could have been in the bag to make the game possible?

Again consider the example games from earlier:

Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue
Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red
Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red
Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green
In game 1, the game could have been played with as few as 4 red, 2 green, and 6 blue cubes. If any color had even one fewer cube, the game would have been impossible.
Game 2 could have been played with a minimum of 1 red, 3 green, and 4 blue cubes.
Game 3 must have been played with at least 20 red, 13 green, and 6 blue cubes.
Game 4 required at least 14 red, 3 green, and 15 blue cubes.
Game 5 needed no fewer than 6 red, 3 green, and 2 blue cubes in the bag.
The power of a set of cubes is equal to the numbers of red, green, and blue cubes multiplied together. The power of the minimum set of cubes in game 1 is 48. In games 2-5 it was 12, 1560, 630, and 36, respectively. Adding up these five powers produces the sum 2286.

For each game, find the minimum set of cubes that must have been present. What is the sum of the power of these sets?

"""
input_type='prod'

def get_input(input_type, day, year):
    root_path = f"{year}/day-{day}"
    if input_type == 'test_p1':
        file_name = f'{root_path}/sample_input_p1.txt'
    elif input_type == 'test_p2':
        file_name = f'{root_path}/sample_input_p2.txt'
    elif input_type == 'prod':
        file_name = f'{root_path}/input.txt'
    else:
        raise Exception(f"Invalid input type {input_type}.")

    with open(file_name, 'r') as f:
        lines = f.readlines()
        lines = [line.strip() for line in lines if line[0] != '#']

    return lines


def process_input(lines):
    processed_games = {}
    for line in lines:
        game_id = int(line.split(':')[0].split(' ')[1].strip())
        results = [part.split(',') for part in line.split(':')[1].split(';')]
        processed_results = []
        for result in results:
            # R G B
            tmp_item = [0, 0, 0]
            for item in result:
                num_balls = int(item.strip().split(' ')[0])
                ball_color = item.strip().split(' ')[1].strip()
                if ball_color == 'red':
                    tmp_item[0] = num_balls
                elif ball_color == 'green':
                    tmp_item[1] = num_balls
                elif ball_color == 'blue':
                    tmp_item[2] = num_balls
            processed_results.append(tmp_item)
        processed_games[game_id] = processed_results
    return processed_games


def solution_part1(games):
    max_rgb = [12, 13, 14]
    game_id_sum = 0
    for game_id, results in games.items():
        game_failed = False
        for result in results:
            for item, max_item in zip(result, max_rgb):
                if item > max_item:
                    game_failed = True
                    break
            if game_failed:
                break
    
        if not game_failed:
            game_id_sum += game_id
    return game_id_sum

def solution_part2(games):
    power_of_cubes = 0
    for game_id, results in games.items():
        max_results = [0, 0, 0]
        for result in results:
            max_results = [max(item, max_item) for item, max_item in zip(result, max_results)]
        game_power = 1
        for max_item in max_results:
            game_power *= max_item if max_item > 0 else 1
        power_of_cubes += game_power
    return power_of_cubes


day = '2'
year = '2023'
lines = get_input(input_type, day, year)
games = process_input(lines)
print(solution_part1(games))
print(solution_part2(games))

