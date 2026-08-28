---
source_url: https://docs.aws.amazon.com/whitepapers/latest/aws-outposts-high-availability-design/rds-outpost-local-backup.html
---

# Amazon RDS on AWS Outposts local backup
<a name="rds-outpost-local-backup"></a>

[Amazon RDS local backups on AWS Outposts](https://aws.amazon.com/about-aws/whats-new/2021/11/amazon-rds-backups-aws-outposts/) enable you to recover an RDS DB instance directly from S3 stored locally on your Outposts. This allows you to meet data residency requirements and reduces latency compared to recovering from an AWS Region. With Amazon RDS on AWS Outposts, you have the following restore options:
+ From a manual DB snapshot stored in the parent Region or locally on your Outposts.
+ From an automated backup (point-in-time recovery):
  + If restoring from the parent AWS Region, you can store backups either in the AWS Region or on your Outposts.
  + If restoring from your Outposts, backups must be stored locally on Outposts with S3 support.

## Considerations for Amazon RDS local backup on AWS Outposts
<a name="rds-outpost-local-backup-considerations"></a>

Refer to the following considerations to take advantage of Amazon RDS local backups on AWS Outposts:
+ You need S3 on Outposts capacity to store the backups locally.
+ Local backups are supported on [MySQL and PostgreSQL](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/rds-on-outposts.features.html) DB instances.
+ Local backups are not supported for [Multi-AZ instance](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/rds-on-outposts.maz.html) deployments or read replicas.

## Snapshot Exporting and Restoring for RDS on AWS Outposts
<a name="rds-outpost-export-restore"></a>

Exporting Snapshots to S3 and restoring a DB instance from Amazon S3: While RDS snapshots can be exported or restored directly from Amazon S3 in the AWS Region, this is not supported within AWS Outposts environments.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Whitepapers. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query whitepapers` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
