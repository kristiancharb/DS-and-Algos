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
    
#abc -> a + bc, a + cb, b + a + c, c + a + b, bc + a, cb + a
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

def get_permutations_dups(word) -> list:
    pass

# 1 -> ()
# 2 -> ()(), (())
# 3 -> ()()(), (())(), ()(()), ((())), (()())
def get_valid_parens(num) -> set:
    if num == 1:
        return set(['()'])

    sub_parens = get_valid_parens(num - 1)
    all_parens = set()
    for sub_paren in sub_parens:
        all_parens.add('()' + sub_paren)
        all_parens.add('(' + sub_paren + ')')
        all_parens.add(sub_paren + '()')
    return all_parens

def parens_helper(parens, left_rem, right_rem, chars, index):
    print('PARENS', parens)
    print('LEFT REM', left_rem)
    print('RIGHT REM', right_rem)
    print('CHARS', chars)
    print('INDEX', index)
    print()
    if left_rem < 0 or right_rem < left_rem:
        return
    
    if left_rem == 0 and right_rem == 0:
        parens.append(''.join(chars))
    else:
        chars[index] = '('
        parens_helper(parens, left_rem - 1, right_rem, chars, index + 1)
        chars[index] = ')'
        parens_helper(parens, left_rem, right_rem - 1, chars, index + 1)

def get_valid_parens2(num) -> list:
    chars = [None] * (num * 2)
    parens = []
    parens_helper(parens, num, num, chars, 0)
    return parens

def paint_fill_helper(screen, x, y, color, orig_color):
    invalid_coords = x < 0 or y < 0 or y >= len(screen) or x >= len(screen[y])
    if invalid_coords or screen[y][x] != orig_color:
        return
    screen[y][x] = color
    paint_fill_helper(screen, x - 1, y, color, orig_color)
    paint_fill_helper(screen, x + 1, y, color, orig_color)
    paint_fill_helper(screen, x, y + 1, color, orig_color)
    paint_fill_helper(screen, x, y - 1, color, orig_color)

def paint_fill(screen, x, y, color):
    paint_fill_helper(screen, x, y, color, screen[y][x])

def get_coins(cents):
    denominations = [25, 10, 5, 1]
    if cents <= 1:
        return 1
    for denomination in denominations:
        if cents > denomination:
            left = cents % denomination
            counted = cents - left
            return 1  + get_coins(left)
    return 0
    

if __name__ == '__main__':
    # grid = [
    #     [0, 0, 0, 0, 0],
    #     [1, 0, 0, 1, 1],
    #     [0, 1, 0, 1, 0],
    #     [0, 0, 0, 0, 0],
    # ]
    # screen = [
    #     ['red', 'red','red','red','red',],
    #     ['red','red', 'black', 'white', 'white'],
    #     ['red', 'black', 'white', 'white', 'white'],
    #     ['black', 'black', 'black', 'black', 'black'],
    #     ['black', 'black', 'black', 'black', 'black']
    # ]
    print(get_coins(27))