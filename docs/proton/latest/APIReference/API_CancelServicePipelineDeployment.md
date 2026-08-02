---
source_url: https://docs.aws.amazon.com/proton/latest/APIReference/API_CancelServicePipelineDeployment.html
---

AWS has decided to discontinue AWS Proton, with support ending on October 7, 2026. New customers will not be able to sign up after October 7, 2025, but existing customers can continue to use the service until October 7, 2026.For more information, see [AWS Proton Service Deprecation and Migration Guide](https://docs.aws.amazon.com/proton/latest/userguide/proton-end-of-support.html).

# CancelServicePipelineDeployment
<a name="API_CancelServicePipelineDeployment"></a>

Attempts to cancel a service pipeline deployment on an [UpdateServicePipeline](API_UpdateServicePipeline.md) action, if the deployment is `IN_PROGRESS`. For more information, see [Update a service pipeline](https://docs.aws.amazon.com/proton/latest/userguide/ag-svc-pipeline-update.html) in the * AWS Proton User guide*.

The following list includes potential cancellation scenarios.
+ If the cancellation attempt succeeds, the resulting deployment state is `CANCELLED`.
+ If the cancellation attempt fails, the resulting deployment state is `FAILED`.
+ If the current [UpdateServicePipeline](API_UpdateServicePipeline.md) action succeeds before the cancellation attempt starts, the resulting deployment state is `SUCCEEDED` and the cancellation attempt has no effect.

## Request Syntax
<a name="API_CancelServicePipelineDeployment_RequestSyntax"></a>

```
{
   "serviceName": "{{string}}"
}
```

## Request Parameters
<a name="API_CancelServicePipelineDeployment_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [serviceName](#API_CancelServicePipelineDeployment_RequestSyntax) **   <a name="proton-CancelServicePipelineDeployment-request-serviceName"></a>
The name of the service with the service pipeline deployment to cancel.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Pattern: `[0-9A-Za-z]+[0-9A-Za-z_\-]*`
Required: Yes

## Response Syntax
<a name="API_CancelServicePipelineDeployment_ResponseSyntax"></a>

```
{
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
   }
}
```

## Response Elements
<a name="API_CancelServicePipelineDeployment_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [pipeline](#API_CancelServicePipelineDeployment_ResponseSyntax) **   <a name="proton-CancelServicePipelineDeployment-response-pipeline"></a>
The service pipeline detail data that's returned by AWS Proton.
Type: [ServicePipeline](API_ServicePipeline.md) object

## Errors
<a name="API_CancelServicePipelineDeployment_Errors"></a>

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
<a name="API_CancelServicePipelineDeployment_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/proton-2020-07-20/CancelServicePipelineDeployment)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/proton-2020-07-20/CancelServicePipelineDeployment)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/proton-2020-07-20/CancelServicePipelineDeployment)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/proton-2020-07-20/CancelServicePipelineDeployment)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/proton-2020-07-20/CancelServicePipelineDeployment)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/proton-2020-07-20/CancelServicePipelineDeployment)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/proton-2020-07-20/CancelServicePipelineDeployment)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/proton-2020-07-20/CancelServicePipelineDeployment)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/proton-2020-07-20/CancelServicePipelineDeployment)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/proton-2020-07-20/CancelServicePipelineDeployment)
