# t(n) = t(n - 3) + t(n - 2) + t(n - 1)
# t(4) = (1, 3) + (3, 1) + (2, 2) + (1,2,1) + (1, 1, 2) + (1, 1, 1, 1)
# t(3) = (3) + (2, 1) + (1, 2) + (1, 1, 1)
# t(2) = (2) + (1, 1)
# t(1) = (1)
def triple_step(n) -> int:
    if n == 3:
        return 3
    elif n == 2:
        return 2
    elif n == 1:
        return 1
    else:
        return triple_step(n - 3) + triple_step(n - 2) + triple_step(n - 1)

def triple_step_memo(n) -> int:
    steps = [None] * n
    steps[0] = 1
    steps[1] = 2
    steps[2] = 3
    for i in range(3, n):
        steps[i] = steps[i-1] + steps[i-2] + steps[i-3]
    return steps[-1]

def robot_in_a_grid(grid, i, j) -> list:
    n = len(grid)
    m = len(grid[i])
    if i == n - 1 and j == m - 1:
        return [(i, j)]
    elif grid[i][j] == 1:
        return None
    else:
        down = robot_in_a_grid(grid, i + 1, j) if i < n - 1 else None
        right = robot_in_a_grid(grid, i, j + 1) if j < m - 1 else None
        path = [(i, j)]
        if right is None and down is None:
            return None 
        elif down is None:
            path.extend(right)
        elif right is None:
            path.extend(down)
        else:
            shortest = down if len(down) < len(right) else right
            path.extend(shortest)
        return path
        
def get_magic_index(nums, start, end) -> int:
    middle = (end - start) // 2 + start
    if nums[middle] == middle:
        return middle
    elif end - start == 0:
        return None
    elif nums[middle] < middle:
        return get_magic_index(nums, middle, end)
    return get_magic_index(nums, start, middle)
 
# {a, b, c}
# c + {a, b} + {a} + {b} = {a, b} + {a} + {b} + {a, b, c} + {a, c} + {b, c} 
# missing: {c}
def get_power_set(nums: set) -> set:
    num = nums.pop()
    sets = []
    sets.append(set([num]))
    if len(nums) == 0:
        return sets
    other_sets = get_power_set(nums)
    for other_set in other_sets:
        sets.append(other_set.copy())
        other_set.add(num)
        sets.append(other_set)
    return sets
    
#abc -> abc, acb, bac, cab, bca, cba
def get_permutations_unique(word) -> list:
    if len(word) <= 1:
        return [word]
    
    ending = word[1:]
    sub_perms = get_permutations_unique(ending)
    all_perms = []
    for sub_perm in sub_perms:
        for i in range(len(sub_perm) + 1):
            pre = sub_perm[:i]
            post = sub_perm[i:]
            all_perms.append(pre + word[0] + post)

    return all_perms


if __name__ == '__main__':
    # grid = [
    #     [0, 0, 0, 0, 0],
    #     [1, 0, 0, 1, 1],
    #     [0, 1, 0, 1, 0],
    #     [0, 0, 0, 0, 0],
    # ]
    print(get_permutations_unique('abcd'))