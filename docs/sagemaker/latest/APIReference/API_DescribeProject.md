---
source_url: https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_DescribeProject.html
---

# DescribeProject
<a name="API_DescribeProject"></a>

Describes the details of a project.

## Request Syntax
<a name="API_DescribeProject_RequestSyntax"></a>

```
{
   "ProjectName": "{{string}}"
}
```

## Request Parameters
<a name="API_DescribeProject_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [ProjectName](#API_DescribeProject_RequestSyntax) **   <a name="sagemaker-DescribeProject-request-ProjectName"></a>
The name of the project to describe.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 32.
Pattern: `[a-zA-Z0-9](-*[a-zA-Z0-9]){0,31}`
Required: Yes

## Response Syntax
<a name="API_DescribeProject_ResponseSyntax"></a>

```
{
   "CreatedBy": {
      "DomainId": "string",
      "IamIdentity": {
         "Arn": "string",
         "PrincipalId": "string",
         "SourceIdentity": "string"
      },
      "UserProfileArn": "string",
      "UserProfileName": "string"
   },
   "CreationTime": number,
   "LastModifiedBy": {
      "DomainId": "string",
      "IamIdentity": {
         "Arn": "string",
         "PrincipalId": "string",
         "SourceIdentity": "string"
      },
      "UserProfileArn": "string",
      "UserProfileName": "string"
   },
   "LastModifiedTime": number,
   "ProjectArn": "string",
   "ProjectDescription": "string",
   "ProjectId": "string",
   "ProjectName": "string",
   "ProjectStatus": "string",
   "ServiceCatalogProvisionedProductDetails": {
      "ProvisionedProductId": "string",
      "ProvisionedProductStatusMessage": "string"
   },
   "ServiceCatalogProvisioningDetails": {
      "PathId": "string",
      "ProductId": "string",
      "ProvisioningArtifactId": "string",
      "ProvisioningParameters": [
         {
            "Key": "string",
            "Value": "string"
         }
      ]
   },
   "TemplateProviderDetails": [
      {
         "CfnTemplateProviderDetail": {
            "Parameters": [
               {
                  "Key": "string",
                  "Value": "string"
               }
            ],
            "RoleARN": "string",
            "StackDetail": {
               "Id": "string",
               "Name": "string",
               "StatusMessage": "string"
            },
            "TemplateName": "string",
            "TemplateURL": "string"
         }
      }
   ]
}
```

## Response Elements
<a name="API_DescribeProject_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [CreatedBy](#API_DescribeProject_ResponseSyntax) **   <a name="sagemaker-DescribeProject-response-CreatedBy"></a>
Information about the user who created or modified a SageMaker resource.
Type: [UserContext](API_UserContext.md) object

 ** [CreationTime](#API_DescribeProject_ResponseSyntax) **   <a name="sagemaker-DescribeProject-response-CreationTime"></a>
The time when the project was created.
Type: Timestamp

 ** [LastModifiedBy](#API_DescribeProject_ResponseSyntax) **   <a name="sagemaker-DescribeProject-response-LastModifiedBy"></a>
Information about the user who created or modified a SageMaker resource.
Type: [UserContext](API_UserContext.md) object

 ** [LastModifiedTime](#API_DescribeProject_ResponseSyntax) **   <a name="sagemaker-DescribeProject-response-LastModifiedTime"></a>
The timestamp when project was last modified.
Type: Timestamp

 ** [ProjectArn](#API_DescribeProject_ResponseSyntax) **   <a name="sagemaker-DescribeProject-response-ProjectArn"></a>
The Amazon Resource Name (ARN) of the project.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Pattern: `arn:aws[a-z\-]*:sagemaker:[a-z0-9\-]{9,16}:[0-9]{12}:project/[\S]{1,2048}`

 ** [ProjectDescription](#API_DescribeProject_ResponseSyntax) **   <a name="sagemaker-DescribeProject-response-ProjectDescription"></a>
The description of the project.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1024.
Pattern: `[\p{L}\p{M}\p{Z}\p{S}\p{N}\p{P}]*`

 ** [ProjectId](#API_DescribeProject_ResponseSyntax) **   <a name="sagemaker-DescribeProject-response-ProjectId"></a>
The ID of the project.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 20.
Pattern: `[a-zA-Z0-9](-*[a-zA-Z0-9])*`

 ** [ProjectName](#API_DescribeProject_ResponseSyntax) **   <a name="sagemaker-DescribeProject-response-ProjectName"></a>
The name of the project.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 32.
Pattern: `[a-zA-Z0-9](-*[a-zA-Z0-9]){0,31}`

 ** [ProjectStatus](#API_DescribeProject_ResponseSyntax) **   <a name="sagemaker-DescribeProject-response-ProjectStatus"></a>
The status of the project.
Type: String
Valid Values: `Pending | CreateInProgress | CreateCompleted | CreateFailed | DeleteInProgress | DeleteFailed | DeleteCompleted | UpdateInProgress | UpdateCompleted | UpdateFailed`

 ** [ServiceCatalogProvisionedProductDetails](#API_DescribeProject_ResponseSyntax) **   <a name="sagemaker-DescribeProject-response-ServiceCatalogProvisionedProductDetails"></a>
Information about a provisioned service catalog product.
Type: [ServiceCatalogProvisionedProductDetails](API_ServiceCatalogProvisionedProductDetails.md) object

 ** [ServiceCatalogProvisioningDetails](#API_DescribeProject_ResponseSyntax) **   <a name="sagemaker-DescribeProject-response-ServiceCatalogProvisioningDetails"></a>
Information used to provision a service catalog product. For information, see [What is AWS Service Catalog](https://docs.aws.amazon.com/servicecatalog/latest/adminguide/introduction.html).
Type: [ServiceCatalogProvisioningDetails](API_ServiceCatalogProvisioningDetails.md) object

 ** [TemplateProviderDetails](#API_DescribeProject_ResponseSyntax) **   <a name="sagemaker-DescribeProject-response-TemplateProviderDetails"></a>
 An array of template providers associated with the project.
Type: Array of [TemplateProviderDetail](API_TemplateProviderDetail.md) objects
Array Members: Fixed number of 1 item.

## Errors
<a name="API_DescribeProject_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

## See Also
<a name="API_DescribeProject_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/sagemaker-2017-07-24/DescribeProject)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/sagemaker-2017-07-24/DescribeProject)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sagemaker-2017-07-24/DescribeProject)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/sagemaker-2017-07-24/DescribeProject)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sagemaker-2017-07-24/DescribeProject)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/sagemaker-2017-07-24/DescribeProject)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/sagemaker-2017-07-24/DescribeProject)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/sagemaker-2017-07-24/DescribeProject)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/sagemaker-2017-07-24/DescribeProject)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sagemaker-2017-07-24/DescribeProject)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon SageMaker. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query sagemaker` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
