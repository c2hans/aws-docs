---
source_url: https://docs.aws.amazon.com/proton/latest/APIReference/API_ListDeployments.html
---

AWS has decided to discontinue AWS Proton, with support ending on October 7, 2026. New customers will not be able to sign up after October 7, 2025, but existing customers can continue to use the service until October 7, 2026.For more information, see [AWS Proton Service Deprecation and Migration Guide](https://docs.aws.amazon.com/proton/latest/userguide/proton-end-of-support.html).

# ListDeployments
<a name="API_ListDeployments"></a>

List deployments. You can filter the result list by environment, service, or a single service instance.

## Request Syntax
<a name="API_ListDeployments_RequestSyntax"></a>

```
{
   "componentName": "{{string}}",
   "environmentName": "{{string}}",
   "maxResults": {{number}},
   "nextToken": "{{string}}",
   "serviceInstanceName": "{{string}}",
   "serviceName": "{{string}}"
}
```

## Request Parameters
<a name="API_ListDeployments_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [componentName](#API_ListDeployments_RequestSyntax) **   <a name="proton-ListDeployments-request-componentName"></a>
The name of a component for result list filtering. AWS Proton returns deployments associated with that component.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Pattern: `[0-9A-Za-z]+[0-9A-Za-z_\-]*`
Required: No

 ** [environmentName](#API_ListDeployments_RequestSyntax) **   <a name="proton-ListDeployments-request-environmentName"></a>
The name of an environment for result list filtering. AWS Proton returns deployments associated with the environment.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Pattern: `[0-9A-Za-z]+[0-9A-Za-z_\-]*`
Required: No

 ** [maxResults](#API_ListDeployments_RequestSyntax) **   <a name="proton-ListDeployments-request-maxResults"></a>
The maximum number of deployments to list.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 100.
Required: No

 ** [nextToken](#API_ListDeployments_RequestSyntax) **   <a name="proton-ListDeployments-request-nextToken"></a>
A token that indicates the location of the next deployment in the array of deployment, after the list of deployment that was previously requested.
Type: String
Pattern: `[A-Za-z0-9+=/]+`
Required: No

 ** [serviceInstanceName](#API_ListDeployments_RequestSyntax) **   <a name="proton-ListDeployments-request-serviceInstanceName"></a>
The name of a service instance for result list filtering. AWS Proton returns the deployments associated with the service instance.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Pattern: `[0-9A-Za-z]+[0-9A-Za-z_\-]*`
Required: No

 ** [serviceName](#API_ListDeployments_RequestSyntax) **   <a name="proton-ListDeployments-request-serviceName"></a>
The name of a service for result list filtering. AWS Proton returns deployments associated with service instances of the service.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Pattern: `[0-9A-Za-z]+[0-9A-Za-z_\-]*`
Required: No

## Response Syntax
<a name="API_ListDeployments_ResponseSyntax"></a>

```
{
   "deployments": [
      {
         "arn": "string",
         "completedAt": number,
         "componentName": "string",
         "createdAt": number,
         "deploymentStatus": "string",
         "environmentName": "string",
         "id": "string",
         "lastAttemptedDeploymentId": "string",
         "lastModifiedAt": number,
         "lastSucceededDeploymentId": "string",
         "serviceInstanceName": "string",
         "serviceName": "string",
         "targetArn": "string",
         "targetResourceCreatedAt": number,
         "targetResourceType": "string"
      }
   ],
   "nextToken": "string"
}
```

## Response Elements
<a name="API_ListDeployments_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [deployments](#API_ListDeployments_ResponseSyntax) **   <a name="proton-ListDeployments-response-deployments"></a>
An array of deployment with summary data.
Type: Array of [DeploymentSummary](API_DeploymentSummary.md) objects

 ** [nextToken](#API_ListDeployments_ResponseSyntax) **   <a name="proton-ListDeployments-response-nextToken"></a>
A token that indicates the location of the next deployment in the array of deployment, after the current requested list of deployment.
Type: String
Pattern: `[A-Za-z0-9+=/]+`

## Errors
<a name="API_ListDeployments_Errors"></a>

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
<a name="API_ListDeployments_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/proton-2020-07-20/ListDeployments)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/proton-2020-07-20/ListDeployments)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/proton-2020-07-20/ListDeployments)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/proton-2020-07-20/ListDeployments)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/proton-2020-07-20/ListDeployments)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/proton-2020-07-20/ListDeployments)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/proton-2020-07-20/ListDeployments)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/proton-2020-07-20/ListDeployments)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/proton-2020-07-20/ListDeployments)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/proton-2020-07-20/ListDeployments)
