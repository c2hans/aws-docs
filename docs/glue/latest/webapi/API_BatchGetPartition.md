---
source_url: https://docs.aws.amazon.com/glue/latest/webapi/API_BatchGetPartition.html
---

# BatchGetPartition
<a name="API_BatchGetPartition"></a>

Retrieves partitions in a batch request.

## Request Syntax
<a name="API_BatchGetPartition_RequestSyntax"></a>

```
{
   "CatalogId": "{{string}}",
   "DatabaseName": "{{string}}",
   "PartitionsToGet": [
      {
         "Values": [ "{{string}}" ]
      }
   ],
   "TableName": "{{string}}"
}
```

## Request Parameters
<a name="API_BatchGetPartition_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [CatalogId](#API_BatchGetPartition_RequestSyntax) **   <a name="Glue-BatchGetPartition-request-CatalogId"></a>
The ID of the Data Catalog where the partitions in question reside. If none is supplied, the AWS account ID is used by default.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\t]*`
Required: No

 ** [DatabaseName](#API_BatchGetPartition_RequestSyntax) **   <a name="Glue-BatchGetPartition-request-DatabaseName"></a>
The name of the catalog database where the partitions reside.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\t]*`
Required: Yes

 ** [PartitionsToGet](#API_BatchGetPartition_RequestSyntax) **   <a name="Glue-BatchGetPartition-request-PartitionsToGet"></a>
A list of partition values identifying the partitions to retrieve.
Type: Array of [PartitionValueList](API_PartitionValueList.md) objects
Array Members: Minimum number of 0 items. Maximum number of 1000 items.
Required: Yes

 ** [TableName](#API_BatchGetPartition_RequestSyntax) **   <a name="Glue-BatchGetPartition-request-TableName"></a>
The name of the partitions' table.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\t]*`
Required: Yes

## Response Syntax
<a name="API_BatchGetPartition_ResponseSyntax"></a>

```
{
   "Partitions": [
      {
         "CatalogId": "string",
         "CreationTime": number,
         "DatabaseName": "string",
         "LastAccessTime": number,
         "LastAnalyzedTime": number,
         "Parameters": {
            "string" : "string"
         },
         "StorageDescriptor": {
            "AdditionalLocations": [ "string" ],
            "BucketColumns": [ "string" ],
            "Columns": [
               {
                  "Comment": "string",
                  "Name": "string",
                  "Parameters": {
                     "string" : "string"
                  },
                  "Type": "string"
               }
            ],
            "Compressed": boolean,
            "InputFormat": "string",
            "Location": "string",
            "NumberOfBuckets": number,
            "OutputFormat": "string",
            "Parameters": {
               "string" : "string"
            },
            "SchemaReference": {
               "SchemaId": {
                  "RegistryName": "string",
                  "SchemaArn": "string",
                  "SchemaName": "string"
               },
               "SchemaVersionId": "string",
               "SchemaVersionNumber": number
            },
            "SerdeInfo": {
               "Name": "string",
               "Parameters": {
                  "string" : "string"
               },
               "SerializationLibrary": "string"
            },
            "SkewedInfo": {
               "SkewedColumnNames": [ "string" ],
               "SkewedColumnValueLocationMaps": {
                  "string" : "string"
               },
               "SkewedColumnValues": [ "string" ]
            },
            "SortColumns": [
               {
                  "Column": "string",
                  "SortOrder": number
               }
            ],
            "StoredAsSubDirectories": boolean
         },
         "TableName": "string",
         "Values": [ "string" ]
      }
   ],
   "UnprocessedKeys": [
      {
         "Values": [ "string" ]
      }
   ]
}
```

## Response Elements
<a name="API_BatchGetPartition_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [Partitions](#API_BatchGetPartition_ResponseSyntax) **   <a name="Glue-BatchGetPartition-response-Partitions"></a>
A list of the requested partitions.
Type: Array of [Partition](API_Partition.md) objects

 ** [UnprocessedKeys](#API_BatchGetPartition_ResponseSyntax) **   <a name="Glue-BatchGetPartition-response-UnprocessedKeys"></a>
A list of the partition values in the request for which partitions were not returned.
Type: Array of [PartitionValueList](API_PartitionValueList.md) objects
Array Members: Minimum number of 0 items. Maximum number of 1000 items.

## Errors
<a name="API_BatchGetPartition_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** EntityNotFoundException **
A specified entity does not exist
 ** FromFederationSource **
Indicates whether or not the exception relates to a federated source.
 ** Message **
A message describing the problem.
HTTP Status Code: 400

 ** FederationSourceException **
A federation source failed.
 ** FederationSourceErrorCode **
The error code of the problem.
 ** Message **
The message describing the problem.
HTTP Status Code: 400

 ** FederationSourceRetryableException **
A federation source failed, but the operation may be retried.
 ** Message **
A message describing the problem.
HTTP Status Code: 400

 ** GlueEncryptionException **
An encryption operation failed.
 ** Message **
The message describing the problem.
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

 ** InvalidStateException **
An error that indicates your data is in an invalid state.
 ** Message **
A message describing the problem.
HTTP Status Code: 400

 ** OperationTimeoutException **
The operation timed out.
 ** Message **
A message describing the problem.
HTTP Status Code: 400

## See Also
<a name="API_BatchGetPartition_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/glue-2017-03-31/BatchGetPartition)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/glue-2017-03-31/BatchGetPartition)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/glue-2017-03-31/BatchGetPartition)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/glue-2017-03-31/BatchGetPartition)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/glue-2017-03-31/BatchGetPartition)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/glue-2017-03-31/BatchGetPartition)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/glue-2017-03-31/BatchGetPartition)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/glue-2017-03-31/BatchGetPartition)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/glue-2017-03-31/BatchGetPartition)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/glue-2017-03-31/BatchGetPartition)
