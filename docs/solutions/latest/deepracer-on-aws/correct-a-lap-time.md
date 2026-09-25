---
source_url: https://docs.aws.amazon.com/solutions/latest/deepracer-on-aws/correct-a-lap-time.html
---

# Correct a recorded lap time
<a name="correct-a-lap-time"></a>

**Note**
Only admins can correct a recorded lap time.

If a lap was recorded with the wrong time, an admin can correct it from the **Runs** tab of the event details page. Under **Find a run**, choose the track, then the racer, then the run. The run’s laps appear in a table.

![The Runs tab showing the run lookup and the laps recorded for the selected run](https://docs.aws.amazon.com/solutions/latest/deepracer-on-aws/images/deepracer_event_detail_runs.png)

Choose **Edit** on the lap you need to change, then provide:
+  **Lap time**: the corrected time, in mm:ss.sss format, for example 00:37.264.
+  **Reason for edit**: required. An explanation of why the time is being corrected, for example "Timer strip double-triggered; corrected using video replay timing".

![The Edit lap dialog showing the lap time field and the required reason for edit field](https://docs.aws.amazon.com/solutions/latest/deepracer-on-aws/images/deepracer_lap_edit.png)

Choose **Save changes**. The solution keeps the originally recorded time and records who made the change, when, and the reason given. Any lap that has been edited shows this history in the lap table, so a corrected result is always distinguishable from an original one.

If the run has already been submitted, correcting a lap time rescores the run and updates the track leaderboard and any combined leaderboard.
