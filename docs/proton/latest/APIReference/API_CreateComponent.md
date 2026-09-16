---
source_url: https://docs.aws.amazon.com/proton/latest/APIReference/API_CreateComponent.html
---

AWS has decided to discontinue AWS Proton, with support ending on October 7, 2026. New customers will not be able to sign up after October 7, 2025, but existing customers can continue to use the service until October 7, 2026.For more information, see [AWS Proton Service Deprecation and Migration Guide](https://docs.aws.amazon.com/proton/latest/userguide/proton-end-of-support.html).

# CreateComponent
<a name="API_CreateComponent"></a>

Create an AWS Proton component. A component is an infrastructure extension for a service instance.

For more information about components, see [AWS Proton components](https://docs.aws.amazon.com/proton/latest/userguide/ag-components.html) in the * AWS Proton User Guide*.

## Request Syntax
<a name="API_CreateComponent_RequestSyntax"></a>

```
{
   "clientToken": "{{string}}",
   "description": "{{string}}",
   "environmentName": "{{string}}",
   "manifest": "{{string}}",
   "name": "{{string}}",
   "serviceInstanceName": "{{string}}",
   "serviceName": "{{string}}",
   "serviceSpec": "{{string}}",
   "tags": [
      {
         "key": "{{string}}",
         "value": "{{string}}"
      }
   ],
   "templateFile": "{{string}}"
}
```

## Request Parameters
<a name="API_CreateComponent_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [clientToken](#API_CreateComponent_RequestSyntax) **   <a name="proton-CreateComponent-request-clientToken"></a>
The client token for the created component.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 64.
Pattern: `[!-~]*`
Required: No

 ** [description](#API_CreateComponent_RequestSyntax) **   <a name="proton-CreateComponent-request-description"></a>
An optional customer-provided description of the component.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 500.
Required: No

 ** [environmentName](#API_CreateComponent_RequestSyntax) **   <a name="proton-CreateComponent-request-environmentName"></a>
The name of the AWS Proton environment that you want to associate this component with. You must specify this when you don't specify `serviceInstanceName` and `serviceName`.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Pattern: `[0-9A-Za-z]+[0-9A-Za-z_\-]*`
Required: No

 ** [manifest](#API_CreateComponent_RequestSyntax) **   <a name="proton-CreateComponent-request-manifest"></a>
A path to a manifest file that lists the Infrastructure as Code (IaC) file, template language, and rendering engine for infrastructure that a custom component provisions.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Required: Yes

 ** [name](#API_CreateComponent_RequestSyntax) **   <a name="proton-CreateComponent-request-name"></a>
The customer-provided name of the component.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Pattern: `[0-9A-Za-z]+[0-9A-Za-z_\-]*`
Required: Yes

 ** [serviceInstanceName](#API_CreateComponent_RequestSyntax) **   <a name="proton-CreateComponent-request-serviceInstanceName"></a>
The name of the service instance that you want to attach this component to. If you don't specify this, the component isn't attached to any service instance. Specify both `serviceInstanceName` and `serviceName` or neither of them.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Pattern: `[0-9A-Za-z]+[0-9A-Za-z_\-]*`
Required: No

 ** [serviceName](#API_CreateComponent_RequestSyntax) **   <a name="proton-CreateComponent-request-serviceName"></a>
The name of the service that `serviceInstanceName` is associated with. If you don't specify this, the component isn't attached to any service instance. Specify both `serviceInstanceName` and `serviceName` or neither of them.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Pattern: `[0-9A-Za-z]+[0-9A-Za-z_\-]*`
Required: No

 ** [serviceSpec](#API_CreateComponent_RequestSyntax) **   <a name="proton-CreateComponent-request-serviceSpec"></a>
The service spec that you want the component to use to access service inputs. Set this only when you attach the component to a service instance.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 51200.
Required: No

 ** [tags](#API_CreateComponent_RequestSyntax) **   <a name="proton-CreateComponent-request-tags"></a>
An optional list of metadata items that you can associate with the AWS Proton component. A tag is a key-value pair.
For more information, see [AWS Proton resources and tagging](https://docs.aws.amazon.com/proton/latest/userguide/resources.html) in the * AWS Proton User Guide*.
Type: Array of [Tag](API_Tag.md) objects
Array Members: Minimum number of 0 items. Maximum number of 50 items.
Required: No

 ** [templateFile](#API_CreateComponent_RequestSyntax) **   <a name="proton-CreateComponent-request-templateFile"></a>
A path to the Infrastructure as Code (IaC) file describing infrastructure that a custom component provisions.
Components support a single IaC file, even if you use Terraform as your template language.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 51200.
Required: Yes

## Response Syntax
<a name="API_CreateComponent_ResponseSyntax"></a>

```
{
   "component": {
      "arn": "string",
      "createdAt": number,
      "deploymentStatus": "string",
      "deploymentStatusMessage": "string",
      "description": "string",
      "environmentName": "string",
      "lastAttemptedDeploymentId": "string",
      "lastClientRequestToken": "string",
      "lastDeploymentAttemptedAt": number,
      "lastDeploymentSucceededAt": number,
      "lastModifiedAt": number,
      "lastSucceededDeploymentId": "string",
      "name": "string",
      "serviceInstanceName": "string",
      "serviceName": "string",
      "serviceSpec": "string"
   }
}
```

## Response Elements
<a name="API_CreateComponent_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [component](#API_CreateComponent_ResponseSyntax) **   <a name="proton-CreateComponent-response-component"></a>
The detailed data of the created component.
Type: [Component](API_Component.md) object

## Errors
<a name="API_CreateComponent_Errors"></a>

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
<a name="API_CreateComponent_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/proton-2020-07-20/CreateComponent)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/proton-2020-07-20/CreateComponent)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/proton-2020-07-20/CreateComponent)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/proton-2020-07-20/CreateComponent)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/proton-2020-07-20/CreateComponent)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/proton-2020-07-20/CreateComponent)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/proton-2020-07-20/CreateComponent)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/proton-2020-07-20/CreateComponent)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/proton-2020-07-20/CreateComponent)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/proton-2020-07-20/CreateComponent)
