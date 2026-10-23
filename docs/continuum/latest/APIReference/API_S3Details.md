---
source_url: https://docs.aws.amazon.com/continuum/latest/APIReference/API_S3Details.html
---

# S3Details
<a name="API_S3Details"></a>

Public details for a customer-managed S3 integration. The sensitive external ID is intentionally omitted.

## Contents
<a name="API_S3Details_Contents"></a>

 ** bucket **   <a name="continuum-Type-S3Details-bucket"></a>
The bucket.
Type: String
Length Constraints: Minimum length of 3. Maximum length of 63.
Pattern: `[a-z0-9][a-z0-9.\-]{1,61}[a-z0-9]`
Required: Yes

 ** roleArn **   <a name="continuum-Type-S3Details-roleArn"></a>
The Amazon Resource Name (ARN) of the role.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1011.
Pattern: `arn:[a-z0-9-]+:iam::[0-9]{12}:role/[a-zA-Z0-9_+=,.@/-]+`
Required: Yes

## See Also
<a name="API_S3Details_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/continuum-2022-07-26/S3Details)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/continuum-2022-07-26/S3Details)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/continuum-2022-07-26/S3Details)
