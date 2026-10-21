
import heapq


def can_attend_all(events):
    events = sorted(events, key=lambda event: event[0])

    for i in range(1, len(events)):
        if events[i - 1][1] > events[i][0]:
            return False

    return True


def min_rooms_required(events):
    events = sorted(events, key=lambda event: event[0])

    end_times = []
    max_rooms = 0

    for start, end in events:

        while end_times and end_times[0] <= start:
            heapq.heappop(end_times)

        heapq.heappush(end_times, end)

        max_rooms = max(max_rooms, len(end_times))

    return max_rooms

events = [(9, 10), (10, 11), (11, 12)]

print(can_attend_all(events))      # True
print(min_rooms_required(events))  # 1

events = [(9, 11), (10, 12), (11, 13)]

print(can_attend_all(events))      # False
print(min_rooms_required(events))  # 2