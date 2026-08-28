---
source_url: https://docs.aws.amazon.com/mgn/latest/ug/launch-settings-source.html
---

NEW - You can now accelerate your migration and modernization with AWS Transform. Read [Getting Started](https://docs.aws.amazon.com/transform/latest/userguide/getting-started.html) in the *AWS Transform User Guide*.

# Review launch settings for a source server
<a name="launch-settings-source"></a>

The launch settings are a set of instructions that comprise an EC2 launch template and other settings, which determine how a test or cutover instance is launched for each source server on AWS.

Launch settings, including the EC2 launch template, are automatically created every time you add a server to AWS Transform MGN.

The launch settings can be modified at any time, including before the source servers have even completed initial sync.

[Learn more about individual launch settings.](launch-settings.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Transform MGN. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query mgn` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
