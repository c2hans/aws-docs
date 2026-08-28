---
source_url: https://docs.aws.amazon.com/AmazonS3/latest/s3-outposts/S3OutpostsOtherServices.html
---

# Other AWS services that use S3 on Outposts
<a name="S3OutpostsOtherServices"></a>

Other AWS services that run local to your AWS Outposts can also use your Amazon S3 on Outposts capacity. In Amazon CloudWatch the `S3Outposts` namespace shows detailed metrics for buckets within S3 on Outposts, but these metrics don't include usage for other AWS services. To manage your S3 on Outposts capacity that is consumed by other AWS services, see the information in the following table.

| AWS service | Description | Learn more |
| --- | --- | --- |
| Amazon S3 | All direct S3 on Outposts usage has a matching account and bucket CloudWatch metric. | [See metrics](https://docs.aws.amazon.com/AmazonS3/latest/userguide/S3OutpostsCapacity.html#S3OutpostsCloudWatchMetrics) |
| Amazon Elastic Block Store (Amazon EBS) | For Amazon EBS on Outposts, you can choose an AWS Outpost as your snapshot destination and store locally in your S3 on Outpost. | [Learn more](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/snapshots-outposts.html) |
| Amazon Relational Database Service (Amazon RDS) | You can use Amazon RDS local backups to store your RDS backups locally on your Outpost. | [Learn more](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/rds-on-outposts.html) |

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Simple Storage Service (S3). To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AmazonS3` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
