---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/oracle-dump-files-aws/moving-dump-files.html
---

# Moving on-premises Oracle Database dump files to AWS
<a name="moving-dump-files"></a>

The following options describes the ways to move the on-premises Oracle Database dump files to an AWS source technology stack during a migration:
+ Use Amazon S3 to transfer Oracle database dump files, targeting Amazon RDS or Amazon EC2.
+ Use a database link to transmit Oracle Database dump files to Amazon RDS or Amazon EC2.
+ Move Oracle Database dump files to Amazon EFS.

## Prerequisites
<a name="prerequisites"></a>
+ A virtual private cloud (VPC)
+ An AWS Identity and Access Management (IAM) role with permissions to access the on-premises data source and the target data source (for more information, see the [AWS documentation](https://docs.aws.amazon.com/cli/latest/userguide/cli-configure-role.html))
+ AWS Command Line Interface (AWS CLI) configured by using the IAM role, with connectivity between the on-premises database and the AWS environment
+ An [S3 bucket](https://docs.aws.amazon.com/AmazonS3/latest/userguide/creating-bucket.html) that can access the on-premises data source (for Amazon S3 security guidelines, see the [AWS documentation](https://docs.aws.amazon.com/AmazonS3/latest/userguide/security-best-practices.html))
+ An IAM role for Amazon S3 integration with Amazon RDS (for more information, see the [AWS documentation](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/oracle-s3-integration.html))
+ Amazon EFS
+ A source Oracle Database server
+ An Amazon RDS for Oracle instance
+ An EC2 instance
+ A database link with validated connectivity from the on-premises data source to the Amazon EC2 or Amazon RDS for Oracle instance

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Prescriptive Guidance. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prescriptive-guidance` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
