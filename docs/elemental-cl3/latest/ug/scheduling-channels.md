---
source_url: https://docs.aws.amazon.com/elemental-cl3/latest/ug/scheduling-channels.html
---

# Starting channels using a schedule
<a name="scheduling-channels"></a>

You can schedule channels to run once or repeatedly, and for a specified duration. Schedules must be at least 60 seconds in duration, with at least one minute between scheduled runs.

**To schedule a channel to run**

1. On the Conductor Live main menu, choose **Channels**.

1. Choose the channel by selecting its ID or name.

1. Select the **Schedules **tab on the left. Then choose the** New Schedule** button. Complete the **New Schedule** dialog:
   + **Duration**: Enter a duration. The minimum duration is 60 seconds. Or leave the duration empty to create a schedule without an end time.
   + **Run once** or **Repeat**: Complete the fields to specify the number of times to run the schedule.

1. Choose **Save**. The new schedule is added to the list of schedules.

1. Choose **Enable**. The channel will run as specified.

   See also [View active schedules](#view-active-schedules).

## The procedure
<a name="scheduling-once"></a>

## View active schedules
<a name="view-active-schedules"></a>

After you have enabled at least one schedule, choose **All Active Schedules **to see a calendar view of all active schedules. You can change the display to show one day, week, or month.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Elemental Conductor Live 3. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query elemental-cl3` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
