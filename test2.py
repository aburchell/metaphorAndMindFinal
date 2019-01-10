from psychopy import core, visual, event
import pandas as pd

# Following tutorial found: https://www.socsci.ru.nl/wilberth/nocms/psychopy/print.php

def flip_some_frames(window,frames=500):
    for frame_num in range(frames):
        if frame_num % 20 == 0:
            update_message = visual.TextStim(
                window, text=f"{frame_num} frames have elapsed")
            update_message.draw()
            window.flip()

def main():

    

    # Create a window
    win = visual.Window([400,300], monitor="testMonitor")

    # Set up a global shutdown key
    event.globalKeys.add(key='q', func = core.quit)
    
    # Create a stimulus for a certain window
    message = visual.TextStim(win, text="Time to start!")

    # Draw the stimulus to the window
    message.draw()

    # Flip backside of the window
    win.flip()

    # Pause3 sec
    core.wait(3.0)

    # Present a new stimulus for 500 frames, changing the stimulus
    #   every 20 frames
    flip_some_frames(win, 500000) 

    #Present a final message, notifying the end of the 500 frames
    final_message = visual.TextStim(
            win, text="Finished! Closing shortly")
    final_message.draw()
    win.flip()

    # Wait again to appreciate
    core.wait(3.0)

    # Close the window
    win.close()

    # Close PsychoPy
    core.quit()

main()
