---
source_url: https://docs.aws.amazon.com/proton/latest/APIReference/API_ListEnvironments.html
---

AWS has decided to discontinue AWS Proton, with support ending on October 7, 2026. New customers will not be able to sign up after October 7, 2025, but existing customers can continue to use the service until October 7, 2026.For more information, see [AWS Proton Service Deprecation and Migration Guide](https://docs.aws.amazon.com/proton/latest/userguide/proton-end-of-support.html).

# ListEnvironments
<a name="API_ListEnvironments"></a>

List environments with detail data summaries.

## Request Syntax
<a name="API_ListEnvironments_RequestSyntax"></a>

```
{
   "environmentTemplates": [
      {
         "majorVersion": "{{string}}",
         "templateName": "{{string}}"
      }
   ],
   "maxResults": {{number}},
   "nextToken": "{{string}}"
}
```

## Request Parameters
<a name="API_ListEnvironments_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [environmentTemplates](#API_ListEnvironments_RequestSyntax) **   <a name="proton-ListEnvironments-request-environmentTemplates"></a>
An array of the versions of the environment template.
Type: Array of [EnvironmentTemplateFilter](API_EnvironmentTemplateFilter.md) objects
Required: No

 ** [maxResults](#API_ListEnvironments_RequestSyntax) **   <a name="proton-ListEnvironments-request-maxResults"></a>
The maximum number of environments to list.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 100.
Required: No

 ** [nextToken](#API_ListEnvironments_RequestSyntax) **   <a name="proton-ListEnvironments-request-nextToken"></a>
A token that indicates the location of the next environment in the array of environments, after the list of environments that was previously requested.
Type: String
Pattern: `[A-Za-z0-9+=/]+`
Required: No

## Response Syntax
<a name="API_ListEnvironments_ResponseSyntax"></a>

```
{
   "environments": [
      {
         "arn": "string",
         "componentRoleArn": "string",
         "createdAt": number,
         "deploymentStatus": "string",
         "deploymentStatusMessage": "string",
         "description": "string",
         "environmentAccountConnectionId": "string",
         "environmentAccountId": "string",
         "lastAttemptedDeploymentId": "string",
         "lastDeploymentAttemptedAt": number,
         "lastDeploymentSucceededAt": number,
         "lastSucceededDeploymentId": "string",
         "name": "string",
         "protonServiceRoleArn": "string",
         "provisioning": "string",
         "templateMajorVersion": "string",
         "templateMinorVersion": "string",
         "templateName": "string"
      }
   ],
   "nextToken": "string"
}
```

## Response Elements
<a name="API_ListEnvironments_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [environments](#API_ListEnvironments_ResponseSyntax) **   <a name="proton-ListEnvironments-response-environments"></a>
An array of environment detail data summaries.
Type: Array of [EnvironmentSummary](API_EnvironmentSummary.md) objects

 ** [nextToken](#API_ListEnvironments_ResponseSyntax) **   <a name="proton-ListEnvironments-response-nextToken"></a>
A token that indicates the location of the next environment in the array of environments, after the current requested list of environments.
Type: String
Pattern: `[A-Za-z0-9+=/]+`

## Errors
<a name="API_ListEnvironments_Errors"></a>

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
<a name="API_ListEnvironments_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/proton-2020-07-20/ListEnvironments)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/proton-2020-07-20/ListEnvironments)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/proton-2020-07-20/ListEnvironments)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/proton-2020-07-20/ListEnvironments)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/proton-2020-07-20/ListEnvironments)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/proton-2020-07-20/ListEnvironments)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/proton-2020-07-20/ListEnvironments)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/proton-2020-07-20/ListEnvironments)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/proton-2020-07-20/ListEnvironments)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/proton-2020-07-20/ListEnvironments)
