from psychopy import visual
from psychopy import event
from psychopy import core
import math
import random

def get_trial_type(n):
    return {
        0: 'distance',
        1: 'duration'
    }[math.floor(n/81)]

def get_distance_index(n, array, trials):
    denominator_val = trials/len(array)
    return math.floor(n/denominator_val)

def get_duration_index(n, array):
    return n%len(array)

def present_trial_type_message(win, txt, this_trial_type):
    if this_trial_type == 'distance':
        message_text = "Line Distance (SPATIAL)"
    else:
        message_text = "Line Duration (TEMPORAL)"

    # Update the text stimulus object to reflect the new text
    txt.text = message_text
    txt.pos = (0, 0)
    txt.draw()

    # Make a message saying to press a button to continue
    txt.text = "Press any key to continue"
    txt.pos = (0,-50)
    txt.draw()

    # Flip the window onto the screen
    win.flip()
    # Keep the message there until a key is pressed
    event.waitKeys()
    # Flip the window again to get rid of the message_text
    win.flip()
    # Return true so that we can check that the message was fully displayed
    return True

def present_stimulus(win, line, this_distance, this_duration_frames):
    # Wait a certain amount of time
    core.wait(1.5)

    # Update the line to represent the current stimulus parameters
    line.start = [-this_distance/2, 0]
    line.end = [this_distance/2, 0]

    for frame_num in range(int(this_duration_frames)):
        line.draw()
        win.flip()

    win.flip()

    # Reset line length so it isn't accidentally preserved and shown again to the user
    line.start = [0, 0]
    line.end = [0, 0]

    return True


def collect_distance_response(win, line, mouse):

    # Create a line at center of screen, less than minimum distance
    line.start = [0, 0]
    line.end = [0, 0]
    line.lineColor = 'yellow'
    line.draw()
    win.flip()

    # Reset mouse
    mouse.clickReset()

    # When getTime is set to true, mouse.getPressed will return a
    #   tuple of size two. The first element will be a list of 3 booleans, 
    #   each of which corresponds to whether the mouse button 0,1,2
    #   has been pressed since the last time mouse.clickReset was called.
    #   The second element will be a list of timestamps of when the
    #   mouse was clicked.
    while True not in mouse.getPressed(getTime=True)[0]:
   
        # Get mouse position
        # mouse.getPos() returns a tuple of size 2, indicating the current
        #   x and y positions -- (0,0) is at the center of the window
        mouse_position = mouse.getPos()

        # Update line start,end to -/+ mouse x-pos
        line.start = [-mouse_position[0], 0]
        line.end = [mouse_position[0], 0]
        line.draw()

        win.flip()

    # Store x pos so that it can be returned
    #   Double it, since 0 is at the center of window so the mouse position's
    #   x value only represents half of the length of the line
    user_inputted_length = 2*abs(line.start[0])

    # Change the color of the line, or something, to indicate its clicked
    line.lineColor = 'red'
    line.draw()
    win.flip()

    # Wait a second or two
    core.wait(1.5)

    # Flip the screen to make it blank again
    win.flip()

    # Reset the color of the line for future use
    line.lineColor = 'black'

    return user_inputted_length

def collect_duration_response(win, line, mouse):
    # Present a short line or square or something at the center of screen
    line.start = [-30, 0]
    line.end = [30, 0]
    line.draw()
    win.flip()

    # Initialize a counter that will keep track of inputted 
    user_inputted_duration_frames = 0

    # Wait until the mouse is clicked
    mouse.clickReset()
    while True not in mouse.getPressed(getTime=True)[0]:
        pass

    core.wait(0.5)
    mouse.clickReset()
    # Once the mouse is clicked, color the line a different color
    line.lineColor = 'yellow'
    

    while True not in mouse.getPressed(getTime=True)[0]:
        user_inputted_duration_frames += 1

        line.draw()
        win.flip()

    line.lineColor = 'red'
    line.draw()
    win.flip()

    line.lineColor = 'black'
    core.wait(1.5)
    win.flip()

    return user_inputted_duration_frames



def main(): 

    distances = [50, 100, 150, 200, 250, 300, 350, 400, 450]
    durations = [1, 1.5, 2, 2.5, 3, 3.5, 4, 4.5, 5]
    screen_refresh_rate = 60

    win = visual.Window(
        #size=[500,500],
        units='pix',
        fullscr=True,
        color=[1, 1, 1]
    )

    mouse = event.Mouse(
        visible=False,
        win=win
    )

    # http://www.psychopy.org/general/timing/detectingFrameDrops.html
    # I read in the link above that it is faster to create the stimuli
    #   once at the top of the script then update them as you go than
    #   it is to create them from scratch each time, so I will do that
    #   here for a line stimulus and a text stimulus.
    # The line will be used to present the experiment stimulus, as well
    #   as visualize the user's response as they enter it.
    # The text will be used to display various text as we go.
    
    # Note, I don't really like this way of coding, eg using a single
    #   object rather than creating different ones for their actual
    #   purposes, but if it makes PsychoPy less likely to break stuff
    #   then so be it.

    txt = visual.TextStim(
        win=win,
        units='pix',
        color=[-1,-1,-1],
        text="Welcome to the experiment."
    )

    line = visual.Line(
        win=win,
        units='pix',
        lineWidth = 10,
        lineColor=[-1, -1, -1],
        start=(0,0),
        end=(0,0)
    )

    txt.draw()

    txt.text = "Please press any key to begin, and 'q' to quit."
    txt.pos = (0, -150)
    txt.draw()

    win.flip()

    event.waitKeys()

    # Total number of trials = distances*durations *2, since there are two
    #   types of trials
    number_of_trials = len(distances)*len(durations)*2

    # Create a list of indicies between 0 and number_of_trials-1
    # This will be looped over and will determine the conditions for 
    #       each trial
    trial_indicies = list(range(number_of_trials))
    
    # Shuffle the order of the trial indicies to randomize
    random.shuffle(trial_indicies)


    # Loop through the trial_indicies list, each time through the
    # loop representing one trial
    for trial_number in trial_indicies:
        
        # First, figure out what type of trial it is,
        # ie time or distance, which will determine which type of
        # response will be collected
        this_trial_type = get_trial_type(trial_number)
    
        # Get the distance value that will be used
        this_distance = distances[
            get_distance_index(trial_number, distances, number_of_trials)
        ]
        
        # Get the duration value that will be used
        this_duration = durations[
            get_duration_index(trial_number, durations)
        ]

        # Get the current duration in frames, rather than seconds
        this_duration_frames = screen_refresh_rate*this_duration

        # Just to make sure everything is working, print out the trial conditions to the console
        # print([this_trial_type, this_distance, this_duration])

        # Present a message indicating which type of trial it will be, ie duration or distance
        trial_type_message_presented = present_trial_type_message(
            win, txt, this_trial_type)


        # Then present a line of length this_distance for a duration this_duration
        stimulus_finished_presenting = present_stimulus(
            win, line, this_distance, this_duration_frames)

        # Then wait another period of time
        core.wait(1.5)

        # Then either collect a time response or duration response, depending on this_trial_type
        if this_trial_type == "distance": 
            user_stimulus_estimate = collect_distance_response(win, line, mouse)
            print(f"Actual length: {this_distance}\nEstimated length: {user_stimulus_estimate}")
        else: # then it's duration 
            user_stimulus_estimate = collect_duration_response(win, line, mouse)
            print(f"Actual duration: {this_duration_frames}\nEstimated duration: {user_stimulus_estimate}")

        # Write the data to file
        

main()