---
source_url: https://docs.aws.amazon.com/solutions/latest/deepracer-on-aws/create-an-event.html
---

# Create an event
<a name="create-an-event"></a>

**Note**
Only admins can create an event.

To create an event, choose **Events** in the left sidebar, then choose **Create event**.

![The Events page listing events with their type](https://docs.aws.amazon.com/solutions/latest/deepracer-on-aws/images/deepracer_events_list.png)

The form is divided into two sections.

 **Event details**
+  **Event name**: a unique name to identify the event.
+  **Event type**: one of **Private workshop**, **Official workshop**, **Private track race**, **Official track race**, **AWS Summit**, **Test event**, or **Other**.
+  **Event date**: the date the event takes place, in YYYY/MM/DD format. The date must be today or in the future.
+  **Country**: the country where the event takes place.
+  **Sponsor**: optional. Sponsor text displayed on leaderboards.

 **Race configuration**
+  **Race format**: determines how each run is scored:
  +  **Best lap**: the racer’s fastest valid lap in the run.
  +  **Average laps**: the average of the racer’s valid lap times.
+  **Average lap window**: when the race format is **Average laps**, the number of most-recent laps to average.
+  **Combined scoring strategy**: how results from multiple tracks are combined into a single ranking. Required for events with more than one track. See [Combined leaderboard](combined-leaderboard.md).
+  **Maximum laps**: the maximum number of laps in a run. This value is advisory: the timekeeping page displays progress against it, but the facilitator decides when to end the run.
+  **Maximum time (minutes)**: how long a run may last. The run finishes automatically when this time expires.
+  **Maximum runs per racer**: how many runs a racer may complete during the event, or **Unlimited**. When a racer reaches the limit, the solution declines to create another run for them.
+  **Maximum resets**: how many times a racer’s car may be reset within a single run, or **Unlimited**.
+  **Track layout**: the physical track layout. This applies to every track added to the event.

![The Create event form showing the Event details and Race configuration sections](https://docs.aws.amazon.com/solutions/latest/deepracer-on-aws/images/deepracer_create_event.png)

When you are ready, choose **Create**. The event is created in **Draft** status.

To change an event later, select it on the **Events** page and choose **Edit event**. What you can change depends on the event’s current status. See [Event lifecycle](event-lifecycle.md).
