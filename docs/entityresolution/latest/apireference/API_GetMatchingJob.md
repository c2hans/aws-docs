---
source_url: https://docs.aws.amazon.com/entityresolution/latest/apireference/API_GetMatchingJob.html
---

# GetMatchingJob
<a name="API_GetMatchingJob"></a>

Returns the status, metrics, and errors (if there are any) that are associated with a job.

## Request Syntax
<a name="API_GetMatchingJob_RequestSyntax"></a>

```
GET /matchingworkflows/{{workflowName}}/jobs/{{jobId}} HTTP/1.1
```

## URI Request Parameters
<a name="API_GetMatchingJob_RequestParameters"></a>

The request uses the following URI parameters.

 ** [jobId](#API_GetMatchingJob_RequestSyntax) **   <a name="API-GetMatchingJob-request-uri-jobId"></a>
The ID of the job.
Pattern: `[a-f0-9]{32}`
Required: Yes

 ** [workflowName](#API_GetMatchingJob_RequestSyntax) **   <a name="API-GetMatchingJob-request-uri-workflowName"></a>
The name of the workflow.
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[a-zA-Z_0-9-]*`
Required: Yes

## Request Body
<a name="API_GetMatchingJob_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_GetMatchingJob_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "endTime": number,
   "errorDetails": {
      "errorMessage": "string"
   },
   "jobId": "string",
   "metrics": {
      "deleteRecordsProcessed": number,
      "inputRecords": number,
      "matchIDs": number,
      "recordsNotProcessed": number,
      "totalRecordsProcessed": number
   },
   "outputSourceConfig": [
      {
         "KMSArn": "string",
         "outputS3Path": "string",
         "roleArn": "string"
      }
   ],
   "startTime": number,
   "status": "string"
}
```

## Response Elements
<a name="API_GetMatchingJob_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [endTime](#API_GetMatchingJob_ResponseSyntax) **   <a name="API-GetMatchingJob-response-endTime"></a>
The time at which the job has finished.
Type: Timestamp

 ** [errorDetails](#API_GetMatchingJob_ResponseSyntax) **   <a name="API-GetMatchingJob-response-errorDetails"></a>
An object containing an error message, if there was an error.
Type: [ErrorDetails](API_ErrorDetails.md) object

 ** [jobId](#API_GetMatchingJob_ResponseSyntax) **   <a name="API-GetMatchingJob-response-jobId"></a>
The unique identifier of the matching job.
Type: String
Pattern: `[a-f0-9]{32}`

 ** [metrics](#API_GetMatchingJob_ResponseSyntax) **   <a name="API-GetMatchingJob-response-metrics"></a>
Metrics associated with the execution, specifically total records processed, unique IDs generated, and records the execution skipped.
Type: [JobMetrics](API_JobMetrics.md) object

 ** [outputSourceConfig](#API_GetMatchingJob_ResponseSyntax) **   <a name="API-GetMatchingJob-response-outputSourceConfig"></a>
A list of `OutputSource` objects.
Type: Array of [JobOutputSource](API_JobOutputSource.md) objects
Array Members: Fixed number of 1 item.

 ** [startTime](#API_GetMatchingJob_ResponseSyntax) **   <a name="API-GetMatchingJob-response-startTime"></a>
The time at which the job was started.
Type: Timestamp

 ** [status](#API_GetMatchingJob_ResponseSyntax) **   <a name="API-GetMatchingJob-response-status"></a>
The current status of the job.
Type: String
Valid Values: `RUNNING | SUCCEEDED | FAILED | QUEUED`

## Errors
<a name="API_GetMatchingJob_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You do not have sufficient access to perform this action.
HTTP Status Code: 403

 ** InternalServerException **
This exception occurs when there is an internal failure in the AWS Entity Resolution service.
HTTP Status Code: 500

 ** ResourceNotFoundException **
The resource couldn't be found.
HTTP Status Code: 404

 ** ThrottlingException **
The request was denied due to request throttling.
HTTP Status Code: 429

 ** ValidationException **
The input fails to satisfy the constraints specified by AWS Entity Resolution.
HTTP Status Code: 400

## See Also
<a name="API_GetMatchingJob_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/entityresolution-2018-05-10/GetMatchingJob)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/entityresolution-2018-05-10/GetMatchingJob)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/entityresolution-2018-05-10/GetMatchingJob)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/entityresolution-2018-05-10/GetMatchingJob)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/entityresolution-2018-05-10/GetMatchingJob)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/entityresolution-2018-05-10/GetMatchingJob)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/entityresolution-2018-05-10/GetMatchingJob)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/entityresolution-2018-05-10/GetMatchingJob)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/entityresolution-2018-05-10/GetMatchingJob)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/entityresolution-2018-05-10/GetMatchingJob)
