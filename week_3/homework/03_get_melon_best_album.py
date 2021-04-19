genres = ["classic", "pop", "classic", "classic", "pop"]
plays = [500, 600, 150, 800, 2500]


def get_melon_best_album(genre_array, play_array):
    genre_count_dict = dict()
    ordered_genre_play_count_list = []

    for x in range(len(genres)):
        genre_count_dict[genres[x]] = genre_count_dict.get(genres[x], 0) + plays[x]
        ordered_genre_play_count_list.append((x, genres[x], plays[x]))
    genre_count_dict_sorted = sorted(genre_count_dict.items(), key=lambda x: x[1])

    result = []
    while genre_count_dict_sorted:
        genre = genre_count_dict_sorted.pop()[0]
        genre_filtered_list = sorted([x for x in ordered_genre_play_count_list if x[1] == genre],
                                     key=lambda x: x[2])
        genre_len = len(genre_filtered_list)
        for x in range(min(2, genre_len)):
            genre_play_item = genre_filtered_list.pop()
            for y in genre_filtered_list:
                if y[2] == genre_play_item[2]:
                    genre_play_item = y
                    break
            result.append(genre_play_item[0])
    return result


print(get_melon_best_album(genres, plays))  # 결과로 [4, 1, 3, 0] 가 와야 합니다!