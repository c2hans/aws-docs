---
source_url: https://docs.aws.amazon.com/medialive/latest/ug/schedule-fields-activate-image-per-output.html
---

# Fields for activating a per-outputs image overlay
<a name="schedule-fields-activate-image-per-output"></a>

This table shows the fields that apply for an action to activate an image overlay.

| Field | Description |
| --- | --- |
| Action type | Static Image Output Activate. |
| Action name | A name for this activation action. For example, the layer and the name of the image to overlay.  |
| Start type  | Fixed or Immediate. |
| Date and time | The date and time (in UTC format) that the channel must activate the image overlay. The time should be at least 60 seconds later than the time that you submit the action. <br />Note that the time is the wall clock time, not the timecode in the input. |
| Input location | Enter the locations (URLs) on the server where the image file is stored.Also complete **Credentials**, if the server requires that you provide user credentials. |
| Other fields | Complete these fields to control the layer, position, look (such as fade-in), and other behavior of the image.  |

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for MediaLive. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query medialive` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
