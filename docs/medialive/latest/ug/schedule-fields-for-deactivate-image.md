---
source_url: https://docs.aws.amazon.com/medialive/latest/ug/schedule-fields-for-deactivate-image.html
---

# Fields for deactivating a global image overlay
<a name="schedule-fields-for-deactivate-image"></a>

This table shows the fields that apply for an action to deactivate an image overlay.

| Field | Description |
| --- | --- |
| Action type | Static Image Deactivate.  |
| Action name | A name for this deactivation action. For example, the name of the image. Or a name that ties back to the activation action plus the term "deactivate." |
| Start type  | Fixed or Immediate. |
| Date and time | If the **Start type** is **Fixed**, specify the date and time (in UTC format) that the channel must deactivate the image overlay. The time should be at least 60 seconds later than the time that you submit the action. <br />Note that the time is the wall clock time, not the timecode in the input. |
| Layer | Enter the layer that contains the image overlay that you want to deactivate. A value 0 to 7. Default is 0. |
| Fade out | Enter the time in milliseconds for the image to fade out. Default is 0 (no fade-out). |

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for MediaLive. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query medialive` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
