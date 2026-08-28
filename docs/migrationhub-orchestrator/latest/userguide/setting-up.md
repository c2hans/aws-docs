---
source_url: https://docs.aws.amazon.com/migrationhub-orchestrator/latest/userguide/setting-up.html
---

AWS Migration Hub is no longer open to new customers as of November 7, 2025. For capabilities similar to AWS Migration Hub, explore [AWS Transform](https://aws.amazon.com/transform).

# Setting up to use Migration Hub Orchestrator
<a name="setting-up"></a>

Before you get started with AWS Migration Hub Orchestrator, ensure that users have the required permissions.

## Permissions
<a name="setting-up-create-iam-user"></a>

By default, an IAM administrator has all the permissions that are required to access Migration Hub Orchestrator.

The following managed policies grant permissions required to use Migration Hub Orchestrator to a **non-administrative** IAM user.
+ **Console access** – AWSMigrationHubFullAccess and AWSMigrationHubOrchestratorConsoleFullAccess
+ **Plugin** – AWSMigrationHubOrchestratorPlugin
+ **Instances** – AWSMigrationHubOrchestratorInstanceRolePolicy

For more information, see [AWS managed policies for Migration Hub Orchestrator](https://docs.aws.amazon.com/migrationhub-orchestrator/latest/userguide/security-iam-awsmanpol.html).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Migration Hub Orchestrator. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query migrationhub-orchestrator` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
