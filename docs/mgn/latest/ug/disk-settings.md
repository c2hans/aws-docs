---
source_url: https://docs.aws.amazon.com/mgn/latest/ug/disk-settings.html
---

NEW - You can now accelerate your migration and modernization with AWS Transform. Read [Getting Started](https://docs.aws.amazon.com/transform/latest/userguide/getting-started.html) in the *AWS Transform User Guide*.

# Review disk settings for source servers
<a name="disk-settings"></a>

The **Disk settings** tab shows a list of all of the disks on the source server and information for each disk.

Disk settings include:
+ **Disk name**
+ **Staging disk type** – The storage type being used for the disk. When using Amazon EBS, this shows the Amazon EBS volume type. When using FSx for ONTAP, this shows the FSx for ONTAP volume configuration.
+ **Replicated storage** – The amount of storage that has been replicated from the disk to the Replication Server.
+ **Total storage** – The total storage capacity of the disk.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Transform MGN. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query mgn` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
