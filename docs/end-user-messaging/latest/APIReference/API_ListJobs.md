---
source_url: https://docs.aws.amazon.com/end-user-messaging/latest/APIReference/API_ListJobs.html
---

# ListJobs
<a name="API_ListJobs"></a>

Retrieves a paginated list of the asynchronous jobs in your account. You can filter the results by status, brand profile, or operation type.

## Request Syntax
<a name="API_ListJobs_RequestSyntax"></a>

```
GET /v1/jobs?brandProfileId={{brandProfileId}}&maxResults={{maxResults}}&nextToken={{nextToken}}&operationType={{operationType}}&status={{status}} HTTP/1.1
```

## URI Request Parameters
<a name="API_ListJobs_RequestParameters"></a>

The request uses the following URI parameters.

 ** [brandProfileId](#API_ListJobs_RequestSyntax) **   <a name="endusermessaging-ListJobs-request-uri-brandProfileId"></a>
Filters the results to jobs for the specified brand profile.
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `[A-Za-z0-9_:/-]+`

 ** [maxResults](#API_ListJobs_RequestSyntax) **   <a name="endusermessaging-ListJobs-request-uri-maxResults"></a>
The maximum number of results to return per page.
Valid Range: Minimum value of 1. Maximum value of 100.

 ** [nextToken](#API_ListJobs_RequestSyntax) **   <a name="endusermessaging-ListJobs-request-uri-nextToken"></a>
The token to retrieve the next page of results. This value is returned when more results are available, and is null when there are no more results to return.
Length Constraints: Minimum length of 1. Maximum length of 2048.
Pattern: `.+`

 ** [operationType](#API_ListJobs_RequestSyntax) **   <a name="endusermessaging-ListJobs-request-uri-operationType"></a>
Filters the results to jobs of the specified operation type.
Length Constraints: Minimum length of 1. Maximum length of 128.

 ** [status](#API_ListJobs_RequestSyntax) **   <a name="endusermessaging-ListJobs-request-uri-status"></a>
Filters the results to jobs that have the specified status.
Valid Values: `SUCCESS | PROCESSING | FAILED`

## Request Body
<a name="API_ListJobs_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_ListJobs_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "jobs": [
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
   ],
   "nextToken": "string"
}
```

## Response Elements
<a name="API_ListJobs_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [jobs](#API_ListJobs_ResponseSyntax) **   <a name="endusermessaging-ListJobs-response-jobs"></a>
The list of asynchronous jobs.
Type: Array of [JobSummary](API_JobSummary.md) objects
Array Members: Minimum number of 0 items. Maximum number of 100 items.

 ** [nextToken](#API_ListJobs_ResponseSyntax) **   <a name="endusermessaging-ListJobs-response-nextToken"></a>
The token to retrieve the next page of results. This value is returned when more results are available, and is null when there are no more results to return.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Pattern: `.+`

## Errors
<a name="API_ListJobs_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You do not have sufficient access to perform this action.
HTTP Status Code: 403

 ** InternalServerException **
An unexpected error occurred during the processing of the request.
HTTP Status Code: 500

 ** ThrottlingException **
The request was denied because it exceeded the allowed request rate.
HTTP Status Code: 429

 ** ValidationException **
The input fails to satisfy the constraints specified by the service. Check your request parameters and retry the request.
HTTP Status Code: 400

## See Also
<a name="API_ListJobs_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/endusermessaging-2026-09-21/ListJobs)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/endusermessaging-2026-09-21/ListJobs)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/endusermessaging-2026-09-21/ListJobs)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/endusermessaging-2026-09-21/ListJobs)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/endusermessaging-2026-09-21/ListJobs)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/endusermessaging-2026-09-21/ListJobs)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/endusermessaging-2026-09-21/ListJobs)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/endusermessaging-2026-09-21/ListJobs)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/endusermessaging-2026-09-21/ListJobs)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/endusermessaging-2026-09-21/ListJobs)
