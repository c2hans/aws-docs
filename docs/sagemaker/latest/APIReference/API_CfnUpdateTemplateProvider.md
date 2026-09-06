---
source_url: https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_CfnUpdateTemplateProvider.html
---

# CfnUpdateTemplateProvider
<a name="API_CfnUpdateTemplateProvider"></a>

 Contains configuration details for updating an existing CloudFormation template provider in the project.

## Contents
<a name="API_CfnUpdateTemplateProvider_Contents"></a>

 ** TemplateName **   <a name="sagemaker-Type-CfnUpdateTemplateProvider-TemplateName"></a>
 The unique identifier of the template to update within the project.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 32.
Pattern: `(?=.{1,32}$)[a-zA-Z0-9](-*[a-zA-Z0-9])*`
Required: Yes

 ** TemplateURL **   <a name="sagemaker-Type-CfnUpdateTemplateProvider-TemplateURL"></a>
 The Amazon S3 URL of the CloudFormation template.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Pattern: `(?=.{1,1024}$)(https)://([^/]+)/(.+)`
Required: Yes

 ** Parameters **   <a name="sagemaker-Type-CfnUpdateTemplateProvider-Parameters"></a>
 An array of CloudFormation stack parameters.
Type: Array of [CfnStackUpdateParameter](API_CfnStackUpdateParameter.md) objects
Array Members: Minimum number of 0 items. Maximum number of 180 items.
Required: No

## See Also
<a name="API_CfnUpdateTemplateProvider_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sagemaker-2017-07-24/CfnUpdateTemplateProvider)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sagemaker-2017-07-24/CfnUpdateTemplateProvider)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sagemaker-2017-07-24/CfnUpdateTemplateProvider)
