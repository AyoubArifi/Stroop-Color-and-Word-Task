from psychopy import visual, core,event, gui
from psychopy.hardware import keyboard
import random
import csv
import time
# In Order For The Program To Run, Install The Above Libraries


# Getting Info From The Participants ----------------------------------
Task_name = gui.Dlg(title="Simple Stroop Task")
Task_name.addField("Please Enter Your Name:")
Task_name.addField("Age:")
Task_name.addField("Gender:", choices=["Male", "Female"])

participant_data = Task_name.show()
if Task_name.OK:
    participant_id = participant_data[0]
    age = participant_data[1]
    gender = participant_data[2]
else:
    core.quit()

# You Can Modify The Characteristics Of The Screen Here ---------------------------
win = visual.Window(fullscr=True, color="white", units="pix")
fixation = visual.TextStim(win, text="+", height=40, color="black")
stimulus = visual.TextStim(win, text="", height=60)
stimulus.bold = True
instructions = visual.TextStim(win, text="", height=30, wrapWidth=800, color="black")
instructions.text = (
    "You will see color words (RED, GREEN, BLUE, YELLOW) displayed in different inks.\n"
    "Respond to the INK of the text, NOT the meaning of the word.\n\n"
    "Press:\n r for red\n g for green\n b for blue\n y for yellow\n\n"
    "Respond as quickly and accurately as possible.\n"
    "Press SPACE to start.")
thank_you = visual.TextStim(win, text="Thank you!\n Experiment completed.", height=40, color="black")
kb = keyboard.Keyboard()
clock = core.Clock()


colors = {
    "red": "r",
    "green": "g",
    "blue": "b",
    "yellow": "y"
} # We Define The Colors Here

# You Can Change The keyboard Keys If You need. Just Change The Alphabet To the Key You Need.
color_names = list(colors.keys())





# Trial Conditions -------------------------------------------------------
def generate_trials():
    trials = []
# Congruent Trials: This Loop Will Generate 4 Trials.
    for color in color_names:
        trials.append({
            "word": color.upper(),
            "color": color,
            "condition": "congruent",
            "correct_key": colors[color]
        })
# Incongruent Trials: This Loop Will Generate 12 Incongruent Trials.
    for word in color_names:
        for ink in color_names:
            if word != ink: # The Congruent Matches Will Be Filtered.
                trials.append({
                    "word": word.upper(),
                    "color": ink,
                    "condition": "incongruent",
                    "correct_key": colors[ink]
                })
    return trials

# The Base Trials Will Result In 16 Trials Total. But Here, We Set The Amount Of Trials To 48 By Multiplying It By 3.
base_trials = generate_trials()
all_trials = base_trials * 3
random.shuffle(all_trials)

# Data File  ----------------------------------------------------------
timestamp = time.strftime("%Y%m%d")
data_filename = f"{participant_id}_{timestamp}.csv"
data_file = open(data_filename, "w", newline="")
writer = csv.writer(data_file)
writer.writerow(["participant_id", "trial_num", "word", "color", "condition", "response", "rt", "correct","age","gender"])







# Instructions Window ------------------------------------------
instructions.draw()
win.flip()
kb.waitKeys(keyList=["space"])







# Experiment loop -----------------------------------------------------

for i, trial in enumerate(all_trials):
    if kb.getKeys(keyList=["escape"]): # You Can Set The Key Of Your Choice For Exiting The Program.
        break
    
    fixation.draw()
    win.flip()
    core.wait(0.5 + random.uniform(-0.1, 0.1))  # Variable Fixation Cross In Order To Avoid Entrainment Effects.

  
    stimulus.text = trial["word"]        # Showing Stimulus
    stimulus.color = trial["color"]
    kb.clearEvents()
    clock.reset()
  
    stimulus.draw()
    win.flip()
    # The Stimulus Is Shown And Next Is To Press The Key For The Shown Trial.
    keys = kb.waitKeys(maxWait=1.5, keyList=["r", "g", "b", "y", "escape"])

    if keys:
        key = keys[0]
        response = getattr(key, 'name', None) or getattr(key, 'key', None) or key
        rt = clock.getTime()
        if response == "escape":
            break
        correct = int(response == trial["correct_key"])
    else:
        response = 'no_response'
        rt = 1.5
        correct = 0  
    
    writer.writerow([
        participant_id,
        i+1,
        trial["word"],
        trial["color"],
        trial["condition"],
        response,
        rt,
        correct,
        age,
        gender
    ])

  
    win.flip()
    core.wait(0.5 + random.uniform(-0.1, 0.1))


thank_you.draw()
win.flip()
core.wait(3.0)          # The Experiment Ends Here.


data_file.close()
win.close()
core.quit()            