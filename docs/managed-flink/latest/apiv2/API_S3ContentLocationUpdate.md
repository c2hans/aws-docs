---
source_url: https://docs.aws.amazon.com/managed-flink/latest/apiv2/API_S3ContentLocationUpdate.html
---

# S3ContentLocationUpdate
<a name="API_S3ContentLocationUpdate"></a>

Describes an update for the Amazon S3 code content location for an application.

## Contents
<a name="API_S3ContentLocationUpdate_Contents"></a>

 ** BucketARNUpdate **   <a name="APIReference-Type-S3ContentLocationUpdate-BucketARNUpdate"></a>
The new Amazon Resource Name (ARN) for the S3 bucket containing the application code.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Pattern: `arn:.*`
Required: No

 ** FileKeyUpdate **   <a name="APIReference-Type-S3ContentLocationUpdate-FileKeyUpdate"></a>
The new file key for the object containing the application code.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Required: No

 ** ObjectVersionUpdate **   <a name="APIReference-Type-S3ContentLocationUpdate-ObjectVersionUpdate"></a>
The new version of the object containing the application code.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1024.
Required: No

## See Also
<a name="API_S3ContentLocationUpdate_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/kinesisanalyticsv2-2018-05-23/S3ContentLocationUpdate)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/kinesisanalyticsv2-2018-05-23/S3ContentLocationUpdate)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/kinesisanalyticsv2-2018-05-23/S3ContentLocationUpdate)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Managed Service for Apache Flink (formerly Amazon Kinesis Data Analytics for Apache Flink). To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query managed-flink` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
