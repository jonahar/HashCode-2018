import sys
import Parser

input_file = sys.argv[1]
rides, cars, bonus = Parser.build_data(input_file)
rides.sort(key=lambda r: r.start_time())
for r in rides:
    print(r)
