current_r, current_c, current_d = 7, 4, 0
current_room_map = [
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 1, 1, 1, 1, 0, 1],
    [1, 0, 0, 1, 1, 0, 0, 0, 0, 1],
    [1, 0, 1, 1, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 1, 0, 1],
    [1, 0, 0, 0, 0, 0, 1, 1, 0, 1],
    [1, 0, 0, 0, 0, 0, 1, 1, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
]

find_dir_dict = {0: 3, 1: 0, 2: 1, 3: 2}


def is_possible_to_clean(r, c, d, room_map, visited):
    np = new_pos(r, c, d)
    try:
        return room_map[np[0]][np[1]] == 0 and [np[0], np[1]] not in visited
    except IndexError:
        return False


def new_pos(r, c, d):
    if d == 0:
        return [r - 1, c]
    if d == 1:
        return [r, c + 1]
    if d == 2:
        return [r + 1, c]
    if d == 3:
        return [r, c - 1]


def get_count_of_departments_cleaned_by_robot_vacuum(r, c, d, room_map):
    pos_queue = []

    pos_queue.append([r, c])

    visited = []

    result_count = 0

    tot_cnt = 0
    while pos_queue:
        tot_cnt += 1
        cur_pos = pos_queue.pop(0)
        #print("{} {} {}".format(tot_cnt, cur_pos, room_map[cur_pos[0]][cur_pos[1]]))
        if room_map[cur_pos[0]][cur_pos[1]] == 1 or room_map[cur_pos[0]][cur_pos[1]] == 2:
            break
        else:
            room_map[cur_pos[0]][cur_pos[1]] == 2
            visited.append(cur_pos)
            result_count += 1
            dir_cnt = 0
            for i in range(4):
                dir_cnt += 1
                new_dir = find_dir_dict[d % 4]
                #print("{} new_dir {}".format(tot_cnt, new_dir))
                if is_possible_to_clean(cur_pos[0], cur_pos[1], new_dir, room_map, visited):
                    d = new_dir
                    pos_queue.append(new_pos(cur_pos[0], cur_pos[1], new_dir))
                    break
                else:
                    d += 1
            if dir_cnt == 4:
                break
    #print(visited)
    return result_count


# 57 가 출력되어야 합니다!
print(get_count_of_departments_cleaned_by_robot_vacuum(current_r, current_c, current_d, current_room_map))
