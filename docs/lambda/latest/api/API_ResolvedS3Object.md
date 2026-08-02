---
source_url: https://docs.aws.amazon.com/lambda/latest/api/API_ResolvedS3Object.html
---

# ResolvedS3Object
<a name="API_ResolvedS3Object"></a>

Details about the resolved Amazon S3 object that contains a function's deployment package.

## Contents
<a name="API_ResolvedS3Object_Contents"></a>

 ** S3Bucket **   <a name="lambda-Type-ResolvedS3Object-S3Bucket"></a>
The Amazon S3 bucket that contains the deployment package.
Type: String
Length Constraints: Minimum length of 3. Maximum length of 63.
Pattern: `[0-9A-Za-z\.\-_]*(?<!\.)`
Required: No

 ** S3Key **   <a name="lambda-Type-ResolvedS3Object-S3Key"></a>
The Amazon S3 key of the deployment package.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Required: No

 ** S3ObjectVersion **   <a name="lambda-Type-ResolvedS3Object-S3ObjectVersion"></a>
The version of the deployment package object.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Required: No

## See Also
<a name="API_ResolvedS3Object_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/lambda-2015-03-31/ResolvedS3Object)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/lambda-2015-03-31/ResolvedS3Object)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/lambda-2015-03-31/ResolvedS3Object)
