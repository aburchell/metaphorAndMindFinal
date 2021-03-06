from psychopy import visual
from psychopy import event
from psychopy import core
import math
import random
import os
import sys
import csv
import datetime

def get_trial_type(n, trials):
    return {
        0: 'distance',
        1: 'duration'
    }[math.floor(n/(trials/2))]

def get_distance_index(n, array, trials):
    denominator_val = trials/len(array)
    return math.floor(n/denominator_val)

def get_duration_index(n, array):
    return n%len(array)

def get_user_info(win, txt):

    starting_prompt_text = "Please enter a participant name, then ENTER to continue.\nName: "
    txt.pos = [-300, 300]
    txt.text = starting_prompt_text
    txt.draw()
    win.flip()

    # Write out the keys that you want to register, then change it into a list of single chars
    valid_keys_string = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890'
    valid_keys = list(valid_keys_string)
    # Add in a few more keys
    valid_keys.extend(['return','space','underscore','backspace'])

    # This inputting is fairly brittle. qI figured this is probably fine for 
    #   this early/relatively unimportant step, but it could be made more robust using the 
    #   information from:
    #   https://stackoverflow.com/questions/26274454/getting-free-text-string-input-from-participant
    keys = event.waitKeys(keyList=valid_keys)
    while 'return' not in keys:
        # Replace the word space (returned by waitKeys) into the actual space char
        if keys[-1] == 'space':
            keys[-1] = ' '
        elif keys[-1] == 'underscore':
            keys[-1] = '_'

        # Add the last inputted key to the end of the prompt on screen
        if keys[-1] == 'backspace':
            txt.text = txt.text[:-1]
        else:
            txt.text += keys[-1]

        txt.draw()
        win.flip()

        # Wait for some more keys
        keys = event.waitKeys(keyList=valid_keys)

    win.flip()
    core.wait(1)

    # Send back all the text after the text from the starting prompt
    participant_input = str(txt.text[len(starting_prompt_text):])
    return participant_input

def present_trial_type_message(win, txt, this_trial_type, practice):
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

    # If it is a practice round, say so
    if practice:
        txt.text = "PRACTICE"
        txt.pos = (0, 50)
        txt.draw()

    # Flip the window onto the screen
    win.flip()
    # Keep the message there until a key is pressed
    event.waitKeys()
    # Flip the window again to get rid of the message_text
    win.flip()
    # Return true so that we can check that the message was fully displayed
    return True

def present_stimulus(win, line, this_distance, this_duration_frames,
                        time_after_click_before_stim):
    # Wait a certain amount of time
    core.wait(time_after_click_before_stim)

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

def collect_distance_response(win, line, mouse, txt,
                                time_after_user_input_is_finalized,
                                practice):

    # Create a line at center of screen, less than minimum distance
    line.start = [0, 0]
    line.end = [0, 0]
    line.lineColor = 'blue'
    line.draw()

    # If it's practice, give some direction messages
    if practice:
        txt.pos = [-300, 250]
        txt.text = 'Move the mouse to change the length of the line.\nOnce you have the line as long as you want, click once to finalize.\nThe line will turn red, and you will move on to the next trial.'
        txt.draw()

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

        if practice:
                    txt.draw()

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
    core.wait(time_after_user_input_is_finalized)

    # Flip the screen to make it blank again
    win.flip()

    # Reset the color of the line for future use
    line.lineColor = 'black'

    return user_inputted_length

def collect_duration_response(win, line, mouse, txt,
                                time_after_user_input_is_finalized,
                                practice):
    # Present a short line or square or something at the center of screen
    line.start = [-30, 0]
    line.end = [30, 0]
    line.draw()

    # If it's practice, give some direction messages
    if practice:
        txt.pos = [-300, 250]
        txt.text = 'Click once to start.\nTiming will begin when the line turns blue,\nand end when you click again and the line turns red.'
        txt.draw()

    win.flip()

    # Initialize a counter that will keep track of inputted time
    user_inputted_duration_frames = 0

    # Wait until the mouse is clicked
    mouse.clickReset()
    while True not in mouse.getPressed(getTime=True)[0]:
        pass

    # Wait half a second before resetting the mouse and changing
    #   the color so that the same click isn't picked up more than
    #   once and accidentally record a super short participant 
    #   response.
    # This is not a super elegant solution, and perhaps should be fixed
    #   or improved upon in the future. For example, in the current
    #   implementation the user's response starts to be timed when
    #   the color changes, not when the participant clicks the mouse
    core.wait(0.5)
    mouse.clickReset()

    # Once the mouse is clicked, color the line a different color
    line.lineColor = 'blue'
    

    # While the user hasn't clicked again, keep incrementing a
    #   counter of how many frames have passed -- this is our
    #   timer.
    while True not in mouse.getPressed(getTime=True)[0]:
        user_inputted_duration_frames += 1
        line.draw()
        win.flip()

    # Now that the user has clicked again, change the line to red
    #   as feedback
    line.lineColor = 'red'
    line.draw()
    win.flip()

    core.wait(time_after_user_input_is_finalized)

    # Reset the line object back to its normal properties
    line.lineColor = 'black'

    # Clear the screen
    win.flip()

    return user_inputted_duration_frames

def run_experiment(
    distances, durations, screen_refresh_rate, 
    data_path, between_stim_and_resp_time, time_after_click_before_stim,
    time_after_user_input_is_finalized, practice=False):

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




    # Get user information and write the headers to a csv file
    username = get_user_info(win, txt)
    print(username)

    filename = './data/'+username+data_path
    if os.path.exists(filename):
        sys.exit(f"Filename '{filename}' already exists.")
    else:
        with open(filename, 'a') as fp:
            writer = csv.writer(fp)
            writer.writerow(
                ['trial_num', 'participant', 'practice', 'time', 
                'stim_presented',
                'trial_id', 'trial_type', 'line_distance', 'line_duration',
                'user_distance', 'user_duration'])

    # If we want to have some practice rounds, lets do them
    if practice:
        run_trials(
            win,
            line,
            txt,
            mouse,
            [50, 150], 
            [1, 2],
            screen_refresh_rate, 
            filename,
            username,
            between_stim_and_resp_time, 
            time_after_click_before_stim,
            time_after_user_input_is_finalized, 
            practice=True)
        
        win.flip()
        txt.text = "END OF PRACTICE\nClick to continue onto experiment"
        txt.pos = [0, 0]
        txt.draw()
        win.flip()
        event.waitKeys()
        win.flip()

    # If not, just get to the real deal
    run_trials(
            win,
            line,
            txt,
            mouse,
            distances, 
            durations,
            screen_refresh_rate, 
            filename,
            username,
            between_stim_and_resp_time, 
            time_after_click_before_stim,
            time_after_user_input_is_finalized, 
            practice=False)

def run_trials(
            win,
            line,
            txt,
            mouse,
            distances, 
            durations,
            screen_refresh_rate, 
            filename,
            username,
            between_stim_and_resp_time, 
            time_after_click_before_stim,
            time_after_user_input_is_finalized, 
            practice=False):

    # Total number of trials = distances*durations *2, since there are two
    #   types of trials
    number_of_trials = len(distances)*len(durations)*2

    # Create a list of indicies between 0 and number_of_trials-1
    # This will be looped over and will determine the conditions for 
    #       each trial
    trial_indicies = list(range(number_of_trials))
    
    # Shuffle the order of the trial indicies to randomize
    random.shuffle(trial_indicies)
    print(trial_indicies)

    # Loop through the trial_indicies list, each time through the
    # loop representing one trial
    #   NOTE: 
    #       trial_num = 0, 1, 2, 3, ..., ie how many times through 
    #                   the loop it's been
    #       trial_id = 17, 93, 23, ..., ie the number from the 
    #                   shuffled list trial_indicies, which 
    #                   indicates the properties of the trial
    for trial_num, trial_id in enumerate(trial_indicies):
        print(f"Trial number: {trial_num}\nCondition ID: {trial_id}")

        # First, figure out what type of trial it is,
        # ie time or distance, which will determine which type of
        # response will be collected
        this_trial_type = get_trial_type(trial_id, number_of_trials)
    
        # Get the distance value that will be used
        this_distance = distances[
            get_distance_index(trial_id, distances, number_of_trials)
        ]
        
        # Get the duration value that will be used
        this_duration = durations[
            get_duration_index(trial_id, durations)
        ]

        # Get the current duration in frames, rather than seconds
        this_duration_frames = screen_refresh_rate*this_duration

        # Just to make sure everything is working, print out the trial conditions to the console
        # print([this_trial_type, this_distance, this_duration])

        # Present a message indicating which type of trial it will be, ie duration or distance
        trial_type_message_presented = present_trial_type_message(
            win, txt, this_trial_type, practice)


        # Then present a line of length this_distance for a duration this_duration
        stimulus_finished_presenting = present_stimulus(
            win, line, this_distance, this_duration_frames, 
            time_after_click_before_stim)

        # Then wait another period of time
        core.wait(between_stim_and_resp_time)

        # Then either collect a time response or duration response, depending on this_trial_type
        if this_trial_type == "distance": 
            user_stimulus_estimate = collect_distance_response(
                win, line, mouse, txt, time_after_user_input_is_finalized,
                practice)

            # Write the data from this trial to file
            with open(filename, 'a') as fp:
                writer = csv.writer(fp)
                writer.writerow(
                    [trial_num,
                    username,
                    practice,
                    datetime.datetime.now(),
                    stimulus_finished_presenting,
                    trial_id, 
                    this_trial_type, 
                    this_distance, 
                    this_duration,
                    user_stimulus_estimate, 
                    'NaN'
                    ])

        else: # then it's duration 
            user_stimulus_estimate = collect_duration_response(
                win, line, mouse, txt, time_after_user_input_is_finalized,
                practice)

            # Write the data from this trial to file
            with open(filename, 'a') as fp:
                writer = csv.writer(fp)
                writer.writerow(
                    [trial_num, 
                    username,
                    practice,
                    datetime.datetime.now(),
                    stimulus_finished_presenting,
                    trial_id, 
                    this_trial_type, 
                    this_distance, 
                    this_duration,
                    'NaN', 
                    user_stimulus_estimate/screen_refresh_rate
                    ])

def main(): 

    # Distances are in pixels
    # Durations are in seconds
    # screen_refresh_rate is in Hz
    distances = [425, 444, 463, 484, 505, 527, 550, 575, 600]
    durations = [.500, .629, .792, .997, 1.254, 1.578, 1.987, 2.500, 3.15]
    screen_refresh_rate = 60
    data_path = '_duration_distance_solid_line_data.csv'
    want_practice_block = True 

    # NOTE: All these times in seconds 
    # Time between the functions that present the stimulus and 
    #   record the response
    between_stim_and_resp_time = 1.5
    # Time after clicking to continue past the screen that says what
    #   type of trial it is
    time_after_click_before_stim = 1.5
    # Time before next trial, after the user has input their response
    time_after_user_input_is_finalized = 1.5


    run_experiment(
        distances, durations, screen_refresh_rate, data_path,
        between_stim_and_resp_time, time_after_click_before_stim,
        time_after_user_input_is_finalized, want_practice_block)



main()