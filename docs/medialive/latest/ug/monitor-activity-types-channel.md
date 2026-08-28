---
source_url: https://docs.aws.amazon.com/medialive/latest/ug/monitor-activity-types-channel.html
---

# States for channels and multiplexes
<a name="monitor-activity-types-channel"></a>

You can monitor the states of MediaLive channels and multiplexes.

MediaLive reports the state of all channels. MediaLive turns these states into CloudWatch events with the detailType set to `MediaLive Channel State Change`. For an example of the JSON for these events, see [JSON for a state change event](monitoring-cloudwatch-json-state-change.md).

The channel states are the following:
+ **Creating**
+ **Deleting**
+ **Idle**: The channel isn't running. For information about charges that you accrue when a channel is idle, see [Pricing in MediaLive](pricing.md).
+ **Recovering**: One or both pipelines in the channel failed, but MediaLive is restarting it.
+ **Running**.
+ **Starting**
+ **Stopping**
+ **Updating**: You changed the [channel class](class-channel-input.md)for a channel. This state is captured on the console but not in [Amazon CloudWatch events](monitoring-via-cloudwatch.md).

MediaLive reports the state of all multiplexes. MediaLive turns these states into CloudWatch events with the detailType set to `MediaLive Multiplex State Change`.

The multiplex states are the following:
+ **Creating**
+ **Deleting**
+ **Idle**: The multiplex isn't running. For information about charges that you accrue when a multiplex is idle, see [Pricing in MediaLive](pricing.md).
+ **Recovering**: One or both pipelines in the multiplex failed, but MediaLive is restarting it.
+ **Running**
+ **Starting**
+ **Stopping**

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for MediaLive. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query medialive` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
