---
source_url: https://docs.aws.amazon.com/securityhub/latest/userguide/securityhub-control-manage-findings.html
---

# Reviewing and managing control findings in Security Hub CSPM
<a name="securityhub-control-manage-findings"></a>

The control details page displays a list of active findings for a control. The list does not include archived findings.

The control details page supports cross-Region aggregation. If you have set an aggregation Region, the control status and list of security checks on the control details page include checks from all linked AWS Regions.

The list provides tools to filter and sort the findings, so that you can focus on more urgent findings first. A finding may include links to resource details in the related service console. For controls that are based on AWS Config rules, you can view details about the rule.

You can also use the AWS Security Hub CSPM API to retrieve a list of findings and finding details.

For more information, see [Reviewing finding details and history](securityhub-findings-viewing.md#finding-view-details-console).

To reflect the current status of your investigation of a control finding, you set the workflow status. For more information, see [Setting the workflow status of findings in Security Hub CSPM](findings-workflow-status.md).

You can also send selected Security Hub CSPM findings to a custom action in Amazon EventBridge. For more information, see [Sending findings to a custom Security Hub CSPM action](findings-custom-action.md).

**Topics**
+ [Filtering and sorting control findings](control-finding-list.md)
+ [Samples of control findings](sample-control-findings.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Security Hub. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query securityhub` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
