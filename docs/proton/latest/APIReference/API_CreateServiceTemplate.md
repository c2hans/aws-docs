---
source_url: https://docs.aws.amazon.com/proton/latest/APIReference/API_CreateServiceTemplate.html
---

AWS has decided to discontinue AWS Proton, with support ending on October 7, 2026. New customers will not be able to sign up after October 7, 2025, but existing customers can continue to use the service until October 7, 2026.For more information, see [AWS Proton Service Deprecation and Migration Guide](https://docs.aws.amazon.com/proton/latest/userguide/proton-end-of-support.html).

# CreateServiceTemplate
<a name="API_CreateServiceTemplate"></a>

Create a service template. The administrator creates a service template to define standardized infrastructure and an optional CI/CD service pipeline. Developers, in turn, select the service template from AWS Proton. If the selected service template includes a service pipeline definition, they provide a link to their source code repository. AWS Proton then deploys and manages the infrastructure defined by the selected service template. For more information, see [AWS Proton templates](https://docs.aws.amazon.com/proton/latest/userguide/ag-templates.html) in the * AWS Proton User Guide*.

## Request Syntax
<a name="API_CreateServiceTemplate_RequestSyntax"></a>

```
{
   "description": "{{string}}",
   "displayName": "{{string}}",
   "encryptionKey": "{{string}}",
   "name": "{{string}}",
   "pipelineProvisioning": "{{string}}",
   "tags": [
      {
         "key": "{{string}}",
         "value": "{{string}}"
      }
   ]
}
```

## Request Parameters
<a name="API_CreateServiceTemplate_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [description](#API_CreateServiceTemplate_RequestSyntax) **   <a name="proton-CreateServiceTemplate-request-description"></a>
A description of the service template.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 500.
Required: No

 ** [displayName](#API_CreateServiceTemplate_RequestSyntax) **   <a name="proton-CreateServiceTemplate-request-displayName"></a>
The name of the service template as displayed in the developer interface.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Required: No

 ** [encryptionKey](#API_CreateServiceTemplate_RequestSyntax) **   <a name="proton-CreateServiceTemplate-request-encryptionKey"></a>
A customer provided encryption key that's used to encrypt data.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 200.
Pattern: `arn:(aws|aws-cn|aws-us-gov):[a-zA-Z0-9-]+:[a-zA-Z0-9-]*:\d{12}:([\w+=,.@-]+[/:])*[\w+=,.@-]+`
Required: No

 ** [name](#API_CreateServiceTemplate_RequestSyntax) **   <a name="proton-CreateServiceTemplate-request-name"></a>
The name of the service template.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Pattern: `[0-9A-Za-z]+[0-9A-Za-z_\-]*`
Required: Yes

 ** [pipelineProvisioning](#API_CreateServiceTemplate_RequestSyntax) **   <a name="proton-CreateServiceTemplate-request-pipelineProvisioning"></a>
By default, AWS Proton provides a service pipeline for your service. When this parameter is included, it indicates that an AWS Proton service pipeline *isn't* provided for your service. After it's included, it *can't* be changed. For more information, see [Template bundles](https://docs.aws.amazon.com/proton/latest/userguide/ag-template-authoring.html#ag-template-bundles) in the * AWS Proton User Guide*.
Type: String
Valid Values: `CUSTOMER_MANAGED`
Required: No

 ** [tags](#API_CreateServiceTemplate_RequestSyntax) **   <a name="proton-CreateServiceTemplate-request-tags"></a>
An optional list of metadata items that you can associate with the AWS Proton service template. A tag is a key-value pair.
For more information, see [AWS Proton resources and tagging](https://docs.aws.amazon.com/proton/latest/userguide/resources.html) in the * AWS Proton User Guide*.
Type: Array of [Tag](API_Tag.md) objects
Array Members: Minimum number of 0 items. Maximum number of 50 items.
Required: No

## Response Syntax
<a name="API_CreateServiceTemplate_ResponseSyntax"></a>

```
{
   "serviceTemplate": {
      "arn": "string",
      "createdAt": number,
      "description": "string",
      "displayName": "string",
      "encryptionKey": "string",
      "lastModifiedAt": number,
      "name": "string",
      "pipelineProvisioning": "string",
      "recommendedVersion": "string"
   }
}
```

## Response Elements
<a name="API_CreateServiceTemplate_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [serviceTemplate](#API_CreateServiceTemplate_ResponseSyntax) **   <a name="proton-CreateServiceTemplate-response-serviceTemplate"></a>
The service template detail data that's returned by AWS Proton.
Type: [ServiceTemplate](API_ServiceTemplate.md) object

## Errors
<a name="API_CreateServiceTemplate_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
There *isn't* sufficient access for performing this action.
HTTP Status Code: 400

 ** ConflictException **
The request *couldn't* be made due to a conflicting operation or resource.
HTTP Status Code: 400

 ** InternalServerException **
The request failed to register with the service.
HTTP Status Code: 500

 ** ServiceQuotaExceededException **
A quota was exceeded. For more information, see [AWS Proton Quotas](https://docs.aws.amazon.com/proton/latest/userguide/ag-limits.html) in the * AWS Proton User Guide*.
HTTP Status Code: 400

 ** ThrottlingException **
The request was denied due to request throttling.
HTTP Status Code: 400

 ** ValidationException **
The input is invalid or an out-of-range value was supplied for the input parameter.
HTTP Status Code: 400

## See Also
<a name="API_CreateServiceTemplate_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/proton-2020-07-20/CreateServiceTemplate)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/proton-2020-07-20/CreateServiceTemplate)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/proton-2020-07-20/CreateServiceTemplate)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/proton-2020-07-20/CreateServiceTemplate)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/proton-2020-07-20/CreateServiceTemplate)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/proton-2020-07-20/CreateServiceTemplate)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/proton-2020-07-20/CreateServiceTemplate)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/proton-2020-07-20/CreateServiceTemplate)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/proton-2020-07-20/CreateServiceTemplate)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/proton-2020-07-20/CreateServiceTemplate)
