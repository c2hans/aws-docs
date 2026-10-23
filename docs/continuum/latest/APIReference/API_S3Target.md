---
source_url: https://docs.aws.amazon.com/continuum/latest/APIReference/API_S3Target.html
---

# S3Target
<a name="API_S3Target"></a>

The s3 Target.

## Contents
<a name="API_S3Target_Contents"></a>

 ** bucket **   <a name="continuum-Type-S3Target-bucket"></a>
The bucket.
Type: String
Length Constraints: Minimum length of 3. Maximum length of 63.
Pattern: `[a-z0-9][a-z0-9.\-]{1,61}[a-z0-9]`
Required: Yes

 ** key **   <a name="continuum-Type-S3Target-key"></a>
The key.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Required: Yes

 ** version **   <a name="continuum-Type-S3Target-version"></a>
The version.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Required: No

## See Also
<a name="API_S3Target_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/continuum-2022-07-26/S3Target)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/continuum-2022-07-26/S3Target)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/continuum-2022-07-26/S3Target)
