---
source_url: https://docs.aws.amazon.com/mpa/latest/APIReference/API_IamIdentityCenter.html
---

# IamIdentityCenter
<a name="API_IamIdentityCenter"></a>

 AWS IAM Identity Center credentials. For more information see, [AWS IAM Identity Center](http://aws.amazon.com/identity-center/) .

## Contents
<a name="API_IamIdentityCenter_Contents"></a>

 ** InstanceArn **   <a name="mpa-Type-IamIdentityCenter-InstanceArn"></a>
Amazon Resource Name (ARN) for the IAM Identity Center instance.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `arn:.+:sso:::instance/(?:sso)?ins-[a-zA-Z0-9-.]{16}`
Required: Yes

 ** Region **   <a name="mpa-Type-IamIdentityCenter-Region"></a>
 AWS Region where the IAM Identity Center instance is located.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1000.
Required: Yes

## See Also
<a name="API_IamIdentityCenter_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/mpa-2022-07-26/IamIdentityCenter)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/mpa-2022-07-26/IamIdentityCenter)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/mpa-2022-07-26/IamIdentityCenter)
