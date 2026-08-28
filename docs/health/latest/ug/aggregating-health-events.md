---
source_url: https://docs.aws.amazon.com/health/latest/ug/aggregating-health-events.html
---

# Aggregating AWS Health events using organizational view and delegated administrator access
<a name="aggregating-health-events"></a>

AWS Health supports organizational view and delegated administrator access for AWS Health events published on Amazon EventBridge. When organizational view is turned on in AWS Health, then the management account or a delegated administrator account receives a single feed of AWS Health events from all accounts within your organization in AWS Organizations.

This feature is designed to provide a centralized view to help manage AWS Health events across your organization. Setting up organizational view and an EventBridge rule in the management account doesn't deactivate EventBridge rules for other accounts in your organization.

For more information on enabling organizational view and delegated administrator access on AWS Health, see [Aggregating AWS Health Events](https://docs.aws.amazon.com/health/latest/ug/aggregate-events.html).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Health. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query health` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
