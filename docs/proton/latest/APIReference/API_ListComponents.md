---
source_url: https://docs.aws.amazon.com/proton/latest/APIReference/API_ListComponents.html
---

AWS has decided to discontinue AWS Proton, with support ending on October 7, 2026. New customers will not be able to sign up after October 7, 2025, but existing customers can continue to use the service until October 7, 2026.For more information, see [AWS Proton Service Deprecation and Migration Guide](https://docs.aws.amazon.com/proton/latest/userguide/proton-end-of-support.html).

# ListComponents
<a name="API_ListComponents"></a>

List components with summary data. You can filter the result list by environment, service, or a single service instance.

For more information about components, see [AWS Proton components](https://docs.aws.amazon.com/proton/latest/userguide/ag-components.html) in the * AWS Proton User Guide*.

## Request Syntax
<a name="API_ListComponents_RequestSyntax"></a>

```
{
   "environmentName": "{{string}}",
   "maxResults": {{number}},
   "nextToken": "{{string}}",
   "serviceInstanceName": "{{string}}",
   "serviceName": "{{string}}"
}
```

## Request Parameters
<a name="API_ListComponents_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [environmentName](#API_ListComponents_RequestSyntax) **   <a name="proton-ListComponents-request-environmentName"></a>
The name of an environment for result list filtering. AWS Proton returns components associated with the environment or attached to service instances running in it.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Pattern: `[0-9A-Za-z]+[0-9A-Za-z_\-]*`
Required: No

 ** [maxResults](#API_ListComponents_RequestSyntax) **   <a name="proton-ListComponents-request-maxResults"></a>
The maximum number of components to list.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 100.
Required: No

 ** [nextToken](#API_ListComponents_RequestSyntax) **   <a name="proton-ListComponents-request-nextToken"></a>
A token that indicates the location of the next component in the array of components, after the list of components that was previously requested.
Type: String
Pattern: `[A-Za-z0-9+=/]+`
Required: No

 ** [serviceInstanceName](#API_ListComponents_RequestSyntax) **   <a name="proton-ListComponents-request-serviceInstanceName"></a>
The name of a service instance for result list filtering. AWS Proton returns the component attached to the service instance, if any.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Pattern: `[0-9A-Za-z]+[0-9A-Za-z_\-]*`
Required: No

 ** [serviceName](#API_ListComponents_RequestSyntax) **   <a name="proton-ListComponents-request-serviceName"></a>
The name of a service for result list filtering. AWS Proton returns components attached to service instances of the service.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Pattern: `[0-9A-Za-z]+[0-9A-Za-z_\-]*`
Required: No

## Response Syntax
<a name="API_ListComponents_ResponseSyntax"></a>

```
{
   "components": [
      {
         "arn": "string",
         "createdAt": number,
         "deploymentStatus": "string",
         "deploymentStatusMessage": "string",
         "environmentName": "string",
         "lastAttemptedDeploymentId": "string",
         "lastDeploymentAttemptedAt": number,
         "lastDeploymentSucceededAt": number,
         "lastModifiedAt": number,
         "lastSucceededDeploymentId": "string",
         "name": "string",
         "serviceInstanceName": "string",
         "serviceName": "string"
      }
   ],
   "nextToken": "string"
}
```

## Response Elements
<a name="API_ListComponents_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [components](#API_ListComponents_ResponseSyntax) **   <a name="proton-ListComponents-response-components"></a>
An array of components with summary data.
Type: Array of [ComponentSummary](API_ComponentSummary.md) objects

 ** [nextToken](#API_ListComponents_ResponseSyntax) **   <a name="proton-ListComponents-response-nextToken"></a>
A token that indicates the location of the next component in the array of components, after the current requested list of components.
Type: String
Pattern: `[A-Za-z0-9+=/]+`

## Errors
<a name="API_ListComponents_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
There *isn't* sufficient access for performing this action.
HTTP Status Code: 400

 ** InternalServerException **
The request failed to register with the service.
HTTP Status Code: 500

 ** ThrottlingException **
The request was denied due to request throttling.
HTTP Status Code: 400

 ** ValidationException **
The input is invalid or an out-of-range value was supplied for the input parameter.
HTTP Status Code: 400

## See Also
<a name="API_ListComponents_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/proton-2020-07-20/ListComponents)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/proton-2020-07-20/ListComponents)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/proton-2020-07-20/ListComponents)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/proton-2020-07-20/ListComponents)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/proton-2020-07-20/ListComponents)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/proton-2020-07-20/ListComponents)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/proton-2020-07-20/ListComponents)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/proton-2020-07-20/ListComponents)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/proton-2020-07-20/ListComponents)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/proton-2020-07-20/ListComponents)
