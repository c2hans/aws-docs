---
source_url: https://docs.aws.amazon.com/wellarchitected/latest/analytics-lens/best-practice-12.3---restrict-and-record-resource-allocation-permissions-using-aws-identity-and-access-management-iam..html
---

# Best practice 12.3 – Restrict and record resource allocation permissions using AWS Identity and Access Management (IAM)
<a name="best-practice-12.3---restrict-and-record-resource-allocation-permissions-using-aws-identity-and-access-management-iam."></a>

 To better control costs, create distinct IAM roles that authorize users to provision certain resources. This ensures that only permitted individuals can provision the resources they are allowed to, preventing unauthorized and unnecessary spending.

## Suggestion 12.3.1 – Create a cost governance framework that uses specialized IAM roles, rather than individual users, to provision costly infrastructure
<a name="suggestion-12.3.1---create-a-cost-governance-framework-that-uses-specialized-iam-roles-rather-than-individual-iam-users-to-provision-costly-infrastructure."></a>

 Restrict the authorization to launch costly resources to specific IAM roles. For example, certain instances types can only be provisioned by certain teams to reduce unnecessary expenditure.

## Suggestion 12.3.2 – Track AWS CloudTrail logs to determine overall usage-per-user and role
<a name="suggestion-12.3.2---track-iam-usage-logs-to-determine-overall-usage-per-user-and-role."></a>

 Track the usage across users and roles to get a clear understanding of resource usage. As part of your cost-allocation governance, automatically process the AWS CloudTrail logs so that cost allocation is properly attributed to the relevant department.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Well-Architected. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query wellarchitected` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
