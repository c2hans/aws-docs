---
source_url: https://docs.aws.amazon.com/drs/latest/userguide/launch-settings-source.html
---

# AWS DRS launch settings
<a name="launch-settings-source"></a>

The launch settings are a set of instructions that comprise an EC2 launch template and other settings, which determine how a recovery instance is launched for each source server on AWS.

Launch settings, including the EC2 launch template, are automatically created every time you add a server to AWS Elastic Disaster Recovery.

The launch settings can be modified at any time, including before the source servers have even completed initial sync.

[Learn more about individual launch settings.](launching-target-servers.md)

**Important**
**If the source server’s instance type includes instance store, please consider the following: **
 It is **not** recommended to change the instance type of an instance to a type that has no ephemeral volumes, or has a different number of ephemeral volumes, as such changes could lead to data inconsistencies and may even cause recovery, drill, or failback to fail.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Elastic Disaster Recovery. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query drs` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
