---
source_url: https://docs.aws.amazon.com/entityresolution/latest/apireference/API_GetIdMappingJob.html
---

# GetIdMappingJob
<a name="API_GetIdMappingJob"></a>

Returns the status, metrics, and errors (if there are any) that are associated with a job.

## Request Syntax
<a name="API_GetIdMappingJob_RequestSyntax"></a>

```
GET /idmappingworkflows/{{workflowName}}/jobs/{{jobId}} HTTP/1.1
```

## URI Request Parameters
<a name="API_GetIdMappingJob_RequestParameters"></a>

The request uses the following URI parameters.

 ** [jobId](#API_GetIdMappingJob_RequestSyntax) **   <a name="API-GetIdMappingJob-request-uri-jobId"></a>
The ID of the job.
Pattern: `[a-f0-9]{32}`
Required: Yes

 ** [workflowName](#API_GetIdMappingJob_RequestSyntax) **   <a name="API-GetIdMappingJob-request-uri-workflowName"></a>
The name of the workflow.
Pattern: `[a-zA-Z_0-9-=+/]*$|^arn:(aws|aws-us-gov|aws-cn):entityresolution:[a-z]{2}-[a-z]{1,10}-[0-9]:[0-9]{12}:(idmappingworkflow/[a-zA-Z_0-9-]{1,255})`
Required: Yes

## Request Body
<a name="API_GetIdMappingJob_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_GetIdMappingJob_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "endTime": number,
   "errorDetails": {
      "errorMessage": "string"
   },
   "jobId": "string",
   "jobType": "string",
   "metrics": {
      "deleteRecordsProcessed": number,
      "inputRecords": number,
      "mappedRecordsRemoved": number,
      "mappedSourceRecordsRemoved": number,
      "mappedTargetRecordsRemoved": number,
      "newMappedRecords": number,
      "newMappedSourceRecords": number,
      "newMappedTargetRecords": number,
      "newUniqueRecordsLoaded": number,
      "recordsNotProcessed": number,
      "totalMappedRecords": number,
      "totalMappedSourceRecords": number,
      "totalMappedTargetRecords": number,
      "totalRecordsProcessed": number,
      "uniqueRecordsLoaded": number
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
<a name="API_GetIdMappingJob_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [endTime](#API_GetIdMappingJob_ResponseSyntax) **   <a name="API-GetIdMappingJob-response-endTime"></a>
The time at which the job has finished.
Type: Timestamp

 ** [errorDetails](#API_GetIdMappingJob_ResponseSyntax) **   <a name="API-GetIdMappingJob-response-errorDetails"></a>
An object containing an error message, if there was an error.
Type: [ErrorDetails](API_ErrorDetails.md) object

 ** [jobId](#API_GetIdMappingJob_ResponseSyntax) **   <a name="API-GetIdMappingJob-response-jobId"></a>
The ID of the job.
Type: String
Pattern: `[a-f0-9]{32}`

 ** [jobType](#API_GetIdMappingJob_ResponseSyntax) **   <a name="API-GetIdMappingJob-response-jobType"></a>
 The job type of the ID mapping job.
A value of `INCREMENTAL` indicates that only new or changed data was processed since the last job run. This is the default job type if the workflow was created with an `incrementalRunConfig`.
A value of `BATCH` indicates that all data was processed from the input source, regardless of previous job runs. This is the default job type if the workflow wasn't created with an `incrementalRunConfig`.
A value of `DELETE_ONLY` indicates that only deletion requests from `BatchDeleteUniqueIds` were processed.
Type: String
Valid Values: `BATCH | INCREMENTAL | DELETE_ONLY`

 ** [metrics](#API_GetIdMappingJob_ResponseSyntax) **   <a name="API-GetIdMappingJob-response-metrics"></a>
Metrics associated with the execution, specifically total records processed, unique IDs generated, and records the execution skipped.
Type: [IdMappingJobMetrics](API_IdMappingJobMetrics.md) object

 ** [outputSourceConfig](#API_GetIdMappingJob_ResponseSyntax) **   <a name="API-GetIdMappingJob-response-outputSourceConfig"></a>
A list of `OutputSource` objects.
Type: Array of [IdMappingJobOutputSource](API_IdMappingJobOutputSource.md) objects
Array Members: Fixed number of 1 item.

 ** [startTime](#API_GetIdMappingJob_ResponseSyntax) **   <a name="API-GetIdMappingJob-response-startTime"></a>
The time at which the job was started.
Type: Timestamp

 ** [status](#API_GetIdMappingJob_ResponseSyntax) **   <a name="API-GetIdMappingJob-response-status"></a>
The current status of the job.
Type: String
Valid Values: `RUNNING | SUCCEEDED | FAILED | QUEUED`

## Errors
<a name="API_GetIdMappingJob_Errors"></a>

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
<a name="API_GetIdMappingJob_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/entityresolution-2018-05-10/GetIdMappingJob)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/entityresolution-2018-05-10/GetIdMappingJob)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/entityresolution-2018-05-10/GetIdMappingJob)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/entityresolution-2018-05-10/GetIdMappingJob)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/entityresolution-2018-05-10/GetIdMappingJob)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/entityresolution-2018-05-10/GetIdMappingJob)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/entityresolution-2018-05-10/GetIdMappingJob)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/entityresolution-2018-05-10/GetIdMappingJob)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/entityresolution-2018-05-10/GetIdMappingJob)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/entityresolution-2018-05-10/GetIdMappingJob)
