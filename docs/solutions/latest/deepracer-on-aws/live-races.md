---
source_url: https://docs.aws.amazon.com/solutions/latest/deepracer-on-aws/live-races.html
---

# Live races
<a name="live-races"></a>

![Live races](https://docs.aws.amazon.com/solutions/latest/deepracer-on-aws/images/deepracer_live_race_overview.png)

When you want everyone in the room to watch each model race in real-time — whether in a classroom, workshop, or competition — community races fall short. They evaluate models asynchronously as submissions arrive, so there is no shared moment when the crowd watches together and a result is declared live. Live races solve this: a facilitator controls the pace, all participants watch the same video stream simultaneously, and the leaderboard updates in real-time as each evaluation completes.

Live races are facilitator-managed racing events where submitted models are evaluated one at a time in sequence while all participants watch together. A facilitator (or the [autolaunch system](#autolaunch)) triggers each model evaluation in turn, and when all models have been evaluated or the facilitator is satisfied with the results, they declare a winner, ending the race.

Live races appear alongside community races on the **Races** page, distinguished by a **Live Race** badge on their card. The card also displays the scheduled event time or current status (for example, "In Progress" or a countdown to the event start).

## Entering a live race
<a name="entering-a-live-race"></a>

Racers enter a live race by submitting a [trained model](train-and-evaluate-models.md), using the same workflow as community races. From the **Races** page, click on the "See race details" button from the live race card to view its details, then click **Enter race**. Select a model from the list of eligible trained models and confirm your submission.

![Live race details page](https://docs.aws.amazon.com/solutions/latest/deepracer-on-aws/images/deepracer_live_race_details.png)

Whether you can submit a model depends on the submission period, which is controlled by the facilitator. If submissions are closed, the **Enter race** button will be disabled and a message will indicate that submissions are not currently being accepted. Models that have already been submitted to the race’s queue cannot be submitted again.

## Watching a live race
<a name="watching-a-live-race"></a>

Once a live race is in progress, click the **Watch live** button on the race details page to open the live race interface. This view is available to all users — you do not need to be a facilitator or have submitted a model to watch.

![Live race participant view](https://docs.aws.amazon.com/solutions/latest/deepracer-on-aws/images/deepracer_live_race_participant.png)

The live race interface includes:
+  **Video panel** — a real-time video stream of the vehicle currently being evaluated on the track. When no evaluation is running, the panel displays a status message (for example, "Waiting for launch" or "All evaluations complete").
+  **Leaderboard** — a ranked list of participants updated in real-time as evaluations complete, showing rank, participant name, model name, and best result.
+  **Progress bar** — shows how many models have been evaluated out of the total in the queue.
+  **Participant notifications** — toast messages that appear when your model starts evaluation, completes, achieves a top-3 ranking, or sets the best result.
+  **Winner overlay** — a full-screen celebration when the facilitator declares a winner, showing the winner’s name, model, and best result.

Real-time leaderboard updates and participant notifications are delivered via a persistent WebSocket connection (powered by AWS IoT Core) that the browser establishes when you open the live race interface. This means the page updates instantly as evaluations complete — no manual refreshing required. If your connection drops, the interface automatically re-fetches the latest race state when it reconnects, so you will never see stale results.

**Note**
The video stream and the race state updates travel over two independent channels. The video is delivered as an HLS stream from Kinesis Video Streams, while leaderboard, queue status, and notification events are pushed from the server over the WebSocket connection via AWS IoT Core.

## Broadcast mode
<a name="broadcast-mode"></a>

Broadcast mode is a full-screen spectator view optimized for projecting onto a large display. To open broadcast mode, click the **Open broadcast** button (external link icon) in the live race interface header. This opens a new browser tab with a streamlined view that includes:
+ The race name and live status indicator
+ The current participant’s name
+ The video stream
+ A progress bar
+ Participant notifications and winner overlay

![Live race broadcast mode](https://docs.aws.amazon.com/solutions/latest/deepracer-on-aws/images/deepracer_live_race_broadcast.png)

In broadcast mode, the mouse cursor automatically hides after 3 seconds of inactivity to keep the projected display clean.

## Facilitating a live race
<a name="facilitating-a-live-race"></a>

**Note**
Only [admins and race facilitators](types-of-users.md) can facilitate live races.

Facilitators manage the flow of a live race from the same live race interface that participants use, but with additional controls visible in the page header and queue panel. The facilitator view includes a **Launch** button, an **Actions** dropdown menu, and management controls within the queue panel.

![Live race facilitator view](https://docs.aws.amazon.com/solutions/latest/deepracer-on-aws/images/deepracer_live_race_facilitator.png)

### Launching evaluations
<a name="launching-evaluations"></a>

The **Launch** button in the page header starts the evaluation of the next model in the queue. When clicked, the system spins up the simulation environment, begins evaluating the model, and streams the video feed to all connected viewers.

The **Launch** button is disabled when:
+ An evaluation is already in progress
+ The race has been completed (winner declared)
+ The current time is before the scheduled live event time

<a name="autolaunch"></a>Alternatively, facilitators can enable **Autolaunch** using the toggle in the queue panel. When autolaunch is enabled, the next model in the queue is automatically launched as soon as the previous evaluation completes, without requiring the facilitator to manually click **Launch** each time.

### Managing the queue
<a name="managing-the-queue"></a>

The queue panel displays all submitted models and their current status. Each queue item shows the participant’s name, model name, and status (**Pending**, **In progress**, **Completed**, or **Failed**).

Facilitators can perform the following actions on queue items:
+  **Reorder** — select a pending queue item and use the up and down buttons to change its position in the evaluation order. Only items in **Pending** status can be reordered.
+  **Remove** — remove a model from the queue entirely. This removes the submission and the model will not be evaluated.
+  **Reset** — reset a failed or in-progress model back to pending status so it can be evaluated again. When a model is reset, the system takes approximately 30 seconds to clean up the previous evaluation environment before the model can be relaunched. A progress indicator is shown during this period.

### Handling live race failures
<a name="handling-live-race-failures"></a>

If a model evaluation fails mid-race, the queue item displays a **Failed** status. Autolaunch is automatically disabled when a failure occurs, so the facilitator must take an explicit action before the race can continue.

The recommended approach depends on the cause of the failure:
+  **Transient failure (most common)** — Click **Reset** on the failed item and wait for the cleanup to complete (\~30 seconds). Once the item returns to **Pending** status, click **Launch** (or re-enable Autolaunch) to retry the evaluation.
+  **Persistent failure** — If the same model fails again after a reset, click **Remove** to remove it from the queue and proceed with the remaining submissions.
+  **Unknown cause** — For repeated or unexpected failures, a cloud admin can examine the `/aws/lambda/DeepRacerTraining` and `/aws/lambda/DeepRacerLiveRacing` log groups in Amazon CloudWatch Logs to identify the root cause. See [Using CloudWatch Logs to diagnose issues](troubleshooting-the-solution.md#using-cloudwatch-logs-to-diagnose-issues).

**Note**
Removing a model from the queue is permanent. The participant’s submission is deleted and cannot be re-queued without the facilitator opening submissions and the participant re-entering the race.

### Controlling submissions
<a name="controlling-submissions"></a>

Facilitators can open or close the submission period using the toggle in the queue panel. When the submission period is closed, racers cannot submit new models to the race. This allows the facilitator to lock the queue before or during the live event to prevent late entries from disrupting the flow.

The submission period is independent of the scheduled live event time — a facilitator can open submissions well before the event to allow participants to queue their models in advance, then close submissions once the event begins.

### Declaring a winner
<a name="declaring-a-winner"></a>

When the facilitator is ready to end the race, they click **Actions > Declare winner**. A confirmation modal appears showing the current top-3 rankings. Confirming this action:
+ Ends the race permanently (status changes to **Completed**)
+ Stops any running evaluation
+ Triggers the winner overlay for all connected viewers, displaying the first-place participant’s name, model, and best result
+ Disables all further facilitator controls

**Note**
Declaring a winner is a permanent action. Once a winner is declared, the race cannot be resumed or restarted.

### Clearing the leaderboard
<a name="clearing-the-leaderboard"></a>

Facilitators can click **Actions > Clear leaderboard** to reset all race progress. This action:
+ Resets all queue items back to pending status
+ Clears all rankings from the leaderboard
+ Stops any running evaluation
+ Disables autolaunch

This is useful when running practice rounds before the official race, or when a technical issue requires starting over. A confirmation modal is shown before the action is applied.

**Note**
Clearing the leaderboard does not remove submitted models from the queue — it only resets their evaluation status and the leaderboard rankings.
