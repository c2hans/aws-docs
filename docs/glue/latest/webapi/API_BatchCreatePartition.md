---
source_url: https://docs.aws.amazon.com/glue/latest/webapi/API_BatchCreatePartition.html
---

# BatchCreatePartition
<a name="API_BatchCreatePartition"></a>

Creates one or more partitions in a batch operation.

## Request Syntax
<a name="API_BatchCreatePartition_RequestSyntax"></a>

```
{
   "CatalogId": "{{string}}",
   "DatabaseName": "{{string}}",
   "PartitionInputList": [
      {
         "LastAccessTime": {{number}},
         "LastAnalyzedTime": {{number}},
         "Parameters": {
            "{{string}}" : "{{string}}"
         },
         "StorageDescriptor": {
            "AdditionalLocations": [ "{{string}}" ],
            "BucketColumns": [ "{{string}}" ],
            "Columns": [
               {
                  "Comment": "{{string}}",
                  "Name": "{{string}}",
                  "Parameters": {
                     "{{string}}" : "{{string}}"
                  },
                  "Type": "{{string}}"
               }
            ],
            "Compressed": {{boolean}},
            "InputFormat": "{{string}}",
            "Location": "{{string}}",
            "NumberOfBuckets": {{number}},
            "OutputFormat": "{{string}}",
            "Parameters": {
               "{{string}}" : "{{string}}"
            },
            "SchemaReference": {
               "SchemaId": {
                  "RegistryName": "{{string}}",
                  "SchemaArn": "{{string}}",
                  "SchemaName": "{{string}}"
               },
               "SchemaVersionId": "{{string}}",
               "SchemaVersionNumber": {{number}}
            },
            "SerdeInfo": {
               "Name": "{{string}}",
               "Parameters": {
                  "{{string}}" : "{{string}}"
               },
               "SerializationLibrary": "{{string}}"
            },
            "SkewedInfo": {
               "SkewedColumnNames": [ "{{string}}" ],
               "SkewedColumnValueLocationMaps": {
                  "{{string}}" : "{{string}}"
               },
               "SkewedColumnValues": [ "{{string}}" ]
            },
            "SortColumns": [
               {
                  "Column": "{{string}}",
                  "SortOrder": {{number}}
               }
            ],
            "StoredAsSubDirectories": {{boolean}}
         },
         "Values": [ "{{string}}" ]
      }
   ],
   "TableName": "{{string}}"
}
```

## Request Parameters
<a name="API_BatchCreatePartition_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [CatalogId](#API_BatchCreatePartition_RequestSyntax) **   <a name="Glue-BatchCreatePartition-request-CatalogId"></a>
The ID of the catalog in which the partition is to be created. Currently, this should be the AWS account ID.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\t]*`
Required: No

 ** [DatabaseName](#API_BatchCreatePartition_RequestSyntax) **   <a name="Glue-BatchCreatePartition-request-DatabaseName"></a>
The name of the metadata database in which the partition is to be created.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\t]*`
Required: Yes

 ** [PartitionInputList](#API_BatchCreatePartition_RequestSyntax) **   <a name="Glue-BatchCreatePartition-request-PartitionInputList"></a>
A list of `PartitionInput` structures that define the partitions to be created.
Type: Array of [PartitionInput](API_PartitionInput.md) objects
Array Members: Minimum number of 0 items. Maximum number of 100 items.
Required: Yes

 ** [TableName](#API_BatchCreatePartition_RequestSyntax) **   <a name="Glue-BatchCreatePartition-request-TableName"></a>
The name of the metadata table in which the partition is to be created.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\t]*`
Required: Yes

## Response Syntax
<a name="API_BatchCreatePartition_ResponseSyntax"></a>

```
{
   "Errors": [
      {
         "ErrorDetail": {
            "ErrorCode": "string",
            "ErrorMessage": "string"
         },
         "PartitionValues": [ "string" ]
      }
   ]
}
```

## Response Elements
<a name="API_BatchCreatePartition_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [Errors](#API_BatchCreatePartition_ResponseSyntax) **   <a name="Glue-BatchCreatePartition-response-Errors"></a>
The errors encountered when trying to create the requested partitions.
Type: Array of [PartitionError](API_PartitionError.md) objects

## Errors
<a name="API_BatchCreatePartition_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AlreadyExistsException **
A resource to be created or added already exists.
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

 ** ResourceNumberLimitExceededException **
A resource numerical limit was exceeded.
 ** Message **
A message describing the problem.
HTTP Status Code: 400

## See Also
<a name="API_BatchCreatePartition_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/glue-2017-03-31/BatchCreatePartition)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/glue-2017-03-31/BatchCreatePartition)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/glue-2017-03-31/BatchCreatePartition)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/glue-2017-03-31/BatchCreatePartition)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/glue-2017-03-31/BatchCreatePartition)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/glue-2017-03-31/BatchCreatePartition)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/glue-2017-03-31/BatchCreatePartition)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/glue-2017-03-31/BatchCreatePartition)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/glue-2017-03-31/BatchCreatePartition)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/glue-2017-03-31/BatchCreatePartition)
