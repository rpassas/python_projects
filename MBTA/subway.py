'''
Robert Passas
CS5001
hw5 - subway
provides directions for getting around via the Boston subway
'''
LINE_NAMES = ['Red', 'Orange', 'Blue', 'Green']
LINES = [['Alewife', 'Davis', 'Porter', 'Harvard',
         'Central', 'Kendall/MIT', 'Charles/MGH',
          'Downtown Crossing', 'South Station',
          'Broadway', 'Andrew', 'JFK/UMass'],
         ['Oak Grove', 'Malden Center', 'Wellington', 'Assembly',
          'Sullivan Square', 'Community College', 'North Station',
          'Haymarket', 'State', 'Downtown Crossing',
          'Chinatown', 'Tufts Medical Center', 'Back Bay',
          'Mass Avenue', 'Ruggles', 'Roxbury Crossing',
          'Jackson Square', 'Stony Brook', 'Green Street', 'Forest Hills'],
         ['Wonderland', 'Revere Beach', 'Beachmont',
          'Suffolk Downs', 'Orient Heights', 'Wood Island',
          'Airport', 'Maverick', 'Aquarium', 'State'],
         ['Haymarket', 'Government Center', 'Park Street', 'Boylston',
          'Arlington', 'Copley', 'Haynes Convention Center',
          'Kenmore', 'Blandford Street', 'Boston University East',
          'Boston University Central', 'Boston University West',
          'Saint Paul Street', 'Pleasant Street', 'Babcock Street',
          'Packards Corner', 'Harvard Avenue', 'Griggs Street',
          'Allston Street', 'Warren Street', 'Washington Street',
          'Sutherland Road', 'Chiswick Road',
          'Chestnut Hill Avenue', 'South Street', 'Boston College']]


def is_valid_station(name):
    '''
function - is_valid_station
indicate if station name exists
parameters: station name
returns boolean indicating existence
    '''
    for line in LINES:
        for stop in line:
            if '/' in stop:
                if name in stop:
                    return True
        if name in line:
            return True
    return False


def on_redline(station):
    '''
function - on_redline
indicates if the station is on the red line
parameters: station
returns boolean indicating presence on the red line
    '''
    if station == '':
        return False
    for stop in LINES[0]:
        if '/' in stop:
            if station in stop.replace('/', ''):
                return True
    if station in LINES[0]:
        return True
    else:
        return False


def on_orangeline(station):
    '''
function - on_orangeline
indicates if the station is on the orange line
parameters: station
returns boolean indicating presence on the orange line
    '''
    for stop in LINES[1]:
        if '/' in stop:
            if station in stop:
                return True
    if station in LINES[1]:
        return True
    else:
        return False


def on_blueline(station):
    '''
function - on_blueline
indicates if the station is on the blue line
parameters: station
returns boolean indicating presence on the blue line
    '''
    for stop in LINES[2]:
        if '/' in stop:
            if station in stop:
                return True
    if station in LINES[2]:
        return True
    else:
        return False


def on_greenline(station):
    '''
function - on_greenline
indicates if the station is on the green line
parameters: station
returns boolean indicating presence on the green line
    '''
    for stop in LINES[3]:
        if '/' in stop:
            if station in stop:
                return True
    if station in LINES[3]:
        return True
    else:
        return False


def get_intersecting_station(line_one, line_two):
    '''
function - get_intersecting_station
provides station name for intersection point of lines
parameters: two lines (str)
returns str name of station
    '''
    start_line = None
    stop_line = None
    if line_one == 'Red':
        start_line = 0
    elif line_one == 'Orange':
        start_line = 1
    elif line_one == 'Blue':
        start_line = 2
    elif line_one == 'Green':
        start_line = 3

    if line_two == 'Red':
        stop_line = 0
    elif line_two == 'Orange':
        stop_line = 1
    elif line_two == 'Blue':
        stop_line = 2
    elif line_two == 'Green':
        stop_line = 3
    if start_line is not None and stop_line is not None:
        for station in LINES[start_line]:
            if station in LINES[stop_line]:
                return station
    else:
        return None


def get_direction(start, end):
    '''
function - get_direction
indicates proper direction for travel towards the destination
parameters: str start and end stations
returns str indicating end station (direciton)
    '''
    start_pos = -1
    end_pos = -1
    for line in LINES:
        # assumes /
        for i in range(len(line)):
            if '/' in line[i]:
                if start in line[i]:
                    start_pos = i
                elif end in line[i]:
                    end_pos = i
            elif line[i] == start:
                start_pos = i
            elif line[i] == end:
                end_pos = i
        if start_pos > -1 and end_pos > -1:
            if start_pos > end_pos:
                return line[0]
            else:
                return line[-1]
        # otherwise
        elif start in line and end in line:
            for i in range(len(line)):
                if line[i] == start:
                    start_pos = i
                elif line[i] == end:
                    end_pos = i
        if start_pos > -1 and end_pos > -1:
            if start_pos > end_pos:
                return line[0]
            else:
                return line[-1]
    return None


def get_number_stops(start, end):
    '''
function - get_number_stops
provides the number of stops between stations
parameters: str names of two stations on the same line
returns int indicating number of stops
    '''
    start_pos = -1
    end_pos = -1
    for line in LINES:
        # assumes /
        for i in range(len(line)):
            if '/' in line[i]:
                if start in line[i]:
                    start_pos = i
                elif end in line[i]:
                    end_pos = i
            elif line[i] == start:
                start_pos = i
            elif line[i] == end:
                end_pos = i
        if start_pos > -1 and end_pos > -1:
            return abs(start_pos - end_pos)
        # assumes no /
        if start in line and end in line:
            for i in range(len(line)):
                if line[i] == start:
                    start_pos = i
                if line[i] == end:
                    end_pos = i
            return abs(start_pos - end_pos)
    return -1


def main():


    start = input("Enter starting station: ")
    stop = input("Enter destination station: ")
    if is_valid_station(start) is True and is_valid_station(stop) is True:
        pass
    else:
        print("I've never heard of that station, please try again")
        return
    start_lines = []
    stop_lines = []
    start_lines_i = []
    stop_lines_i = []
    # establish start lines
    if on_redline(start) is True:
        start_lines.append('Red')
        start_lines_i.append(0)
    if on_orangeline(start) is True:
        start_lines.append('Orange')
        start_lines_i.append(1)
    if on_blueline(start) is True:
        start_lines.append('Blue')
        start_lines_i.append(2)
    if on_greenline(start) is True:
        start_lines.append('Green')
        start_lines_i.append(3)
    # establish end lines
    if on_redline(stop) is True:
        stop_lines.append('Red')
        stop_lines_i.append(0)
    if on_orangeline(stop) is True:
        stop_lines.append('Orange')
        stop_lines_i.append(1)
    if on_blueline(stop) is True:
        stop_lines.append('Blue')
        stop_lines_i.append(2)
    if on_greenline(stop) is True:
        stop_lines.append('Green')
        stop_lines_i.append(3)
    start_line = start_lines[0]
    stop_line = stop_lines[0]
    start_line_i = -1
    stop_line_i = -1
    # same line?
    for i in range(len(start_lines_i)):
        if start_lines_i[i] in stop_lines_i:
            stop_line_i = start_lines_i[i]
            start_line_i = start_lines_i[i]
            stop_line = start_lines[i]
            start_line = start_lines[i]
    # intersecting?
    if start_line_i == -1:
        for i in range(len(start_lines_i)):
            for j in range(len(stop_lines_i)):
                if (get_intersecting_station(start_lines[i], stop_lines[j])
                        is not None):
                    stop_line_i = stop_lines_i[j]
                    start_line_i = start_lines_i[i]
                    stop_line = stop_lines[j]
                    start_line = start_lines[i]
    # hop from line to line if necessary
    current_line = start_line
    next_line = stop_line
    current_start = start
    current_stop = ''
    while current_stop != stop:
        if get_intersecting_station(current_line, next_line) is None:
            for line in LINE_NAMES:
                for stops in LINES:
                    if (get_intersecting_station(current_line, line) in stops
                        and get_intersecting_station(next_line, line)
                            in stops):
                        next_line = line
                    else:
                        pass
        if current_line != next_line:
            current_stop = get_intersecting_station(current_line, next_line)
        else:
            current_stop = stop
        direction = get_direction(current_start, current_stop)
        num_stops = get_number_stops(current_start, current_stop)
        print('Get on the', current_line, 'Line at',
              current_start, 'towards', str(direction) + '.')
        if num_stops > 1:
            print('Take the train for', num_stops,
                  'stops and arrive at', str(current_stop) + '.')
        else:
            print('Take the train for', num_stops,
                  'stop and arrive at', str(current_stop) + '.')
        current_start = current_stop
        current_line = next_line
        next_line = stop_line


if __name__ == "__main__":
    main()
