---
source_url: https://docs.aws.amazon.com/securityhub/latest/userguide/securityhub-integration-view-findings.html
---

# Viewing findings from a Security Hub CSPM integration
<a name="securityhub-integration-view-findings"></a>

When you start accepting findings from an AWS Security Hub CSPM integration, the **Integrations** page of the Security Hub CSPM console displays the **Status** of the integration as **Accepting findings**. To review a list of findings from the integration, choose **See findings**.

The findings list shows the active findings for the selected integration that have a workflow status of `NEW` or `NOTIFIED`.

If you enable cross-Region aggregation, then in the aggregation Region, the list includes findings from the aggregation Region and from linked Regions where the integration is enabled. Security Hub does not automatically enable integrations based on the cross-Region aggregation configuration.

In other Regions, the finding list for an integration only contains findings from the current Region.

For information on how to configure cross-Region aggregation, see [Understanding cross-Region aggregation in Security Hub CSPM](finding-aggregation.md).

From the findings list, you can perform the following actions.
+ [Change the filters and grouping for the list](securityhub-findings-manage.md)
+ [View details for individual findings](securityhub-findings-viewing.md#finding-view-details-console)
+ [Update the workflow status of findings](findings-workflow-status.md)
+ [Send findings to custom actions](findings-custom-action.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Security Hub. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query securityhub` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
