---
source_url: https://docs.aws.amazon.com/transfer/latest/APIReference/API_IdentityCenterConfig.html
---

# IdentityCenterConfig
<a name="API_IdentityCenterConfig"></a>

A structure that describes the values to use for the IAM Identity Center settings when you create or update a web app.

## Contents
<a name="API_IdentityCenterConfig_Contents"></a>

 ** InstanceArn **   <a name="TransferFamily-Type-IdentityCenterConfig-InstanceArn"></a>
The Amazon Resource Name (ARN) for the IAM Identity Center used for the web app.
Type: String
Length Constraints: Minimum length of 10. Maximum length of 1224.
Pattern: `arn:[\w-]+:sso:::instance/(sso)?ins-[a-zA-Z0-9-.]{16}`
Required: No

 ** Role **   <a name="TransferFamily-Type-IdentityCenterConfig-Role"></a>
The IAM role in IAM Identity Center used for the web app.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `arn:.*role/\S+`
Required: No

## See Also
<a name="API_IdentityCenterConfig_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/transfer-2018-11-05/IdentityCenterConfig)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/transfer-2018-11-05/IdentityCenterConfig)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/transfer-2018-11-05/IdentityCenterConfig)
