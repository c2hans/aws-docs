---
source_url: https://docs.aws.amazon.com/keyspaces/latest/devguide/access.cross-account.html
---

# Configure cross-account access to Amazon Keyspaces with VPC endpoints
<a name="access.cross-account"></a>

You can create and use separate AWS accounts to isolate resources and for use in different environments, for example development and production. This topic walks you through cross-account access for Amazon Keyspaces using interface VPC endpoints in an Amazon Virtual Private Cloud. For more information about IAM cross-account access configuration, see [Example scenario using separate development and production accounts](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_common-scenarios_aws-accounts.html#id_roles_common-scenarios_aws-accounts-example) in the IAM User Guide.

For more information about Amazon Keyspaces and private VPC endpoints, see [Using Amazon Keyspaces with interface VPC endpoints](vpc-endpoints.md).

**Topics**
+ [Configure cross-account access in a shared VPC](access.cross-account.sharedVPC.md)
+ [Configure cross-account access without a shared VPC](access.cross-account.noVPC.setup.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Keyspaces. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query keyspaces` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
