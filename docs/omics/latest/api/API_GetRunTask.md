---
source_url: https://docs.aws.amazon.com/omics/latest/api/API_GetRunTask.html
---

# GetRunTask
<a name="API_GetRunTask"></a>

Gets detailed information about a run task using its ID.

## Request Syntax
<a name="API_GetRunTask_RequestSyntax"></a>

```
GET /run/{{id}}/task/{{taskId}} HTTP/1.1
```

## URI Request Parameters
<a name="API_GetRunTask_RequestParameters"></a>

The request uses the following URI parameters.

 ** [id](#API_GetRunTask_RequestSyntax) **   <a name="omics-GetRunTask-request-uri-id"></a>
The workflow run ID.
Length Constraints: Minimum length of 1. Maximum length of 18.
Pattern: `[0-9]+`
Required: Yes

 ** [taskId](#API_GetRunTask_RequestSyntax) **   <a name="omics-GetRunTask-request-uri-taskId"></a>
The task's ID.
Length Constraints: Minimum length of 1. Maximum length of 18.
Pattern: `[0-9]+`
Required: Yes

## Request Body
<a name="API_GetRunTask_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_GetRunTask_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "cacheHit": boolean,
   "cacheS3Uri": "string",
   "cpus": number,
   "creationTime": "string",
   "failureReason": "string",
   "gpus": number,
   "imageDetails": {
      "image": "string",
      "imageDigest": "string",
      "sourceImage": "string"
   },
   "instanceType": "string",
   "logStream": "string",
   "memory": number,
   "name": "string",
   "startTime": "string",
   "status": "string",
   "statusMessage": "string",
   "stopTime": "string",
   "taskId": "string"
}
```

## Response Elements
<a name="API_GetRunTask_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [cacheHit](#API_GetRunTask_ResponseSyntax) **   <a name="omics-GetRunTask-response-cacheHit"></a>
Set to true if AWS HealthOmics found a matching entry in the run cache for this task.
Type: Boolean

 ** [cacheS3Uri](#API_GetRunTask_ResponseSyntax) **   <a name="omics-GetRunTask-response-cacheS3Uri"></a>
The S3 URI of the cache location.
Type: String
Pattern: `s3://([a-z0-9][a-z0-9-.]{1,61}[a-z0-9])(/(.{0,1024}))?`

 ** [cpus](#API_GetRunTask_ResponseSyntax) **   <a name="omics-GetRunTask-response-cpus"></a>
The task's CPU usage.
Type: Integer
Valid Range: Minimum value of 1.

 ** [creationTime](#API_GetRunTask_ResponseSyntax) **   <a name="omics-GetRunTask-response-creationTime"></a>
When the task was created.
Type: Timestamp

 ** [failureReason](#API_GetRunTask_ResponseSyntax) **   <a name="omics-GetRunTask-response-failureReason"></a>
The reason a task has failed.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[\p{L}||\p{M}||\p{Z}||\p{S}||\p{N}||\p{P}]+`

 ** [gpus](#API_GetRunTask_ResponseSyntax) **   <a name="omics-GetRunTask-response-gpus"></a>
The number of Graphics Processing Units (GPU) specified in the task.
Type: Integer
Valid Range: Minimum value of 0.

 ** [imageDetails](#API_GetRunTask_ResponseSyntax) **   <a name="omics-GetRunTask-response-imageDetails"></a>
Details about the container image that this task uses.
Type: [ImageDetails](API_ImageDetails.md) object

 ** [instanceType](#API_GetRunTask_ResponseSyntax) **   <a name="omics-GetRunTask-response-instanceType"></a>
The instance type for a task.
Type: String
Pattern: `[\p{L}||\p{M}||\p{Z}||\p{S}||\p{N}||\p{P}]+`

 ** [logStream](#API_GetRunTask_ResponseSyntax) **   <a name="omics-GetRunTask-response-logStream"></a>
The task's log stream.
Type: String
Pattern: `[\p{L}||\p{M}||\p{Z}||\p{S}||\p{N}||\p{P}]+`

 ** [memory](#API_GetRunTask_ResponseSyntax) **   <a name="omics-GetRunTask-response-memory"></a>
The task's memory use in gigabytes.
Type: Integer
Valid Range: Minimum value of 1.

 ** [name](#API_GetRunTask_ResponseSyntax) **   <a name="omics-GetRunTask-response-name"></a>
The task's name.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.

 ** [startTime](#API_GetRunTask_ResponseSyntax) **   <a name="omics-GetRunTask-response-startTime"></a>
The task's start time.
Type: Timestamp

 ** [status](#API_GetRunTask_ResponseSyntax) **   <a name="omics-GetRunTask-response-status"></a>
The task's status.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Valid Values: `PENDING | STARTING | RUNNING | STOPPING | COMPLETED | CANCELLED | FAILED`

 ** [statusMessage](#API_GetRunTask_ResponseSyntax) **   <a name="omics-GetRunTask-response-statusMessage"></a>
The task's status message.
Type: String
Pattern: `[\p{L}||\p{M}||\p{Z}||\p{S}||\p{N}||\p{P}]+`

 ** [stopTime](#API_GetRunTask_ResponseSyntax) **   <a name="omics-GetRunTask-response-stopTime"></a>
The task's stop time.
Type: Timestamp

 ** [taskId](#API_GetRunTask_ResponseSyntax) **   <a name="omics-GetRunTask-response-taskId"></a>
The task's ID.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 18.
Pattern: `[0-9]+`

## Errors
<a name="API_GetRunTask_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You do not have sufficient access to perform this action.
HTTP Status Code: 403

 ** ConflictException **
The request cannot be applied to the target resource in its current state.
HTTP Status Code: 409

 ** InternalServerException **
An unexpected error occurred. Try the request again.
HTTP Status Code: 500

 ** RequestTimeoutException **
The request timed out.
HTTP Status Code: 408

 ** ResourceNotFoundException **
The target resource was not found in the current Region.
HTTP Status Code: 404

 ** ServiceQuotaExceededException **
The request exceeds a service quota.
HTTP Status Code: 402

 ** ThrottlingException **
The request was denied due to request throttling.
HTTP Status Code: 429

 ** ValidationException **
The input fails to satisfy the constraints specified by an AWS service.
HTTP Status Code: 400

## See Also
<a name="API_GetRunTask_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/omics-2022-11-28/GetRunTask)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/omics-2022-11-28/GetRunTask)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/omics-2022-11-28/GetRunTask)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/omics-2022-11-28/GetRunTask)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/omics-2022-11-28/GetRunTask)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/omics-2022-11-28/GetRunTask)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/omics-2022-11-28/GetRunTask)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/omics-2022-11-28/GetRunTask)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/omics-2022-11-28/GetRunTask)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/omics-2022-11-28/GetRunTask)
