/******************* 
 * Ratingsnew Test *
 *******************/

// init psychoJS:
var psychoJS = new PsychoJS({
  debug: true
});

// open window:
psychoJS.openWindow({
  fullscr: false,
  color: new util.Color([0, 0, 0]),
  units: 'use prefs'
});

// store info about the experiment session:
let expName = 'ratingsNew';  // from the Builder filename that created this script
let expInfo = {'session': '001', 'participant': ''};

// schedule the experiment:
psychoJS.schedule(psychoJS.gui.DlgFromDict({
  dictionary: expInfo,
  title: expName
}));

const flowScheduler = new Scheduler(psychoJS);
const dialogCancelScheduler = new Scheduler(psychoJS);
psychoJS.scheduleCondition(function() { return (psychoJS.gui.dialogComponent.button === 'OK'); }, flowScheduler, dialogCancelScheduler);

// flowScheduler gets run if the participants presses OK
flowScheduler.add(updateInfo); // add timeStamp
flowScheduler.add(experimentInit);
const trialsLoopScheduler = new Scheduler(psychoJS);
flowScheduler.add(trialsLoopBegin, trialsLoopScheduler);
flowScheduler.add(trialsLoopScheduler);
flowScheduler.add(trialsLoopEnd);
flowScheduler.add(dynamicStimRoutineBegin);
flowScheduler.add(dynamicStimRoutineEachFrame);
flowScheduler.add(dynamicStimRoutineEnd);
flowScheduler.add(sliderStylesRoutineBegin);
flowScheduler.add(sliderStylesRoutineEachFrame);
flowScheduler.add(sliderStylesRoutineEnd);
flowScheduler.add(quitPsychoJS);

// quit if user presses Cancel in dialog box:
dialogCancelScheduler.add(quitPsychoJS);

psychoJS.start({configURL: 'config.json', expInfo: expInfo});

var frameDur;
function updateInfo() {
  expInfo['date'] = util.MonotonicClock.getDateStr();  // add a simple timestamp
  expInfo['expName'] = expName;

  // store frame rate of monitor if we can measure it successfully
  expInfo['frameRate'] = psychoJS.window.getActualFrameRate();
  if (typeof expInfo['frameRate'] !== 'undefined')
    frameDur = 1.0/Math.round(expInfo['frameRate']);
  else
    frameDur = 1.0/60.0; // couldn't get a reliable measure so guess

  // add info from the URL:
  util.addInfoFromUrl(expInfo);

  return Scheduler.Event.NEXT;
}

var rate_a_fruitClock;
var fruit;
var intruct1;
var dynamicStimClock;
var oriLabel;
var xPosLabel;
var instruct2;
var sliderStylesClock;
var instruct3;
var categFeedback;
var globalClock;
var routineTimer;
function experimentInit() {
  // Initialize components for Routine "rate_a_fruit"
  rate_a_fruitClock = new util.Clock();
  fruit = new visual.TextStim({
    win : psychoJS.window,
    name : 'fruit',
    text : 'default text',
    font : 'Arial',
    units : 'norm',   pos : [0, 0.5], height : 0.1,  wrapWidth : undefined, ori: 0,
    color : new util.Color('white'),  opacity : 1,
    depth : 0.0 
  });
  
  intruct1 = new visual.TextStim({
    win : psychoJS.window,
    name : 'intruct1',
    text : 'Press a key to confirm and move on',
    font : 'Arial',
    units : 'norm',   pos : [0, (-0.9)], height : 0.1,  wrapWidth : undefined, ori: 0,
    color : new util.Color('white'),  opacity : 1,
    depth : -3.0 
  });
  
  // Initialize components for Routine "dynamicStim"
  dynamicStimClock = new util.Clock();
  oriLabel = new visual.TextStim({
    win : psychoJS.window,
    name : 'oriLabel',
    text : 'Ori',
    font : 'Arial',
    pos : [(-0.7), (-0.7)], height : 0.1,  wrapWidth : undefined, ori: 0,
    color : new util.Color('white'),  opacity : 1,
    depth : -1.0 
  });
  
  xPosLabel = new visual.TextStim({
    win : psychoJS.window,
    name : 'xPosLabel',
    text : 'xPos',
    font : 'Arial',
    pos : [(-0.3), (-0.7)], height : 0.1,  wrapWidth : undefined, ori: 0,
    color : new util.Color('white'),  opacity : 1,
    depth : -3.0 
  });
  
  
  instruct2 = new visual.TextStim({
    win : psychoJS.window,
    name : 'instruct2',
    text : 'slider markerPos can update other things.\n\nPress a key to move on',
    font : 'Arial',
    units : 'norm',   pos : [0, 0.8], height : 0.05,  wrapWidth : undefined, ori: 0,
    color : new util.Color('white'),  opacity : 1,
    depth : -7.0 
  });
  
  // Initialize components for Routine "sliderStyles"
  sliderStylesClock = new util.Clock();
  instruct3 = new visual.TextStim({
    win : psychoJS.window,
    name : 'instruct3',
    text : 'Click on some sldiers to see their markers\n\nPress any key to finalise ratings',
    font : 'Arial',
    units : 'norm',   pos : [0, 0], height : 0.07,  wrapWidth : undefined, ori: 0,
    color : new util.Color('white'),  opacity : 1,
    depth : -1.0 
  });
  
  categFeedback = new Rect ({
    win: psychoJS.window, name: 'categFeedback',
    units: psychoJS.window.units,
    width: [0.3, 0.3][0], height: [0.3, 0.3][1],
    ori: 0, pos: [0.5, [-0.5]],
    lineWidth: 1, lineColor: new util.Color([1, 1, 1]),
    fillColor: new util.Color(categScale.getRating()),
    opacity: 1, depth: -1.0, interpolate: true,
  });
  
  // Create some handy timers
  globalClock = new util.Clock();  // to track the time since experiment started
  routineTimer = new util.CountdownTimer();  // to track time remaining of each (non-slip) routine
  
  return Scheduler.Event.NEXT;
}

var trials;
function trialsLoopBegin(thisScheduler) {
  // set up handler to look after randomisation of conditions etc
  trials = new TrialHandler({
    psychoJS,
    nReps: 1, method: TrialHandler.Method.RANDOM,
    extraInfo: expInfo, originPath: undefined,
    trialList: 'fruitConditions.xlsx',
    seed: undefined, name: 'trials'});
  psychoJS.experiment.addLoop(trials); // add the loop to the experiment

  // Schedule all the trials in the trialList:
  for (const thisTrial of trials) {
    thisScheduler.add(importTrialAttributes(thisTrial));
    thisScheduler.add(rate_a_fruitRoutineBegin);
    thisScheduler.add(rate_a_fruitRoutineEachFrame);
    thisScheduler.add(rate_a_fruitRoutineEnd);
    thisScheduler.add(endLoopIteration(thisTrial));
  }

  return Scheduler.Event.NEXT;
}


function trialsLoopEnd() {
  psychoJS.experiment.removeLoop(trials);
  psychoJS.experiment.save({
    attributes: trials.getAttributes()
  });

  return Scheduler.Event.NEXT;
}

var t;
var frameN;
var fruitDone;
var rate_a_fruitComponents;
function rate_a_fruitRoutineBegin() {
  //------Prepare to start Routine 'rate_a_fruit'-------
  t = 0;
  rate_a_fruitClock.reset(); // clock
  frameN = -1;
  // update component parameters for each repeat
  fruit.setText(fruitName);
  fruitDone = new core.BuilderKeyResponse(psychoJS);
  // keep track of which components have finished
  rate_a_fruitComponents = [];
  rate_a_fruitComponents.push(fruit);
  rate_a_fruitComponents.push(intruct1);
  rate_a_fruitComponents.push(fruitDone);
  
  for (const thisComponent of rate_a_fruitComponents)
    if ('status' in thisComponent)
      thisComponent.status = PsychoJS.Status.NOT_STARTED;
  
  return Scheduler.Event.NEXT;
}

var continueRoutine;
function rate_a_fruitRoutineEachFrame() {
  //------Loop for each frame of Routine 'rate_a_fruit'-------
  let continueRoutine = true; // until we're told otherwise
  // get current time
  t = rate_a_fruitClock.getTime();
  frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
  // update/draw components on each frame
  
  // *fruit* updates
  if (t >= 0.0 && fruit.status === PsychoJS.Status.NOT_STARTED) {
    // keep track of start time/frame for later
    fruit.tStart = t;  // (not accounting for frame time here)
    fruit.frameNStart = frameN;  // exact frame index
    fruit.setAutoDraw(true);
  }
  
  // *intruct1* updates
  if (t >= 0.0 && intruct1.status === PsychoJS.Status.NOT_STARTED) {
    // keep track of start time/frame for later
    intruct1.tStart = t;  // (not accounting for frame time here)
    intruct1.frameNStart = frameN;  // exact frame index
    intruct1.setAutoDraw(true);
  }
  
  // *fruitDone* updates
  if (t >= 0.0 && fruitDone.status === PsychoJS.Status.NOT_STARTED) {
    // keep track of start time/frame for later
    fruitDone.tStart = t;  // (not accounting for frame time here)
    fruitDone.frameNStart = frameN;  // exact frame index
    fruitDone.status = PsychoJS.Status.STARTED;
    // keyboard checking is just starting
    fruitDone.clock.reset();  // now t=0
    psychoJS.eventManager.clearEvents({eventType:'keyboard'});
  }
  if (fruitDone.status === PsychoJS.Status.STARTED) {
    let theseKeys = psychoJS.eventManager.getKeys();
    
    // check for quit:
    if ("escape" in theseKeys) {
        psychoJS.experiment.experimentEnded = true;
    }
    if (theseKeys.length > 0) {  // at least one key was pressed
      fruitDone.keys = theseKeys[theseKeys.length-1]  // just the last key pressed
      fruitDone.rt = fruitDone.clock.getTime();
      // a response ends the routine
      continueRoutine = false;
    }
  }
  
  // check if the Routine should terminate
  if (!continueRoutine) {  // a component has requested a forced-end of Routine
    return Scheduler.Event.NEXT;
  }
  continueRoutine = false;// reverts to True if at least one component still running
  for (const thisComponent of rate_a_fruitComponents)
    if ('status' in thisComponent && thisComponent.status != PsychoJS.Status.FINISHED) {
      continueRoutine = true;
      break;
    }
  // check for quit (the Esc key)
  if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
    psychoJS.quit('The [Escape] key was pressed. Goodbye!');
  }
  
  // refresh the screen if continuing
  if (continueRoutine) {
    return Scheduler.Event.FLIP_REPEAT;
  }
  else {
    return Scheduler.Event.NEXT;
  }
}


function rate_a_fruitRoutineEnd() {
  //------Ending Routine 'rate_a_fruit'-------
  for (const thisComponent of rate_a_fruitComponents) {
    if (typeof thisComponent.setAutoDraw === 'function') {
      thisComponent.setAutoDraw(false);
    }
  }
  // check responses
  if (['', [], undefined].indexOf(fruitDone.keys) >= 0) {    // No response was made
      fruitDone.keys = undefined;
  }
  psychoJS.experiment.addData('fruitDone.keys', fruitDone.keys);
  if (fruitDone.keys != undefined) {  // we had a response
      psychoJS.experiment.addData('fruitDone.rt', fruitDone.rt);
      routineTimer.reset();
      }
  // the Routine "rate_a_fruit" was not non-slip safe, so reset the non-slip timer
  routineTimer.reset();
  
  return Scheduler.Event.NEXT;
}

var dynamicDone;
var dynamicStimComponents;
function dynamicStimRoutineBegin() {
  //------Prepare to start Routine 'dynamicStim'-------
  t = 0;
  dynamicStimClock.reset(); // clock
  frameN = -1;
  // update component parameters for each repeat
  dynamicDone = new core.BuilderKeyResponse(psychoJS);
  
  // keep track of which components have finished
  dynamicStimComponents = [];
  dynamicStimComponents.push(oriLabel);
  dynamicStimComponents.push(xPosLabel);
  dynamicStimComponents.push(dynamicDone);
  dynamicStimComponents.push(instruct2);
  
  for (const thisComponent of dynamicStimComponents)
    if ('status' in thisComponent)
      thisComponent.status = PsychoJS.Status.NOT_STARTED;
  
  return Scheduler.Event.NEXT;
}


function dynamicStimRoutineEachFrame() {
  //------Loop for each frame of Routine 'dynamicStim'-------
  let continueRoutine = true; // until we're told otherwise
  // get current time
  t = dynamicStimClock.getTime();
  frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
  // update/draw components on each frame
  
  // *oriLabel* updates
  if (t >= 0.0 && oriLabel.status === PsychoJS.Status.NOT_STARTED) {
    // keep track of start time/frame for later
    oriLabel.tStart = t;  // (not accounting for frame time here)
    oriLabel.frameNStart = frameN;  // exact frame index
    oriLabel.setAutoDraw(true);
  }
  
  // *xPosLabel* updates
  if (t >= 0.0 && xPosLabel.status === PsychoJS.Status.NOT_STARTED) {
    // keep track of start time/frame for later
    xPosLabel.tStart = t;  // (not accounting for frame time here)
    xPosLabel.frameNStart = frameN;  // exact frame index
    xPosLabel.setAutoDraw(true);
  }
  
  // *dynamicDone* updates
  if (t >= 0.0 && dynamicDone.status === PsychoJS.Status.NOT_STARTED) {
    // keep track of start time/frame for later
    dynamicDone.tStart = t;  // (not accounting for frame time here)
    dynamicDone.frameNStart = frameN;  // exact frame index
    dynamicDone.status = PsychoJS.Status.STARTED;
    // keyboard checking is just starting
    dynamicDone.clock.reset();  // now t=0
    psychoJS.eventManager.clearEvents({eventType:'keyboard'});
  }
  if (dynamicDone.status === PsychoJS.Status.STARTED) {
    let theseKeys = psychoJS.eventManager.getKeys();
    
    // check for quit:
    if ("escape" in theseKeys) {
        psychoJS.experiment.experimentEnded = true;
    }
    if (theseKeys.length > 0) {  // at least one key was pressed
      dynamicDone.keys = theseKeys[theseKeys.length-1]  // just the last key pressed
      dynamicDone.rt = dynamicDone.clock.getTime();
      // a response ends the routine
      continueRoutine = false;
    }
  }
  
  
  // *instruct2* updates
  if (t >= 0.0 && instruct2.status === PsychoJS.Status.NOT_STARTED) {
    // keep track of start time/frame for later
    instruct2.tStart = t;  // (not accounting for frame time here)
    instruct2.frameNStart = frameN;  // exact frame index
    instruct2.setAutoDraw(true);
  }
  
  // check if the Routine should terminate
  if (!continueRoutine) {  // a component has requested a forced-end of Routine
    return Scheduler.Event.NEXT;
  }
  continueRoutine = false;// reverts to True if at least one component still running
  for (const thisComponent of dynamicStimComponents)
    if ('status' in thisComponent && thisComponent.status != PsychoJS.Status.FINISHED) {
      continueRoutine = true;
      break;
    }
  // check for quit (the Esc key)
  if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
    psychoJS.quit('The [Escape] key was pressed. Goodbye!');
  }
  
  // refresh the screen if continuing
  if (continueRoutine) {
    return Scheduler.Event.FLIP_REPEAT;
  }
  else {
    return Scheduler.Event.NEXT;
  }
}


function dynamicStimRoutineEnd() {
  //------Ending Routine 'dynamicStim'-------
  for (const thisComponent of dynamicStimComponents) {
    if (typeof thisComponent.setAutoDraw === 'function') {
      thisComponent.setAutoDraw(false);
    }
  }
  // check responses
  if (['', [], undefined].indexOf(dynamicDone.keys) >= 0) {    // No response was made
      dynamicDone.keys = undefined;
  }
  psychoJS.experiment.addData('dynamicDone.keys', dynamicDone.keys);
  if (dynamicDone.keys != undefined) {  // we had a response
      psychoJS.experiment.addData('dynamicDone.rt', dynamicDone.rt);
      routineTimer.reset();
      }
  
  // the Routine "dynamicStim" was not non-slip safe, so reset the non-slip timer
  routineTimer.reset();
  
  return Scheduler.Event.NEXT;
}

var endStyles;
var sliderStylesComponents;
function sliderStylesRoutineBegin() {
  //------Prepare to start Routine 'sliderStyles'-------
  t = 0;
  sliderStylesClock.reset(); // clock
  frameN = -1;
  // update component parameters for each repeat
  endStyles = new core.BuilderKeyResponse(psychoJS);
  
  // keep track of which components have finished
  sliderStylesComponents = [];
  sliderStylesComponents.push(endStyles);
  sliderStylesComponents.push(instruct3);
  sliderStylesComponents.push(categFeedback);
  
  for (const thisComponent of sliderStylesComponents)
    if ('status' in thisComponent)
      thisComponent.status = PsychoJS.Status.NOT_STARTED;
  
  return Scheduler.Event.NEXT;
}


function sliderStylesRoutineEachFrame() {
  //------Loop for each frame of Routine 'sliderStyles'-------
  let continueRoutine = true; // until we're told otherwise
  // get current time
  t = sliderStylesClock.getTime();
  frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
  // update/draw components on each frame
  
  // *endStyles* updates
  if (t >= 0.0 && endStyles.status === PsychoJS.Status.NOT_STARTED) {
    // keep track of start time/frame for later
    endStyles.tStart = t;  // (not accounting for frame time here)
    endStyles.frameNStart = frameN;  // exact frame index
    endStyles.status = PsychoJS.Status.STARTED;
    // keyboard checking is just starting
    endStyles.clock.reset();  // now t=0
    psychoJS.eventManager.clearEvents({eventType:'keyboard'});
  }
  if (endStyles.status === PsychoJS.Status.STARTED) {
    let theseKeys = psychoJS.eventManager.getKeys();
    
    // check for quit:
    if ("escape" in theseKeys) {
        psychoJS.experiment.experimentEnded = true;
    }
    if (theseKeys.length > 0) {  // at least one key was pressed
      endStyles.keys = theseKeys[theseKeys.length-1]  // just the last key pressed
      endStyles.rt = endStyles.clock.getTime();
      // a response ends the routine
      continueRoutine = false;
    }
  }
  
  // *instruct3* updates
  if (t >= 0.0 && instruct3.status === PsychoJS.Status.NOT_STARTED) {
    // keep track of start time/frame for later
    instruct3.tStart = t;  // (not accounting for frame time here)
    instruct3.frameNStart = frameN;  // exact frame index
    instruct3.setAutoDraw(true);
  }
  
  // *categFeedback* updates
  if (t >= 0.0 && categFeedback.status === PsychoJS.Status.NOT_STARTED) {
    // keep track of start time/frame for later
    categFeedback.tStart = t;  // (not accounting for frame time here)
    categFeedback.frameNStart = frameN;  // exact frame index
    categFeedback.setAutoDraw(true);
  }
  if (categFeedback.status === PsychoJS.Status.STARTED){ // only update if being drawn
    categFeedback.setFillColor(categScale.getRating());
  }
  
  
  // check if the Routine should terminate
  if (!continueRoutine) {  // a component has requested a forced-end of Routine
    return Scheduler.Event.NEXT;
  }
  continueRoutine = false;// reverts to True if at least one component still running
  for (const thisComponent of sliderStylesComponents)
    if ('status' in thisComponent && thisComponent.status != PsychoJS.Status.FINISHED) {
      continueRoutine = true;
      break;
    }
  // check for quit (the Esc key)
  if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
    psychoJS.quit('The [Escape] key was pressed. Goodbye!');
  }
  
  // refresh the screen if continuing
  if (continueRoutine) {
    return Scheduler.Event.FLIP_REPEAT;
  }
  else {
    return Scheduler.Event.NEXT;
  }
}


function sliderStylesRoutineEnd() {
  //------Ending Routine 'sliderStyles'-------
  for (const thisComponent of sliderStylesComponents) {
    if (typeof thisComponent.setAutoDraw === 'function') {
      thisComponent.setAutoDraw(false);
    }
  }
  // check responses
  if (['', [], undefined].indexOf(endStyles.keys) >= 0) {    // No response was made
      endStyles.keys = undefined;
  }
  psychoJS.experiment.addData('endStyles.keys', endStyles.keys);
  if (endStyles.keys != undefined) {  // we had a response
      psychoJS.experiment.addData('endStyles.rt', endStyles.rt);
      routineTimer.reset();
      }
  
  // the Routine "sliderStyles" was not non-slip safe, so reset the non-slip timer
  routineTimer.reset();
  
  return Scheduler.Event.NEXT;
}


function endLoopIteration(thisTrial) {
  // ------Prepare for next entry------
  return function () {
    if (typeof thisTrial === 'undefined' || !('isTrials' in thisTrial) || thisTrial.isTrials) {
      psychoJS.experiment.nextEntry();
    }
  return Scheduler.Event.NEXT;
  };
}


function importTrialAttributes(thisTrial) {
  return function () {
    psychoJS.importAttributes(thisTrial);

    return Scheduler.Event.NEXT;
  };
}


function quitPsychoJS() {
  psychoJS.window.close();
  psychoJS.quit();

  return Scheduler.Event.QUIT;
}
