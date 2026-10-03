---
source_url: https://docs.aws.amazon.com/end-user-messaging/latest/APIReference/API_GetJob.html
---

# GetJob
<a name="API_GetJob"></a>

Retrieves the current state of an asynchronous job, including its status and any resources that it created or updated.

## Request Syntax
<a name="API_GetJob_RequestSyntax"></a>

```
GET /v1/jobs/{{jobId}} HTTP/1.1
```

## URI Request Parameters
<a name="API_GetJob_RequestParameters"></a>

The request uses the following URI parameters.

 ** [jobId](#API_GetJob_RequestSyntax) **   <a name="endusermessaging-GetJob-request-uri-jobId"></a>
The unique identifier of the asynchronous job. Use the GetJob operation to check the status of the job and to retrieve its results.
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[A-Za-z0-9_-]+`
Required: Yes

## Request Body
<a name="API_GetJob_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_GetJob_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "brandProfileId": "string",
   "createdAt": number,
   "errorCode": "string",
   "errorMessage": "string",
   "jobId": "string",
   "operationType": "string",
   "resources": [
      {
         "resourceArn": "string",
         "resourceId": "string",
         "resourceType": "string"
      }
   ],
   "status": "string",
   "updatedAt": number
}
```

## Response Elements
<a name="API_GetJob_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [brandProfileId](#API_GetJob_ResponseSyntax) **   <a name="endusermessaging-GetJob-response-brandProfileId"></a>
The brand profile that the job operates on. This value is absent for operations that create a brand profile.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `[A-Za-z0-9_:/-]+`

 ** [createdAt](#API_GetJob_ResponseSyntax) **   <a name="endusermessaging-GetJob-response-createdAt"></a>
The time when the resource was created, in Unix epoch time.
Type: Timestamp

 ** [errorCode](#API_GetJob_ResponseSyntax) **   <a name="endusermessaging-GetJob-response-errorCode"></a>
A machine-readable code that identifies why the job failed. This value is present only when the job status is FAILED.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.

 ** [errorMessage](#API_GetJob_ResponseSyntax) **   <a name="endusermessaging-GetJob-response-errorMessage"></a>
A human-readable description of why the job failed. This value is present only when the job status is FAILED.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.

 ** [jobId](#API_GetJob_ResponseSyntax) **   <a name="endusermessaging-GetJob-response-jobId"></a>
The unique identifier of the asynchronous job. Use the GetJob operation to check the status of the job and to retrieve its results.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[A-Za-z0-9_-]+`

 ** [operationType](#API_GetJob_ResponseSyntax) **   <a name="endusermessaging-GetJob-response-operationType"></a>
The type of mutating operation that created the job.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.

 ** [resources](#API_GetJob_ResponseSyntax) **   <a name="endusermessaging-GetJob-response-resources"></a>
The resources that were created or updated by the job.
Type: Array of [JobResource](API_JobResource.md) objects
Array Members: Minimum number of 1 item. Maximum number of 10 items.

 ** [status](#API_GetJob_ResponseSyntax) **   <a name="endusermessaging-GetJob-response-status"></a>
The current lifecycle status of the job.
Type: String
Valid Values: `SUCCESS | PROCESSING | FAILED`

 ** [updatedAt](#API_GetJob_ResponseSyntax) **   <a name="endusermessaging-GetJob-response-updatedAt"></a>
The time when the resource was last updated, in Unix epoch time.
Type: Timestamp

## Errors
<a name="API_GetJob_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You do not have sufficient access to perform this action.
HTTP Status Code: 403

 ** InternalServerException **
An unexpected error occurred during the processing of the request.
HTTP Status Code: 500

 ** ResourceNotFoundException **
The request references a resource that does not exist. Verify that the resource identifier is correct and try your request again.
 ** resourceId **
The identifier of the resource that could not be found.
 ** resourceType **
The type of the resource that could not be found.
HTTP Status Code: 404

 ** ThrottlingException **
The request was denied because it exceeded the allowed request rate.
HTTP Status Code: 429

 ** ValidationException **
The input fails to satisfy the constraints specified by the service. Check your request parameters and retry the request.
HTTP Status Code: 400

## See Also
<a name="API_GetJob_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/endusermessaging-2026-09-21/GetJob)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/endusermessaging-2026-09-21/GetJob)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/endusermessaging-2026-09-21/GetJob)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/endusermessaging-2026-09-21/GetJob)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/endusermessaging-2026-09-21/GetJob)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/endusermessaging-2026-09-21/GetJob)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/endusermessaging-2026-09-21/GetJob)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/endusermessaging-2026-09-21/GetJob)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/endusermessaging-2026-09-21/GetJob)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/endusermessaging-2026-09-21/GetJob)
