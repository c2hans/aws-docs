---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/oracle-dump-files-aws/copy-to-amazon-s3.html
---

# Transferring Oracle Database dump files to Amazon S3
<a name="copy-to-amazon-s3"></a>

[Amazon S3](https://docs.aws.amazon.com/AmazonS3/latest/userguide/) is an object storage service designed for scalability, security, and performance. When you use Amazon S3, you can store and retrieve any amount of data from anywhere at any time.

|
|
| Note: When you store data in an S3 bucket, you can help protect data at rest by using server-side encryption or client-side encryption. For more information about protecting data in Amazon S3, see [Protecting data with encryption](https://docs.aws.amazon.com/AmazonS3/latest/userguide/UsingEncryption.html) in the Amazon S3 documentation. |
| --- |

## AWS CLI setup
<a name="aws-cli-setup"></a>

To use [Amazon S3](https://docs.aws.amazon.com/AmazonS3/latest/userguide/) as a target for transferring the Oracle Database dump files, you must configure the AWS Command Line Interface (AWS CLI) on the source server. For information about how to install and configure the AWS CLI, see [Getting started with the AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-getting-started.html) in the AWS CLI documentation.

After you configure the AWS CLI, run the following commands on the source server to validate the configuration:
+ **Windows machine** – At the command prompt, run `aws --version`. If the setup is successful, the command displays the installed version of the AWS CLI.
+ **Linux machine** – At the shell prompt, run `aws --version`. If the setup is successful, the command displays the installed version of the AWS CLI.

## Copy the source Oracle Database dump files to Amazon S3
<a name="copy-to-s3"></a>

After successful validation of the AWS CLI, you can start copying the source Oracle Database dump files to Amazon S3 by following the instructions in the [AWS documentation](https://docs.aws.amazon.com/cli/latest/userguide/cli-services-s3-commands.html).

## Download the Oracle Database dump files to target systems
<a name="download-dump-files"></a>

The process for transferring the dump files from Amazon S3 differs depending on the target that you are using:
+ [Amazon RDS for Oracle](amazon-rds-target.md)
+ [Amazon EC2](amazon-ec2-target.md)
