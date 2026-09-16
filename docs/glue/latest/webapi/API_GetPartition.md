---
source_url: https://docs.aws.amazon.com/glue/latest/webapi/API_GetPartition.html
---

# GetPartition
<a name="API_GetPartition"></a>

Retrieves information about a specified partition.

## Request Syntax
<a name="API_GetPartition_RequestSyntax"></a>

```
{
   "CatalogId": "{{string}}",
   "DatabaseName": "{{string}}",
   "PartitionValues": [ "{{string}}" ],
   "TableName": "{{string}}"
}
```

## Request Parameters
<a name="API_GetPartition_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [CatalogId](#API_GetPartition_RequestSyntax) **   <a name="Glue-GetPartition-request-CatalogId"></a>
The ID of the Data Catalog where the partition in question resides. If none is provided, the AWS account ID is used by default.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\t]*`
Required: No

 ** [DatabaseName](#API_GetPartition_RequestSyntax) **   <a name="Glue-GetPartition-request-DatabaseName"></a>
The name of the catalog database where the partition resides.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\t]*`
Required: Yes

 ** [PartitionValues](#API_GetPartition_RequestSyntax) **   <a name="Glue-GetPartition-request-PartitionValues"></a>
The values that define the partition.
Type: Array of strings
Length Constraints: Minimum length of 1. Maximum length of 1024.
Required: Yes

 ** [TableName](#API_GetPartition_RequestSyntax) **   <a name="Glue-GetPartition-request-TableName"></a>
The name of the partition's table.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\t]*`
Required: Yes

## Response Syntax
<a name="API_GetPartition_ResponseSyntax"></a>

```
{
   "Partition": {
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
}
```

## Response Elements
<a name="API_GetPartition_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [Partition](#API_GetPartition_ResponseSyntax) **   <a name="Glue-GetPartition-response-Partition"></a>
The requested information, in the form of a `Partition` object.
Type: [Partition](API_Partition.md) object

## Errors
<a name="API_GetPartition_Errors"></a>

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

 ** OperationTimeoutException **
The operation timed out.
 ** Message **
A message describing the problem.
HTTP Status Code: 400

## See Also
<a name="API_GetPartition_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/glue-2017-03-31/GetPartition)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/glue-2017-03-31/GetPartition)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/glue-2017-03-31/GetPartition)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/glue-2017-03-31/GetPartition)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/glue-2017-03-31/GetPartition)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/glue-2017-03-31/GetPartition)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/glue-2017-03-31/GetPartition)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/glue-2017-03-31/GetPartition)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/glue-2017-03-31/GetPartition)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/glue-2017-03-31/GetPartition)
