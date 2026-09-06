---
source_url: https://docs.aws.amazon.com/iot-sitewise/latest/APIReference/API_DescribeBulkImportJob.html
---

# DescribeBulkImportJob
<a name="API_DescribeBulkImportJob"></a>

Retrieves information about a bulk import job request. For more information, see [Describe a bulk import job (AWS CLI)](https://docs.aws.amazon.com/iot-sitewise/latest/userguide/DescribeBulkImportJob.html) in the *Amazon Simple Storage Service User Guide*.

## Request Syntax
<a name="API_DescribeBulkImportJob_RequestSyntax"></a>

```
GET /jobs/{{jobId}}?workspaceName={{workspaceName}} HTTP/1.1
```

## URI Request Parameters
<a name="API_DescribeBulkImportJob_RequestParameters"></a>

The request uses the following URI parameters.

 ** [jobId](#API_DescribeBulkImportJob_RequestSyntax) **   <a name="iotsitewise-DescribeBulkImportJob-request-uri-jobId"></a>
The ID of the job.
Length Constraints: Fixed length of 36.
Pattern: `^(?!00000000-0000-0000-0000-000000000000)[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$`
Required: Yes

 ** [workspaceName](#API_DescribeBulkImportJob_RequestSyntax) **   <a name="iotsitewise-DescribeBulkImportJob-request-uri-workspaceName"></a>
The name of the workspace.
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `^[a-zA-Z0-9_-]+$`

## Request Body
<a name="API_DescribeBulkImportJob_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_DescribeBulkImportJob_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "adaptiveIngestion": boolean,
   "datasetId": "string",
   "deleteFilesAfterImport": boolean,
   "errorReportLocation": {
      "bucket": "string",
      "prefix": "string"
   },
   "files": [
      {
         "alias": "string",
         "bucket": "string",
         "fileFormat": {
            "annotation": {
            },
            "csv": {
               "columnNames": [ "string" ]
            },
            "mp4": {
            },
            "parquet": {
            }
         },
         "key": "string",
         "startTime": {
            "offsetInNanos": number,
            "timeInSeconds": number
         },
         "versionId": "string"
      }
   ],
   "jobConfiguration": {
      "fileFormat": {
         "annotation": {
         },
         "csv": {
            "columnNames": [ "string" ]
         },
         "mp4": {
         },
         "parquet": {
         }
      }
   },
   "jobCreationDate": number,
   "jobId": "string",
   "jobLastUpdateDate": number,
   "jobName": "string",
   "jobRoleArn": "string",
   "jobStatus": "string",
   "workspaceName": "string"
}
```

## Response Elements
<a name="API_DescribeBulkImportJob_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [adaptiveIngestion](#API_DescribeBulkImportJob_ResponseSyntax) **   <a name="iotsitewise-DescribeBulkImportJob-response-adaptiveIngestion"></a>
If set to true, ingest new data into AWS IoT SiteWise storage. Measurements with notifications, metrics and transforms are computed. If set to false, historical data is ingested into AWS IoT SiteWise as is.
Type: Boolean

 ** [datasetId](#API_DescribeBulkImportJob_ResponseSyntax) **   <a name="iotsitewise-DescribeBulkImportJob-response-datasetId"></a>
The ID of the dataset.
Type: String
Length Constraints: Fixed length of 36.
Pattern: `^(?!00000000-0000-0000-0000-000000000000)[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$`

 ** [deleteFilesAfterImport](#API_DescribeBulkImportJob_ResponseSyntax) **   <a name="iotsitewise-DescribeBulkImportJob-response-deleteFilesAfterImport"></a>
If set to true, your data files is deleted from S3, after ingestion into AWS IoT SiteWise storage.
Type: Boolean

 ** [errorReportLocation](#API_DescribeBulkImportJob_ResponseSyntax) **   <a name="iotsitewise-DescribeBulkImportJob-response-errorReportLocation"></a>
The Amazon S3 destination where errors associated with the job creation request are saved.
Type: [ErrorReportLocation](API_ErrorReportLocation.md) object

 ** [files](#API_DescribeBulkImportJob_ResponseSyntax) **   <a name="iotsitewise-DescribeBulkImportJob-response-files"></a>
The files in the specified Amazon S3 bucket that contain your data. You can specify up to 100 files for each bulk import job. Each file supports the following size limits:
+ Parquet files – Up to 256 MiB.
+ Other file formats – Up to 5 GiB.
Type: Array of [File](API_File.md) objects

 ** [jobConfiguration](#API_DescribeBulkImportJob_ResponseSyntax) **   <a name="iotsitewise-DescribeBulkImportJob-response-jobConfiguration"></a>
Contains the configuration information of a job, such as the file format used to save data in Amazon S3.
Type: [JobConfiguration](API_JobConfiguration.md) object

 ** [jobCreationDate](#API_DescribeBulkImportJob_ResponseSyntax) **   <a name="iotsitewise-DescribeBulkImportJob-response-jobCreationDate"></a>
The date the job was created, in Unix epoch TIME.
Type: Timestamp

 ** [jobId](#API_DescribeBulkImportJob_ResponseSyntax) **   <a name="iotsitewise-DescribeBulkImportJob-response-jobId"></a>
The ID of the job.
Type: String
Length Constraints: Fixed length of 36.
Pattern: `^(?!00000000-0000-0000-0000-000000000000)[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$`

 ** [jobLastUpdateDate](#API_DescribeBulkImportJob_ResponseSyntax) **   <a name="iotsitewise-DescribeBulkImportJob-response-jobLastUpdateDate"></a>
The date the job was last updated, in Unix epoch time.
Type: Timestamp

 ** [jobName](#API_DescribeBulkImportJob_ResponseSyntax) **   <a name="iotsitewise-DescribeBulkImportJob-response-jobName"></a>
The unique name that helps identify the job request.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `[^\u0000-\u001F\u007F]+`

 ** [jobRoleArn](#API_DescribeBulkImportJob_ResponseSyntax) **   <a name="iotsitewise-DescribeBulkImportJob-response-jobRoleArn"></a>
The [ARN](https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html) of the IAM role that allows AWS IoT SiteWise to read Amazon S3 data.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1600.
Pattern: `^arn:aws(-cn|-us-gov)?:[a-zA-Z0-9-:\/_\.]+$`

 ** [jobStatus](#API_DescribeBulkImportJob_ResponseSyntax) **   <a name="iotsitewise-DescribeBulkImportJob-response-jobStatus"></a>
The status of the bulk import job can be one of following values:
+  `PENDING` – AWS IoT SiteWise is waiting for the current bulk import job to finish.
+  `CANCELLED` – The bulk import job has been canceled.
+  `RUNNING` – AWS IoT SiteWise is processing your request to import your data from Amazon S3.
+  `COMPLETED` – AWS IoT SiteWise successfully completed your request to import data from Amazon S3.
+  `FAILED` – AWS IoT SiteWise couldn't process your request to import data from Amazon S3. You can use logs saved in the specified error report location in Amazon S3 to troubleshoot issues.
+  `COMPLETED_WITH_FAILURES` – AWS IoT SiteWise completed your request to import data from Amazon S3 with errors. You can use logs saved in the specified error report location in Amazon S3 to troubleshoot issues.
Type: String
Valid Values: `PENDING | CANCELLED | RUNNING | COMPLETED | FAILED | COMPLETED_WITH_FAILURES`

 ** [workspaceName](#API_DescribeBulkImportJob_ResponseSyntax) **   <a name="iotsitewise-DescribeBulkImportJob-response-workspaceName"></a>
The name of the workspace.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `^[a-zA-Z0-9_-]+$`

## Errors
<a name="API_DescribeBulkImportJob_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InternalFailureException **
 AWS IoT SiteWise can't process your request right now. Try again later.
HTTP Status Code: 500

 ** InvalidRequestException **
The request isn't valid. This can occur if your request contains malformed JSON or unsupported characters. Check your request and try again.
HTTP Status Code: 400

 ** ResourceNotFoundException **
The requested resource can't be found.
HTTP Status Code: 404

 ** ThrottlingException **
Your request exceeded a rate limit. For example, you might have exceeded the number of AWS IoT SiteWise assets that can be created per second, the allowed number of messages per second, and so on.
For more information, see [Quotas](https://docs.aws.amazon.com/iot-sitewise/latest/userguide/quotas.html) in the * AWS IoT SiteWise User Guide*.
HTTP Status Code: 429

## See Also
<a name="API_DescribeBulkImportJob_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/iotsitewise-2019-12-02/DescribeBulkImportJob)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/iotsitewise-2019-12-02/DescribeBulkImportJob)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iotsitewise-2019-12-02/DescribeBulkImportJob)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/iotsitewise-2019-12-02/DescribeBulkImportJob)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iotsitewise-2019-12-02/DescribeBulkImportJob)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/iotsitewise-2019-12-02/DescribeBulkImportJob)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/iotsitewise-2019-12-02/DescribeBulkImportJob)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/iotsitewise-2019-12-02/DescribeBulkImportJob)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/iotsitewise-2019-12-02/DescribeBulkImportJob)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iotsitewise-2019-12-02/DescribeBulkImportJob)
