---
source_url: https://docs.aws.amazon.com/solutions/latest/dynamic-image-transformation-for-amazon-cloudfront/opt-in-regions.html
---

# Opt-in Regions
<a name="opt-in-regions"></a>

An opt-in Region is an AWS Region that’s deactivated by default. You can activate opt-in Regions in the AWS console. For additional information about opt-in Regions and how to activate them, refer to [Managing AWS Regions](https://docs.aws.amazon.com/general/latest/gr/rande-manage.html) in the *AWS General Reference guide*.

This solution supports four opt-in Regions:
+ Asia Pacific (Hong Kong)
+ Middle East (Bahrain)
+ Africa (Cape Town)
+ Europe (Milan)

  When launched in an opt-in Region, this solution creates an S3 logging bucket for CloudFront in the US East (N. Virginia) Region. This is because CloudFront doesn’t deliver access logs to buckets in the supported opt-in Regions. For more information about S3 buckets, refer to [Choosing an Amazon S3 bucket for your standard logs](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/AccessLogs.html#access-logs-choosing-s3-bucket) in the *Amazon CloudFront Developer Guide*.

To deploy in an opt-in Region, the S3 bucket(s) that you provide for the **Source Buckets** parameter must be in the same Region where you launch the CloudFormation template.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Dynamic Image Transformation for Amazon CloudFront. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query solutions` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
