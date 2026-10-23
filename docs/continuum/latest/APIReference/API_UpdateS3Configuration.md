---
source_url: https://docs.aws.amazon.com/continuum/latest/APIReference/API_UpdateS3Configuration.html
---

# UpdateS3Configuration
<a name="API_UpdateS3Configuration"></a>

Replacement credentials for a customer-managed S3 integration. The bucket cannot be changed.

## Contents
<a name="API_UpdateS3Configuration_Contents"></a>

 ** roleArn **   <a name="continuum-Type-UpdateS3Configuration-roleArn"></a>
The Amazon Resource Name (ARN) of the role.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1011.
Pattern: `arn:[a-z0-9-]+:iam::[0-9]{12}:role/[a-zA-Z0-9_+=,.@/-]+`
Required: Yes

 ** externalId **   <a name="continuum-Type-UpdateS3Configuration-externalId"></a>
The identifier of the external.
Type: String
Length Constraints: Minimum length of 2. Maximum length of 1224.
Pattern: `[\w+=,.@:\/-]+`
Required: No

## See Also
<a name="API_UpdateS3Configuration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/continuum-2022-07-26/UpdateS3Configuration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/continuum-2022-07-26/UpdateS3Configuration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/continuum-2022-07-26/UpdateS3Configuration)
