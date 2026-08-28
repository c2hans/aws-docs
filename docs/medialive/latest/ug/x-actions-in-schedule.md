---
source_url: https://docs.aws.amazon.com/medialive/latest/ug/x-actions-in-schedule.html
---

# Types of actions in the schedule
<a name="x-actions-in-schedule"></a>

The schedule is a list of actions that a channel performs as it is running. You can use actions to do the following:
+ Switch the input that the running channel is ingesting.
+ Prepare an input that is associated with an immediate input switch, in order to reduce the delay that occurs when MediaLive performs the switch.
+ Insert a static image overlay (an image layered over the underlying video) in every output in every output group. This action is called global image overlay.
+ Insert a static image overlay into the running channel, only in specific outputs in specific output groups. The action is called per-outputs image overlay.
+ Insert a motion graphics overlay into the running channel.
+ Insert SCTE 35 messages into the running channel.
+ Insert ID3 metadata into the running channel.
+ Insert ID3 segment tags into the running channel.
+ Pause one or both of the pipelines in the channel.
+ Unpause one or both of the pipelines in the channel.

For more information, see [How schedule actions work](sched-how-actions-work.md).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for MediaLive. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query medialive` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
