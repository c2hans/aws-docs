---
source_url: https://docs.aws.amazon.com/securityhub/latest/userguide/securityhub-cwe-custom-actions.html
---

# Using custom actions to send findings and insight results to EventBridge
<a name="securityhub-cwe-custom-actions"></a>

To use AWS Security Hub CSPM custom actions to send findings or insight results to Amazon EventBridge, you first create the custom action in Security Hub CSPM. Then, you can define rules in EventBridge that apply to your custom actions.

You can create up to 50 custom actions.

If you enable cross-Region aggregation, and manage findings from the aggregation Region, then create custom actions in the aggregation Region.

The rule in EventBridge uses the Amazon Resource Name (ARN) from the custom action.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Security Hub. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query securityhub` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
