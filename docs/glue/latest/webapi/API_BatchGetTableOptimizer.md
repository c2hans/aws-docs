---
source_url: https://docs.aws.amazon.com/glue/latest/webapi/API_BatchGetTableOptimizer.html
---

# BatchGetTableOptimizer
<a name="API_BatchGetTableOptimizer"></a>

Returns the configuration for the specified table optimizers.

## Request Syntax
<a name="API_BatchGetTableOptimizer_RequestSyntax"></a>

```
{
   "Entries": [
      {
         "catalogId": "{{string}}",
         "databaseName": "{{string}}",
         "tableName": "{{string}}",
         "type": "{{string}}"
      }
   ]
}
```

## Request Parameters
<a name="API_BatchGetTableOptimizer_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [Entries](#API_BatchGetTableOptimizer_RequestSyntax) **   <a name="Glue-BatchGetTableOptimizer-request-Entries"></a>
A list of `BatchGetTableOptimizerEntry` objects specifying the table optimizers to retrieve.
Type: Array of [BatchGetTableOptimizerEntry](API_BatchGetTableOptimizerEntry.md) objects
Required: Yes

## Response Syntax
<a name="API_BatchGetTableOptimizer_ResponseSyntax"></a>

```
{
   "Failures": [
      {
         "catalogId": "string",
         "databaseName": "string",
         "error": {
            "ErrorCode": "string",
            "ErrorMessage": "string"
         },
         "tableName": "string",
         "type": "string"
      }
   ],
   "TableOptimizers": [
      {
         "catalogId": "string",
         "databaseName": "string",
         "tableName": "string",
         "tableOptimizer": {
            "configuration": {
               "compactionConfiguration": {
                  "icebergConfiguration": {
                     "deleteFileThreshold": number,
                     "minInputFiles": number,
                     "strategy": "string"
                  }
               },
               "enabled": boolean,
               "orphanFileDeletionConfiguration": {
                  "icebergConfiguration": {
                     "location": "string",
                     "orphanFileRetentionPeriodInDays": number,
                     "runRateInHours": number
                  }
               },
               "retentionConfiguration": {
                  "icebergConfiguration": {
                     "cleanExpiredFiles": boolean,
                     "numberOfSnapshotsToRetain": number,
                     "runRateInHours": number,
                     "snapshotRetentionPeriodInDays": number
                  }
               },
               "roleArn": "string",
               "vpcConfiguration": { ... }
            },
            "configurationSource": "string",
            "lastRun": {
               "compactionMetrics": {
                  "IcebergMetrics": {
                     "DpuHours": number,
                     "JobDurationInHour": number,
                     "NumberOfBytesCompacted": number,
                     "NumberOfDpus": number,
                     "NumberOfFilesCompacted": number
                  }
               },
               "compactionStrategy": "string",
               "endTimestamp": number,
               "error": "string",
               "eventType": "string",
               "metrics": {
                  "JobDurationInHour": "string",
                  "NumberOfBytesCompacted": "string",
                  "NumberOfDpus": "string",
                  "NumberOfFilesCompacted": "string"
               },
               "orphanFileDeletionMetrics": {
                  "IcebergMetrics": {
                     "DpuHours": number,
                     "JobDurationInHour": number,
                     "NumberOfDpus": number,
                     "NumberOfOrphanFilesDeleted": number
                  }
               },
               "retentionMetrics": {
                  "IcebergMetrics": {
                     "DpuHours": number,
                     "JobDurationInHour": number,
                     "NumberOfDataFilesDeleted": number,
                     "NumberOfDpus": number,
                     "NumberOfManifestFilesDeleted": number,
                     "NumberOfManifestListsDeleted": number
                  }
               },
               "startTimestamp": number
            },
            "type": "string"
         }
      }
   ]
}
```

## Response Elements
<a name="API_BatchGetTableOptimizer_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [Failures](#API_BatchGetTableOptimizer_ResponseSyntax) **   <a name="Glue-BatchGetTableOptimizer-response-Failures"></a>
A list of errors from the operation.
Type: Array of [BatchGetTableOptimizerError](API_BatchGetTableOptimizerError.md) objects

 ** [TableOptimizers](#API_BatchGetTableOptimizer_ResponseSyntax) **   <a name="Glue-BatchGetTableOptimizer-response-TableOptimizers"></a>
A list of `BatchTableOptimizer` objects.
Type: Array of [BatchTableOptimizer](API_BatchTableOptimizer.md) objects

## Errors
<a name="API_BatchGetTableOptimizer_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
Access to a resource was denied.
 ** Message **
A message describing the problem.
HTTP Status Code: 400

 ** EntityNotFoundException **
A specified entity does not exist
 ** FromFederationSource **
Indicates whether or not the exception relates to a federated source.
 ** Message **
A message describing the problem.
HTTP Status Code: 400

 ** InternalServiceException **
An internal service error occurred.
 ** Message **
A message describing the problem.
HTTP Status Code: 500

 ** InvalidInputException **
The input provided was not valid.
 ** FromFederationSource **
Indicates whether or not the exception relates to a federated source.
 ** Message **
A message describing the problem.
HTTP Status Code: 400

 ** ThrottlingException **
The throttling threshhold was exceeded.
 ** Message **
A message describing the problem.
HTTP Status Code: 400

## See Also
<a name="API_BatchGetTableOptimizer_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/glue-2017-03-31/BatchGetTableOptimizer)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/glue-2017-03-31/BatchGetTableOptimizer)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/glue-2017-03-31/BatchGetTableOptimizer)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/glue-2017-03-31/BatchGetTableOptimizer)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/glue-2017-03-31/BatchGetTableOptimizer)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/glue-2017-03-31/BatchGetTableOptimizer)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/glue-2017-03-31/BatchGetTableOptimizer)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/glue-2017-03-31/BatchGetTableOptimizer)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/glue-2017-03-31/BatchGetTableOptimizer)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/glue-2017-03-31/BatchGetTableOptimizer)
