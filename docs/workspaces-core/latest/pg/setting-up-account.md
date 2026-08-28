---
source_url: https://docs.aws.amazon.com/workspaces-core/latest/pg/setting-up-account.html
---

# Setting up partner access to AWS accounts
<a name="setting-up-account"></a>

This section explains how to deploy WorkSpaces Core Managed Instances in your AWS environment. You can enable partner solutions to access your AWS account by completing a connection setup with your technology partner. This connection establishes secure access to your AWS environment.

WorkSpaces Core Managed Instances allow EC2 instances to launch directly in your AWS account rather than in an Amazon WorkSpaces Core-owned account. This architecture provides more flexibility and direct access to AWS services while maintaining WorkSpaces Core management capabilities.

For general information about security credentials, see [AWS security credentials](https://console.harmony.a2z.com/link) the *IAM User Guide*.

**Topics**
+ [Grant authorization and permissions](auth-permissions.md)
+ [Create a Service-Linked Role](create-service-linked-role.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon WorkSpaces Core. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query workspaces-core` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
