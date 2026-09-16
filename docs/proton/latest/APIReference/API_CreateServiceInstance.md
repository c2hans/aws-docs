---
source_url: https://docs.aws.amazon.com/proton/latest/APIReference/API_CreateServiceInstance.html
---

AWS has decided to discontinue AWS Proton, with support ending on October 7, 2026. New customers will not be able to sign up after October 7, 2025, but existing customers can continue to use the service until October 7, 2026.For more information, see [AWS Proton Service Deprecation and Migration Guide](https://docs.aws.amazon.com/proton/latest/userguide/proton-end-of-support.html).

# CreateServiceInstance
<a name="API_CreateServiceInstance"></a>

Create a service instance.

## Request Syntax
<a name="API_CreateServiceInstance_RequestSyntax"></a>

```
{
   "clientToken": "{{string}}",
   "name": "{{string}}",
   "serviceName": "{{string}}",
   "spec": "{{string}}",
   "tags": [
      {
         "key": "{{string}}",
         "value": "{{string}}"
      }
   ],
   "templateMajorVersion": "{{string}}",
   "templateMinorVersion": "{{string}}"
}
```

## Request Parameters
<a name="API_CreateServiceInstance_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [clientToken](#API_CreateServiceInstance_RequestSyntax) **   <a name="proton-CreateServiceInstance-request-clientToken"></a>
The client token of the service instance to create.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 64.
Pattern: `[!-~]*`
Required: No

 ** [name](#API_CreateServiceInstance_RequestSyntax) **   <a name="proton-CreateServiceInstance-request-name"></a>
The name of the service instance to create.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Pattern: `[0-9A-Za-z]+[0-9A-Za-z_\-]*`
Required: Yes

 ** [serviceName](#API_CreateServiceInstance_RequestSyntax) **   <a name="proton-CreateServiceInstance-request-serviceName"></a>
The name of the service the service instance is added to.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Pattern: `[0-9A-Za-z]+[0-9A-Za-z_\-]*`
Required: Yes

 ** [spec](#API_CreateServiceInstance_RequestSyntax) **   <a name="proton-CreateServiceInstance-request-spec"></a>
The spec for the service instance you want to create.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 51200.
Required: Yes

 ** [tags](#API_CreateServiceInstance_RequestSyntax) **   <a name="proton-CreateServiceInstance-request-tags"></a>
An optional list of metadata items that you can associate with the AWS Proton service instance. A tag is a key-value pair.
For more information, see [AWS Proton resources and tagging](https://docs.aws.amazon.com/proton/latest/userguide/resources.html) in the * AWS Proton User Guide*.
Type: Array of [Tag](API_Tag.md) objects
Array Members: Minimum number of 0 items. Maximum number of 50 items.
Required: No

 ** [templateMajorVersion](#API_CreateServiceInstance_RequestSyntax) **   <a name="proton-CreateServiceInstance-request-templateMajorVersion"></a>
To create a new major and minor version of the service template, *exclude* `major Version`.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 20.
Pattern: `(0|([1-9]{1}\d*))`
Required: No

 ** [templateMinorVersion](#API_CreateServiceInstance_RequestSyntax) **   <a name="proton-CreateServiceInstance-request-templateMinorVersion"></a>
To create a new minor version of the service template, include a `major Version`.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 20.
Pattern: `(0|([1-9]{1}\d*))`
Required: No

## Response Syntax
<a name="API_CreateServiceInstance_ResponseSyntax"></a>

```
{
   "serviceInstance": {
      "arn": "string",
      "createdAt": number,
      "deploymentStatus": "string",
      "deploymentStatusMessage": "string",
      "environmentName": "string",
      "lastAttemptedDeploymentId": "string",
      "lastClientRequestToken": "string",
      "lastDeploymentAttemptedAt": number,
      "lastDeploymentSucceededAt": number,
      "lastSucceededDeploymentId": "string",
      "name": "string",
      "serviceName": "string",
      "spec": "string",
      "templateMajorVersion": "string",
      "templateMinorVersion": "string",
      "templateName": "string"
   }
}
```

## Response Elements
<a name="API_CreateServiceInstance_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [serviceInstance](#API_CreateServiceInstance_ResponseSyntax) **   <a name="proton-CreateServiceInstance-response-serviceInstance"></a>
The detailed data of the service instance being created.
Type: [ServiceInstance](API_ServiceInstance.md) object

## Errors
<a name="API_CreateServiceInstance_Errors"></a>

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

 ** ThrottlingException **
The request was denied due to request throttling.
HTTP Status Code: 400

 ** ValidationException **
The input is invalid or an out-of-range value was supplied for the input parameter.
HTTP Status Code: 400

## See Also
<a name="API_CreateServiceInstance_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/proton-2020-07-20/CreateServiceInstance)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/proton-2020-07-20/CreateServiceInstance)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/proton-2020-07-20/CreateServiceInstance)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/proton-2020-07-20/CreateServiceInstance)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/proton-2020-07-20/CreateServiceInstance)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/proton-2020-07-20/CreateServiceInstance)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/proton-2020-07-20/CreateServiceInstance)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/proton-2020-07-20/CreateServiceInstance)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/proton-2020-07-20/CreateServiceInstance)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/proton-2020-07-20/CreateServiceInstance)
