---
source_url: https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_VerifiedAccessLogs.html
---

# VerifiedAccessLogs
<a name="API_VerifiedAccessLogs"></a>

Describes the options for Verified Access logs.

## Contents
<a name="API_VerifiedAccessLogs_Contents"></a>

 ** cloudWatchLogs **
CloudWatch Logs logging destination.
Type: [VerifiedAccessLogCloudWatchLogsDestination](API_VerifiedAccessLogCloudWatchLogsDestination.md) object
Required: No

 ** includeTrustContext **
Indicates whether trust data is included in the logs.
Type: Boolean
Required: No

 ** kinesisDataFirehose **
Kinesis logging destination.
Type: [VerifiedAccessLogKinesisDataFirehoseDestination](API_VerifiedAccessLogKinesisDataFirehoseDestination.md) object
Required: No

 ** logVersion **
The log version.
Type: String
Required: No

 ** s3 **
Amazon S3 logging options.
Type: [VerifiedAccessLogS3Destination](API_VerifiedAccessLogS3Destination.md) object
Required: No

## See Also
<a name="API_VerifiedAccessLogs_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ec2-2016-11-15/VerifiedAccessLogs)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ec2-2016-11-15/VerifiedAccessLogs)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ec2-2016-11-15/VerifiedAccessLogs)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon EC2. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSEC2` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
