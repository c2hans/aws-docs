---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/aws-startup-security-baseline/acct-07.html
---

# ACCT.07 Deliver CloudTrail logs to a protected Amazon S3 bucket
<a name="acct-07"></a>

Actions taken by users, roles, and services in your AWS account are recorded as events in AWS CloudTrail. CloudTrail is enabled by default, and in the CloudTrail console, you can access 90 days of event history information. To view, search, download, archive, analyze, and respond to account activity across your AWS infrastructure, see [Viewing events with CloudTrail event history](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/view-cloudtrail-events.html) in theCloudTrail documentation.

To retain CloudTrail history beyond 90 days, create a trail that delivers log files to an Amazon Simple Storage Service (Amazon S3) bucket for all event types. When you create a trail in the CloudTrail console, you create a multi-Region trail.

**To create a trail that delivers logs for all AWS Regions to an Amazon S3 bucket**

1. Open the [CloudTrail console](https://console.aws.amazon.com/cloudtrail/).

1. Follow the steps in [Creating a trail](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-create-a-trail-using-the-console-first-time.html) in the CloudTrail documentation. On the **Choose log events **page, do the following:

   1. For **API activity**, select both **Read** and **Write**.

   1. For the **Exclude AWS KMS events **option, use the following guidance:
      + For preproduction environments, select **Exclude AWS KMS events **to exclude all AWS Key Management Service (AWS KMS) events from your trail. AWS KMS read actions such as `Encrypt`, `Decrypt`, and `GenerateDataKey` can generate a large volume of events.
      + For production environments, select **Write** for management events, and clear the **Read **and **Exclude AWS KMS events **check boxes. This excludes high-volume AWS KMS read events but still logs relevant AWS KMS actions, such as `Disable`, `Delete`, and `ScheduleKey`.

   1. If you do not plan to use the Amazon Relational Database Service (Amazon RDS) Data API and want to use CloudTrail for troubleshooting and data access auditing purposes, select **Exclude Amazon RDS Data API events**. The Data API can generate a high volume of CloudTrail events.

After you create the trail, it appears on the **Trails** page. CloudTrail begins publishing log files to the Amazon S3 bucket you specified within approximately 15 minutes.

**Note**
As a cost consideration, you can deliver one copy of your ongoing management events to your Amazon S3 bucket at no charge from CloudTrail by creating a trail. Amazon S3 storage charges apply. For information about Amazon S3 pricing, see [Amazon S3 pricing](https://aws.amazon.com/s3/pricing/).

**To help secure the Amazon S3 buckets where you store CloudTrail log files**

1. Review the [Amazon S3 bucket policy](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/create-s3-bucket-policy-for-cloudtrail.html) in the CloudTrail documentation for each bucket where you store log files, and adjust it as needed to remove unnecessary access.

1. Make sure to add an `aws:SourceArn` condition key to the bucket policy. For more information, see [Create or update an Amazon S3 bucket for an organization trail](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-create-and-update-an-organizational-trail-by-using-the-aws-cli.html) in the CloudTrail documentation.

1. To add an additional layer of protection against accidental or unauthorized deletion of log files, see [Configuring MFA delete](https://docs.aws.amazon.com/AmazonS3/latest/userguide/MultiFactorAuthenticationDelete.html) in the Amazon S3 documentation.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Prescriptive Guidance. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prescriptive-guidance` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
