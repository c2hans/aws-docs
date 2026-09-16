---
source_url: https://docs.aws.amazon.com/m2/latest/APIReference/API_GetDeployment.html
---

# GetDeployment
<a name="API_GetDeployment"></a>

**Important**
 AWS Mainframe Modernization Service (Managed Runtime Environment experience) will no longer be open to new customers starting on November 7, 2025. If you would like to use the service, please sign up prior to November 7, 2025. For capabilities similar to AWS Mainframe Modernization Service (Managed Runtime Environment experience) explore AWS Mainframe Modernization Service (Self-Managed Experience). Existing customers can continue to use the service as normal. For more information, see [AWS Mainframe Modernization availability change](https://docs.aws.amazon.com/m2/latest/userguide/mainframe-modernization-availability-change.html).

Gets details of a specific deployment with a given deployment identifier.

## Request Syntax
<a name="API_GetDeployment_RequestSyntax"></a>

```
GET /applications/{{applicationId}}/deployments/{{deploymentId}} HTTP/1.1
```

## URI Request Parameters
<a name="API_GetDeployment_RequestParameters"></a>

The request uses the following URI parameters.

 ** [applicationId](#API_GetDeployment_RequestSyntax) **   <a name="m2-GetDeployment-request-uri-applicationId"></a>
The unique identifier of the application.
Pattern: `\S{1,80}`
Required: Yes

 ** [deploymentId](#API_GetDeployment_RequestSyntax) **   <a name="m2-GetDeployment-request-uri-deploymentId"></a>
The unique identifier for the deployment.
Pattern: `\S{1,80}`
Required: Yes

## Request Body
<a name="API_GetDeployment_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_GetDeployment_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "applicationId": "string",
   "applicationVersion": number,
   "creationTime": number,
   "deploymentId": "string",
   "environmentId": "string",
   "status": "string",
   "statusReason": "string"
}
```

## Response Elements
<a name="API_GetDeployment_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [applicationId](#API_GetDeployment_ResponseSyntax) **   <a name="m2-GetDeployment-response-applicationId"></a>
The unique identifier of the application.
Type: String
Pattern: `\S{1,80}`

 ** [applicationVersion](#API_GetDeployment_ResponseSyntax) **   <a name="m2-GetDeployment-response-applicationVersion"></a>
The application version.
Type: Integer
Valid Range: Minimum value of 1.

 ** [creationTime](#API_GetDeployment_ResponseSyntax) **   <a name="m2-GetDeployment-response-creationTime"></a>
The timestamp when the deployment was created.
Type: Timestamp

 ** [deploymentId](#API_GetDeployment_ResponseSyntax) **   <a name="m2-GetDeployment-response-deploymentId"></a>
The unique identifier of the deployment.
Type: String
Pattern: `\S{1,80}`

 ** [environmentId](#API_GetDeployment_ResponseSyntax) **   <a name="m2-GetDeployment-response-environmentId"></a>
The unique identifier of the runtime environment.
Type: String
Pattern: `\S{1,80}`

 ** [status](#API_GetDeployment_ResponseSyntax) **   <a name="m2-GetDeployment-response-status"></a>
The status of the deployment.
Type: String
Valid Values: `Deploying | Succeeded | Failed | Updating Deployment`

 ** [statusReason](#API_GetDeployment_ResponseSyntax) **   <a name="m2-GetDeployment-response-statusReason"></a>
The reason for the reported status.
Type: String

## Errors
<a name="API_GetDeployment_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
The account or role doesn't have the right permissions to make the request.
HTTP Status Code: 403

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
<a name="API_GetDeployment_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/m2-2021-04-28/GetDeployment)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/m2-2021-04-28/GetDeployment)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/m2-2021-04-28/GetDeployment)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/m2-2021-04-28/GetDeployment)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/m2-2021-04-28/GetDeployment)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/m2-2021-04-28/GetDeployment)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/m2-2021-04-28/GetDeployment)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/m2-2021-04-28/GetDeployment)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/m2-2021-04-28/GetDeployment)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/m2-2021-04-28/GetDeployment)
