---
source_url: https://docs.aws.amazon.com/securityhub/1.0/APIReference/API_AwsCloudTrailTrailDetails.html
---

# AwsCloudTrailTrailDetails
<a name="API_AwsCloudTrailTrailDetails"></a>

Provides details about a CloudTrail trail.

## Contents
<a name="API_AwsCloudTrailTrailDetails_Contents"></a>

 ** CloudWatchLogsLogGroupArn **   <a name="securityhub-Type-AwsCloudTrailTrailDetails-CloudWatchLogsLogGroupArn"></a>
The ARN of the log group that CloudTrail logs are delivered to.
Type: String
Pattern: `.*\S.*`
Required: No

 ** CloudWatchLogsRoleArn **   <a name="securityhub-Type-AwsCloudTrailTrailDetails-CloudWatchLogsRoleArn"></a>
The ARN of the role that the CloudWatch Events endpoint assumes when it writes to the log group.
Type: String
Pattern: `.*\S.*`
Required: No

 ** HasCustomEventSelectors **   <a name="securityhub-Type-AwsCloudTrailTrailDetails-HasCustomEventSelectors"></a>
Indicates whether the trail has custom event selectors.
Type: Boolean
Required: No

 ** HomeRegion **   <a name="securityhub-Type-AwsCloudTrailTrailDetails-HomeRegion"></a>
The Region where the trail was created.
Type: String
Pattern: `.*\S.*`
Required: No

 ** IncludeGlobalServiceEvents **   <a name="securityhub-Type-AwsCloudTrailTrailDetails-IncludeGlobalServiceEvents"></a>
Indicates whether the trail publishes events from global services such as IAM to the log files.
Type: Boolean
Required: No

 ** IsMultiRegionTrail **   <a name="securityhub-Type-AwsCloudTrailTrailDetails-IsMultiRegionTrail"></a>
Indicates whether the trail applies only to the current Region or to all Regions.
Type: Boolean
Required: No

 ** IsOrganizationTrail **   <a name="securityhub-Type-AwsCloudTrailTrailDetails-IsOrganizationTrail"></a>
Whether the trail is created for all accounts in an organization in AWS Organizations, or only for the current AWS account.
Type: Boolean
Required: No

 ** KmsKeyId **   <a name="securityhub-Type-AwsCloudTrailTrailDetails-KmsKeyId"></a>
The AWS KMS key ID to use to encrypt the logs.
Type: String
Pattern: `.*\S.*`
Required: No

 ** LogFileValidationEnabled **   <a name="securityhub-Type-AwsCloudTrailTrailDetails-LogFileValidationEnabled"></a>
Indicates whether CloudTrail log file validation is enabled.
Type: Boolean
Required: No

 ** Name **   <a name="securityhub-Type-AwsCloudTrailTrailDetails-Name"></a>
The name of the trail.
Type: String
Pattern: `.*\S.*`
Required: No

 ** S3BucketName **   <a name="securityhub-Type-AwsCloudTrailTrailDetails-S3BucketName"></a>
The name of the S3 bucket where the log files are published.
Type: String
Pattern: `.*\S.*`
Required: No

 ** S3KeyPrefix **   <a name="securityhub-Type-AwsCloudTrailTrailDetails-S3KeyPrefix"></a>
The S3 key prefix. The key prefix is added after the name of the S3 bucket where the log files are published.
Type: String
Pattern: `.*\S.*`
Required: No

 ** SnsTopicArn **   <a name="securityhub-Type-AwsCloudTrailTrailDetails-SnsTopicArn"></a>
The ARN of the SNS topic that is used for notifications of log file delivery.
Type: String
Pattern: `.*\S.*`
Required: No

 ** SnsTopicName **   <a name="securityhub-Type-AwsCloudTrailTrailDetails-SnsTopicName"></a>
The name of the SNS topic that is used for notifications of log file delivery.
Type: String
Pattern: `.*\S.*`
Required: No

 ** TrailArn **   <a name="securityhub-Type-AwsCloudTrailTrailDetails-TrailArn"></a>
The ARN of the trail.
Type: String
Pattern: `.*\S.*`
Required: No

## See Also
<a name="API_AwsCloudTrailTrailDetails_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/securityhub-2018-10-26/AwsCloudTrailTrailDetails)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/securityhub-2018-10-26/AwsCloudTrailTrailDetails)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/securityhub-2018-10-26/AwsCloudTrailTrailDetails)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Security Hub. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query securityhub` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
