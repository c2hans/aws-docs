---
source_url: https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/oracle-s3-integration.html
---

# Amazon S3 integration
<a name="oracle-s3-integration"></a>

You can transfer files between your RDS for Oracle DB instance and an Amazon S3 bucket. You can use Amazon S3 integration with Oracle Database features such as Oracle Data Pump. For example, you can download Data Pump files from Amazon S3 to your RDS for Oracle DB instance. For more information, see [Importing data into Oracle on Amazon RDS](Oracle.Procedural.Importing.md).

**Note**
Your DB instance and your Amazon S3 bucket must be in the same AWS Region.

**Topics**
+ [Configuring IAM permissions for RDS for Oracle integration with Amazon S3](oracle-s3-integration.preparing.md)
+ [Adding the Amazon S3 integration option](oracle-s3-integration.preparing.option-group.md)
+ [Transferring files between Amazon RDS for Oracle and an Amazon S3 bucket](oracle-s3-integration.using.md)
+ [Troubleshooting Amazon S3 integration](#oracle-s3-integration.troubleshooting)
+ [Removing the Amazon S3 integration option](oracle-s3-integration.removing.md)

## Troubleshooting Amazon S3 integration
<a name="oracle-s3-integration.troubleshooting"></a>

For troubleshooting tips, see the AWS re:Post article [How do troubleshoot issues when I integrate Amazon RDS for Oracle with Amazon S3?](https://repost.aws/en/knowledge-center/rds-oracle-s3-integration).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon RDS. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AmazonRDS` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
