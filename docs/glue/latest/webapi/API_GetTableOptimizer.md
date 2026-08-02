---
source_url: https://docs.aws.amazon.com/glue/latest/webapi/API_GetTableOptimizer.html
---

# GetTableOptimizer
<a name="API_GetTableOptimizer"></a>

Returns the configuration of all optimizers associated with a specified table.

## Request Syntax
<a name="API_GetTableOptimizer_RequestSyntax"></a>

```
{
   "CatalogId": "{{string}}",
   "DatabaseName": "{{string}}",
   "TableName": "{{string}}",
   "Type": "{{string}}"
}
```

## Request Parameters
<a name="API_GetTableOptimizer_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [CatalogId](#API_GetTableOptimizer_RequestSyntax) **   <a name="Glue-GetTableOptimizer-request-CatalogId"></a>
The Catalog ID of the table.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\t]*`
Required: Yes

 ** [DatabaseName](#API_GetTableOptimizer_RequestSyntax) **   <a name="Glue-GetTableOptimizer-request-DatabaseName"></a>
The name of the database in the catalog in which the table resides.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\t]*`
Required: Yes

 ** [TableName](#API_GetTableOptimizer_RequestSyntax) **   <a name="Glue-GetTableOptimizer-request-TableName"></a>
The name of the table.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\t]*`
Required: Yes

 ** [Type](#API_GetTableOptimizer_RequestSyntax) **   <a name="Glue-GetTableOptimizer-request-Type"></a>
The type of table optimizer.
Type: String
Valid Values: `compaction | retention | orphan_file_deletion`
Required: Yes

## Response Syntax
<a name="API_GetTableOptimizer_ResponseSyntax"></a>

```
{
   "CatalogId": "string",
   "DatabaseName": "string",
   "TableName": "string",
   "TableOptimizer": {
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
```

## Response Elements
<a name="API_GetTableOptimizer_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [CatalogId](#API_GetTableOptimizer_ResponseSyntax) **   <a name="Glue-GetTableOptimizer-response-CatalogId"></a>
The Catalog ID of the table.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\t]*`

 ** [DatabaseName](#API_GetTableOptimizer_ResponseSyntax) **   <a name="Glue-GetTableOptimizer-response-DatabaseName"></a>
The name of the database in the catalog in which the table resides.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\t]*`

 ** [TableName](#API_GetTableOptimizer_ResponseSyntax) **   <a name="Glue-GetTableOptimizer-response-TableName"></a>
The name of the table.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\t]*`

 ** [TableOptimizer](#API_GetTableOptimizer_ResponseSyntax) **   <a name="Glue-GetTableOptimizer-response-TableOptimizer"></a>
The optimizer associated with the specified table.
Type: [TableOptimizer](API_TableOptimizer.md) object

## Errors
<a name="API_GetTableOptimizer_Errors"></a>

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
<a name="API_GetTableOptimizer_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/glue-2017-03-31/GetTableOptimizer)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/glue-2017-03-31/GetTableOptimizer)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/glue-2017-03-31/GetTableOptimizer)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/glue-2017-03-31/GetTableOptimizer)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/glue-2017-03-31/GetTableOptimizer)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/glue-2017-03-31/GetTableOptimizer)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/glue-2017-03-31/GetTableOptimizer)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/glue-2017-03-31/GetTableOptimizer)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/glue-2017-03-31/GetTableOptimizer)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/glue-2017-03-31/GetTableOptimizer)
