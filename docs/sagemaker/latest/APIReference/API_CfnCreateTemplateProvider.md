---
source_url: https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_CfnCreateTemplateProvider.html
---

# CfnCreateTemplateProvider
<a name="API_CfnCreateTemplateProvider"></a>

 The CloudFormation template provider configuration for creating infrastructure resources.

## Contents
<a name="API_CfnCreateTemplateProvider_Contents"></a>

 ** TemplateName **   <a name="sagemaker-Type-CfnCreateTemplateProvider-TemplateName"></a>
 A unique identifier for the template within the project.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 32.
Pattern: `(?=.{1,32}$)[a-zA-Z0-9](-*[a-zA-Z0-9])*`
Required: Yes

 ** TemplateURL **   <a name="sagemaker-Type-CfnCreateTemplateProvider-TemplateURL"></a>
 The Amazon S3 URL of the CloudFormation template.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Pattern: `(?=.{1,1024}$)(https)://([^/]+)/(.+)`
Required: Yes

 ** Parameters **   <a name="sagemaker-Type-CfnCreateTemplateProvider-Parameters"></a>
 An array of CloudFormation stack parameters.
Type: Array of [CfnStackCreateParameter](API_CfnStackCreateParameter.md) objects
Array Members: Minimum number of 0 items. Maximum number of 180 items.
Required: No

 ** RoleARN **   <a name="sagemaker-Type-CfnCreateTemplateProvider-RoleARN"></a>
 The IAM role that CloudFormation assumes when creating the stack.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `arn:aws[a-z\-]*:iam::\d{12}:role/?[a-zA-Z_0-9+=,.@\-_/]+`
Required: No

## See Also
<a name="API_CfnCreateTemplateProvider_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sagemaker-2017-07-24/CfnCreateTemplateProvider)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sagemaker-2017-07-24/CfnCreateTemplateProvider)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sagemaker-2017-07-24/CfnCreateTemplateProvider)
