---
source_url: https://docs.aws.amazon.com/medialive/latest/ug/mgi-insert-overlay.html
---

# Step 3: Insert the overlay
<a name="mgi-insert-overlay"></a>

When you are ready, you can create an action in the MediaLive channel schedule to activate (insert) the overlay. You can create the action at any time – before the channel has started or while it is already running.

The schedule is a timetable that is attached to each channel. The schedule is designed to let you specify actions to perform on the channel at a specific time. You can set up the action so that a motion graphic is active for a specific time, or so that it is active indefinitely. In both cases, you can stop the overlay at any time by creating a deactivate action.

For detailed information, see [Creating an AWS Elemental MediaLive schedule](working-with-schedule.md) and [Creating actions in the schedule (console)](schedule-using-console-create.md).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for MediaLive. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query medialive` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
