---
source_url: https://docs.aws.amazon.com/managedservices/latest/accelerate-guide/acc-report-config-control-compliance.html
---

# AWS Config Control Compliance report
<a name="acc-report-config-control-compliance"></a>

The AWS Config Control Compliance report provides an in-depth look at resource and AWS Config rule compliance of AMS accounts, You filter the report by Config Rule Severity to prioritize the most critical findings. The following table lists the data provided by this report:

| **Field ** | **Description ** |
| --- | --- |
| Date | Report date |
| Customer name | Customer name |
| AWS account ID | Associated AWS account ID for customer |
| Source identifier | AWS Config rule unique source identifier |
| Rule Description | AWS Config rule description |
| Rule Type | AWS Config rule type |
| Compliance Flag | AWS Config rule compliance state |
| Resource Type | AWS resource type |
| Resource Name | AWS resource name |
| Severity | Default recommended severity defined by AMS for the AWS Config rule |
| Remediation Category | Associated remediation response category for a AWS Config rule |
| Remediation Description | Remediation action explained to make AWS Config rule to be compliant |
| Customer action | Customer action required to make the AWS Config rule to be compliant |
| Delta metrics report | Changes for compliance of a rule between given 2 dates |

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Managed Services. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query managedservices` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
