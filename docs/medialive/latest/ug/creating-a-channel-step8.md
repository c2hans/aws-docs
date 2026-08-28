---
source_url: https://docs.aws.amazon.com/medialive/latest/ug/creating-a-channel-step8.html
---

# Set up the captions encodes
<a name="creating-a-channel-step8"></a>

In [Configure outputs](creating-a-channel-step4.md), you created the output groups and outputs that you identified when you planned the channel. Each output section contains a **Stream settings** section. You must now create all the captions encodes for the outputs.

**General procedure**
Follow this general procedure to set up the captions encode.

1. Decide how you're going to create each encode:
   + From scratch.
   + By sharing an encode that already exists in this output or another output in the channel.
   + By cloning an encode that already exists in this output or another output in the channel.

   You might have already made this decision. If not, you should decide now. For more information, see [Design the encodes](designing-encodes.md).

   You can share or clone captions encodes within one output, from one output to another in the same output group, or from one output to an output in another output group.

1. Read the appropriate sections that follow.

**Topics**
+ [Creating a captions encode from scratch](create-captions-scratch.md)
+ [Creating a captions encode by sharing](create-captions-share.md)
+ [Creating a captions encode by cloning](create-captions-clone.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for MediaLive. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query medialive` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
