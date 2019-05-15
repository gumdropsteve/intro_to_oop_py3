from time import sleep


class AntiochToSFO:
    
    def __init__(self, stops):
        # set number of stops
        self.stops = stops
        # start at beginning
        self.stop_number = 0
        # train starts moving forward
        self.reverse = False
    
    def to_the_next_stop(self):
        """moves train 
            > from current stop
            > to next stop
        """
        # check for end of the line
        if self.stop_number + 1 == len(self.stops):
            # reverse if at the end of line
            self.reverse = True
        # check if reverse trip has completed
        if self.stop_number == 0:
            # set the train to go back forward if so
            self.reverse = False
        
        # advance stops, check direction forward
        if self.reverse == False:
            # moving forward one stop
            self.stop_number += 1
        # check direction reverse
        if self.reverse == True:
            # moving backward one stop
            self.stop_number -= 1
        
        # let us know where we are stopping
        print(f'Stopping at {str(self.stops[self.stop_number])}\n')
        # wait for passangers to enter/exit
        sleep(1)


# for when we call this script
if __name__ == '__main__':
    # set stops for this train
    stations = ['Antioch','Pittsburg Center','Pittsburg / Bay Point', 'North Concord / Martinex', 
                'Concord', 'Pleasant Hill/ Contra costa Centre', 'Walnut Creek', 'Lafayette', 
                'Orinda', 'Rockridge', 'MacArthur', '19th St/Oakland', '12th St/Oakland City Center', 
                'West Oakland', 'Embarcadero', 'Montgomery St', 'Powell St', 'Civic Center/ UN Plaza', 
                '16th St Mission', '24th St Mission', 'Glen Park', 'Balboa Park', 'Daly City', 
                'Colma', 'South San Francisco', 'San Bruno', 'San Francisco International Airport'] 
    # set test case
    test_000 = AntiochToSFO(stops=stations)
    # go through 50 stops
    for _ in range(50):
        # one at a time
        test_000.to_the_next_stop()
