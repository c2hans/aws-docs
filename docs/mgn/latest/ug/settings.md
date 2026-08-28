---
source_url: https://docs.aws.amazon.com/mgn/latest/ug/settings.html
---

NEW - You can now accelerate your migration and modernization with AWS Transform. Read [Getting Started](https://docs.aws.amazon.com/transform/latest/userguide/getting-started.html) in the *AWS Transform User Guide*.

# Configuring AWS Transform MGN Settings
<a name="settings"></a>

AWS Transform MGN uses replication settings to determine how data is replicated from source servers to your AWS account and Region. Learn how to configure your initial replication template and how to set individual server replication settings.

You must configure the replication template upon first use of AWS Transform MGN. The replication template determines how your servers are replicated to AWS through settings such as Replication Server instance type, target storage type, security groups, data routing, and tags. The settings configured in the replication template are automatically used for every server you add to AWS Transform MGN.

Once you have configured your Replication template, you can make changes to individual servers or a group of servers by editing their replication settings within the Server Details View.

You can also configure optional post-launch settings that automate target instance deployment and prepare your migrated servers for disaster recovery with AWS Elastic Disaster Recovery.

**Topics**
+ [Replication template](replication-settings-template.md)
+ [Launch template](launch-template.md)
+ [Post-launch template](post-launch-settings.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Transform MGN. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query mgn` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
