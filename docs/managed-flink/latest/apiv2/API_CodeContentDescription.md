---
source_url: https://docs.aws.amazon.com/managed-flink/latest/apiv2/API_CodeContentDescription.html
---

# CodeContentDescription
<a name="API_CodeContentDescription"></a>

Describes details about the code of a Managed Service for Apache Flink application.

## Contents
<a name="API_CodeContentDescription_Contents"></a>

 ** CodeMD5 **   <a name="APIReference-Type-CodeContentDescription-CodeMD5"></a>
The checksum that can be used to validate zip-format code.
Type: String
Length Constraints: Fixed length of 128.
Required: No

 ** CodeSize **   <a name="APIReference-Type-CodeContentDescription-CodeSize"></a>
The size in bytes of the application code. Can be used to validate zip-format code.
Type: Long
Valid Range: Minimum value of 0. Maximum value of 52428800.
Required: No

 ** S3ApplicationCodeLocationDescription **   <a name="APIReference-Type-CodeContentDescription-S3ApplicationCodeLocationDescription"></a>
The S3 bucket Amazon Resource Name (ARN), file key, and object version of the application code stored in Amazon S3.
Type: [S3ApplicationCodeLocationDescription](API_S3ApplicationCodeLocationDescription.md) object
Required: No

 ** TextContent **   <a name="APIReference-Type-CodeContentDescription-TextContent"></a>
The text-format code
Type: String
Length Constraints: Minimum length of 0. Maximum length of 102400.
Required: No

## See Also
<a name="API_CodeContentDescription_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/kinesisanalyticsv2-2018-05-23/CodeContentDescription)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/kinesisanalyticsv2-2018-05-23/CodeContentDescription)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/kinesisanalyticsv2-2018-05-23/CodeContentDescription)
