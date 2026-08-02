---
source_url: https://docs.aws.amazon.com/proton/latest/APIReference/API_CreateService.html
---

AWS has decided to discontinue AWS Proton, with support ending on October 7, 2026. New customers will not be able to sign up after October 7, 2025, but existing customers can continue to use the service until October 7, 2026.For more information, see [AWS Proton Service Deprecation and Migration Guide](https://docs.aws.amazon.com/proton/latest/userguide/proton-end-of-support.html).

# CreateService
<a name="API_CreateService"></a>

Create an AWS Proton service. An AWS Proton service is an instantiation of a service template and often includes several service instances and pipeline. For more information, see [Services](https://docs.aws.amazon.com/proton/latest/userguide/ag-services.html) in the * AWS Proton User Guide*.

## Request Syntax
<a name="API_CreateService_RequestSyntax"></a>

```
{
   "branchName": "{{string}}",
   "description": "{{string}}",
   "name": "{{string}}",
   "repositoryConnectionArn": "{{string}}",
   "repositoryId": "{{string}}",
   "spec": "{{string}}",
   "tags": [
      {
         "key": "{{string}}",
         "value": "{{string}}"
      }
   ],
   "templateMajorVersion": "{{string}}",
   "templateMinorVersion": "{{string}}",
   "templateName": "{{string}}"
}
```

## Request Parameters
<a name="API_CreateService_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [branchName](#API_CreateService_RequestSyntax) **   <a name="proton-CreateService-request-branchName"></a>
The name of the code repository branch that holds the code that's deployed in AWS Proton. *Don't* include this parameter if your service template *doesn't* include a service pipeline.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 200.
Required: No

 ** [description](#API_CreateService_RequestSyntax) **   <a name="proton-CreateService-request-description"></a>
A description of the AWS Proton service.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 500.
Required: No

 ** [name](#API_CreateService_RequestSyntax) **   <a name="proton-CreateService-request-name"></a>
The service name.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Pattern: `[0-9A-Za-z]+[0-9A-Za-z_\-]*`
Required: Yes

 ** [repositoryConnectionArn](#API_CreateService_RequestSyntax) **   <a name="proton-CreateService-request-repositoryConnectionArn"></a>
The Amazon Resource Name (ARN) of the repository connection. For more information, see [Setting up an AWS CodeStar connection](https://docs.aws.amazon.com/proton/latest/userguide/setting-up-for-service.html#setting-up-vcontrol) in the * AWS Proton User Guide*. *Don't* include this parameter if your service template *doesn't* include a service pipeline.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 200.
Pattern: `arn:(aws|aws-cn|aws-us-gov):[a-zA-Z0-9-]+:[a-zA-Z0-9-]*:\d{12}:([\w+=,.@-]+[/:])*[\w+=,.@-]+`
Required: No

 ** [repositoryId](#API_CreateService_RequestSyntax) **   <a name="proton-CreateService-request-repositoryId"></a>
The ID of the code repository. *Don't* include this parameter if your service template *doesn't* include a service pipeline.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 200.
Required: No

 ** [spec](#API_CreateService_RequestSyntax) **   <a name="proton-CreateService-request-spec"></a>
A link to a spec file that provides inputs as defined in the service template bundle schema file. The spec file is in YAML format. *Don’t* include pipeline inputs in the spec if your service template *doesn’t* include a service pipeline. For more information, see [Create a service](https://docs.aws.amazon.com/proton/latest/userguide/ag-create-svc.html) in the * AWS Proton User Guide*.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 51200.
Required: Yes

 ** [tags](#API_CreateService_RequestSyntax) **   <a name="proton-CreateService-request-tags"></a>
An optional list of metadata items that you can associate with the AWS Proton service. A tag is a key-value pair.
For more information, see [AWS Proton resources and tagging](https://docs.aws.amazon.com/proton/latest/userguide/resources.html) in the * AWS Proton User Guide*.
Type: Array of [Tag](API_Tag.md) objects
Array Members: Minimum number of 0 items. Maximum number of 50 items.
Required: No

 ** [templateMajorVersion](#API_CreateService_RequestSyntax) **   <a name="proton-CreateService-request-templateMajorVersion"></a>
The major version of the service template that was used to create the service.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 20.
Pattern: `(0|([1-9]{1}\d*))`
Required: Yes

 ** [templateMinorVersion](#API_CreateService_RequestSyntax) **   <a name="proton-CreateService-request-templateMinorVersion"></a>
The minor version of the service template that was used to create the service.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 20.
Pattern: `(0|([1-9]{1}\d*))`
Required: No

 ** [templateName](#API_CreateService_RequestSyntax) **   <a name="proton-CreateService-request-templateName"></a>
The name of the service template that's used to create the service.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Pattern: `[0-9A-Za-z]+[0-9A-Za-z_\-]*`
Required: Yes

## Response Syntax
<a name="API_CreateService_ResponseSyntax"></a>

```
{
   "service": {
      "arn": "string",
      "branchName": "string",
      "createdAt": number,
      "description": "string",
      "lastModifiedAt": number,
      "name": "string",
      "pipeline": {
         "arn": "string",
         "createdAt": number,
         "deploymentStatus": "string",
         "deploymentStatusMessage": "string",
         "lastAttemptedDeploymentId": "string",
         "lastDeploymentAttemptedAt": number,
         "lastDeploymentSucceededAt": number,
         "lastSucceededDeploymentId": "string",
         "spec": "string",
         "templateMajorVersion": "string",
         "templateMinorVersion": "string",
         "templateName": "string"
      },
      "repositoryConnectionArn": "string",
      "repositoryId": "string",
      "spec": "string",
      "status": "string",
      "statusMessage": "string",
      "templateName": "string"
   }
}
```

## Response Elements
<a name="API_CreateService_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [service](#API_CreateService_ResponseSyntax) **   <a name="proton-CreateService-response-service"></a>
The service detail data that's returned by AWS Proton.
Type: [Service](API_Service.md) object

## Errors
<a name="API_CreateService_Errors"></a>

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

 ** ResourceNotFoundException **
The requested resource *wasn't* found.
HTTP Status Code: 400

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
<a name="API_CreateService_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/proton-2020-07-20/CreateService)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/proton-2020-07-20/CreateService)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/proton-2020-07-20/CreateService)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/proton-2020-07-20/CreateService)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/proton-2020-07-20/CreateService)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/proton-2020-07-20/CreateService)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/proton-2020-07-20/CreateService)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/proton-2020-07-20/CreateService)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/proton-2020-07-20/CreateService)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/proton-2020-07-20/CreateService)
