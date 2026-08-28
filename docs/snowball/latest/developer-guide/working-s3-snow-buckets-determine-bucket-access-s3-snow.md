---
source_url: https://docs.aws.amazon.com/snowball/latest/developer-guide/working-s3-snow-buckets-determine-bucket-access-s3-snow.html
---

AWS Snowball Edge is no longer available to new customers. New customers should explore [AWS DataSync](https://aws.amazon.com/datasync/) for online transfers, [AWS Data Transfer Terminal](https://aws.amazon.com/data-transfer-terminal/) for secure physical transfers, or AWS Partner solutions. For edge computing, explore [AWS Outposts](https://aws.amazon.com/outposts/).

# Determining whether you can access an Amazon S3 compatible storage on Snowball Edge bucket on a Snowball Edge
<a name="working-s3-snow-buckets-determine-bucket-access-s3-snow"></a>

The following example uses the `head-bucket` command to determine if an Amazon S3 bucket exists and you have permissions to access it using the AWS CLI. To use this command, replace each user input placeholder with your own information.

```
aws s3api head-bucket --bucket {{sample-bucket}} --endpoint-url https://{{s3api-endpoint-ip}} --profile {{your-profile}}
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Snowball Edge. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query snowball` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
