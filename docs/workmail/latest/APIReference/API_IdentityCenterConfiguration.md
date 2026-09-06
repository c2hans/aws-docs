---
source_url: https://docs.aws.amazon.com/workmail/latest/APIReference/API_IdentityCenterConfiguration.html
---

# IdentityCenterConfiguration
<a name="API_IdentityCenterConfiguration"></a>

**Important**
End of support notice: On March 31, 2027, AWS will end support for Amazon WorkMail. After March 31, 2027, you will no longer be able to access the WorkMail console or WorkMail resources. For more information, see [Amazon WorkMail end of support](https://docs.aws.amazon.com/workmail/latest/adminguide/workmail-end-of-support.html).

 The IAM Identity Center configuration.

## Contents
<a name="API_IdentityCenterConfiguration_Contents"></a>

 ** ApplicationArn **   <a name="workmail-Type-IdentityCenterConfiguration-ApplicationArn"></a>
 The Amazon Resource Name (ARN) of IAMIdentity Center Application for WorkMail. Must be created by the WorkMail API, see CreateIdentityCenterApplication.
Type: String
Length Constraints: Minimum length of 10. Maximum length of 1224.
Pattern: `^arn:(aws|aws-us-gov|aws-cn|aws-iso|aws-iso-b):sso::\d{12}:application/(sso)?ins-[a-zA-Z0-9-.]{16}/apl-[a-zA-Z0-9]{16}$`
Required: Yes

 ** InstanceArn **   <a name="workmail-Type-IdentityCenterConfiguration-InstanceArn"></a>
 The Amazon Resource Name (ARN) of the of IAM Identity Center instance. Must be in the same AWS account and region as WorkMail organization.
Type: String
Length Constraints: Minimum length of 10. Maximum length of 1124.
Pattern: `^arn:(aws|aws-us-gov|aws-cn|aws-iso|aws-iso-b):sso:::instance/(sso)?ins-[a-zA-Z0-9-.]{16}$`
Required: Yes

## See Also
<a name="API_IdentityCenterConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/workmail-2017-10-01/IdentityCenterConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/workmail-2017-10-01/IdentityCenterConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/workmail-2017-10-01/IdentityCenterConfiguration)
