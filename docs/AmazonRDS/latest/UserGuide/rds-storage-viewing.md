---
source_url: https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/rds-storage-viewing.html
---

# Viewing storage volume details for your DB instance
<a name="rds-storage-viewing"></a>

You can view your storage volume configuration from the AWS Management Console or AWS CLI. This includes details about both your primary storage volume and any additional storage volumes attached to your DB instance.

The `StorageVolumeStatus` field indicates whether the volume is currently in use by your database. A status of `Not-in-use` means the volume is attached but it's not in use by the database engine or an RDS feature.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon RDS. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AmazonRDS` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
