---
source_url: https://docs.aws.amazon.com/medialive/latest/ug/schedule-fields-for-unpause.html
---

# Fields for unpause
<a name="schedule-fields-for-unpause"></a>

In **Schedule action settings**, complete the following fields.

| Field | Description |
| --- | --- |
| Action type | Pause. |
| Action name | A name for the action.  |
|  Start type  | Fixed or Immediate. |
| Date and time | If the **Start type** is **Fixed**, specify the UTC start time for the action. The time should be at least 15 seconds in the future.<br />Note that the time is the wall clock time, not the timecode in the input. |
| Actions | Keep this section empty. Don't add any actions.  |

When you choose **Create**, the empty **Actions** section instructs MediaLive to add an action to the schedule to unpause all pipelines.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for MediaLive. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query medialive` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
