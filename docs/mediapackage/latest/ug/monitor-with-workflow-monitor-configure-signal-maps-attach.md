---
source_url: https://docs.aws.amazon.com/mediapackage/latest/ug/monitor-with-workflow-monitor-configure-signal-maps-attach.html
---

# Attaching alarm and event templates to the signal map of your AWS media workflow
<a name="monitor-with-workflow-monitor-configure-signal-maps-attach"></a>

After you have created alarm and event templates, you need to attach these to a signal map. Any of the alarm and event templates you have created can be attached to any discovered signal maps.

**To attach alarm and event templates to your signal map**

1. From the workflow monitor console's navigation pane, select **Signal maps** and select the signal map you want to work with.

1. In the upper-right of the signal map page, in the **CloudWatch alarm template groups** tab, select **Attach CloudWatch alarm template groups**.

   1. In the new section that opens, choose all of the alarm template groups that you want to apply to this signal map, then select **Add**. This will cause the selected alarm template groups to move to the **Attached CloudWatch alarm template groups** section.

   1. Selecting **Save** will save your changes and return you to the signal map page.

1. At the right of the signal map page, select the **EventBridge rule template groups** tab then select **Attach EventBridge rule template groups**.

   1. In the new section that opens, choose all of the event template groups that you want to apply to this signal map, then select **Add**. This will cause the selected rule template groups to move to the **Attached EventBridge rule template groups** section.

   1. Selecting **Save** will save your changes and return you to the signal map page.

1. You have assigned CloudWatch alarm and EventBridge rule templates to the signal map, but the monitoring is not yet deployed. The next section will cover the deployment of the monitoring resources.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Elemental MediaPackage V1. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query mediapackage` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
