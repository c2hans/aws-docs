---
source_url: https://docs.aws.amazon.com/iot-sitewise/latest/APIReference/API_CreateBulkImportJob.html
---

# CreateBulkImportJob
<a name="API_CreateBulkImportJob"></a>

Defines a job to ingest data to AWS IoT SiteWise from Amazon S3. For more information, see [Create a bulk import job (AWS CLI)](https://docs.aws.amazon.com/iot-sitewise/latest/userguide/CreateBulkImportJob.html) in the *Amazon Simple Storage Service User Guide*.

**Important**
Before you create a bulk import job that ingests data into time series outside of a workspace, you must enable AWS IoT SiteWise warm tier or AWS IoT SiteWise cold tier. For more information about how to configure storage settings, see [PutStorageConfiguration](https://docs.aws.amazon.com/iot-sitewise/latest/APIReference/API_PutStorageConfiguration.html). This requirement doesn't apply to bulk import jobs that ingest data into a session dataset in a workspace (jobs that specify a `workspaceName` and `datasetId`). Those jobs don't use AWS IoT SiteWise warm or cold tier storage.
Bulk import is designed to store historical data to AWS IoT SiteWise.
Newly ingested data in the hot tier triggers notifications and computations.
After data moves from the hot tier to the warm or cold tier based on retention settings, it does not trigger computations or notifications.
Data older than 7 days does not trigger computations or notifications.

## Request Syntax
<a name="API_CreateBulkImportJob_RequestSyntax"></a>

```
POST /jobs HTTP/1.1
Content-type: application/json

{
   "adaptiveIngestion": {{boolean}},
   "datasetId": "{{string}}",
   "deleteFilesAfterImport": {{boolean}},
   "errorReportLocation": {
      "bucket": "{{string}}",
      "prefix": "{{string}}"
   },
   "files": [
      {
         "alias": "{{string}}",
         "bucket": "{{string}}",
         "fileFormat": {
            "annotation": {
            },
            "csv": {
               "columnNames": [ "{{string}}" ]
            },
            "mp4": {
            },
            "parquet": {
            }
         },
         "key": "{{string}}",
         "startTime": {
            "offsetInNanos": {{number}},
            "timeInSeconds": {{number}}
         },
         "versionId": "{{string}}"
      }
   ],
   "jobConfiguration": {
      "fileFormat": {
         "annotation": {
         },
         "csv": {
            "columnNames": [ "{{string}}" ]
         },
         "mp4": {
         },
         "parquet": {
         }
      }
   },
   "jobName": "{{string}}",
   "jobRoleArn": "{{string}}",
   "workspaceName": "{{string}}"
}
```

## URI Request Parameters
<a name="API_CreateBulkImportJob_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_CreateBulkImportJob_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [adaptiveIngestion](#API_CreateBulkImportJob_RequestSyntax) **   <a name="iotsitewise-CreateBulkImportJob-request-adaptiveIngestion"></a>
If set to true, ingest new data into AWS IoT SiteWise storage. Measurements with notifications, metrics and transforms are computed. If set to false, historical data is ingested into AWS IoT SiteWise as is.
Type: Boolean
Required: No

 ** [datasetId](#API_CreateBulkImportJob_RequestSyntax) **   <a name="iotsitewise-CreateBulkImportJob-request-datasetId"></a>
The ID of the session dataset to ingest data into. Specify this field, together with `workspaceName`, to ingest data into a session dataset in a workspace.
Type: String
Length Constraints: Fixed length of 36.
Pattern: `^(?!00000000-0000-0000-0000-000000000000)[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$`
Required: No

 ** [deleteFilesAfterImport](#API_CreateBulkImportJob_RequestSyntax) **   <a name="iotsitewise-CreateBulkImportJob-request-deleteFilesAfterImport"></a>
If set to true, your data files is deleted from S3, after ingestion into AWS IoT SiteWise storage.
Type: Boolean
Required: No

 ** [errorReportLocation](#API_CreateBulkImportJob_RequestSyntax) **   <a name="iotsitewise-CreateBulkImportJob-request-errorReportLocation"></a>
The Amazon S3 destination where errors associated with the job creation request are saved.
Type: [ErrorReportLocation](API_ErrorReportLocation.md) object
Required: Yes

 ** [files](#API_CreateBulkImportJob_RequestSyntax) **   <a name="iotsitewise-CreateBulkImportJob-request-files"></a>
The files in the specified Amazon S3 bucket that contain your data. You can specify up to 100 files for each bulk import job. Each file supports the following size limits:
+ Parquet files – Up to 256 MiB.
+ Other file formats – Up to 5 GiB.
Type: Array of [File](API_File.md) objects
Required: Yes

 ** [jobConfiguration](#API_CreateBulkImportJob_RequestSyntax) **   <a name="iotsitewise-CreateBulkImportJob-request-jobConfiguration"></a>
Contains the configuration information of a job, such as the file format used to save data in Amazon S3.
Type: [JobConfiguration](API_JobConfiguration.md) object
Required: No

 ** [jobName](#API_CreateBulkImportJob_RequestSyntax) **   <a name="iotsitewise-CreateBulkImportJob-request-jobName"></a>
The unique name that helps identify the job request.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `^[\p{L}\p{N}\p{Zs}._:/-]+$`
Required: Yes

 ** [jobRoleArn](#API_CreateBulkImportJob_RequestSyntax) **   <a name="iotsitewise-CreateBulkImportJob-request-jobRoleArn"></a>
The [ARN](https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html) of the IAM role that allows AWS IoT SiteWise to read Amazon S3 data.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1600.
Pattern: `^arn:aws(-cn|-us-gov)?:[a-zA-Z0-9-:\/_\.]+$`
Required: Yes

 ** [workspaceName](#API_CreateBulkImportJob_RequestSyntax) **   <a name="iotsitewise-CreateBulkImportJob-request-workspaceName"></a>
The name of the workspace that contains the session dataset. Specify this field together with `datasetId`.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `^[a-zA-Z0-9_-]+$`
Required: No

## Response Syntax
<a name="API_CreateBulkImportJob_ResponseSyntax"></a>

```
HTTP/1.1 202
Content-type: application/json

{
   "jobId": "string",
   "jobName": "string",
   "jobStatus": "string"
}
```

## Response Elements
<a name="API_CreateBulkImportJob_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 202 response.

The following data is returned in JSON format by the service.

 ** [jobId](#API_CreateBulkImportJob_ResponseSyntax) **   <a name="iotsitewise-CreateBulkImportJob-response-jobId"></a>
The ID of the job.
Type: String
Length Constraints: Fixed length of 36.
Pattern: `^(?!00000000-0000-0000-0000-000000000000)[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$`

 ** [jobName](#API_CreateBulkImportJob_ResponseSyntax) **   <a name="iotsitewise-CreateBulkImportJob-response-jobName"></a>
The unique name that helps identify the job request.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `^[\p{L}\p{N}\p{Zs}._:/-]+$`

 ** [jobStatus](#API_CreateBulkImportJob_ResponseSyntax) **   <a name="iotsitewise-CreateBulkImportJob-response-jobStatus"></a>
The status of the bulk import job can be one of following values:
+  `PENDING` – AWS IoT SiteWise is waiting for the current bulk import job to finish.
+  `CANCELLED` – The bulk import job has been canceled.
+  `RUNNING` – AWS IoT SiteWise is processing your request to import your data from Amazon S3.
+  `COMPLETED` – AWS IoT SiteWise successfully completed your request to import data from Amazon S3.
+  `FAILED` – AWS IoT SiteWise couldn't process your request to import data from Amazon S3. You can use logs saved in the specified error report location in Amazon S3 to troubleshoot issues.
+  `COMPLETED_WITH_FAILURES` – AWS IoT SiteWise completed your request to import data from Amazon S3 with errors. You can use logs saved in the specified error report location in Amazon S3 to troubleshoot issues.
Type: String
Valid Values: `PENDING | CANCELLED | RUNNING | COMPLETED | FAILED | COMPLETED_WITH_FAILURES`

## Errors
<a name="API_CreateBulkImportJob_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** ConflictingOperationException **
Your request has conflicting operations. This can occur if you're trying to perform more than one operation on the same resource at the same time.
 ** resourceArn **
The ARN of the resource that conflicts with this operation.
 ** resourceId **
The ID of the resource that conflicts with this operation.
HTTP Status Code: 409

 ** InternalFailureException **
 AWS IoT SiteWise can't process your request right now. Try again later.
HTTP Status Code: 500

 ** InvalidRequestException **
The request isn't valid. This can occur if your request contains malformed JSON or unsupported characters. Check your request and try again.
HTTP Status Code: 400

 ** LimitExceededException **
You've reached the quota for a resource. For example, this can occur if you're trying to associate more than the allowed number of child assets or attempting to create more than the allowed number of properties for an asset model.
For more information, see [Quotas](https://docs.aws.amazon.com/iot-sitewise/latest/userguide/quotas.html) in the * AWS IoT SiteWise User Guide*.
HTTP Status Code: 410

 ** ResourceAlreadyExistsException **
The resource already exists.
 ** resourceArn **
The ARN of the resource that already exists.
 ** resourceId **
The ID of the resource that already exists.
HTTP Status Code: 409

 ** ResourceNotFoundException **
The requested resource can't be found.
HTTP Status Code: 404

 ** ThrottlingException **
Your request exceeded a rate limit. For example, you might have exceeded the number of AWS IoT SiteWise assets that can be created per second, the allowed number of messages per second, and so on.
For more information, see [Quotas](https://docs.aws.amazon.com/iot-sitewise/latest/userguide/quotas.html) in the * AWS IoT SiteWise User Guide*.
HTTP Status Code: 429

## See Also
<a name="API_CreateBulkImportJob_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/iotsitewise-2019-12-02/CreateBulkImportJob)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/iotsitewise-2019-12-02/CreateBulkImportJob)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iotsitewise-2019-12-02/CreateBulkImportJob)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/iotsitewise-2019-12-02/CreateBulkImportJob)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iotsitewise-2019-12-02/CreateBulkImportJob)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/iotsitewise-2019-12-02/CreateBulkImportJob)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/iotsitewise-2019-12-02/CreateBulkImportJob)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/iotsitewise-2019-12-02/CreateBulkImportJob)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/iotsitewise-2019-12-02/CreateBulkImportJob)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iotsitewise-2019-12-02/CreateBulkImportJob)
