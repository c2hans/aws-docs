---
source_url: https://docs.aws.amazon.com/mwaa-serverless/latest/APIReference/API_S3Location.html
---

# S3Location
<a name="API_S3Location"></a>

Specifies the Amazon S3 location of code artifacts that workflows use during execution.

## Contents
<a name="API_S3Location_Contents"></a>

 ** Bucket **   <a name="mwaaserverless-Type-S3Location-Bucket"></a>
The name of the Amazon S3 bucket.
Type: String
Length Constraints: Minimum length of 3. Maximum length of 63.
Required: Yes

 ** ObjectKey **   <a name="mwaaserverless-Type-S3Location-ObjectKey"></a>
The key of the code artifact within the Amazon S3 bucket.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Required: Yes

 ** VersionId **   <a name="mwaaserverless-Type-S3Location-VersionId"></a>
The version ID of the object in Amazon S3. If not specified, the latest version is used.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Required: No

## See Also
<a name="API_S3Location_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/mwaa-serverless-2024-07-26/S3Location)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/mwaa-serverless-2024-07-26/S3Location)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/mwaa-serverless-2024-07-26/S3Location)
