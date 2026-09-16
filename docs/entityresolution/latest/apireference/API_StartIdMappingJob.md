---
source_url: https://docs.aws.amazon.com/entityresolution/latest/apireference/API_StartIdMappingJob.html
---

# StartIdMappingJob
<a name="API_StartIdMappingJob"></a>

Starts the `IdMappingJob` of a workflow. The workflow must have previously been created using the `CreateIdMappingWorkflow` endpoint.

## Request Syntax
<a name="API_StartIdMappingJob_RequestSyntax"></a>

```
POST /idmappingworkflows/{{workflowName}}/jobs HTTP/1.1
Content-type: application/json

{
   "jobType": "{{string}}",
   "outputSourceConfig": [
      {
         "KMSArn": "{{string}}",
         "outputS3Path": "{{string}}",
         "roleArn": "{{string}}"
      }
   ]
}
```

## URI Request Parameters
<a name="API_StartIdMappingJob_RequestParameters"></a>

The request uses the following URI parameters.

 ** [workflowName](#API_StartIdMappingJob_RequestSyntax) **   <a name="API-StartIdMappingJob-request-uri-workflowName"></a>
The name of the ID mapping job to be retrieved.
Pattern: `[a-zA-Z_0-9-=+/]*$|^arn:(aws|aws-us-gov|aws-cn):entityresolution:[a-z]{2}-[a-z]{1,10}-[0-9]:[0-9]{12}:(idmappingworkflow/[a-zA-Z_0-9-]{1,255})`
Required: Yes

## Request Body
<a name="API_StartIdMappingJob_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [jobType](#API_StartIdMappingJob_RequestSyntax) **   <a name="API-StartIdMappingJob-request-jobType"></a>
 The job type for the ID mapping job.
If the `jobType` value is set to `INCREMENTAL`, only new or changed data is processed since the last job run. This is the default value if the `CreateIdMappingWorkflow` API is configured with an `incrementalRunConfig`.
If the `jobType` value is set to `BATCH`, all data is processed from the input source, regardless of previous job runs. This is the default value if the `CreateIdMappingWorkflow` API isn't configured with an `incrementalRunConfig`.
If the `jobType` value is set to `DELETE_ONLY`, only deletion requests from `BatchDeleteUniqueIds` are processed.
Type: String
Valid Values: `BATCH | INCREMENTAL | DELETE_ONLY`
Required: No

 ** [outputSourceConfig](#API_StartIdMappingJob_RequestSyntax) **   <a name="API-StartIdMappingJob-request-outputSourceConfig"></a>
A list of `OutputSource` objects.
Type: Array of [IdMappingJobOutputSource](API_IdMappingJobOutputSource.md) objects
Array Members: Fixed number of 1 item.
Required: No

## Response Syntax
<a name="API_StartIdMappingJob_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "jobId": "string",
   "jobType": "string",
   "outputSourceConfig": [
      {
         "KMSArn": "string",
         "outputS3Path": "string",
         "roleArn": "string"
      }
   ]
}
```

## Response Elements
<a name="API_StartIdMappingJob_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [jobId](#API_StartIdMappingJob_ResponseSyntax) **   <a name="API-StartIdMappingJob-response-jobId"></a>
The ID of the job.
Type: String
Pattern: `[a-f0-9]{32}`

 ** [jobType](#API_StartIdMappingJob_ResponseSyntax) **   <a name="API-StartIdMappingJob-response-jobType"></a>
 The job type for the started ID mapping job.
A value of `INCREMENTAL` indicates that only new or changed data was processed since the last job run. This is the default job type if the workflow was created with an `incrementalRunConfig`.
A value of `BATCH` indicates that all data was processed from the input source, regardless of previous job runs. This is the default job type if the workflow wasn't created with an `incrementalRunConfig`.
A value of `DELETE_ONLY` indicates that only deletion requests from `BatchDeleteUniqueIds` were processed.
Type: String
Valid Values: `BATCH | INCREMENTAL | DELETE_ONLY`

 ** [outputSourceConfig](#API_StartIdMappingJob_ResponseSyntax) **   <a name="API-StartIdMappingJob-response-outputSourceConfig"></a>
A list of `OutputSource` objects.
Type: Array of [IdMappingJobOutputSource](API_IdMappingJobOutputSource.md) objects
Array Members: Fixed number of 1 item.

## Errors
<a name="API_StartIdMappingJob_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You do not have sufficient access to perform this action.
HTTP Status Code: 403

 ** ConflictException **
The request couldn't be processed because of conflict in the current state of the resource. Example: Workflow already exists, Schema already exists, Workflow is currently running, etc.
HTTP Status Code: 400

 ** ExceedsLimitException **
The request was rejected because it attempted to create resources beyond the current AWS Entity Resolution account limits. The error message describes the limit exceeded.
 ** quotaName **
The name of the quota that has been breached.
 ** quotaValue **
The current quota value for the customers.
HTTP Status Code: 402

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
<a name="API_StartIdMappingJob_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/entityresolution-2018-05-10/StartIdMappingJob)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/entityresolution-2018-05-10/StartIdMappingJob)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/entityresolution-2018-05-10/StartIdMappingJob)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/entityresolution-2018-05-10/StartIdMappingJob)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/entityresolution-2018-05-10/StartIdMappingJob)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/entityresolution-2018-05-10/StartIdMappingJob)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/entityresolution-2018-05-10/StartIdMappingJob)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/entityresolution-2018-05-10/StartIdMappingJob)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/entityresolution-2018-05-10/StartIdMappingJob)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/entityresolution-2018-05-10/StartIdMappingJob)
