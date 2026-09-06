---
source_url: https://docs.aws.amazon.com/transfer/latest/APIReference/API_DescribedIdentityCenterConfig.html
---

# DescribedIdentityCenterConfig
<a name="API_DescribedIdentityCenterConfig"></a>

A structure that contains the details of the IAM Identity Center used for your web app. Returned during a call to `DescribeWebApp`.

## Contents
<a name="API_DescribedIdentityCenterConfig_Contents"></a>

 ** ApplicationArn **   <a name="TransferFamily-Type-DescribedIdentityCenterConfig-ApplicationArn"></a>
The Amazon Resource Name (ARN) for the IAM Identity Center application: this value is set automatically when you create your web app.
Type: String
Length Constraints: Minimum length of 10. Maximum length of 1224.
Pattern: `arn:[\w-]+:sso::\d{12}:application/(sso)?ins-[a-zA-Z0-9-.]{16}/apl-[a-zA-Z0-9]{16}`
Required: No

 ** InstanceArn **   <a name="TransferFamily-Type-DescribedIdentityCenterConfig-InstanceArn"></a>
The Amazon Resource Name (ARN) for the IAM Identity Center used for the web app.
Type: String
Length Constraints: Minimum length of 10. Maximum length of 1224.
Pattern: `arn:[\w-]+:sso:::instance/(sso)?ins-[a-zA-Z0-9-.]{16}`
Required: No

 ** Role **   <a name="TransferFamily-Type-DescribedIdentityCenterConfig-Role"></a>
The IAM role in IAM Identity Center used for the web app.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `arn:.*role/\S+`
Required: No

## See Also
<a name="API_DescribedIdentityCenterConfig_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/transfer-2018-11-05/DescribedIdentityCenterConfig)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/transfer-2018-11-05/DescribedIdentityCenterConfig)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/transfer-2018-11-05/DescribedIdentityCenterConfig)
