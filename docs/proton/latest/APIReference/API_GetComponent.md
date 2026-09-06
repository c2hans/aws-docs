---
source_url: https://docs.aws.amazon.com/proton/latest/APIReference/API_GetComponent.html
---

AWS has decided to discontinue AWS Proton, with support ending on October 7, 2026. New customers will not be able to sign up after October 7, 2025, but existing customers can continue to use the service until October 7, 2026.For more information, see [AWS Proton Service Deprecation and Migration Guide](https://docs.aws.amazon.com/proton/latest/userguide/proton-end-of-support.html).

# GetComponent
<a name="API_GetComponent"></a>

Get detailed data for a component.

For more information about components, see [AWS Proton components](https://docs.aws.amazon.com/proton/latest/userguide/ag-components.html) in the * AWS Proton User Guide*.

## Request Syntax
<a name="API_GetComponent_RequestSyntax"></a>

```
{
   "name": "{{string}}"
}
```

## Request Parameters
<a name="API_GetComponent_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [name](#API_GetComponent_RequestSyntax) **   <a name="proton-GetComponent-request-name"></a>
The name of the component that you want to get the detailed data for.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Pattern: `[0-9A-Za-z]+[0-9A-Za-z_\-]*`
Required: Yes

## Response Syntax
<a name="API_GetComponent_ResponseSyntax"></a>

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
<a name="API_GetComponent_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [component](#API_GetComponent_ResponseSyntax) **   <a name="proton-GetComponent-response-component"></a>
The detailed data of the requested component.
Type: [Component](API_Component.md) object

## Errors
<a name="API_GetComponent_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
There *isn't* sufficient access for performing this action.
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
<a name="API_GetComponent_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/proton-2020-07-20/GetComponent)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/proton-2020-07-20/GetComponent)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/proton-2020-07-20/GetComponent)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/proton-2020-07-20/GetComponent)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/proton-2020-07-20/GetComponent)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/proton-2020-07-20/GetComponent)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/proton-2020-07-20/GetComponent)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/proton-2020-07-20/GetComponent)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/proton-2020-07-20/GetComponent)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/proton-2020-07-20/GetComponent)
