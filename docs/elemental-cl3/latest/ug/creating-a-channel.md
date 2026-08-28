---
source_url: https://docs.aws.amazon.com/elemental-cl3/latest/ug/creating-a-channel.html
---

# Creating a channel
<a name="creating-a-channel"></a>

**To create a channel**

1. Decide which profile you will use as the basis for the channel.

1. On the Conductor Live main menu, choose **Channels**.

1. On the **Channels** page, choose **New Channel**. The **New Channel** page appears.

1. Complete the fields. Take note of the following:
   + **Profile**: Choose the profile to base this channel on. When you choose a profile, the page changes to show all the profile parameters for that profile.

     The page doesn't show fields from the profile that you didn't set in the profile. For those fields, the default value applies.

     The pages doesn't show fields that you did set in the profile. For those fields, the value from the profile applies. You can't change the value locally in the channel.
   + **Node**: You can choose a node now, or you can leave this field empty and assign a node later. Make sure that the node is appropriate for the density of the channel. Make sure that the node has all the licenses required for the channel. For example, make sure that it has the required codec licenses.
   + **Profile parameters**: Complete the profile parameters. Remember that some fields aren't required, even if you created a profile parameter for the field.

     For example, there might be a profile parameter for an interface. The interface field might be optional. In this field, you can enter a value. Or you can leave the field empty —Elemental Live will use the default interface.

1. Choose **Save**. The channel is created. If you specified all the parameters, then the channel is ready to run: see [Starting and stopping a channel](starting-and-stopping-channels.md).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Elemental Conductor Live 3. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query elemental-cl3` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
