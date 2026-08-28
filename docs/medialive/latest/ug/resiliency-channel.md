---
source_url: https://docs.aws.amazon.com/medialive/latest/ug/resiliency-channel.html
---

# Implementing resiliency in the channel
<a name="resiliency-channel"></a>

AWS Elemental MediaLive has several features that provide resiliency in the channel:
+ Automatic input failover – You can set up two inputs in an *input failover pair*. Setting up this way provides resiliency in case of a failure either in the upstream system, or between the upstream system and the channel.

  For more information, see [Implementing automatic input failover](automatic-input-failover.md).
+ Input loss behavior – MediaLive always reacts to loss of video input.You can configure the fine points of how MediaLive behaves. This feature covers all inputs—those that are set up with automatic input failover, and those that aren't.

  For more information, see [Handling loss of video input](feature-input-loss.md).
+ Pipeline redundancy – You can set up the channel with two pipelines, to provide resiliency within the channel pipeline. This feature is controlled by the class of the inputs attached to the channel and by the class of the channel. For more information see the following:
  + [Implementing pipeline redundancy](plan-redundancy-mode.md)
  + [Choosing the channel class and input class](class-channel-input.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for MediaLive. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query medialive` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
