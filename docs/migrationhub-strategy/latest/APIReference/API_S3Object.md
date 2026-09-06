---
source_url: https://docs.aws.amazon.com/migrationhub-strategy/latest/APIReference/API_S3Object.html
---

# S3Object
<a name="API_S3Object"></a>

 Contains the S3 bucket name and the Amazon S3 key name.

## Contents
<a name="API_S3Object_Contents"></a>

 ** s3Bucket **   <a name="migrationhubstrategy-Type-S3Object-s3Bucket"></a>
 The S3 bucket name.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 63.
Pattern: `.*[0-9a-z]+[0-9a-z\.\-]*[0-9a-z]+.*`
Required: No

 ** s3key **   <a name="migrationhubstrategy-Type-S3Object-s3key"></a>
 The Amazon S3 key name.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1024.
Pattern: `.*\S.*`
Required: No

## See Also
<a name="API_S3Object_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/migrationhubstrategy-2020-02-19/S3Object)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/migrationhubstrategy-2020-02-19/S3Object)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/migrationhubstrategy-2020-02-19/S3Object)
