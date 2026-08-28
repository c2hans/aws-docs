---
source_url: https://docs.aws.amazon.com/workspaces-core/latest/pg/create-service-linked-role.html
---

# Create a Service-Linked Role
<a name="create-service-linked-role"></a>

WorkSpaces Core Managed Instances require an IAM service-linked role. This role:
+ Contains predefined trust and permissions policies.
+ Can only be assumed by WorkSpaces Instances.
+ Must be removed after associated resources are deleted.

For more information on service linked roles, see [Using service-linked roles for Amazon WorkSpaces Instances](https://docs.aws.amazon.com/workspaces-core/latest/ag/using-service-linked-roles.html)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon WorkSpaces Core. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query workspaces-core` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
