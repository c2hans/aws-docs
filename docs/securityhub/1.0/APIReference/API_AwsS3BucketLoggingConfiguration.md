---
source_url: https://docs.aws.amazon.com/securityhub/1.0/APIReference/API_AwsS3BucketLoggingConfiguration.html
---

# AwsS3BucketLoggingConfiguration
<a name="API_AwsS3BucketLoggingConfiguration"></a>

Information about logging for the S3 bucket

## Contents
<a name="API_AwsS3BucketLoggingConfiguration_Contents"></a>

 ** DestinationBucketName **   <a name="securityhub-Type-AwsS3BucketLoggingConfiguration-DestinationBucketName"></a>
The name of the S3 bucket where log files for the S3 bucket are stored.
Type: String
Pattern: `.*\S.*`
Required: No

 ** LogFilePrefix **   <a name="securityhub-Type-AwsS3BucketLoggingConfiguration-LogFilePrefix"></a>
The prefix added to log files for the S3 bucket.
Type: String
Pattern: `.*\S.*`
Required: No

## See Also
<a name="API_AwsS3BucketLoggingConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/securityhub-2018-10-26/AwsS3BucketLoggingConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/securityhub-2018-10-26/AwsS3BucketLoggingConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/securityhub-2018-10-26/AwsS3BucketLoggingConfiguration)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Security Hub. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query securityhub` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
