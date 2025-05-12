from random import sample
from .settings import SUB_GRID_SIZE, GRID_SIZE

#from stack-overflow


# pattern for a baseline valid solution
def pattern(row: int, col: int): 
    return (SUB_GRID_SIZE*(row%SUB_GRID_SIZE)+row//SUB_GRID_SIZE+col)%GRID_SIZE

# randomize rows, columns and numbers (of valid base pattern)
def shuffle(s):
    return sample(s,len(s)) 

def create_grid(sub_grid: int):
    #creatin the 9x9 grid filled with random numbers
    row_base = range(sub_grid) 
    rows  = [ g*sub_grid + r for g in shuffle(row_base) for r in shuffle(row_base) ] 
    cols  = [ g*sub_grid + c for g in shuffle(row_base) for c in shuffle(row_base) ]
    nums  = shuffle(range(1,sub_grid*sub_grid+1))
    # produce board using randomized baseline pattern
    # print([ [nums[pattern(r,c)] for c in cols] for r in rows ])
    return [ [nums[pattern(r,c)] for c in cols] for r in rows ]