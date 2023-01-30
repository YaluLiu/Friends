import cv2


def parse_episode(season,episode):
    txt_path = f"{season}/Friends{season}{episode}.txt"
    print(txt_path)
    with open(txt_path,"rb") as file:
        flines = file.readlines()

    next_line_print = False
    ret_lines = []
    for line in flines:
        line = line.decode()
        if line.startswith("……………"):
            next_line_print = True
            continue
        if next_line_print:
            ret_lines.append(line[1:-2])
            next_line_print=False
    return ret_lines

if __name__ == "__main__":
    season ="S06"
    episode_start = 5
    episode_end  = 25
    for episode in range(episode_start, episode_end):
        episode = "E"+str(episode).zfill(2)
        lines = parse_episode(season, episode)
        for line in lines:
            print(line)
        break

