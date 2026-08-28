---
source_url: https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_PIOPS.ModifyingExisting.html
---

# Increasing DB instance storage capacity
<a name="USER_PIOPS.ModifyingExisting"></a>

To increase storage capacity for your DB instance, use either of the following techniques:

**Scale up the storage volume**
Every DB instance has a primary storage volume with a maximum capacity of 64 TiB. You can increase the allocated space on a storage volume by a minimum of 10%. You can't deallocate space.

**Add up to three storage volumes (io2 or gp3)**
You can increase the total storage capacity of an RDS for Oracle or RDS for SQL Server instance by adding up to three volumes to each DB instance. Each additional volume allocates up to 64 TiB of storage, up to a maximum of 256 TiB per instance.
For RDS for Oracle DB instances, you can add a storage volume with the minimum storage size of 200 GiB.

You can use the Amazon RDS Management Console, the Amazon RDS API, or the AWS Command Line Interface (AWS CLI) for the preceding techniques. For information about storage limits, see [Amazon RDS DB instance storage](CHAP_Storage.md).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon RDS. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AmazonRDS` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
