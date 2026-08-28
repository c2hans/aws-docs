---
source_url: https://docs.aws.amazon.com/medialive/latest/ug/creating-channel-clone.html
---

# Creating a channel by cloning
<a name="creating-channel-clone"></a>

Cloning lets you use an existing channel as the basis for a new channel. When you clone an existing channel, all sections of the **Create channel** page are populated with the data from the cloned channel, *except* for the following:
+ The input sections. These sections are always empty in the cloned channel.
+ The tags. There are no tags in the cloned channel.

You can edit the existing fields and complete the empty fields as needed.

You can clone a channel that is in the **Channels** list. (You can also clone a channel after choosing **Create channel**; for more information, see [Creating a channel from a template](creating-channel-template.md).)

**To create a channel by cloning (console)**

1. Open the MediaLive console at [https://console.aws.amazon.com/medialive/](https://console.aws.amazon.com/medialive/).

1. In the navigation pane, choose **Channels**.

1. On the **Channels** page, choose the radio button next to the channel name.

1. Choose **Clone**.

   The **Create channel** page appears with all the original data except for the inputs and the tags.

1. Give the channel a new name and complete the input sections. Change other fields as needed. For more information, see [Creating a channel from scratch](creating-channel-scratch.md).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for MediaLive. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query medialive` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
