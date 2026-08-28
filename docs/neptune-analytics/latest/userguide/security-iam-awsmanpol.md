---
source_url: https://docs.aws.amazon.com/neptune-analytics/latest/userguide/security-iam-awsmanpol.html
---

# AWS managed policies for Neptune Analytics
<a name="security-iam-awsmanpol"></a>

AWS provides the following managed IAM policies for Neptune Analytics:
+ **NeptuneGraphReadOnlyAccess** — Grants read-only access to Neptune Analytics graph resources, including actions such as `neptune-graph:Get*`, `neptune-graph:List*`, and `neptune-graph:Read*`. Use this policy for users who need to view Neptune Analytics graph configurations without making changes.
+ **AWSServiceRoleForNeptuneGraphPolicy** — Used by the Neptune Analytics service-linked role to publish CloudWatch metrics and logs on behalf of your graphs. You do not attach this policy to users directly.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Neptune Analytics. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query neptune-analytics` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
