---
source_url: https://docs.aws.amazon.com/solutions/latest/deepracer-on-aws/event-lifecycle.html
---

# Event lifecycle
<a name="event-lifecycle"></a>

An event moves forward through five states. Each state narrows what can still be changed, which protects an event that is underway or finished from accidental modification. An event never moves backward.

| Status | What you can do | How to advance |
| --- | --- | --- |
|  **Draft**  | Change any setting. Add or remove tracks. Delete the event. | Choose **Publish event**  |
|  **Open**  | Add tracks and edit leaderboard text. Delete the event. | Choose **Start racing**  |
|  **In progress**  | Operate timekeeping: create runs, record laps, submit results. Delete the event. | Choose **Complete event**  |
|  **Completed**  | View results and statistics. Correct recorded lap times. Delete the event. | Choose **Archive event**  |
|  **Archived**  | View results and statistics. Delete the event. | Archived is the final state |

The status transition buttons appear on the event details page and are visible to admins only.

**Important**
Configure an event’s tracks before you start racing:
You can add tracks only while an event is in **Draft** or **Open** status.
You can remove tracks only while an event is in **Draft** status.
Timekeeping becomes available only when an event reaches **In progress**.
