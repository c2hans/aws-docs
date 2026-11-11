---
source_url: https://docs.aws.amazon.com/solutions/latest/deepracer-on-aws/timekeeping.html
---

# Run an event with timekeeping
<a name="timekeeping"></a>

The **timekeeping** page is where a race facilitator runs each racer’s attempt: starting the run, recording each lap as the car crosses the line, and submitting the result to the leaderboard. Open it from the **Timekeep** link on the event’s **Tracks** tab or from the sidebar navigation.

![The timekeeping page showing race setup, the timing mode and timer selector, run controls, the countdown, and the recorded laps table](https://docs.aws.amazon.com/solutions/latest/deepracer-on-aws/images/deepracer_timekeeping.png)

**Note**
Using the **Timekeep** link from an Event will automatically select that event and track in the Top Nav Bar. If navigating via the side bar menu, you must select an Event and Track from the Top Nav Bar menu in order to Start a new Run.

**Important**
Timekeeping is only available while the event is **In progress**. Until then, the **Timekeep** link is unavailable.

A single racer’s attempt on a track is called a **run**. A run progresses through these states:

| Status | Meaning |
| --- | --- |
|  **Ready**  | The run has been created but timing has not started. |
|  **In progress**  | Timing is running and laps can be recorded. |
|  **Paused**  | Timing is suspended. The countdown on spectator displays pauses too. |
|  **Finished**  | Timing has stopped, either because the facilitator ended the run or because the time limit expired. The result has not yet been submitted. |
|  **Submitted**  | The result has been scored and applied to the leaderboard. This is final. |
|  **Discarded**  | The run was abandoned. No result was applied to the leaderboard. |

## Start a run
<a name="start-a-run"></a>

In the **Race setup** section, confirm the event and track in the Top Nav Bar, then choose the racer for this attempt. Where the track has a fleet assigned, you can also choose the car. Choose **Start new Run** to create the run, then choose **Start** to begin timing.

If the racer has already used all of their runs for the event, the solution declines to create another one.

![The timekeeping page showing the select racer modal](https://docs.aws.amazon.com/solutions/latest/deepracer-on-aws/images/deepracer_timekeeping_select_racer.png)

## Record laps
<a name="record-laps"></a>

Choose **Start first lap** as the car crosses the line to begin the first timed lap. From then on, choose **Record lap** each time the car completes a circuit. Each lap is added to the **Recorded laps** table with its time and lap number.

![The timekeeping page showing a race ready to begin](https://docs.aws.amazon.com/solutions/latest/deepracer-on-aws/images/deepracer_timekeeping_start_race.png)

The **Timing** section shows **Time left** for the run and the elapsed time for the **Current lap**. When the time limit expires, the run finishes automatically.

Choose **Car reset** to record a reset, for example when a car leaves the track and is placed back on it. The reset count applies to the lap currently being timed, and is shown against the event’s limit. When the lap is captured, its resets are stored with that lap and the counter returns to zero for the next lap.

Use **Pause** and **Resume** to suspend and restart timing. Pausing also pauses the countdown on any spectator display showing this track, so the venue sees the same clock the facilitator does.

![The timekeeping page showing a race in progress](https://docs.aws.amazon.com/solutions/latest/deepracer-on-aws/images/deepracer_timekeeping_pause_race.png)

**Note**
If you reload the timekeeping page during a run, the countdown and the current lap stopwatch cannot be restored, because neither is saved. The run itself and every lap already recorded are unaffected. Use the run controls to end or discard the run, then start a new one.

## Record laps automatically with a timer
<a name="record-laps-automatically"></a>

With a Raspberry Pi timer and track sensors, you can have the timekeeping page record a lap each time the car crosses the finish line, instead of choosing **Record lap** yourself. To set up a timer, see [Activate a Raspberry Pi timer](activate-a-raspberry-pi-timer.md).

 **To time a run automatically**

1. From the **Timer** list, choose the timer installed on this track. The list shows timers that are currently online.

1. For **Timing mode**, choose **Automatic**. **Automatic** is available only after you select a timer.

1. Start the run as usual.

   In **Automatic** mode, a sensor crossing also starts a **Ready** run or resumes a **Paused** run, so you don’t need to choose **Start** or **Resume** yourself.

1. Each later crossing of the finish line records a lap. The timer measures the lap time from the previous crossing. If there is no previous crossing, for example because you started the run with **Start** or the timer restarted, the browser times the lap from the start of the lap.

A status indicator next to the **Timer** list shows the state of the selected timer.

| Status | Meaning |
| --- | --- |
|  **No timer selected**  | Select a timer to use **Automatic** mode. |
|  **Connecting to timer**  | The page is connecting to the timer’s event stream. |
|  **Timer online**  | The timer is connected and sending events. |
|  **Timer not responding**  | No event or heartbeat has arrived from the timer for more than about a minute. Check the Raspberry Pi’s power and network connection. |
|  **Unable to connect to timer**  | The page couldn’t connect to the timer’s event stream. Reload the page or use **Manual** mode. |

You can switch between **Manual** and **Automatic** at any time, including during a run. Switching modes doesn’t end the current lap. The manual controls (**Record lap**, **Did not finish**, **Mark lap invalid**, **Car reset**, and the run controls) stay available in both modes, so you can step in if a sensor misses the car.

To change the timer, switch back to **Manual** first. Selecting a different track resets the mode to **Manual**.

The timer ignores any further crossing within 2 seconds of the last one, from either sensor, so a single pass that trips both sensors or bounces records one lap. If a crossing arrives after the run has stopped, the page doesn’t record a lap and shows a message instead.

### Laps that need review
<a name="laps-that-need-review"></a>

Sensors can double-trigger or miss the car, so you review automatically recorded laps whose times look wrong before they count. The solution flags a lap for review in these cases:

| Condition | Likely cause |
| --- | --- |
| The lap time is shorter than 3 seconds. | A sensor double-trigger. |
| The lap time is longer than 300 seconds (5 minutes). | A missed crossing. |
| Crossings were lost before this lap. | The timer restarted or a lap couldn’t be saved. The recorded time may span more than one lap. |

The solution saves a flagged lap as invalid and shows **Needs review** in the **Recorded laps** table. Choose **Approve** to count the lap as valid, or **Reject** to keep it invalid. If you finish a run that still has laps needing review, a warning on the **Runs** table reminds you that submitting now counts those laps as invalid.

## End a lap that should not count
<a name="end-a-lap-that-should-not-count"></a>

Not every lap ends with the car crossing the line cleanly. The **Timing** section provides two controls for these cases. Both capture a lap using the time elapsed so far, mark it invalid so it is excluded from scoring and the leaderboard, pause the run so you can reposition the car, and reset the lap stopwatch and reset counter for the next lap.

The difference is whether the racer is charged for the time:
+  **Did not finish**: use this when the car genuinely attempted the lap but did not complete it, for example because it went off track or stalled and you decide not to wait. The elapsed time stays charged against the run’s **Time left**, because the attempt consumed real time.
+  **Mark lap invalid**: use this when the capture itself was the mistake, for example a false trigger, or choosing **Record lap** before the car actually finished. The elapsed time is returned to the run’s **Time left**, as though the lap had never happened, so the racer loses nothing for an error that was not theirs.

|  | Did not finish | Mark lap invalid |
| --- | --- | --- |
| Records a lap and marks it invalid | Yes | Yes |
| Pauses the run | Yes | Yes |
| Time charged against **Time left**  | Yes | No, the time is returned |

In short, choose **Did not finish** when the attempt happened and used up real time. Choose **Mark lap invalid** when the capture was the mistake.

After either action the run is paused. Choose **Resume** when the car and racer are ready to continue.

## Change the validity of a recorded lap
<a name="change-the-validity-of-a-recorded-lap"></a>

Separately from the timing controls, you can change the validity of any lap already in the **Recorded laps** table. Use the action on the lap’s row to mark it valid or invalid. For a lap that shows **Needs review**, choose **Approve** or **Reject** instead. Invalid laps remain visible in the table but are ignored when the run is scored.

Admins and race facilitators can also change lap validity, including approving or rejecting laps that need review, on the **Runs** tab of the event details page.

This works at any time, including after the run has been submitted. If the run has already been submitted, changing a lap’s validity rescores the run and updates the leaderboard.

**Note**
Changing validity from the table only affects whether the lap counts toward the score. Unlike **Mark lap invalid** in the **Timing** section, it does not alter the run’s remaining time.

## Submit or discard the run
<a name="submit-or-discard-the-run"></a>

When timing has stopped and the run is **Finished**, review the recorded laps and choose one of the following actions on the run’s row in the **Runs** table:
+  **Submit Run**: scores the run using the event’s race format, applies the result to the track leaderboard if it improves on the racer’s previous best, and updates any combined leaderboard. Submitting is final.
+  **Discard Run**: abandons the run. No result is applied to the leaderboard. The recorded laps are kept for reference but are excluded from event statistics.

If you ended a run by mistake, choose **Resume** to return it to **In progress** and continue timing.

**Note**
You can’t submit a run with no valid laps, because there is nothing to score. Either record a valid lap or discard the run. Laps that still show **Needs review** count as invalid, so approve or reject them before you submit.
