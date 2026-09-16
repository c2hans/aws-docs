---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/APIReference/API_CreateGeneratedTemplate.html
---

# CreateGeneratedTemplate
<a name="API_CreateGeneratedTemplate"></a>

Creates a template from existing resources that are not already managed with CloudFormation. You can check the status of the template generation using the `DescribeGeneratedTemplate` API action.

## Request Parameters
<a name="API_CreateGeneratedTemplate_RequestParameters"></a>

 For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

 ** GeneratedTemplateName **
The name assigned to the generated template.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Required: Yes

 **Resources.member.N**
An optional list of resources to be included in the generated template.
If no resources are specified,the template will be created without any resources. Resources can be added to the template using the `UpdateGeneratedTemplate` API action.
Type: Array of [ResourceDefinition](API_ResourceDefinition.md) objects
Array Members: Minimum number of 1 item. Maximum number of 500 items.
Required: No

 ** StackName **
An optional name or ARN of a stack to use as the base stack for the generated template.
Type: String
Required: No

 ** TemplateConfiguration **
The configuration details of the generated template, including the `DeletionPolicy` and `UpdateReplacePolicy`.
Type: [TemplateConfiguration](API_TemplateConfiguration.md) object
Required: No

## Response Elements
<a name="API_CreateGeneratedTemplate_ResponseElements"></a>

The following element is returned by the service.

 ** GeneratedTemplateId **
The ID of the generated template.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.

## Errors
<a name="API_CreateGeneratedTemplate_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AlreadyExists **
The resource with the name requested already exists.
HTTP Status Code: 400

 ** ConcurrentResourcesLimitExceeded **
No more than 5 generated templates can be in an `InProgress` or `Pending` status at one time. This error is also returned if a generated template that is in an `InProgress` or `Pending` status is attempted to be updated or deleted.
HTTP Status Code: 429

 ** LimitExceeded **
The quota for the resource has already been reached.
For information about resource and stack limitations, see [CloudFormation quotas](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/cloudformation-limits.html) in the * AWS CloudFormation User Guide*.
HTTP Status Code: 400

## See Also
<a name="API_CreateGeneratedTemplate_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/cloudformation-2010-05-15/CreateGeneratedTemplate)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/cloudformation-2010-05-15/CreateGeneratedTemplate)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/cloudformation-2010-05-15/CreateGeneratedTemplate)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/cloudformation-2010-05-15/CreateGeneratedTemplate)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cloudformation-2010-05-15/CreateGeneratedTemplate)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/cloudformation-2010-05-15/CreateGeneratedTemplate)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/cloudformation-2010-05-15/CreateGeneratedTemplate)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/cloudformation-2010-05-15/CreateGeneratedTemplate)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/cloudformation-2010-05-15/CreateGeneratedTemplate)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cloudformation-2010-05-15/CreateGeneratedTemplate)
