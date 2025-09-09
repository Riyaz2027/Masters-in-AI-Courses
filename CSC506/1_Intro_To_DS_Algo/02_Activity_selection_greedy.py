from operator import attrgetter

class Activity:
    def __init__(self, name, initial_start_time, initial_finish_time):
        self.name = name
        self.start_time = initial_start_time
        self.finish_time = initial_finish_time
        
    def conflicts_with(self, other_activity):
        # No conflict exists if this activity's finish_time comes
        # at or before the other activity's start_time.
        if self.finish_time <= other_activity.start_time:
            return False
            
        # No conflict exists if the other activity's finish_time
        # comes at or before this activity's start_time.
        elif other_activity.finish_time <= self.start_time:
            return False
            
        # In all other cases the two activity's conflict with each
        # other.
        else:
            return True
            
def activity_selection(activities):

    # Start with an empty list of selected activities.
    chosen_activities = []
    
    # Sort the list of activities in increasing order of finish_time.
    activities.sort(key = attrgetter("finish_time"))
    
    # Select the first activity, and add it to the chosen_activities list.
    current = activities[0]
    chosen_activities.append(current)
    
    # Process all the remaining activities, in order.
    for i in range(1, len(activities)):
    
        # If the next activity does not conflict with
        # the most recently selected activity, select the
        # next activity.
        if not activities[i].conflicts_with(current):
            chosen_activities.append(activities[i])
            current = activities[i]
            
    # The chosen_activities list is an optimal list of
    # activities with no conflicts.
    return chosen_activities

            
# Program to test Activity Selection greedy algorithm. The
# start_time and finish_time are represented with integers
# (ex. "20" is 20:00, or 8:00 PM).
activity_1 = Activity('Fireworks show', 20, 21)
activity_2 = Activity('Morning mountain hike', 9, 12)
activity_3 = Activity('History museum tour', 9, 10)
activity_4 = Activity('Day mountain hike', 13, 16)
activity_5 = Activity('Night movie', 19, 21)
activity_6 = Activity('Snorkeling', 15, 17)
activity_7 = Activity('Hang gliding', 14, 16)
activity_8 = Activity('Boat tour', 11, 14)

activities = [ activity_1, activity_2, activity_3, activity_4,
               activity_5, activity_6, activity_7, activity_8 ]

# Use the activity_selection() method to get a list of optimal
# activities with no conflicts.               
itinerary = activity_selection(activities)
for activity in itinerary:
    # Output the activity's information.
    print('%s - start time: %d, finish time: %d' %
         (activity.name, activity.start_time, activity.finish_time))
