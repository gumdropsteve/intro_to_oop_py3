class AntiochToSFO:
    def __init__(self, stops):
        self.stops = stops
        self.stop_number = 0
        self.reverse = False
    def to_the_next_stop(self):
        if self.stop_number + 1 == len(self.stops):
            self.reverse = True
        if self.stop_number == 0:
            self.reverse = False
        # advance stops
        if self.reverse == False:
            self.stop_number += 1
        if self.reverse == True:
            self.stop_number -= 1
        print(f'Stopping at {str(self.stops[self.stop_number])}\n')
test_000 = AntiochToSFO(['Antioch','Pittsburg Center','Pittsburg / Bay Point', 'North Concord / Martinex'])
for _ in range(7):
    test_000.to_the_next_stop()
