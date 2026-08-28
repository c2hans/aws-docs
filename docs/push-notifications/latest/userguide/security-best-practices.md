---
source_url: https://docs.aws.amazon.com/push-notifications/latest/userguide/security-best-practices.html
---

# Security best practices
<a name="security-best-practices"></a>

Use AWS Identity and Access Management (IAM) accounts to control access to API operations, especially operations that create, modify, or delete resources. For the API, such resources include projects, campaigns and journeys.
+ Create an individual user for each person who manages resources, including yourself. Don't use AWS root credentials to manage resources.
+ Grant each user the minimum set of permissions required to perform his or her duties.
+ Use IAM groups to effectively manage permissions for multiple users.
+ Rotate your IAM credentials regularly.

For more information about security, see [Security in AWS End User Messaging Push](security.md). For more information about IAM, see [AWS Identity and Access Management](https://docs.aws.amazon.com/IAM/latest/UserGuide/getting-set-up.html). For information on IAM best practices, see [IAM best practices](https://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS End User Messaging Push. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query push-notifications` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
