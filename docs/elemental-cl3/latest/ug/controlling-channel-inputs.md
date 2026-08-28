---
source_url: https://docs.aws.amazon.com/elemental-cl3/latest/ug/controlling-channel-inputs.html
---

# Controlling channels
<a name="controlling-channel-inputs"></a>

When a channel is running, you can control its behaviour from the Conductor Live web interface in several ways. These features work in the same way as they work on the Elemental Live node.

1. On the Conductor Live main menu, choose **Channels**, then select the channel by ID or by name. The **Channel Details** page appears.

1. On the **Channel Details** page, choose the **Status** tab.

**Switching inputs**

If the channel is configured with more than one input, you can switch to a different input.

The **Status** tab shows the inputs in the channel. The input that is currently being ingested has an active icon. It also shows a green line going from the input to the output panel.

To switch, choose the green **Start** button to the left of another input. The selected input turns blue and is represented by a rotating circle of dots while it connects. The buttons dim and additional actions are disabled until the input has switched.

**Controlling ad avail blanking for the channel**

If the channel has been configured for ad avail blanking, an Ad avail blanking viewer shows whether blanking is currently active.

To start or stop blanking, select the window.

**Starting, stopping, and pausing the output**

You can start, stop, and pause each output that is in the channel.

In the output panel, there is a section for each output. In each section, buttons appear for the actions that apply to that output type.

Select the button.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Elemental Conductor Live 3. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query elemental-cl3` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
