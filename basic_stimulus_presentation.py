from psychopy import core, visual
import pandas as pd

# Following tutorial found: https://www.socsci.ru.nl/wilberth/nocms/psychopy/print.php

def main():

    # Create a window
    win = visual.Window([400,300], monitor="testMonitor")

    # Create a stimulus for a certain window
    message = visual.TextStim(win, text="Hello there, world!")

    # Draw the stimulus to the window
    message.draw()

    # Flip backside of the window
    win.flip()

    # Pause3 sec
    core.wait(3.0)

    # Write a new message
    new_message = visual.TextStim(
            win, text="Now, for something entirely different")

    # Draw the new message
    new_message.draw()

    # And show the new message on the screen
    win.flip()

    # Wait again to appreciate
    core.wait(3.0)

    # Close the window
    win.close()

    # Close PsychoPy
    core.quit()

main()
