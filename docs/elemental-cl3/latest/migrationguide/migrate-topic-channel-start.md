---
source_url: https://docs.aws.amazon.com/elemental-cl3/latest/migrationguide/migrate-topic-channel-start.html
---

# Restarting channels
<a name="migrate-topic-channel-start"></a>

**To restart one channel**

1. To decide which channels to restart, use the list of running channels that you made when you stopped the channel. This list identifies the node that each channel is assigned to.

1. Choose the **Channels** page, then select the start button beside the channel to start.

**To restart several or all channels**

1. On the web interface for the primary Conductor node, choose the **Channels** page.

1. Toward the top of the page, choose **Tasks**, then choose **Start Channels**.

1. Choose **Select all channels**.

   Or select individual channels. If you are starting channels on a specific node, use the list of running channels that you made when you stopped the channel. This list identifies the node that each channel is assigned to.

1. Choose **Next**, then choose **Process Now**.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Elemental Conductor Live 3. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query elemental-cl3` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
