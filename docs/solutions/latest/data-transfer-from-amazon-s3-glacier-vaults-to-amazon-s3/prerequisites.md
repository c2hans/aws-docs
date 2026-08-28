---
source_url: https://docs.aws.amazon.com/solutions/latest/data-transfer-from-amazon-s3-glacier-vaults-to-amazon-s3/prerequisites.html
---

# Prerequisites
<a name="prerequisites"></a>

Before deployment, ensure that there are no new uploads or deletes of archives occurring on your source Glacier vault. Your Glacier vault content must be static.
+  Ensure you have reviewed the [cost section ](cost.md)before deployment.
+  Create a new destination Amazon S3 bucket. This bucket will be the destination storage location for your Glacier vault archives. For more information, refer to [Creating a bucket](https://docs.aws.amazon.com/AmazonS3/latest/userguide/create-bucket-overview.html) in the Amazon Simple Storage Service User Guide.
  + The new destination Amazon S3 bucket should be in the same Region as the S3 Glacier vault, otherwise an excessive additional cost of "Data Transfer OUT From Amazon S3 Glacier" will be added, see [Data transfer pricing. ](https://aws.amazon.com/s3/glacier/pricing/#Data_transfer_pricing)
**Note**
The destination Amazon S3 bucket must be created in the same account as the Glacier vault, which is also the account where the Guidance is deployed. Currently, the Guidance does not support cross-account transfers.
  + It is advisable to review and modify any Service Control Policies (SCP) on the destination bucket that may block or prevent PUT operations.
  + If you are using CloudTrail on your destination Amazon S3 bucket, please review and modify the CloudTrail export configurations to prevent excessive API charges.
+ Ensure that your account has permissions to deploy the CloudFormation template and create the necessary AWS IAM roles. Your account must have permissions to grant access to the source Glacier vault and destination Amazon S3 bucket.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Data Transfer from Amazon S3 Glacier Vaults to Amazon S3. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query solutions` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
