---
source_url: https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_VerifiedAccessLogOptions.html
---

# VerifiedAccessLogOptions
<a name="API_VerifiedAccessLogOptions"></a>

Options for Verified Access logs.

## Contents
<a name="API_VerifiedAccessLogOptions_Contents"></a>

 ** CloudWatchLogs **
Sends Verified Access logs to CloudWatch Logs.
Type: [VerifiedAccessLogCloudWatchLogsDestinationOptions](API_VerifiedAccessLogCloudWatchLogsDestinationOptions.md) object
Required: No

 ** IncludeTrustContext **
Indicates whether to include trust data sent by trust providers in the logs.
Type: Boolean
Required: No

 ** KinesisDataFirehose **
Sends Verified Access logs to Kinesis.
Type: [VerifiedAccessLogKinesisDataFirehoseDestinationOptions](API_VerifiedAccessLogKinesisDataFirehoseDestinationOptions.md) object
Required: No

 ** LogVersion **
The logging version.
Valid values: `ocsf-0.1` \| `ocsf-1.0.0-rc.2`
Type: String
Required: No

 ** S3 **
Sends Verified Access logs to Amazon S3.
Type: [VerifiedAccessLogS3DestinationOptions](API_VerifiedAccessLogS3DestinationOptions.md) object
Required: No

## See Also
<a name="API_VerifiedAccessLogOptions_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ec2-2016-11-15/VerifiedAccessLogOptions)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ec2-2016-11-15/VerifiedAccessLogOptions)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ec2-2016-11-15/VerifiedAccessLogOptions)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon EC2. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSEC2` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
