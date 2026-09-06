---
source_url: https://docs.aws.amazon.com/timestream/latest/APIReference/API_DescribeBatchLoadTask.html
---

# DescribeBatchLoadTask
<a name="API_DescribeBatchLoadTask"></a>

Returns information about the batch load task, including configurations, mappings, progress, and other details. [Service quotas apply](https://docs.aws.amazon.com/timestream/latest/developerguide/ts-limits.html). See [code sample](https://docs.aws.amazon.com/timestream/latest/developerguide/code-samples.describe-batch-load.html) for details.

## Request Syntax
<a name="API_DescribeBatchLoadTask_RequestSyntax"></a>

```
{
   "TaskId": "{{string}}"
}
```

## Request Parameters
<a name="API_DescribeBatchLoadTask_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [TaskId](#API_DescribeBatchLoadTask_RequestSyntax) **   <a name="timestream-DescribeBatchLoadTask-request-TaskId"></a>
The ID of the batch load task.
Type: String
Length Constraints: Minimum length of 3. Maximum length of 32.
Pattern: `[A-Z0-9]+`
Required: Yes

## Response Syntax
<a name="API_DescribeBatchLoadTask_ResponseSyntax"></a>

```
{
   "BatchLoadTaskDescription": {
      "CreationTime": number,
      "DataModelConfiguration": {
         "DataModel": {
            "DimensionMappings": [
               {
                  "DestinationColumn": "string",
                  "SourceColumn": "string"
               }
            ],
            "MeasureNameColumn": "string",
            "MixedMeasureMappings": [
               {
                  "MeasureName": "string",
                  "MeasureValueType": "string",
                  "MultiMeasureAttributeMappings": [
                     {
                        "MeasureValueType": "string",
                        "SourceColumn": "string",
                        "TargetMultiMeasureAttributeName": "string"
                     }
                  ],
                  "SourceColumn": "string",
                  "TargetMeasureName": "string"
               }
            ],
            "MultiMeasureMappings": {
               "MultiMeasureAttributeMappings": [
                  {
                     "MeasureValueType": "string",
                     "SourceColumn": "string",
                     "TargetMultiMeasureAttributeName": "string"
                  }
               ],
               "TargetMultiMeasureName": "string"
            },
            "TimeColumn": "string",
            "TimeUnit": "string"
         },
         "DataModelS3Configuration": {
            "BucketName": "string",
            "ObjectKey": "string"
         }
      },
      "DataSourceConfiguration": {
         "CsvConfiguration": {
            "ColumnSeparator": "string",
            "EscapeChar": "string",
            "NullValue": "string",
            "QuoteChar": "string",
            "TrimWhiteSpace": boolean
         },
         "DataFormat": "string",
         "DataSourceS3Configuration": {
            "BucketName": "string",
            "ObjectKeyPrefix": "string"
         }
      },
      "ErrorMessage": "string",
      "LastUpdatedTime": number,
      "ProgressReport": {
         "BytesMetered": number,
         "FileFailures": number,
         "ParseFailures": number,
         "RecordIngestionFailures": number,
         "RecordsIngested": number,
         "RecordsProcessed": number
      },
      "RecordVersion": number,
      "ReportConfiguration": {
         "ReportS3Configuration": {
            "BucketName": "string",
            "EncryptionOption": "string",
            "KmsKeyId": "string",
            "ObjectKeyPrefix": "string"
         }
      },
      "ResumableUntil": number,
      "TargetDatabaseName": "string",
      "TargetTableName": "string",
      "TaskId": "string",
      "TaskStatus": "string"
   }
}
```

## Response Elements
<a name="API_DescribeBatchLoadTask_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [BatchLoadTaskDescription](#API_DescribeBatchLoadTask_ResponseSyntax) **   <a name="timestream-DescribeBatchLoadTask-response-BatchLoadTaskDescription"></a>
Description of the batch load task.
Type: [BatchLoadTaskDescription](API_BatchLoadTaskDescription.md) object

## Errors
<a name="API_DescribeBatchLoadTask_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You are not authorized to perform this action.
HTTP Status Code: 400

 ** InternalServerException **
 Timestream was unable to fully process this request because of an internal server error.
HTTP Status Code: 500

 ** InvalidEndpointException **
The requested endpoint was not valid.
HTTP Status Code: 400

 ** ResourceNotFoundException **
The operation tried to access a nonexistent resource. The resource might not be specified correctly, or its status might not be ACTIVE.
HTTP Status Code: 400

 ** ThrottlingException **
 Too many requests were made by a user and they exceeded the service quotas. The request was throttled.
HTTP Status Code: 400

## See Also
<a name="API_DescribeBatchLoadTask_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/timestream-write-2018-11-01/DescribeBatchLoadTask)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/timestream-write-2018-11-01/DescribeBatchLoadTask)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/timestream-write-2018-11-01/DescribeBatchLoadTask)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/timestream-write-2018-11-01/DescribeBatchLoadTask)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/timestream-write-2018-11-01/DescribeBatchLoadTask)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/timestream-write-2018-11-01/DescribeBatchLoadTask)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/timestream-write-2018-11-01/DescribeBatchLoadTask)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/timestream-write-2018-11-01/DescribeBatchLoadTask)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/timestream-write-2018-11-01/DescribeBatchLoadTask)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/timestream-write-2018-11-01/DescribeBatchLoadTask)
