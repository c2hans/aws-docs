---
source_url: https://docs.aws.amazon.com/medialive/latest/ug/schedule-fields-for-pause.html
---

# Fields for pause
<a name="schedule-fields-for-pause"></a>

In **Schedule action settings**, complete the following fields.

| Field | Description |
| --- | --- |
| Action type | Pause. |
| Action name | A name for the action.  |
|  Start type  | Fixed or Immediate. |
| Date and time | If the **Start type** is **Fixed**, specify the UTC start time for the action. The time should be at least 15 seconds in the future.<br />Note that the time is the wall clock time, not the timecode in the input. |
| Actions | Choose Add actions, then for Pipeline id, choose the pipeline that you want to pause: PIPELINE\_0 or PIPELINE\_1.  |

When you choose **Create**, MediaLive adds an action to the schedule to pause the specified pipeline and to unpause any pipeline that isn't specified. As a result, only the specified pipeline will be paused after the action is performed.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for MediaLive. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query medialive` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
