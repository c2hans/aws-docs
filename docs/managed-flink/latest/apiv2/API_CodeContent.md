---
source_url: https://docs.aws.amazon.com/managed-flink/latest/apiv2/API_CodeContent.html
---

# CodeContent
<a name="API_CodeContent"></a>

Specifies either the application code, or the location of the application code, for a Managed Service for Apache Flink application.

## Contents
<a name="API_CodeContent_Contents"></a>

 ** S3ContentLocation **   <a name="APIReference-Type-CodeContent-S3ContentLocation"></a>
Information about the Amazon S3 bucket that contains the application code.
Type: [S3ContentLocation](API_S3ContentLocation.md) object
Required: No

 ** TextContent **   <a name="APIReference-Type-CodeContent-TextContent"></a>
The text-format code for a Managed Service for Apache Flink application.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 102400.
Required: No

 ** ZipFileContent **   <a name="APIReference-Type-CodeContent-ZipFileContent"></a>
The zip-format code for a Managed Service for Apache Flink application.
Type: Base64-encoded binary data object
Length Constraints: Minimum length of 0. Maximum length of 52428800.
Required: No

## See Also
<a name="API_CodeContent_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/kinesisanalyticsv2-2018-05-23/CodeContent)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/kinesisanalyticsv2-2018-05-23/CodeContent)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/kinesisanalyticsv2-2018-05-23/CodeContent)
