---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/rehost-db2-database-on-aws/prerequisites.html
---

# Pre-migration preparation
<a name="prerequisites"></a>

The migration options that are covered in this guide require the following setup activities before you begin the migration:

1. Install Db2 on Amazon EC2 and create an instance.

1. Connect the on-premises network and AWS through a virtual private network connection (VPN) using [AWS Site-to-Site VPN](https://docs.aws.amazon.com/vpn/latest/s2svpn/VPC_VPN.html) or through [AWS Direct Connect](https://docs.aws.amazon.com/directconnect/latest/UserGuide/Welcome.html).

1. Use [Amazon Simple Storage Service (Amazon S3)](https://docs.aws.amazon.com/AmazonS3/latest/userguide/Welcome.html), and provide access to an S3 bucket from Amazon EC2 and the on-premises server.

   Configure Db2 [storage access](https://www.ibm.com/docs/en/db2/11.5?topic=commands-catalog-storage-access), and use the DB2REMOTE identifier to connect Amazon EC2 to Amazon S3.

1. Set up [AWS Command Line Interface (AWS CLI)](https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-welcome.html) on Db2 servers on premises and on Amazon EC2.

1. Create an [AWS Identity and Access Management (IAM)](https://docs.aws.amazon.com/IAM/latest/UserGuide/introduction.html) user to send Db2 backup images and transaction logs to Amazon S3 from the on-premises server.

|
|
| Warning: This scenario requires IAM users with programmatic access and long-term credentials, which presents a security risk. To help mitigate this risk, we recommend that you provide these users with only the permissions they require to perform the task and that you remove these users after the AWS migration is completed. Access keys can be updated if necessary. For more information, see [Updating access keys](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_access-keys.html#Using_RotateAccessKey) in the *IAM user guide*. |
| --- |

## Tools used
<a name="tools-used"></a>
+ **AWS CLI** – Use the `aws s3 cp` or `aws s3 sync` command to send files from the on-premises server to the S3 bucket. You will use the same commands to retrieve the files from the S3 bucket to Amazon EC2.
  + For the little-endian platform, these files are Db2 backup images and transaction logs.
  + For the big-endian platform, these are data files unloaded from user tables.
+ **Db2 command line processor** – The `CATALOG STORAGE ACCESS` command creates an alias for accessing Amazon S3 directly by using the `INGEST`, `LOAD`, `BACKUP DATABASE`, `RESTORE DATABASE`, and `ROLLFORWARD DATABASE` commands.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Prescriptive Guidance. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prescriptive-guidance` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
