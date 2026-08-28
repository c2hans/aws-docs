---
source_url: https://docs.aws.amazon.com/elemental-cl3/latest/upgradeguide/downgrades-start.html
---

# Step H: Start channels
<a name="downgrades-start"></a>

When all nodes have been downgraded, you can start the channels that were previously running.

**To start channels**

1. On the web interface for the primary Conductor Live node, access the **Channels** screen.

1. Toward the top of the page, select **Tasks** and **Start Channels**.

   Alternatively, if you want to start channels individually, select the play button on each channel that you're starting.

If you have only one Conductor Live, the downgrade process is complete when you start the channels. Otherwise, continue to the following section to enable high availability.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Elemental Conductor Live 3. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query elemental-cl3` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
