---
source_url: https://docs.aws.amazon.com/proton/latest/APIReference/API_CancelServiceInstanceDeployment.html
---

AWS has decided to discontinue AWS Proton, with support ending on October 7, 2026. New customers will not be able to sign up after October 7, 2025, but existing customers can continue to use the service until October 7, 2026.For more information, see [AWS Proton Service Deprecation and Migration Guide](https://docs.aws.amazon.com/proton/latest/userguide/proton-end-of-support.html).

# CancelServiceInstanceDeployment
<a name="API_CancelServiceInstanceDeployment"></a>

Attempts to cancel a service instance deployment on an [UpdateServiceInstance](API_UpdateServiceInstance.md) action, if the deployment is `IN_PROGRESS`. For more information, see [Update a service instance](https://docs.aws.amazon.com/proton/latest/userguide/ag-svc-instance-update.html) in the * AWS Proton User guide*.

The following list includes potential cancellation scenarios.
+ If the cancellation attempt succeeds, the resulting deployment state is `CANCELLED`.
+ If the cancellation attempt fails, the resulting deployment state is `FAILED`.
+ If the current [UpdateServiceInstance](API_UpdateServiceInstance.md) action succeeds before the cancellation attempt starts, the resulting deployment state is `SUCCEEDED` and the cancellation attempt has no effect.

## Request Syntax
<a name="API_CancelServiceInstanceDeployment_RequestSyntax"></a>

```
{
   "serviceInstanceName": "{{string}}",
   "serviceName": "{{string}}"
}
```

## Request Parameters
<a name="API_CancelServiceInstanceDeployment_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [serviceInstanceName](#API_CancelServiceInstanceDeployment_RequestSyntax) **   <a name="proton-CancelServiceInstanceDeployment-request-serviceInstanceName"></a>
The name of the service instance with the deployment to cancel.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Pattern: `[0-9A-Za-z]+[0-9A-Za-z_\-]*`
Required: Yes

 ** [serviceName](#API_CancelServiceInstanceDeployment_RequestSyntax) **   <a name="proton-CancelServiceInstanceDeployment-request-serviceName"></a>
The name of the service with the service instance deployment to cancel.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Pattern: `[0-9A-Za-z]+[0-9A-Za-z_\-]*`
Required: Yes

## Response Syntax
<a name="API_CancelServiceInstanceDeployment_ResponseSyntax"></a>

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
<a name="API_CancelServiceInstanceDeployment_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [serviceInstance](#API_CancelServiceInstanceDeployment_ResponseSyntax) **   <a name="proton-CancelServiceInstanceDeployment-response-serviceInstance"></a>
The service instance summary data that's returned by AWS Proton.
Type: [ServiceInstance](API_ServiceInstance.md) object

## Errors
<a name="API_CancelServiceInstanceDeployment_Errors"></a>

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
<a name="API_CancelServiceInstanceDeployment_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/proton-2020-07-20/CancelServiceInstanceDeployment)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/proton-2020-07-20/CancelServiceInstanceDeployment)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/proton-2020-07-20/CancelServiceInstanceDeployment)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/proton-2020-07-20/CancelServiceInstanceDeployment)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/proton-2020-07-20/CancelServiceInstanceDeployment)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/proton-2020-07-20/CancelServiceInstanceDeployment)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/proton-2020-07-20/CancelServiceInstanceDeployment)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/proton-2020-07-20/CancelServiceInstanceDeployment)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/proton-2020-07-20/CancelServiceInstanceDeployment)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/proton-2020-07-20/CancelServiceInstanceDeployment)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Proton. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query proton` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
