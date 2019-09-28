from bs4 import BeautifulSoup
import requests
import datetime

# Get all the timestamps from the playlist.
def get_time_from_all_clips(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    times = soup.select('span', class_='ytd-thumbnail-overlay-time-status-renderer')
    all_times = []
    for time in times:
        if any(i.isdigit() for i in time.text):
            if ":" in time.text:
                all_times.append(time.text)

    return all_times

# Add the time together.
def calculate_playlist_time(time_list):
    total_sec = 0
    for time in time_list:
        time_split = [int(i) for i in time.split(':')]

        if len(time_split) == 1:
            total_sec += time_split[0]
        elif len(time_split) == 2:
            total_sec += time_split[0] * 60 + time_split[1]
        elif len(time_split) == 3:
            total_sec += time_split[0] * 3600 + time_split[1] * 60 + time_split[2]

    return datetime.timedelta(seconds=total_sec)

if __name__ == '__main__':
    url = input("Enter the playlist url >> ")
    times = get_time_from_all_clips(url)

    playlist_time = calculate_playlist_time(times)

    print(f'Total amount of time in the playlist: {playlist_time}')
