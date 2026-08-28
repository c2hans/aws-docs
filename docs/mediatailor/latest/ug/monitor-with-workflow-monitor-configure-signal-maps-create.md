---
source_url: https://docs.aws.amazon.com/mediatailor/latest/ug/monitor-with-workflow-monitor-configure-signal-maps-create.html
---

# Creating signal maps for AWS media workflows
<a name="monitor-with-workflow-monitor-configure-signal-maps-create"></a>

You can use workflow monitor signal maps to create a visual mapping of all connected AWS resources in your media workflow.

**To create a signal map**

1. From the workflow monitor console's navigation pane, select **Signal maps**.

1. Select **Create signal map**.

1. Give the signal map a **Name** and **Description**.

1. In the **Discover new signal map** section, resources in the current account and selected region are displayed. Select a resource to begin signal map discovery. The selected resource will be the starting point for discovery.

1. Select **Create**. Allow a few moments for the discovery process to complete. After the process is complete, you will be presented with the new signal map.
**Note**
Previews generated in the workflow monitor signal map for AWS Elemental MediaPackage channels are delivered from the MediaPackage Origin Endpoint and will incur Data Transfer Out charges. For pricing, see: [MediaPackage pricing](https://aws.amazon.com/mediapackage/pricing/).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Elemental MediaTailor. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query mediatailor` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
