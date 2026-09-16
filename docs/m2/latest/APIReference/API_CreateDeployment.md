---
source_url: https://docs.aws.amazon.com/m2/latest/APIReference/API_CreateDeployment.html
---

# CreateDeployment
<a name="API_CreateDeployment"></a>

**Important**
 AWS Mainframe Modernization Service (Managed Runtime Environment experience) will no longer be open to new customers starting on November 7, 2025. If you would like to use the service, please sign up prior to November 7, 2025. For capabilities similar to AWS Mainframe Modernization Service (Managed Runtime Environment experience) explore AWS Mainframe Modernization Service (Self-Managed Experience). Existing customers can continue to use the service as normal. For more information, see [AWS Mainframe Modernization availability change](https://docs.aws.amazon.com/m2/latest/userguide/mainframe-modernization-availability-change.html).

Creates and starts a deployment to deploy an application into a runtime environment.

## Request Syntax
<a name="API_CreateDeployment_RequestSyntax"></a>

```
POST /applications/{{applicationId}}/deployments HTTP/1.1
Content-type: application/json

{
   "applicationVersion": {{number}},
   "clientToken": "{{string}}",
   "environmentId": "{{string}}"
}
```

## URI Request Parameters
<a name="API_CreateDeployment_RequestParameters"></a>

The request uses the following URI parameters.

 ** [applicationId](#API_CreateDeployment_RequestSyntax) **   <a name="m2-CreateDeployment-request-uri-applicationId"></a>
The application identifier.
Pattern: `\S{1,80}`
Required: Yes

## Request Body
<a name="API_CreateDeployment_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [applicationVersion](#API_CreateDeployment_RequestSyntax) **   <a name="m2-CreateDeployment-request-applicationVersion"></a>
The version of the application to deploy.
Type: Integer
Valid Range: Minimum value of 1.
Required: Yes

 ** [clientToken](#API_CreateDeployment_RequestSyntax) **   <a name="m2-CreateDeployment-request-clientToken"></a>
Unique, case-sensitive identifier you provide to ensure the idempotency of the request to create a deployment. The service generates the clientToken when the API call is triggered. The token expires after one hour, so if you retry the API within this timeframe with the same clientToken, you will get the same response. The service also handles deleting the clientToken after it expires.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 128.
Pattern: `[!-~]+`
Required: No

 ** [environmentId](#API_CreateDeployment_RequestSyntax) **   <a name="m2-CreateDeployment-request-environmentId"></a>
The identifier of the runtime environment where you want to deploy this application.
Type: String
Pattern: `\S{1,80}`
Required: Yes

## Response Syntax
<a name="API_CreateDeployment_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "deploymentId": "string"
}
```

## Response Elements
<a name="API_CreateDeployment_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [deploymentId](#API_CreateDeployment_ResponseSyntax) **   <a name="m2-CreateDeployment-response-deploymentId"></a>
The unique identifier of the deployment.
Type: String
Pattern: `\S{1,80}`

## Errors
<a name="API_CreateDeployment_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
The account or role doesn't have the right permissions to make the request.
HTTP Status Code: 403

 ** ConflictException **
The parameters provided in the request conflict with existing resources.
 ** resourceId **
The ID of the conflicting resource.
 ** resourceType **
The type of the conflicting resource.
HTTP Status Code: 409

 ** InternalServerException **
An unexpected error occurred during the processing of the request.
 ** retryAfterSeconds **
The number of seconds to wait before retrying the request.
HTTP Status Code: 500

 ** ResourceNotFoundException **
The specified resource was not found.
 ** resourceId **
The ID of the missing resource.
 ** resourceType **
The type of the missing resource.
HTTP Status Code: 404

 ** ServiceQuotaExceededException **
 AWS Mainframe Modernization Service (Managed Runtime Environment experience) will no longer be open to new customers starting on November 7, 2025. If you would like to use the service, please sign up prior to November 7, 2025. For capabilities similar to AWS Mainframe Modernization Service (Managed Runtime Environment experience) explore AWS Mainframe Modernization Service (Self-Managed Experience). Existing customers can continue to use the service as normal. For more information, see [AWS Mainframe Modernization availability change](https://docs.aws.amazon.com/m2/latest/userguide/mainframe-modernization-availability-change.html).
One or more quotas for AWS Mainframe Modernization exceeds the limit.
 ** quotaCode **
The identifier of the exceeded quota.
 ** resourceId **
The ID of the resource that is exceeding the quota limit.
 ** resourceType **
The type of resource that is exceeding the quota limit for AWS Mainframe Modernization.
 ** serviceCode **
A code that identifies the service that the exceeded quota belongs to.
HTTP Status Code: 402

 ** ThrottlingException **
The number of requests made exceeds the limit.
 ** quotaCode **
The identifier of the throttled request.
 ** retryAfterSeconds **
The number of seconds to wait before retrying the request.
 ** serviceCode **
The identifier of the service that the throttled request was made to.
HTTP Status Code: 429

 ** ValidationException **
One or more parameters provided in the request is not valid.
 ** fieldList **
The list of fields that failed service validation.
 ** reason **
The reason why it failed service validation.
HTTP Status Code: 400

## See Also
<a name="API_CreateDeployment_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/m2-2021-04-28/CreateDeployment)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/m2-2021-04-28/CreateDeployment)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/m2-2021-04-28/CreateDeployment)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/m2-2021-04-28/CreateDeployment)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/m2-2021-04-28/CreateDeployment)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/m2-2021-04-28/CreateDeployment)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/m2-2021-04-28/CreateDeployment)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/m2-2021-04-28/CreateDeployment)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/m2-2021-04-28/CreateDeployment)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/m2-2021-04-28/CreateDeployment)
