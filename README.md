## Simple Stroop Task (PsychoPy)
A classic psychological experiment implementation using Python and the PsychoPy library. This script runs a standard Stroop Effect task where participants must identify the color of the ink a word is written in, while ignoring the meaning of the word itself.
This script presents a series of these stimuli and records the participant’s reaction time and accuracy.

### Required Libraries:

psychopy
random
csv
time

### Experiment Design

Stimuli: The words RED, GREEN, BLUE, and YELLOW displayed in corresponding or conflicting ink colors.

### Trials:
Congruent Trials: Word matches ink color (e.g., “RED” in red ink).
Incongruent Trials: Word differs from ink color (e.g., “RED” in blue ink).
Trial Count:48

### Timing:
Fixation Cross: 0.5s (+/- 0.1s jitter)
Stimulus Duration: Max 1.5s (or until response)
Inter-trial Interval: 0.5s (+/- 0.1s jitter)

### Data Output
The script automatically saves data to a .csv file in the same directory as the script.
