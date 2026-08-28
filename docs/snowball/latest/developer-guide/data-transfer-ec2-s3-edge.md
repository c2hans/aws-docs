---
source_url: https://docs.aws.amazon.com/snowball/latest/developer-guide/data-transfer-ec2-s3-edge.html
---

AWS Snowball Edge is no longer available to new customers. New customers should explore [AWS DataSync](https://aws.amazon.com/datasync/) for online transfers, [AWS Data Transfer Terminal](https://aws.amazon.com/data-transfer-terminal/) for secure physical transfers, or AWS Partner solutions. For edge computing, explore [AWS Outposts](https://aws.amazon.com/outposts/).

# Transferring data from EC2-compatible compute instances to S3 buckets on the same Snowball Edge
<a name="data-transfer-ec2-s3-edge"></a>

You can transfer data between compute instances and Amazon S3 buckets on the same Snowball Edge device. You do this by using the supported AWS CLI commands and the appropriate endpoints. For example, assume that you want to move data from a directory in my `sbe1.xlarge` instance into the Amazon S3 bucket, `amzn-s3-demo-bucket` on the same device. Assume that you're using the Amazon S3 compatible storage on Snowball Edge endpoint `https://S3-object-API-endpoint:443`. You use the following procedure.

**To transfer data between a compute instance and a bucket on the same Snowball Edge**

1. Use SSH to connect to your compute instance.

1. Download and install the AWS CLI. If your instance doesn't already have the AWS CLI, download and install it. For more information, see [Installing the AWS Command Line Interface](https://docs.aws.amazon.com/cli/latest/userguide/installing.html).

1. Configure the AWS CLI on your compute instance to work with the Amazon S3 endpoint on the Snowball Edge. For more information, see [Getting and using local Amazon S3 credentials on Snowball Edge](using-adapter.md#adapter-credentials).

1. Use the supported Amazon S3 compatible storage on Snowball Edge commands to transfer data. For example:

   ```
   aws s3 cp ~/june2018/results s3://amzn-s3-demo-bucket/june2018/results --recursive --endpoint https://S3-object-API-endpoint:443
   ```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Snowball Edge. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query snowball` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
