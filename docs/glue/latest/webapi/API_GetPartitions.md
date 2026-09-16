---
source_url: https://docs.aws.amazon.com/glue/latest/webapi/API_GetPartitions.html
---

# GetPartitions
<a name="API_GetPartitions"></a>

Retrieves information about the partitions in a table.

## Request Syntax
<a name="API_GetPartitions_RequestSyntax"></a>

```
{
   "CatalogId": "{{string}}",
   "DatabaseName": "{{string}}",
   "ExcludeColumnSchema": {{boolean}},
   "Expression": "{{string}}",
   "MaxResults": {{number}},
   "NextToken": "{{string}}",
   "QueryAsOfTime": {{number}},
   "Segment": {
      "SegmentNumber": {{number}},
      "TotalSegments": {{number}}
   },
   "TableName": "{{string}}",
   "TransactionId": "{{string}}"
}
```

## Request Parameters
<a name="API_GetPartitions_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [CatalogId](#API_GetPartitions_RequestSyntax) **   <a name="Glue-GetPartitions-request-CatalogId"></a>
The ID of the Data Catalog where the partitions in question reside. If none is provided, the AWS account ID is used by default.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\t]*`
Required: No

 ** [DatabaseName](#API_GetPartitions_RequestSyntax) **   <a name="Glue-GetPartitions-request-DatabaseName"></a>
The name of the catalog database where the partitions reside.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\t]*`
Required: Yes

 ** [ExcludeColumnSchema](#API_GetPartitions_RequestSyntax) **   <a name="Glue-GetPartitions-request-ExcludeColumnSchema"></a>
When true, specifies not returning the partition column schema. Useful when you are interested only in other partition attributes such as partition values or location. This approach avoids the problem of a large response by not returning duplicate data.
Type: Boolean
Required: No

 ** [Expression](#API_GetPartitions_RequestSyntax) **   <a name="Glue-GetPartitions-request-Expression"></a>
An expression that filters the partitions to be returned.
The expression uses SQL syntax similar to the SQL `WHERE` filter clause. The SQL statement parser [JSQLParser](http://jsqlparser.sourceforge.net/home.php) parses the expression.
 *Operators*: The following are the operators that you can use in the `Expression` API call:
=
Checks whether the values of the two operands are equal; if yes, then the condition becomes true.
Example: Assume 'variable a' holds 10 and 'variable b' holds 20.
(a = b) is not true.
< >
Checks whether the values of two operands are equal; if the values are not equal, then the condition becomes true.
Example: (a < > b) is true.
>
Checks whether the value of the left operand is greater than the value of the right operand; if yes, then the condition becomes true.
Example: (a > b) is not true.
<
Checks whether the value of the left operand is less than the value of the right operand; if yes, then the condition becomes true.
Example: (a < b) is true.
>=
Checks whether the value of the left operand is greater than or equal to the value of the right operand; if yes, then the condition becomes true.
Example: (a >= b) is not true.
<=
Checks whether the value of the left operand is less than or equal to the value of the right operand; if yes, then the condition becomes true.
Example: (a <= b) is true.
AND, OR, IN, BETWEEN, LIKE, NOT, IS NULL
Logical operators.
 *Supported Partition Key Types*: The following are the supported partition keys.
+  `string`
+  `date`
+  `timestamp`
+  `int`
+  `bigint`
+  `long`
+  `tinyint`
+  `smallint`
+  `decimal`
If an type is encountered that is not valid, an exception is thrown.
The following list shows the valid operators on each type. When you define a crawler, the `partitionKey` type is created as a `STRING`, to be compatible with the catalog partitions.
 *Sample API Call*:
Type: String
Length Constraints: Minimum length of 0. Maximum length of 2048.
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\r\n\t]*`
Required: No

 ** [MaxResults](#API_GetPartitions_RequestSyntax) **   <a name="Glue-GetPartitions-request-MaxResults"></a>
The maximum number of partitions to return in a single response.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 1000.
Required: No

 ** [NextToken](#API_GetPartitions_RequestSyntax) **   <a name="Glue-GetPartitions-request-NextToken"></a>
A continuation token, if this is not the first call to retrieve these partitions.
Type: String
Required: No

 ** [QueryAsOfTime](#API_GetPartitions_RequestSyntax) **   <a name="Glue-GetPartitions-request-QueryAsOfTime"></a>
The time as of when to read the partition contents. If not set, the most recent transaction commit time will be used. Cannot be specified along with `TransactionId`.
Type: Timestamp
Required: No

 ** [Segment](#API_GetPartitions_RequestSyntax) **   <a name="Glue-GetPartitions-request-Segment"></a>
The segment of the table's partitions to scan in this request.
Type: [Segment](API_Segment.md) object
Required: No

 ** [TableName](#API_GetPartitions_RequestSyntax) **   <a name="Glue-GetPartitions-request-TableName"></a>
The name of the partitions' table.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\t]*`
Required: Yes

 ** [TransactionId](#API_GetPartitions_RequestSyntax) **   <a name="Glue-GetPartitions-request-TransactionId"></a>
The transaction ID at which to read the partition contents.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[\p{L}\p{N}\p{P}]*`
Required: No

## Response Syntax
<a name="API_GetPartitions_ResponseSyntax"></a>

```
{
   "NextToken": "string",
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
   ]
}
```

## Response Elements
<a name="API_GetPartitions_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [NextToken](#API_GetPartitions_ResponseSyntax) **   <a name="Glue-GetPartitions-response-NextToken"></a>
A continuation token, if the returned list of partitions does not include the last one.
Type: String

 ** [Partitions](#API_GetPartitions_ResponseSyntax) **   <a name="Glue-GetPartitions-response-Partitions"></a>
A list of requested partitions.
Type: Array of [Partition](API_Partition.md) objects

## Errors
<a name="API_GetPartitions_Errors"></a>

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

 ** ResourceNotReadyException **
A resource was not ready for a transaction.
 ** Message **
A message describing the problem.
HTTP Status Code: 400

## See Also
<a name="API_GetPartitions_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/glue-2017-03-31/GetPartitions)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/glue-2017-03-31/GetPartitions)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/glue-2017-03-31/GetPartitions)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/glue-2017-03-31/GetPartitions)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/glue-2017-03-31/GetPartitions)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/glue-2017-03-31/GetPartitions)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/glue-2017-03-31/GetPartitions)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/glue-2017-03-31/GetPartitions)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/glue-2017-03-31/GetPartitions)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/glue-2017-03-31/GetPartitions)
