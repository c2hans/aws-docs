---
source_url: https://docs.aws.amazon.com/mgn/latest/ug/launch-settings.html
---

NEW - You can now accelerate your migration and modernization with AWS Transform. Read [Getting Started](https://docs.aws.amazon.com/transform/latest/userguide/getting-started.html) in the *AWS Transform User Guide*.

# Launch settings
<a name="launch-settings"></a>

The launch settings include two sections: the general launch settings, and the EC2 launch template, which determine how a test or cutover instance is launched for each source server in AWS.

Launch settings, including the EC2 launch template, are automatically created each time you add a source server to AWS Transform MGN.

The launch settings can be modified at any time, including before the source server has completed its initial sync.

**Note**
Any changes made to the launch settings only affect newly launched test and cutover instances.

**Note**
For many customers, there is no need to modify the launch settings or the EC2 launch template to launch test or cutover instances.

Launch settings can only be changed for one server at a time through the AWS Transform MGN console.

**Note**
You can modify launch settings for multiple servers at a time by using the AWS Transform MGN API.

You can access the launch settings of a specific source server through the server details view by choosing its Hostname from the **Source servers** page.

Within the individual server view, navigate to the **Launch settings** tab.

The **Launch settings** tab is divided into two sections:
+ General launch settings
+ EC2 launch template

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Transform MGN. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query mgn` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
