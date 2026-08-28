---
source_url: https://docs.aws.amazon.com/quick/latest/userguide/qbiz-indexes-prerequisites.html
---

# Prerequisites
<a name="qbiz-indexes-prerequisites"></a>

Before you can use Amazon Q Business indexes in Amazon Quick, ensure that you meet the following prerequisites:

## Common Prerequisites
<a name="qbiz-indexes-prerequisites-common"></a>
+ You have an existing Amazon Q Business index with indexed data.
+ Both the Amazon Q Business index and the Amazon Quick instance are in the same AWS account and region.
+ You have administrator permissions in Amazon Quick.

## IDC Implementation Prerequisites
<a name="qbiz-indexes-prerequisites-idc"></a>
+ AWS Identity Center is enabled and configured.
+ Both Amazon Q Business and Amazon Quick authenticate through IAM Identity Center.
+ The IAM Identity Center region and Amazon Q Business index region are the same.
+ You have access to both the Amazon Q Business index and AWS Identity Center administration.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Quick. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query quick` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
