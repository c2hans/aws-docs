---
source_url: https://docs.aws.amazon.com/managed-flink/latest/apiv2/API_CodeContentUpdate.html
---

# CodeContentUpdate
<a name="API_CodeContentUpdate"></a>

Describes an update to the code of an application. Not supported for Apache Zeppelin.

## Contents
<a name="API_CodeContentUpdate_Contents"></a>

 ** S3ContentLocationUpdate **   <a name="APIReference-Type-CodeContentUpdate-S3ContentLocationUpdate"></a>
Describes an update to the location of code for an application.
Type: [S3ContentLocationUpdate](API_S3ContentLocationUpdate.md) object
Required: No

 ** TextContentUpdate **   <a name="APIReference-Type-CodeContentUpdate-TextContentUpdate"></a>
Describes an update to the text code for an application.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 102400.
Required: No

 ** ZipFileContentUpdate **   <a name="APIReference-Type-CodeContentUpdate-ZipFileContentUpdate"></a>
Describes an update to the zipped code for an application.
Type: Base64-encoded binary data object
Length Constraints: Minimum length of 0. Maximum length of 52428800.
Required: No

## See Also
<a name="API_CodeContentUpdate_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/kinesisanalyticsv2-2018-05-23/CodeContentUpdate)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/kinesisanalyticsv2-2018-05-23/CodeContentUpdate)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/kinesisanalyticsv2-2018-05-23/CodeContentUpdate)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Managed Service for Apache Flink (formerly Amazon Kinesis Data Analytics for Apache Flink). To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query managed-flink` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
