---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/APIReference/API_UpdateGeneratedTemplate.html
---

# UpdateGeneratedTemplate
<a name="API_UpdateGeneratedTemplate"></a>

Updates a generated template. This can be used to change the name, add and remove resources, refresh resources, and change the `DeletionPolicy` and `UpdateReplacePolicy` settings. You can check the status of the update to the generated template using the `DescribeGeneratedTemplate` API action.

## Request Parameters
<a name="API_UpdateGeneratedTemplate_RequestParameters"></a>

 For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

 **AddResources.member.N**
An optional list of resources to be added to the generated template.
Type: Array of [ResourceDefinition](API_ResourceDefinition.md) objects
Array Members: Minimum number of 1 item. Maximum number of 500 items.
Required: No

 ** GeneratedTemplateName **
The name or Amazon Resource Name (ARN) of a generated template.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Required: Yes

 ** NewGeneratedTemplateName **
An optional new name to assign to the generated template.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Required: No

 ** RefreshAllResources **
If `true`, update the resource properties in the generated template with their current live state. This feature is useful when the resource properties in your generated a template does not reflect the live state of the resource properties. This happens when a user update the resource properties after generating a template.
Type: Boolean
Required: No

 **RemoveResources.member.N**
A list of logical ids for resources to remove from the generated template.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 500 items.
Required: No

 ** TemplateConfiguration **
The configuration details of the generated template, including the `DeletionPolicy` and `UpdateReplacePolicy`.
Type: [TemplateConfiguration](API_TemplateConfiguration.md) object
Required: No

## Response Elements
<a name="API_UpdateGeneratedTemplate_ResponseElements"></a>

The following element is returned by the service.

 ** GeneratedTemplateId **
The Amazon Resource Name (ARN) of the generated template. The format is `arn:${Partition}:cloudformation:${Region}:${Account}:generatedtemplate/${Id}`. For example, `arn:aws:cloudformation:us-east-1:123456789012:generatedtemplate/2e8465c1-9a80-43ea-a3a3-4f2d692fe6dc `.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.

## Errors
<a name="API_UpdateGeneratedTemplate_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AlreadyExists **
The resource with the name requested already exists.
HTTP Status Code: 400

 ** GeneratedTemplateNotFound **
The generated template was not found.
HTTP Status Code: 404

 ** LimitExceeded **
The quota for the resource has already been reached.
For information about resource and stack limitations, see [CloudFormation quotas](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/cloudformation-limits.html) in the * AWS CloudFormation User Guide*.
HTTP Status Code: 400

## See Also
<a name="API_UpdateGeneratedTemplate_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/cloudformation-2010-05-15/UpdateGeneratedTemplate)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/cloudformation-2010-05-15/UpdateGeneratedTemplate)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/cloudformation-2010-05-15/UpdateGeneratedTemplate)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/cloudformation-2010-05-15/UpdateGeneratedTemplate)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cloudformation-2010-05-15/UpdateGeneratedTemplate)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/cloudformation-2010-05-15/UpdateGeneratedTemplate)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/cloudformation-2010-05-15/UpdateGeneratedTemplate)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/cloudformation-2010-05-15/UpdateGeneratedTemplate)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/cloudformation-2010-05-15/UpdateGeneratedTemplate)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cloudformation-2010-05-15/UpdateGeneratedTemplate)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
