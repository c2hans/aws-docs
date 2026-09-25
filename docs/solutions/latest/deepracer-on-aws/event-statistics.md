---
source_url: https://docs.aws.amazon.com/solutions/latest/deepracer-on-aws/event-statistics.html
---

# View event statistics
<a name="event-statistics"></a>

The **Statistics** tab of the event details page summarizes activity across the whole event, covering every track and every racer.

![The Statistics tab showing aggregate metrics for the event](https://docs.aws.amazon.com/solutions/latest/deepracer-on-aws/images/deepracer_event_statistics.png)

| Metric | Meaning |
| --- | --- |
|  **Total runs**  | Every run created during the event, in any state. |
|  **Completed runs**  | Runs whose results were submitted to a leaderboard. |
|  **Discarded runs**  | Runs that were abandoned. |
|  **Unique racers**  | How many different racers took part. |
|  **Total valid laps**  | Laps counted toward scoring, across all runs. |
|  **Average laps per run**  | Valid laps divided by the number of runs. |
|  **Fastest lap**  | The fastest valid lap recorded anywhere in the event. |
|  **Average lap time**  | The mean of all valid lap times. |
|  **Completion rate**  | The proportion of runs that were submitted rather than discarded. |

Statistics are calculated when you open the tab, so they always reflect the latest recorded results. They are available to admins and race facilitators.
