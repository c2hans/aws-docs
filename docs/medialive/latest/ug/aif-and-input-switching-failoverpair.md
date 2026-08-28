---
source_url: https://docs.aws.amazon.com/medialive/latest/ug/aif-and-input-switching-failoverpair.html
---

# Manually forcing a failover
<a name="aif-and-input-switching-failoverpair"></a>

You can set up automatic input failover to allow the MediaLive operator to perform a manual failover.

Keep in mind that the content in the failover pair is identical. Therefore, you only switch between them for specific reasons. For example:
+ You might think that the active input is degrading, but MediaLive hasn't yet made the decision to fail over to the other input.
+ You might want to perform maintenance on the network for the input that is currently active.

**To switch between the two inputs in the input pair**

1. If you think you might want to manually switch inputs, then when you set up the failover pair, set the **Input preference** to **EQUAL\_INPUT\_PREFERENCE**. See [Setting up automatic input failover with RTMP and RTP inputs](aif-setup-other-inputs.md) or [Setting up automatic input failover with MediaConnect inputs](aif-setup-emx.md).

1. To manually switch, [create an input switch action](schedule-using-console-create.md) in the schedule in the usual way.

   Set up the input to switch to the other input, and set the **Start Type** to **Immediate**.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for MediaLive. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query medialive` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
