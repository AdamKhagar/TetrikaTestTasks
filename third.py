from typing import Dict, List, Tuple


class Interval:
    def __init__(self, intervals: List):
        assert len(intervals) % 2 == 0, "array length shoud be even number"
        self.lst = []

        counter = 0
        while counter < len(intervals):
            self.lst.append((intervals[counter], intervals[counter + 1]))
            counter += 2

        self.lst = tuple(self.lst)
        self.idx: int = 0

    def __iter__(self):
        return self

    def __next__(self) -> Tuple[int]:
        try:
            item = self.lst[self.idx]
        except IndexError:
            raise StopIteration()
        
        self.idx += 1
        return item

    def __getitem__(self, index) -> Tuple[int]:
        return self.lst[index]

    @property
    def start(self) -> int:
        return self.lst[0]

    @property
    def end(self) -> int:
        return self.lst[-1]


def appearance(intervals: Dict) -> int:
    lesson = Interval(intervals["lesson"])
    tutor = Interval(intervals["tutor"])
    pupil = Interval(intervals["pupil"])

    start_position = lesson.start
    if start_position < tutor.start:
        start_position = tutor.start
    if start_position < pupil.start:
        start_position = pupil.start

    end_position = lesson.start
    if end_position > tutor.start:
        end_position = tutor.start
    if end_position > pupil.start:
        end_position = pupil.start

    common_time = 0

    pupil_i = next(pupil)
    tutor_i = next(tutor)

    for i in range(start_position, end_position + 1):
        if (pupil_i[0] <= i and i <= pupil_i[1]) and (tutor_i[0] <= i and i <= tutor_i[1]):
            common_time += 1

tests = [
    {
        'data': {
            'lesson': [1594663200, 1594666800],
            'pupil': [1594663340, 1594663389, 1594663390, 1594663395, 1594663396, 1594666472],
            'tutor': [1594663290, 1594663430, 1594663443, 1594666473]
        },
        'answer': 3117
    },
    {
        'data': {
            'lesson': [1594702800, 1594706400],
            'pupil': [1594702789, 1594704500, 1594702807, 1594704542, 1594704512, 1594704513, 1594704564, 1594705150, 1594704581, 1594704582, 1594704734, 1594705009, 1594705095, 1594705096, 1594705106, 1594706480, 1594705158, 1594705773, 1594705849, 1594706480, 1594706500, 1594706875, 1594706502, 1594706503, 1594706524, 1594706524, 1594706579, 1594706641],
            'tutor': [1594700035, 1594700364, 1594702749, 1594705148, 1594705149, 1594706463]
        },
        'answer': 3577
    },
    {   'data': {
            'lesson': [1594692000, 1594695600],
            'pupil': [1594692033, 1594696347],
            'tutor': [1594692017, 1594692066, 1594692068, 1594696341]
        },
        'answer': 3565
    },
]

if __name__ == '__main__':
   for i, test in enumerate(tests):
       test_answer = appearance(test['data'])
       assert test_answer == test['answer'], f'Error on test case {i}, got {test_answer}, expected {test["answer"]}'
