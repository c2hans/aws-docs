---
source_url: https://docs.aws.amazon.com/signer/latest/developerguide/s3-destination-iot.html
---

# Create an Amazon S3 destination bucket for your signed object files
<a name="s3-destination-iot"></a>

This topic discusses how to prepare an Amazon S3 destination bucket where AWS Signer can deposit your signed object files.

To create a bucket, sign into the AWS Management Console at [https://console.aws.amazon.com/console/home](https://console.aws.amazon.com/console/home) and follow the procedure in [Create your first S3 bucket](https://docs.aws.amazon.com/AmazonS3/latest/userguide/creating-bucket.html).

While you are configuring the bucket, note the following requirement.
+ Accept the default security option **Block *all* public access**.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Signer. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query signer` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
