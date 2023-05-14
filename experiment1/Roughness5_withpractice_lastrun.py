#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2022.2.4),
    on May 14, 2023, at 15:47
If you publish work using this script the most relevant publication is:

    Peirce J, Gray JR, Simpson S, MacAskill M, Höchenberger R, Sogo H, Kastman E, Lindeløv JK. (2019) 
        PsychoPy2: Experiments in behavior made easy Behav Res 51: 195. 
        https://doi.org/10.3758/s13428-018-01193-y

"""

# --- Import packages ---
from psychopy import locale_setup
from psychopy import prefs
prefs.hardware['audioLib'] = 'ptb'
from psychopy import sound, gui, visual, core, data, event, logging, clock, colors, layout
from psychopy.constants import (NOT_STARTED, STARTED, PLAYING, PAUSED,
                                STOPPED, FINISHED, PRESSED, RELEASED, FOREVER)

import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import (sin, cos, tan, log, log10, pi, average,
                   sqrt, std, deg2rad, rad2deg, linspace, asarray)
from numpy.random import random, randint, normal, shuffle, choice as randchoice
import os  # handy system and path functions
import sys  # to get file system encoding

import psychopy.iohub as io
from psychopy.hardware import keyboard



# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
os.chdir(_thisDir)
# Store info about the experiment session
psychopyVersion = '2022.2.4'
expName = 'Roughness.'  # from the Builder filename that created this script
expInfo = {
    'gender': '',
    'participant': '',
}
# --- Show participant info dialog --
dlg = gui.DlgFromDict(dictionary=expInfo, sortKeys=False, title=expName)
if dlg.OK == False:
    core.quit()  # user pressed cancel
expInfo['date'] = data.getDateStr()  # add a simple timestamp
expInfo['expName'] = expName
expInfo['psychopyVersion'] = psychopyVersion

# Data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
filename = _thisDir + os.sep + u'data/%s_%s_%s' %(expInfo['participant'], expName, expInfo['date'])

# An ExperimentHandler isn't essential but helps with data saving
thisExp = data.ExperimentHandler(name=expName, version='',
    extraInfo=expInfo, runtimeInfo=None,
    originPath='C:\\Users\\ktamp\\OneDrive\\Desktop\\experiment1\\Roughness5_withpractice_lastrun.py',
    savePickle=True, saveWideText=True,
    dataFileName=filename)
# save a log file for detail verbose info
logFile = logging.LogFile(filename+'.log', level=logging.EXP)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

endExpNow = False  # flag for 'escape' or other condition => quit the exp
frameTolerance = 0.001  # how close to onset before 'same' frame

# Start Code - component code to be run after the window creation

# --- Setup the Window ---
win = visual.Window(
    size=[1920, 1200], fullscr=True, screen=0, 
    winType='pyglet', allowStencil=False,
    monitor='testMonitor', color=[0,0,0], colorSpace='rgb',
    blendMode='avg', useFBO=True)
win.mouseVisible = False
# store frame rate of monitor if we can measure it
expInfo['frameRate'] = win.getActualFrameRate()
if expInfo['frameRate'] != None:
    frameDur = 1.0 / round(expInfo['frameRate'])
else:
    frameDur = 1.0 / 60.0  # could not measure, so guess
# --- Setup input devices ---
ioConfig = {}

# Setup iohub keyboard
ioConfig['Keyboard'] = dict(use_keymap='psychopy')

ioSession = '1'
if 'session' in expInfo:
    ioSession = str(expInfo['session'])
ioServer = io.launchHubServer(window=win, **ioConfig)
eyetracker = None

# create a default keyboard (e.g. to check for escape)
defaultKeyboard = keyboard.Keyboard(backend='iohub')

# --- Initialize components for Routine "instructions" ---
instrText = visual.TextStim(win=win, name='instrText',
    text='You will be presented with two tones and will have to respond to simple questions using a slider. Please pay attention to both tones, as you will need to compare them to each other. The questions will either be about how similar the two tones are in their pitch, tremolo or roughness. \n\nSome example sounds will also be played to introduce what is meant by tremolo, roughness and pitch. \n\nPress any key to proceed. ',
    font='Arial',
    pos=[0, 0], height=0.07, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
instrEnd = keyboard.Keyboard()

# --- Initialize components for Routine "questions" ---
text_8 = visual.TextStim(win=win, name='text_8',
    text='There will be 3 blocks of trials, the duration of each will be approximately 10 minutes. \n\nIf you have any questions about the experiment please ask now, as you will not be able to do so once the experiment has begun.\n\nIf not press any key to continue.',
    font='Arial',
    pos=(0, 0), height=0.07, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
key_resp = keyboard.Keyboard()

# --- Initialize components for Routine "consent" ---
title = visual.TextStim(win=win, name='title',
    text='CONSENT FORM',
    font='Open Sans',
    pos=(0, 0.7), height=0.075, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
Q1 = visual.TextStim(win=win, name='Q1',
    text='Have you read and understood the Information Sheet?',
    font='Open Sans',
    pos=(-0.2, 0.5), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);
Q2 = visual.TextStim(win=win, name='Q2',
    text='Have you had the opportunity to ask questions about the study?',
    font='Open Sans',
    pos=(-0.2, 0.25), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-2.0);
Q3 = visual.TextStim(win=win, name='Q3',
    text='Have all your questions been answered satisfactorily (if applicable)',
    font='Open Sans',
    pos=(-0.2, 0.05), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-3.0);
Q4 = visual.TextStim(win=win, name='Q4',
    text='Do you understand that you are free to withdraw from the study? (at any time and without giving a reason)',
    font='Open Sans',
    pos=(-0.2, -0.2), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-4.0);
Q5 = visual.TextStim(win=win, name='Q5',
    text='I give permission for my data from this study to be shared with other researchers provided that my anonymity is completely protected.',
    font='Open Sans',
    pos=(-0.2, -0.4), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-5.0);
Q6 = visual.TextStim(win=win, name='Q6',
    text='Do you agree to take part in the study?',
    font='Open Sans',
    pos=(-0.2, -0.65), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-6.0);
resp1 = visual.Slider(win=win, name='resp1',
    startValue=None, size=(0.15, 0.015), pos=(0.5, 0.5), units=None,
    labels=("yes", "no"), ticks=(1, 2), granularity=1.0,
    style='radio', styleTweaks=(), opacity=None,
    labelColor='LightGray', markerColor='Red', lineColor='White', colorSpace='rgb',
    font='Open Sans', labelHeight=0.05,
    flip=False, ori=0.0, depth=-7, readOnly=False)
resp2 = visual.Slider(win=win, name='resp2',
    startValue=None, size=(0.15, 0.015), pos=(0.5, 0.25), units=None,
    labels=("yes", "no"), ticks=(1, 2), granularity=1.0,
    style='radio', styleTweaks=(), opacity=None,
    labelColor='LightGray', markerColor='Red', lineColor='White', colorSpace='rgb',
    font='Open Sans', labelHeight=0.05,
    flip=False, ori=0.0, depth=-8, readOnly=False)
resp3 = visual.Slider(win=win, name='resp3',
    startValue=None, size=(0.15, 0.015), pos=(0.5, 0.05), units=None,
    labels=("yes", "no"), ticks=(1, 2), granularity=1.0,
    style='radio', styleTweaks=(), opacity=None,
    labelColor='LightGray', markerColor='Red', lineColor='White', colorSpace='rgb',
    font='Open Sans', labelHeight=0.05,
    flip=False, ori=0.0, depth=-9, readOnly=False)
resp4 = visual.Slider(win=win, name='resp4',
    startValue=None, size=(0.15, 0.015), pos=(0.5, -0.2), units=None,
    labels=("yes", "no"), ticks=(1, 2), granularity=1.0,
    style='radio', styleTweaks=(), opacity=None,
    labelColor='LightGray', markerColor='Red', lineColor='White', colorSpace='rgb',
    font='Open Sans', labelHeight=0.05,
    flip=False, ori=0.0, depth=-10, readOnly=False)
resp5 = visual.Slider(win=win, name='resp5',
    startValue=None, size=(0.15, 0.015), pos=(0.5, -0.4), units=None,
    labels=("yes", "no"), ticks=(1, 2), granularity=1.0,
    style='radio', styleTweaks=(), opacity=None,
    labelColor='LightGray', markerColor='Red', lineColor='White', colorSpace='rgb',
    font='Open Sans', labelHeight=0.05,
    flip=False, ori=0.0, depth=-11, readOnly=False)
resp6 = visual.Slider(win=win, name='resp6',
    startValue=None, size=(0.15, 0.015), pos=(0.5, -0.65), units=None,
    labels=("yes", "no"), ticks=(1, 2), granularity=1.0,
    style='radio', styleTweaks=(), opacity=None,
    labelColor='LightGray', markerColor='Red', lineColor='White', colorSpace='rgb',
    font='Open Sans', labelHeight=0.05,
    flip=False, ori=0.0, depth=-12, readOnly=False)
mouse_consent = event.Mouse(win=win)
x, y = [None, None]
mouse_consent.mouseClock = core.Clock()
nextButton_consent = visual.ImageStim(
    win=win,
    name='nextButton_consent', 
    image='next.png', mask=None, anchor='center',
    ori=0.0, pos=(0, -0.85), size=(0.2, 0.1),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-14.0)

# --- Initialize components for Routine "example_sounds" ---
ExampleKeys = keyboard.Keyboard()
text_6 = visual.TextStim(win=win, name='text_6',
    text='Example Sounds:\nPress the number buttons to hear:\n\n1 - increasing pitch\n2 - decreasing pitch\n\n5 - increasing roughness\n6 - decreasing roughness\n\n\n9 - increasing tremolo\n0 - decreasing tremolo\n\nPlease listen to each of the sounds until you know what is meant by each sensation.',
    font='Arial',
    pos=(0, 0), height=0.07, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-2.0);
text_7 = visual.TextStim(win=win, name='text_7',
    text=None,
    font='Open Sans',
    pos=(0, -0.7), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-3.0);
text_9 = visual.TextStim(win=win, name='text_9',
    text='Play each sound at least once.',
    font='Open Sans',
    pos=(0, -0.9), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-4.0);

# --- Initialize components for Routine "ready_go" ---
text_countdown = visual.TextStim(win=win, name='text_countdown',
    text='',
    font='Arial',
    pos=(0, 0), height=0.07, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);

# --- Initialize components for Routine "Fixation1" ---
fix = visual.TextStim(win=win, name='fix',
    text='+ ',
    font='Arial',
    pos=(0, 0), height=0.07, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
text_11 = visual.TextStim(win=win, name='text_11',
    text='',
    font='Arial',
    pos=(0, 0.25), height=0.07, wrapWidth=0.65, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);

# --- Initialize components for Routine "Trial" ---
stimulus = visual.TextStim(win=win, name='stimulus',
    text='',
    font='Arial',
    pos=[0, 0], height=0.07, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
text_10 = visual.TextStim(win=win, name='text_10',
    text='',
    font='Arial',
    pos=(0, 0.25), height=0.07, wrapWidth=0.65, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-2.0);

# --- Initialize components for Routine "response" ---
text = visual.TextStim(win=win, name='text',
    text='',
    font='Arial',
    pos=(0, 0.25), height=0.07, wrapWidth=0.65, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
slider = visual.Slider(win=win, name='slider',
    startValue=0, size=(1.0, 0.1), pos=(0, -0.4), units=None,
    labels=('The same', 'Completely different'), ticks=(0,100), granularity=0.0,
    style='rating', styleTweaks=(), opacity=None,
    labelColor='LightGray', markerColor=[-1.0000, -1.0000, -1.0000], lineColor='White', colorSpace='rgb',
    font='Arial', labelHeight=0.07,
    flip=False, ori=0.0, depth=-1, readOnly=False)

# --- Initialize components for Routine "end_block" ---
text_2 = visual.TextStim(win=win, name='text_2',
    text="You've reached the end of the block.\n\nYou can take a short break.\n\nPress any key when you're ready to continue. ",
    font='Arial',
    pos=(0, 0), height=0.07, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
key_resp_2 = keyboard.Keyboard()

# --- Initialize components for Routine "thanks" ---
thanksText = visual.TextStim(win=win, name='thanksText',
    text="You're done! Thanks for taking part!",
    font='Arial',
    pos=[0, 0], height=0.07, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.Clock()  # to track time remaining of each (possibly non-slip) routine 

# --- Prepare to start Routine "instructions" ---
continueRoutine = True
routineForceEnded = False
# update component parameters for each repeat
instrEnd.keys = []
instrEnd.rt = []
_instrEnd_allKeys = []
# keep track of which components have finished
instructionsComponents = [instrText, instrEnd]
for thisComponent in instructionsComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
frameN = -1

# --- Run Routine "instructions" ---
while continueRoutine:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *instrText* updates
    if instrText.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        instrText.frameNStart = frameN  # exact frame index
        instrText.tStart = t  # local t and not account for scr refresh
        instrText.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(instrText, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'instrText.started')
        instrText.setAutoDraw(True)
    
    # *instrEnd* updates
    waitOnFlip = False
    if instrEnd.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        instrEnd.frameNStart = frameN  # exact frame index
        instrEnd.tStart = t  # local t and not account for scr refresh
        instrEnd.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(instrEnd, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'instrEnd.started')
        instrEnd.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(instrEnd.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(instrEnd.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if instrEnd.status == STARTED and not waitOnFlip:
        theseKeys = instrEnd.getKeys(keyList=None, waitRelease=False)
        _instrEnd_allKeys.extend(theseKeys)
        if len(_instrEnd_allKeys):
            instrEnd.keys = _instrEnd_allKeys[-1].name  # just the last key pressed
            instrEnd.rt = _instrEnd_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in instructionsComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "instructions" ---
for thisComponent in instructionsComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# the Routine "instructions" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# --- Prepare to start Routine "questions" ---
continueRoutine = True
routineForceEnded = False
# update component parameters for each repeat
key_resp.keys = []
key_resp.rt = []
_key_resp_allKeys = []
# keep track of which components have finished
questionsComponents = [text_8, key_resp]
for thisComponent in questionsComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
frameN = -1

# --- Run Routine "questions" ---
while continueRoutine:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_8* updates
    if text_8.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_8.frameNStart = frameN  # exact frame index
        text_8.tStart = t  # local t and not account for scr refresh
        text_8.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_8, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'text_8.started')
        text_8.setAutoDraw(True)
    
    # *key_resp* updates
    waitOnFlip = False
    if key_resp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        key_resp.frameNStart = frameN  # exact frame index
        key_resp.tStart = t  # local t and not account for scr refresh
        key_resp.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'key_resp.started')
        key_resp.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp.status == STARTED and not waitOnFlip:
        theseKeys = key_resp.getKeys(keyList=None, waitRelease=False)
        _key_resp_allKeys.extend(theseKeys)
        if len(_key_resp_allKeys):
            key_resp.keys = _key_resp_allKeys[-1].name  # just the last key pressed
            key_resp.rt = _key_resp_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in questionsComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "questions" ---
for thisComponent in questionsComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if key_resp.keys in ['', [], None]:  # No response was made
    key_resp.keys = None
thisExp.addData('key_resp.keys',key_resp.keys)
if key_resp.keys != None:  # we had a response
    thisExp.addData('key_resp.rt', key_resp.rt)
thisExp.nextEntry()
# the Routine "questions" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# --- Prepare to start Routine "consent" ---
continueRoutine = True
routineForceEnded = False
# update component parameters for each repeat
resp1.reset()
resp2.reset()
resp3.reset()
resp4.reset()
resp5.reset()
resp6.reset()
# setup some python lists for storing info about the mouse_consent
mouse_consent.x = []
mouse_consent.y = []
mouse_consent.leftButton = []
mouse_consent.midButton = []
mouse_consent.rightButton = []
mouse_consent.time = []
mouse_consent.clicked_name = []
gotValidClick = False  # until a click is received
# keep track of which components have finished
consentComponents = [title, Q1, Q2, Q3, Q4, Q5, Q6, resp1, resp2, resp3, resp4, resp5, resp6, mouse_consent, nextButton_consent]
for thisComponent in consentComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
frameN = -1

# --- Run Routine "consent" ---
while continueRoutine:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *title* updates
    if title.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        title.frameNStart = frameN  # exact frame index
        title.tStart = t  # local t and not account for scr refresh
        title.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(title, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'title.started')
        title.setAutoDraw(True)
    
    # *Q1* updates
    if Q1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        Q1.frameNStart = frameN  # exact frame index
        Q1.tStart = t  # local t and not account for scr refresh
        Q1.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(Q1, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'Q1.started')
        Q1.setAutoDraw(True)
    
    # *Q2* updates
    if Q2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        Q2.frameNStart = frameN  # exact frame index
        Q2.tStart = t  # local t and not account for scr refresh
        Q2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(Q2, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'Q2.started')
        Q2.setAutoDraw(True)
    
    # *Q3* updates
    if Q3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        Q3.frameNStart = frameN  # exact frame index
        Q3.tStart = t  # local t and not account for scr refresh
        Q3.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(Q3, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'Q3.started')
        Q3.setAutoDraw(True)
    
    # *Q4* updates
    if Q4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        Q4.frameNStart = frameN  # exact frame index
        Q4.tStart = t  # local t and not account for scr refresh
        Q4.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(Q4, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'Q4.started')
        Q4.setAutoDraw(True)
    
    # *Q5* updates
    if Q5.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        Q5.frameNStart = frameN  # exact frame index
        Q5.tStart = t  # local t and not account for scr refresh
        Q5.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(Q5, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'Q5.started')
        Q5.setAutoDraw(True)
    
    # *Q6* updates
    if Q6.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        Q6.frameNStart = frameN  # exact frame index
        Q6.tStart = t  # local t and not account for scr refresh
        Q6.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(Q6, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'Q6.started')
        Q6.setAutoDraw(True)
    
    # *resp1* updates
    if resp1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        resp1.frameNStart = frameN  # exact frame index
        resp1.tStart = t  # local t and not account for scr refresh
        resp1.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(resp1, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'resp1.started')
        resp1.setAutoDraw(True)
    
    # *resp2* updates
    if resp2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        resp2.frameNStart = frameN  # exact frame index
        resp2.tStart = t  # local t and not account for scr refresh
        resp2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(resp2, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'resp2.started')
        resp2.setAutoDraw(True)
    
    # *resp3* updates
    if resp3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        resp3.frameNStart = frameN  # exact frame index
        resp3.tStart = t  # local t and not account for scr refresh
        resp3.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(resp3, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'resp3.started')
        resp3.setAutoDraw(True)
    
    # *resp4* updates
    if resp4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        resp4.frameNStart = frameN  # exact frame index
        resp4.tStart = t  # local t and not account for scr refresh
        resp4.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(resp4, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'resp4.started')
        resp4.setAutoDraw(True)
    
    # *resp5* updates
    if resp5.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        resp5.frameNStart = frameN  # exact frame index
        resp5.tStart = t  # local t and not account for scr refresh
        resp5.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(resp5, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'resp5.started')
        resp5.setAutoDraw(True)
    
    # *resp6* updates
    if resp6.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        resp6.frameNStart = frameN  # exact frame index
        resp6.tStart = t  # local t and not account for scr refresh
        resp6.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(resp6, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'resp6.started')
        resp6.setAutoDraw(True)
    # *mouse_consent* updates
    if mouse_consent.status == NOT_STARTED and t >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        mouse_consent.frameNStart = frameN  # exact frame index
        mouse_consent.tStart = t  # local t and not account for scr refresh
        mouse_consent.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(mouse_consent, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.addData('mouse_consent.started', t)
        mouse_consent.status = STARTED
        mouse_consent.mouseClock.reset()
        prevButtonState = mouse_consent.getPressed()  # if button is down already this ISN'T a new click
    if mouse_consent.status == STARTED:  # only update if started and not finished!
        buttons = mouse_consent.getPressed()
        if buttons != prevButtonState:  # button state changed?
            prevButtonState = buttons
            if sum(buttons) > 0:  # state changed to a new click
                # check if the mouse was inside our 'clickable' objects
                gotValidClick = False
                try:
                    iter(nextButton_consent)
                    clickableList = nextButton_consent
                except:
                    clickableList = [nextButton_consent]
                for obj in clickableList:
                    if obj.contains(mouse_consent):
                        gotValidClick = True
                        mouse_consent.clicked_name.append(obj.name)
                x, y = mouse_consent.getPos()
                mouse_consent.x.append(x)
                mouse_consent.y.append(y)
                buttons = mouse_consent.getPressed()
                mouse_consent.leftButton.append(buttons[0])
                mouse_consent.midButton.append(buttons[1])
                mouse_consent.rightButton.append(buttons[2])
                mouse_consent.time.append(mouse_consent.mouseClock.getTime())
                if gotValidClick:
                    continueRoutine = False  # abort routine on response
    
    # *nextButton_consent* updates
    if nextButton_consent.status == NOT_STARTED and resp1.rating and resp2.rating and resp3.rating and resp4.rating and resp5.rating and resp6.rating:
        # keep track of start time/frame for later
        nextButton_consent.frameNStart = frameN  # exact frame index
        nextButton_consent.tStart = t  # local t and not account for scr refresh
        nextButton_consent.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(nextButton_consent, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'nextButton_consent.started')
        nextButton_consent.setAutoDraw(True)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in consentComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "consent" ---
for thisComponent in consentComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('resp1.response', resp1.getRating())
thisExp.addData('resp1.rt', resp1.getRT())
thisExp.addData('resp2.response', resp2.getRating())
thisExp.addData('resp2.rt', resp2.getRT())
thisExp.addData('resp3.response', resp3.getRating())
thisExp.addData('resp3.rt', resp3.getRT())
thisExp.addData('resp4.response', resp4.getRating())
thisExp.addData('resp4.rt', resp4.getRT())
thisExp.addData('resp5.response', resp5.getRating())
thisExp.addData('resp5.rt', resp5.getRT())
thisExp.addData('resp6.response', resp6.getRating())
thisExp.addData('resp6.rt', resp6.getRT())
# store data for thisExp (ExperimentHandler)
thisExp.addData('mouse_consent.x', mouse_consent.x)
thisExp.addData('mouse_consent.y', mouse_consent.y)
thisExp.addData('mouse_consent.leftButton', mouse_consent.leftButton)
thisExp.addData('mouse_consent.midButton', mouse_consent.midButton)
thisExp.addData('mouse_consent.rightButton', mouse_consent.rightButton)
thisExp.addData('mouse_consent.time', mouse_consent.time)
thisExp.addData('mouse_consent.clicked_name', mouse_consent.clicked_name)
thisExp.nextEntry()
# the Routine "consent" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# --- Prepare to start Routine "example_sounds" ---
continueRoutine = True
routineForceEnded = False
# update component parameters for each repeat
# Run 'Begin Routine' code from code_2
from psychopy.event import Mouse
import numpy as np
from psychopy import sound, core, visual
from scipy import signal
myClock = core.Clock()

if ('block' in locals()) and (block.thisN == 2):
    continueRoutine = False

text_7.text = 'Loading...'

def play_tone(tone):
    tone = np.vstack([tone, tone]).T
    wave = sound.Sound(0.99*tone, sampleRate=48000)
    wave.play()
    myClock.reset()
    
sample_rate = 48000
seconds = 3
time = np.linspace(0, seconds, seconds*sample_rate)
pad = int(0.1*sample_rate)
full_time = np.linspace(0, seconds+0.2, int((seconds+0.2)*sample_rate))
pad_time = np.linspace(0, 0.2, int(0.2*sample_rate))

carrier = 1000
am_tremo = 10
am_rough = 70

# Create signals
f0 = carrier-500
f1 = carrier+500

pitch = signal.chirp(time, f0, 3, f1)
start = np.cos(2*np.pi*f0*pad_time)
stop = np.cos(2*np.pi*f1*pad_time)
pitch = np.hstack((start, pitch, stop))
    
am = np.linspace(0, 0.5, len(time))
am = am * (np.cos(2*np.pi*am_rough*time) + 1)
am = np.hstack((np.zeros((pad,)), am, np.ones((pad,))))
am = 1 - am
rough = am * np.sin(2*np.pi*carrier*full_time)

am = np.linspace(0, 0.5, len(time))
am = am * (np.cos(2*np.pi*am_tremo*time) + 1)
am = np.hstack((np.zeros((pad,)), am, np.ones((pad,))))
am = 1 - am

tremolo = am * np.sin(2*np.pi*carrier*full_time)

# Can change these to all False to speed up testing
tones_played = [False, False, False, False, False, False]

ExampleKeys.keys = []
ExampleKeys.rt = []
_ExampleKeys_allKeys = []
# keep track of which components have finished
example_soundsComponents = [ExampleKeys, text_6, text_7, text_9]
for thisComponent in example_soundsComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
frameN = -1

# --- Run Routine "example_sounds" ---
while continueRoutine:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    # Run 'Each Frame' code from code_2
    if myClock.getTime() > 4:
        text_7.text = ''
        if np.all(tones_played):
            text_9.text = 'Press space to continue'
     
        keys = ExampleKeys.getKeys()
        if '1' in keys:
            play_tone(pitch)
            text_7.text = 'playing...'
            tones_played[0] = True
        elif '2' in keys:
            play_tone(np.flipud(pitch))  
            text_7.text = 'playing...'
            tones_played[1] = True
        elif '5' in keys:
            play_tone(rough) 
            text_7.text = 'playing...'
            tones_played[2] = True
        elif '6' in keys:
            play_tone(np.flipud(rough))  
            text_7.text = 'playing...'
            tones_played[3] = True
        elif '9' in keys:
            play_tone(tremolo) 
            text_7.text = 'playing...'
            tones_played[4] = True
        elif '0' in keys:
            play_tone(np.flipud(tremolo))  
            text_7.text = 'playing...'
            tones_played[5] = True
        elif 'space' in keys and np.all(tones_played):
            print('ends')
            continueRoutine = False
        elif 'esc' in keys:
            core.quit()
     
    
    # *ExampleKeys* updates
    waitOnFlip = False
    if ExampleKeys.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        ExampleKeys.frameNStart = frameN  # exact frame index
        ExampleKeys.tStart = t  # local t and not account for scr refresh
        ExampleKeys.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(ExampleKeys, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'ExampleKeys.started')
        ExampleKeys.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(ExampleKeys.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(ExampleKeys.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if ExampleKeys.status == STARTED and not waitOnFlip:
        theseKeys = ExampleKeys.getKeys(keyList=['1', '2', '5', '6', '9','0', 'esc', 'return'], waitRelease=False)
        _ExampleKeys_allKeys.extend(theseKeys)
        if len(_ExampleKeys_allKeys):
            ExampleKeys.keys = _ExampleKeys_allKeys[-1].name  # just the last key pressed
            ExampleKeys.rt = _ExampleKeys_allKeys[-1].rt
    
    # *text_6* updates
    if text_6.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_6.frameNStart = frameN  # exact frame index
        text_6.tStart = t  # local t and not account for scr refresh
        text_6.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_6, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'text_6.started')
        text_6.setAutoDraw(True)
    
    # *text_7* updates
    if text_7.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_7.frameNStart = frameN  # exact frame index
        text_7.tStart = t  # local t and not account for scr refresh
        text_7.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_7, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'text_7.started')
        text_7.setAutoDraw(True)
    
    # *text_9* updates
    if text_9.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_9.frameNStart = frameN  # exact frame index
        text_9.tStart = t  # local t and not account for scr refresh
        text_9.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_9, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'text_9.started')
        text_9.setAutoDraw(True)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in example_soundsComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "example_sounds" ---
for thisComponent in example_soundsComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if ExampleKeys.keys in ['', [], None]:  # No response was made
    ExampleKeys.keys = None
thisExp.addData('ExampleKeys.keys',ExampleKeys.keys)
if ExampleKeys.keys != None:  # we had a response
    thisExp.addData('ExampleKeys.rt', ExampleKeys.rt)
thisExp.nextEntry()
# the Routine "example_sounds" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
block = data.TrialHandler(nReps=3.0, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=[None],
    seed=None, name='block')
thisExp.addLoop(block)  # add the loop to the experiment
thisBlock = block.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisBlock.rgb)
if thisBlock != None:
    for paramName in thisBlock:
        exec('{} = thisBlock[paramName]'.format(paramName))

for thisBlock in block:
    currentLoop = block
    # abbreviate parameter names if possible (e.g. rgb = thisBlock.rgb)
    if thisBlock != None:
        for paramName in thisBlock:
            exec('{} = thisBlock[paramName]'.format(paramName))
    
    # --- Prepare to start Routine "ready_go" ---
    continueRoutine = True
    routineForceEnded = False
    # update component parameters for each repeat
    # keep track of which components have finished
    ready_goComponents = [text_countdown]
    for thisComponent in ready_goComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "ready_go" ---
    while continueRoutine and routineTimer.getTime() < 3.0:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *text_countdown* updates
        if text_countdown.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_countdown.frameNStart = frameN  # exact frame index
            text_countdown.tStart = t  # local t and not account for scr refresh
            text_countdown.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_countdown, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'text_countdown.started')
            text_countdown.setAutoDraw(True)
        if text_countdown.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > text_countdown.tStartRefresh + 3-frameTolerance:
                # keep track of stop time/frame for later
                text_countdown.tStop = t  # not accounting for scr refresh
                text_countdown.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'text_countdown.stopped')
                text_countdown.setAutoDraw(False)
        if text_countdown.status == STARTED:  # only update if drawing
            text_countdown.setText(str(3-int(t)), log=False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in ready_goComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "ready_go" ---
    for thisComponent in ready_goComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
    if routineForceEnded:
        routineTimer.reset()
    else:
        routineTimer.addTime(-3.000000)
    
    # set up handler to look after randomisation of conditions etc
    trials = data.TrialHandler(nReps=1.0, method='random', 
        extraInfo=expInfo, originPath=-1,
        trialList=data.importConditions('conditions.xlsx'),
        seed=None, name='trials')
    thisExp.addLoop(trials)  # add the loop to the experiment
    thisTrial = trials.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisTrial.rgb)
    if thisTrial != None:
        for paramName in thisTrial:
            exec('{} = thisTrial[paramName]'.format(paramName))
    
    for thisTrial in trials:
        currentLoop = trials
        # abbreviate parameter names if possible (e.g. rgb = thisTrial.rgb)
        if thisTrial != None:
            for paramName in thisTrial:
                exec('{} = thisTrial[paramName]'.format(paramName))
        
        # --- Prepare to start Routine "Fixation1" ---
        continueRoutine = True
        routineForceEnded = False
        # update component parameters for each repeat
        text_11.setText(question
)
        # keep track of which components have finished
        Fixation1Components = [fix, text_11]
        for thisComponent in Fixation1Components:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "Fixation1" ---
        while continueRoutine and routineTimer.getTime() < 1.0:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *fix* updates
            if fix.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                fix.frameNStart = frameN  # exact frame index
                fix.tStart = t  # local t and not account for scr refresh
                fix.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(fix, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'fix.started')
                fix.setAutoDraw(True)
            if fix.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > fix.tStartRefresh + 1-frameTolerance:
                    # keep track of stop time/frame for later
                    fix.tStop = t  # not accounting for scr refresh
                    fix.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'fix.stopped')
                    fix.setAutoDraw(False)
            
            # *text_11* updates
            if text_11.status == NOT_STARTED and tThisFlip >= 0.4-frameTolerance:
                # keep track of start time/frame for later
                text_11.frameNStart = frameN  # exact frame index
                text_11.tStart = t  # local t and not account for scr refresh
                text_11.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(text_11, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'text_11.started')
                text_11.setAutoDraw(True)
            if text_11.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > text_11.tStartRefresh + 0.6-frameTolerance:
                    # keep track of stop time/frame for later
                    text_11.tStop = t  # not accounting for scr refresh
                    text_11.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'text_11.stopped')
                    text_11.setAutoDraw(False)
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in Fixation1Components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "Fixation1" ---
        for thisComponent in Fixation1Components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
        if routineForceEnded:
            routineTimer.reset()
        else:
            routineTimer.addTime(-1.000000)
        
        # set up handler to look after randomisation of conditions etc
        pair = data.TrialHandler(nReps=1.0, method='sequential', 
            extraInfo=expInfo, originPath=-1,
            trialList=data.importConditions('modulation.xlsx'),
            seed=None, name='pair')
        thisExp.addLoop(pair)  # add the loop to the experiment
        thisPair = pair.trialList[0]  # so we can initialise stimuli with some values
        # abbreviate parameter names if possible (e.g. rgb = thisPair.rgb)
        if thisPair != None:
            for paramName in thisPair:
                exec('{} = thisPair[paramName]'.format(paramName))
        
        for thisPair in pair:
            currentLoop = pair
            # abbreviate parameter names if possible (e.g. rgb = thisPair.rgb)
            if thisPair != None:
                for paramName in thisPair:
                    exec('{} = thisPair[paramName]'.format(paramName))
            
            # --- Prepare to start Routine "Trial" ---
            continueRoutine = True
            routineForceEnded = False
            # update component parameters for each repeat
            stimulus.setText('+++')
            # Run 'Begin Routine' code from code
            from psychopy import sound, core
            import numpy as np
            
            time = np.linspace(0, 1, 48000)
            carrier_tone = np.sin(2*np.pi*carrier*time)
            
            # amp = (np.cos(2*np.pi*am*time) / 2) + 1
            amp = np.sin(2*np.pi*am*time)
            tone = carrier_tone * (1 + mod * amp)
            
            tone = np.vstack([tone, tone]).T
            wave = sound.Sound(0.99*tone, sampleRate=48000)
            wave.play()
            text_10.setText(question
)
            # keep track of which components have finished
            TrialComponents = [stimulus, text_10]
            for thisComponent in TrialComponents:
                thisComponent.tStart = None
                thisComponent.tStop = None
                thisComponent.tStartRefresh = None
                thisComponent.tStopRefresh = None
                if hasattr(thisComponent, 'status'):
                    thisComponent.status = NOT_STARTED
            # reset timers
            t = 0
            _timeToFirstFrame = win.getFutureFlipTime(clock="now")
            frameN = -1
            
            # --- Run Routine "Trial" ---
            while continueRoutine and routineTimer.getTime() < 2.5:
                # get current time
                t = routineTimer.getTime()
                tThisFlip = win.getFutureFlipTime(clock=routineTimer)
                tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                # update/draw components on each frame
                
                # *stimulus* updates
                if stimulus.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
                    # keep track of start time/frame for later
                    stimulus.frameNStart = frameN  # exact frame index
                    stimulus.tStart = t  # local t and not account for scr refresh
                    stimulus.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(stimulus, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'stimulus.started')
                    stimulus.setAutoDraw(True)
                if stimulus.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > stimulus.tStartRefresh + 2.5-frameTolerance:
                        # keep track of stop time/frame for later
                        stimulus.tStop = t  # not accounting for scr refresh
                        stimulus.frameNStop = frameN  # exact frame index
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'stimulus.stopped')
                        stimulus.setAutoDraw(False)
                
                # *text_10* updates
                if text_10.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    text_10.frameNStart = frameN  # exact frame index
                    text_10.tStart = t  # local t and not account for scr refresh
                    text_10.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(text_10, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'text_10.started')
                    text_10.setAutoDraw(True)
                if text_10.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > text_10.tStartRefresh + 2.5-frameTolerance:
                        # keep track of stop time/frame for later
                        text_10.tStop = t  # not accounting for scr refresh
                        text_10.frameNStop = frameN  # exact frame index
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'text_10.stopped')
                        text_10.setAutoDraw(False)
                
                # check for quit (typically the Esc key)
                if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                    core.quit()
                
                # check if all components have finished
                if not continueRoutine:  # a component has requested a forced-end of Routine
                    routineForceEnded = True
                    break
                continueRoutine = False  # will revert to True if at least one component still running
                for thisComponent in TrialComponents:
                    if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                        continueRoutine = True
                        break  # at least one component has not yet finished
                
                # refresh the screen
                if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                    win.flip()
            
            # --- Ending Routine "Trial" ---
            for thisComponent in TrialComponents:
                if hasattr(thisComponent, "setAutoDraw"):
                    thisComponent.setAutoDraw(False)
            # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
            if routineForceEnded:
                routineTimer.reset()
            else:
                routineTimer.addTime(-2.500000)
            thisExp.nextEntry()
            
        # completed 1.0 repeats of 'pair'
        
        
        # --- Prepare to start Routine "response" ---
        continueRoutine = True
        routineForceEnded = False
        # update component parameters for each repeat
        text.setText(question
)
        slider.reset()
        # keep track of which components have finished
        responseComponents = [text, slider]
        for thisComponent in responseComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "response" ---
        while continueRoutine:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *text* updates
            if text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                text.frameNStart = frameN  # exact frame index
                text.tStart = t  # local t and not account for scr refresh
                text.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(text, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'text.started')
                text.setAutoDraw(True)
            
            # *slider* updates
            if slider.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                slider.frameNStart = frameN  # exact frame index
                slider.tStart = t  # local t and not account for scr refresh
                slider.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(slider, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'slider.started')
                slider.setAutoDraw(True)
            
            # Check slider for response to end routine
            if slider.getRating() is not None and slider.status == STARTED:
                continueRoutine = False
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in responseComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "response" ---
        for thisComponent in responseComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        trials.addData('slider.response', slider.getRating())
        trials.addData('slider.rt', slider.getRT())
        # the Routine "response" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        thisExp.nextEntry()
        
    # completed 1.0 repeats of 'trials'
    
    
    # --- Prepare to start Routine "end_block" ---
    continueRoutine = True
    routineForceEnded = False
    # update component parameters for each repeat
    key_resp_2.keys = []
    key_resp_2.rt = []
    _key_resp_2_allKeys = []
    # keep track of which components have finished
    end_blockComponents = [text_2, key_resp_2]
    for thisComponent in end_blockComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "end_block" ---
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *text_2* updates
        if text_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_2.frameNStart = frameN  # exact frame index
            text_2.tStart = t  # local t and not account for scr refresh
            text_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_2, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'text_2.started')
            text_2.setAutoDraw(True)
        
        # *key_resp_2* updates
        waitOnFlip = False
        if key_resp_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            key_resp_2.frameNStart = frameN  # exact frame index
            key_resp_2.tStart = t  # local t and not account for scr refresh
            key_resp_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(key_resp_2, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'key_resp_2.started')
            key_resp_2.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(key_resp_2.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(key_resp_2.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if key_resp_2.status == STARTED and not waitOnFlip:
            theseKeys = key_resp_2.getKeys(keyList=None, waitRelease=False)
            _key_resp_2_allKeys.extend(theseKeys)
            if len(_key_resp_2_allKeys):
                key_resp_2.keys = _key_resp_2_allKeys[-1].name  # just the last key pressed
                key_resp_2.rt = _key_resp_2_allKeys[-1].rt
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in end_blockComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "end_block" ---
    for thisComponent in end_blockComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # check responses
    if key_resp_2.keys in ['', [], None]:  # No response was made
        key_resp_2.keys = None
    block.addData('key_resp_2.keys',key_resp_2.keys)
    if key_resp_2.keys != None:  # we had a response
        block.addData('key_resp_2.rt', key_resp_2.rt)
    # the Routine "end_block" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 3.0 repeats of 'block'


# --- Prepare to start Routine "thanks" ---
continueRoutine = True
routineForceEnded = False
# update component parameters for each repeat
# keep track of which components have finished
thanksComponents = [thanksText]
for thisComponent in thanksComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
frameN = -1

# --- Run Routine "thanks" ---
while continueRoutine and routineTimer.getTime() < 2.0:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *thanksText* updates
    if thanksText.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        thanksText.frameNStart = frameN  # exact frame index
        thanksText.tStart = t  # local t and not account for scr refresh
        thanksText.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(thanksText, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'thanksText.started')
        thanksText.setAutoDraw(True)
    if thanksText.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > thanksText.tStartRefresh + 2.0-frameTolerance:
            # keep track of stop time/frame for later
            thanksText.tStop = t  # not accounting for scr refresh
            thanksText.frameNStop = frameN  # exact frame index
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'thanksText.stopped')
            thanksText.setAutoDraw(False)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in thanksComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "thanks" ---
for thisComponent in thanksComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
if routineForceEnded:
    routineTimer.reset()
else:
    routineTimer.addTime(-2.000000)

# --- End experiment ---
# Flip one final time so any remaining win.callOnFlip() 
# and win.timeOnFlip() tasks get executed before quitting
win.flip()

# these shouldn't be strictly necessary (should auto-save)
thisExp.saveAsWideText(filename+'.csv', delim='auto')
thisExp.saveAsPickle(filename)
logging.flush()
# make sure everything is closed down
if eyetracker:
    eyetracker.setConnectionState(False)
thisExp.abort()  # or data files will save again on exit
win.close()
core.quit()
