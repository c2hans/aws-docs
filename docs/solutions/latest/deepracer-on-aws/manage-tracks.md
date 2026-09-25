---
source_url: https://docs.aws.amazon.com/solutions/latest/deepracer-on-aws/manage-tracks.html
---

# Manage tracks
<a name="manage-tracks"></a>

An event runs on one or more **tracks**, up to a maximum of 10. Each track keeps its own leaderboard and can be operated independently by a different race facilitator, which lets a large venue run concurrent heats.

Tracks are managed from the **Tracks** tab of the event details page.

![The Tracks tab of an event](https://docs.aws.amazon.com/solutions/latest/deepracer-on-aws/images/deepracer_event_detail_tracks.png)

To add a track, choose **Edit event**, then choose the **Add track** icon (**\+**) and provide:
+  **Header text**: the name for this track, displayed at the top of its leaderboard.
+  **Leaderboard footer**: optional. Text displayed at the bottom of this track’s leaderboard.
+  **Fleet**: optional. The fleet of cars assigned to this track.

![The track configuration section of the create or edit event form](https://docs.aws.amazon.com/solutions/latest/deepracer-on-aws/images/deepracer_event_edit_add_tracks.png)

Each track in the table provides a **Timekeep** link, which opens the timekeeping page for that track, and a **Leaderboard** link, which opens the track’s leaderboard display.

The **Add track** button is unavailable when any of the following is true:
+ The event is not in **Draft** or **Open** status.
+ The event already has 10 tracks.
+ No track layout has been chosen in the event’s race configuration.

To remove a track, select it and choose **Remove track**. Tracks can only be removed while the event is in **Draft** status, and an event must keep at least one track. The solution declines to remove the last one.
