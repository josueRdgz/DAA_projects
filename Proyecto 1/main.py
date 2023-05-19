from generate import cases_generator
from combinatoric import total_team_value
from hungarian import hungarian
import time
matrix = cases_generator(12, 5, 2)
start = time.time()

print(total_team_value(matrix))
end = time.time()
print("Time of combinatoric method: ", end-start)
start = time.time()
print(hungarian(matrix))
end = time.time()
print("Time of hungarian method: ", end-start)
