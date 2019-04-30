from time import sleep
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
test_000 = AntiochToSFO(['Antioch','Pittsburg Center','Pittsburg / Bay Point', 
                        'North Concord / Martinex', 'Concord', 'Pleasant Hill/ Contra costa Centre', 
                        'Walnut Creek', 'Lafayette', 'Orinda', 'Rockridge', 'MacArthur', 
                        '19th St/Oakland', '12th St/Oakland City Center', 'West Oakland', 
                        'Embarcadero', 'Montgomery St', 'Powell St', 'Civic Center/ UN Plaza', 
                        '16th St Mission', '24th St Mission', 'Glen Park', 'Balboa Park', 'Daly City', 
                        'Colma', 'South San Francisco', 'San Bruno', 'San Francisco International Airport'])
for _ in range(50):
    test_000.to_the_next_stop()
    sleep(0.5)
