---
source_url: https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_CreateProject.html
---

# CreateProject
<a name="API_CreateProject"></a>

Creates a machine learning (ML) project that can contain one or more templates that set up an ML pipeline from training to deploying an approved model.

## Request Syntax
<a name="API_CreateProject_RequestSyntax"></a>

```
{
   "ProjectDescription": "{{string}}",
   "ProjectName": "{{string}}",
   "ServiceCatalogProvisioningDetails": {
      "PathId": "{{string}}",
      "ProductId": "{{string}}",
      "ProvisioningArtifactId": "{{string}}",
      "ProvisioningParameters": [
         {
            "Key": "{{string}}",
            "Value": "{{string}}"
         }
      ]
   },
   "Tags": [
      {
         "Key": "{{string}}",
         "Value": "{{string}}"
      }
   ],
   "TemplateProviders": [
      {
         "CfnTemplateProvider": {
            "Parameters": [
               {
                  "Key": "{{string}}",
                  "Value": "{{string}}"
               }
            ],
            "RoleARN": "{{string}}",
            "TemplateName": "{{string}}",
            "TemplateURL": "{{string}}"
         }
      }
   ]
}
```

## Request Parameters
<a name="API_CreateProject_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [ProjectDescription](#API_CreateProject_RequestSyntax) **   <a name="sagemaker-CreateProject-request-ProjectDescription"></a>
A description for the project.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1024.
Pattern: `[\p{L}\p{M}\p{Z}\p{S}\p{N}\p{P}]*`
Required: No

 ** [ProjectName](#API_CreateProject_RequestSyntax) **   <a name="sagemaker-CreateProject-request-ProjectName"></a>
The name of the project.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 32.
Pattern: `[a-zA-Z0-9](-*[a-zA-Z0-9]){0,31}`
Required: Yes

 ** [ServiceCatalogProvisioningDetails](#API_CreateProject_RequestSyntax) **   <a name="sagemaker-CreateProject-request-ServiceCatalogProvisioningDetails"></a>
The product ID and provisioning artifact ID to provision a service catalog. The provisioning artifact ID will default to the latest provisioning artifact ID of the product, if you don't provide the provisioning artifact ID. For more information, see [What is AWS Service Catalog](https://docs.aws.amazon.com/servicecatalog/latest/adminguide/introduction.html).
Type: [ServiceCatalogProvisioningDetails](API_ServiceCatalogProvisioningDetails.md) object
Required: No

 ** [Tags](#API_CreateProject_RequestSyntax) **   <a name="sagemaker-CreateProject-request-Tags"></a>
An array of key-value pairs that you want to use to organize and track your AWS resource costs. For more information, see [Tagging AWS resources](https://docs.aws.amazon.com/general/latest/gr/aws_tagging.html) in the * AWS General Reference Guide*.
Type: Array of [Tag](API_Tag.md) objects
Array Members: Minimum number of 0 items. Maximum number of 50 items.
Required: No

 ** [TemplateProviders](#API_CreateProject_RequestSyntax) **   <a name="sagemaker-CreateProject-request-TemplateProviders"></a>
 An array of template provider configurations for creating infrastructure resources for the project.
Type: Array of [CreateTemplateProvider](API_CreateTemplateProvider.md) objects
Array Members: Fixed number of 1 item.
Required: No

## Response Syntax
<a name="API_CreateProject_ResponseSyntax"></a>

```
{
   "ProjectArn": "string",
   "ProjectId": "string"
}
```

## Response Elements
<a name="API_CreateProject_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [ProjectArn](#API_CreateProject_ResponseSyntax) **   <a name="sagemaker-CreateProject-response-ProjectArn"></a>
The Amazon Resource Name (ARN) of the project.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Pattern: `arn:aws[a-z\-]*:sagemaker:[a-z0-9\-]{9,16}:[0-9]{12}:project/[\S]{1,2048}`

 ** [ProjectId](#API_CreateProject_ResponseSyntax) **   <a name="sagemaker-CreateProject-response-ProjectId"></a>
The ID of the new project.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 20.
Pattern: `[a-zA-Z0-9](-*[a-zA-Z0-9])*`

## Errors
<a name="API_CreateProject_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** ResourceLimitExceeded **
 You have exceeded an SageMaker resource limit. For example, you might have too many training jobs created.
HTTP Status Code: 400

## See Also
<a name="API_CreateProject_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/sagemaker-2017-07-24/CreateProject)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/sagemaker-2017-07-24/CreateProject)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sagemaker-2017-07-24/CreateProject)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/sagemaker-2017-07-24/CreateProject)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sagemaker-2017-07-24/CreateProject)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/sagemaker-2017-07-24/CreateProject)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/sagemaker-2017-07-24/CreateProject)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/sagemaker-2017-07-24/CreateProject)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/sagemaker-2017-07-24/CreateProject)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sagemaker-2017-07-24/CreateProject)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon SageMaker. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query sagemaker` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
