---
source_url: https://docs.aws.amazon.com/solutions/latest/deepracer-on-aws/combined-leaderboard.html
---

# Combined leaderboard
<a name="combined-leaderboard"></a>

When an event has two or more tracks, the solution automatically maintains an additional leaderboard that ranks racers across tracks. It appears as a **Combined** tab alongside the individual track leaderboards, and it updates on its own as results are submitted. No manual step is required.

How scores are combined depends on the **Combined scoring strategy** chosen for the event:

| Strategy | How a racer’s combined score is calculated |
| --- | --- |
|  **Best result per racer**  | The racer’s single best score from any track they raced. |
|  **Sum across tracks**  | The sum of the racer’s best score from every track they have raced. |
|  **Average across tracks**  | The average of the racer’s best score from every track they have raced. |

For **Sum across tracks** and **Average across tracks**, a racer does not need to have raced every track in the event. Because tracks commonly run concurrently as independent heats, the combined leaderboard reflects each racer’s progress so far, using whatever track results they currently have. A racer with no submitted results anywhere does not appear.

**Note**
The combined leaderboard is derived from the individual track leaderboards, so it updates a moment after them. If combining results fails for any reason, the individual track leaderboards continue to update normally.
