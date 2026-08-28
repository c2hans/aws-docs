---
source_url: https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_CfnTemplateProviderDetail.html
---

# CfnTemplateProviderDetail
<a name="API_CfnTemplateProviderDetail"></a>

 Details about a CloudFormation template provider configuration and associated provisioning information.

## Contents
<a name="API_CfnTemplateProviderDetail_Contents"></a>

 ** TemplateName **   <a name="sagemaker-Type-CfnTemplateProviderDetail-TemplateName"></a>
 The unique identifier of the template within the project.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 32.
Pattern: `(?=.{1,32}$)[a-zA-Z0-9](-*[a-zA-Z0-9])*`
Required: Yes

 ** TemplateURL **   <a name="sagemaker-Type-CfnTemplateProviderDetail-TemplateURL"></a>
 The Amazon S3 URL of the CloudFormation template.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Pattern: `(?=.{1,1024}$)(https)://([^/]+)/(.+)`
Required: Yes

 ** Parameters **   <a name="sagemaker-Type-CfnTemplateProviderDetail-Parameters"></a>
 An array of CloudFormation stack parameters.
Type: Array of [CfnStackParameter](API_CfnStackParameter.md) objects
Array Members: Minimum number of 0 items. Maximum number of 180 items.
Required: No

 ** RoleARN **   <a name="sagemaker-Type-CfnTemplateProviderDetail-RoleARN"></a>
 The IAM role used by CloudFormation to create the stack.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `arn:aws[a-z\-]*:iam::\d{12}:role/?[a-zA-Z_0-9+=,.@\-_/]+`
Required: No

 ** StackDetail **   <a name="sagemaker-Type-CfnTemplateProviderDetail-StackDetail"></a>
 Information about the CloudFormation stack created by the template provider.
Type: [CfnStackDetail](API_CfnStackDetail.md) object
Required: No

## See Also
<a name="API_CfnTemplateProviderDetail_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sagemaker-2017-07-24/CfnTemplateProviderDetail)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sagemaker-2017-07-24/CfnTemplateProviderDetail)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sagemaker-2017-07-24/CfnTemplateProviderDetail)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon SageMaker. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query sagemaker` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
