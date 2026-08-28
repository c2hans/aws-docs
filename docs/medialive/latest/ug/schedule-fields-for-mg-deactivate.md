---
source_url: https://docs.aws.amazon.com/medialive/latest/ug/schedule-fields-for-mg-deactivate.html
---

# Fields for deactivating a motion graphics overlay
<a name="schedule-fields-for-mg-deactivate"></a>

This table shows the fields that apply for an action to deactivate an motion graphics overlay.

| Field | Description |
| --- | --- |
| Action type | Motion Graphics Deactivate.  |
| Action name | A name for this deactivation action. For example, deactivate\_motion\_graphic. |
| Start type  | Fixed or Immediate. |
| Date and time | If the **Start type** is **Fixed**, specify the date and time (in UTC format) that the channel must deactivate the motion graphics overlay. The time should be at least 60 seconds later than the time that you submit the action. <br />Note that the time is the wall clock time, not the timecode in the input. |

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for MediaLive. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query medialive` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
