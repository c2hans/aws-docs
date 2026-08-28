---
source_url: https://docs.aws.amazon.com/proton/latest/APIReference/API_GetDeployment.html
---

AWS has decided to discontinue AWS Proton, with support ending on October 7, 2026. New customers will not be able to sign up after October 7, 2025, but existing customers can continue to use the service until October 7, 2026.For more information, see [AWS Proton Service Deprecation and Migration Guide](https://docs.aws.amazon.com/proton/latest/userguide/proton-end-of-support.html).

# GetDeployment
<a name="API_GetDeployment"></a>

Get detailed data for a deployment.

## Request Syntax
<a name="API_GetDeployment_RequestSyntax"></a>

```
{
   "componentName": "{{string}}",
   "environmentName": "{{string}}",
   "id": "{{string}}",
   "serviceInstanceName": "{{string}}",
   "serviceName": "{{string}}"
}
```

## Request Parameters
<a name="API_GetDeployment_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [componentName](#API_GetDeployment_RequestSyntax) **   <a name="proton-GetDeployment-request-componentName"></a>
The name of a component that you want to get the detailed data for.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Pattern: `[0-9A-Za-z]+[0-9A-Za-z_\-]*`
Required: No

 ** [environmentName](#API_GetDeployment_RequestSyntax) **   <a name="proton-GetDeployment-request-environmentName"></a>
The name of a environment that you want to get the detailed data for.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Pattern: `[0-9A-Za-z]+[0-9A-Za-z_\-]*`
Required: No

 ** [id](#API_GetDeployment_RequestSyntax) **   <a name="proton-GetDeployment-request-id"></a>
The ID of the deployment that you want to get the detailed data for.
Type: String
Pattern: `[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}`
Required: Yes

 ** [serviceInstanceName](#API_GetDeployment_RequestSyntax) **   <a name="proton-GetDeployment-request-serviceInstanceName"></a>
The name of the service instance associated with the given deployment ID. `serviceName` must be specified to identify the service instance.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Pattern: `[0-9A-Za-z]+[0-9A-Za-z_\-]*`
Required: No

 ** [serviceName](#API_GetDeployment_RequestSyntax) **   <a name="proton-GetDeployment-request-serviceName"></a>
The name of the service associated with the given deployment ID.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Pattern: `[0-9A-Za-z]+[0-9A-Za-z_\-]*`
Required: No

## Response Syntax
<a name="API_GetDeployment_ResponseSyntax"></a>

```
{
   "deployment": {
      "arn": "string",
      "completedAt": number,
      "componentName": "string",
      "createdAt": number,
      "deploymentStatus": "string",
      "deploymentStatusMessage": "string",
      "environmentName": "string",
      "id": "string",
      "initialState": { ... },
      "lastAttemptedDeploymentId": "string",
      "lastModifiedAt": number,
      "lastSucceededDeploymentId": "string",
      "serviceInstanceName": "string",
      "serviceName": "string",
      "targetArn": "string",
      "targetResourceCreatedAt": number,
      "targetResourceType": "string",
      "targetState": { ... }
   }
}
```

## Response Elements
<a name="API_GetDeployment_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [deployment](#API_GetDeployment_ResponseSyntax) **   <a name="proton-GetDeployment-response-deployment"></a>
The detailed data of the requested deployment.
Type: [Deployment](API_Deployment.md) object

## Errors
<a name="API_GetDeployment_Errors"></a>

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
<a name="API_GetDeployment_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/proton-2020-07-20/GetDeployment)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/proton-2020-07-20/GetDeployment)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/proton-2020-07-20/GetDeployment)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/proton-2020-07-20/GetDeployment)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/proton-2020-07-20/GetDeployment)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/proton-2020-07-20/GetDeployment)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/proton-2020-07-20/GetDeployment)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/proton-2020-07-20/GetDeployment)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/proton-2020-07-20/GetDeployment)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/proton-2020-07-20/GetDeployment)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Proton. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query proton` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
