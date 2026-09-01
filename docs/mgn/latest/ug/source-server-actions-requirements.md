---
source_url: https://docs.aws.amazon.com/mgn/latest/ug/source-server-actions-requirements.html
---

NEW - You can now accelerate your migration and modernization with AWS Transform. Read [Getting Started](https://docs.aws.amazon.com/transform/latest/userguide/getting-started.html) in the *AWS Transform User Guide*.

# Requirements
<a name="source-server-actions-requirements"></a>

Before performing any source server actions, ensure that the following requirements are met:
+ AWS Transform MGN has been [initialized](getting-started.md) in the target AWS Region.
+ The AWS Replication Agent has been installed on the source server. [Learn more about adding source servers](adding-servers.md).
+ The IAM user or role performing actions has the **AWSApplicationMigrationFullAccess** managed policy attached, or equivalent permissions.
+ Network connectivity between the source server and the MGN service endpoints is maintained throughout the migration lifecycle. [Learn more about network requirements](preparing-environments.md#Network-Requirements).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Transform MGN. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query mgn` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
