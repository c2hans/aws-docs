---
source_url: https://docs.aws.amazon.com/medialive/latest/ug/mgi-prepare-channel.html
---

# Step 2: Enable the feature
<a name="mgi-prepare-channel"></a>

Perform this step for each MediaLive channel where you want to insert a motion graphic overlay.

**Note**
The information in this section assumes that you are familiar with the general steps for creating a channel, as described in [Creating a channel from scratch](creating-channel-scratch.md).

**To enable the feature**

Follow this procedure when you create the channel or when you are modifying an existing channel.

1. Display the **General channel settings** section and choose the **Motion graphics configuration** pane.

1. Turn on the **Enable motion graphics configuration**. More fields appear.

1. Set the fields as follows:
   + **Motion graphics insertion** – Set to **Enabled**.
   + **Motion graphics settings** – Leave the value as **HTML motion graphics** (the only option).

   For detailed information about this section of the **Create channel** page on the console, see [Complete general settings](creating-a-channel-step3.md).

   When you create or save the channel, it will be set up for motion graphics overlay. This means that when you add an action to the channel schedule, the option for motion graphics will appear in the list in the **Action type** field.

**Important**
When you save a channel that has the motion graphics overlay feature enabled, there is a charge for the feature that applies when the channel is running, even when there is no motion graphics overlay currently being inserted.
To stop this charge, you must disable the feature.

**To disable the feature**

To disable the motion graphics feature, turn off the **Enable motion graphics configuration** field.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for MediaLive. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query medialive` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
