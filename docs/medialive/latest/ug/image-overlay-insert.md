---
source_url: https://docs.aws.amazon.com/medialive/latest/ug/image-overlay-insert.html
---

# Inserting and removing an overlay
<a name="image-overlay-insert"></a>

When you are ready, you can create an action in the MediaLive channel schedule to activate (insert) the overlay. You can create the action at any time – before the channel has started or while it is already running.The schedule is a timetable that is attached to each channel. It lets you perform actions at a specific time, on a running (active) channel. You can work with the schedule using either the MediaLive console or an AWS API or SDK.

You can set up the action so that an image overlay is active for a specific time, or so that it is active indefinitely. In both cases, you can stop the overlay at any time by creating a deactivate action. For more information, see [Working with image overlays](working-with-image-overlay.md).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for MediaLive. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query medialive` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
