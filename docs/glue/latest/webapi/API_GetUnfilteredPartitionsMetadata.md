---
source_url: https://docs.aws.amazon.com/glue/latest/webapi/API_GetUnfilteredPartitionsMetadata.html
---

# GetUnfilteredPartitionsMetadata
<a name="API_GetUnfilteredPartitionsMetadata"></a>

Retrieves partition metadata from the Data Catalog that contains unfiltered metadata.

For IAM authorization, the public IAM action associated with this API is `glue:GetPartitions`.

## Request Syntax
<a name="API_GetUnfilteredPartitionsMetadata_RequestSyntax"></a>

```
{
   "AuditContext": {
      "AdditionalAuditContext": "{{string}}",
      "AllColumnsRequested": {{boolean}},
      "RequestedColumns": [ "{{string}}" ]
   },
   "CatalogId": "{{string}}",
   "DatabaseName": "{{string}}",
   "Expression": "{{string}}",
   "MaxResults": {{number}},
   "NextToken": "{{string}}",
   "QuerySessionContext": {
      "AdditionalContext": {
         "{{string}}" : "{{string}}"
      },
      "ClusterId": "{{string}}",
      "QueryAuthorizationId": "{{string}}",
      "QueryId": "{{string}}",
      "QueryStartTime": {{number}}
   },
   "Region": "{{string}}",
   "Segment": {
      "SegmentNumber": {{number}},
      "TotalSegments": {{number}}
   },
   "SupportedPermissionTypes": [ "{{string}}" ],
   "TableName": "{{string}}"
}
```

## Request Parameters
<a name="API_GetUnfilteredPartitionsMetadata_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [AuditContext](#API_GetUnfilteredPartitionsMetadata_RequestSyntax) **   <a name="Glue-GetUnfilteredPartitionsMetadata-request-AuditContext"></a>
A structure containing Lake Formation audit context information.
Type: [AuditContext](API_AuditContext.md) object
Required: No

 ** [CatalogId](#API_GetUnfilteredPartitionsMetadata_RequestSyntax) **   <a name="Glue-GetUnfilteredPartitionsMetadata-request-CatalogId"></a>
The ID of the Data Catalog where the partitions in question reside. If none is provided, the AWS account ID is used by default.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\t]*`
Required: Yes

 ** [DatabaseName](#API_GetUnfilteredPartitionsMetadata_RequestSyntax) **   <a name="Glue-GetUnfilteredPartitionsMetadata-request-DatabaseName"></a>
The name of the catalog database where the partitions reside.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\t]*`
Required: Yes

 ** [Expression](#API_GetUnfilteredPartitionsMetadata_RequestSyntax) **   <a name="Glue-GetUnfilteredPartitionsMetadata-request-Expression"></a>
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
Type: String
Length Constraints: Minimum length of 0. Maximum length of 2048.
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\r\n\t]*`
Required: No

 ** [MaxResults](#API_GetUnfilteredPartitionsMetadata_RequestSyntax) **   <a name="Glue-GetUnfilteredPartitionsMetadata-request-MaxResults"></a>
The maximum number of partitions to return in a single response.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 1000.
Required: No

 ** [NextToken](#API_GetUnfilteredPartitionsMetadata_RequestSyntax) **   <a name="Glue-GetUnfilteredPartitionsMetadata-request-NextToken"></a>
A continuation token, if this is not the first call to retrieve these partitions.
Type: String
Required: No

 ** [QuerySessionContext](#API_GetUnfilteredPartitionsMetadata_RequestSyntax) **   <a name="Glue-GetUnfilteredPartitionsMetadata-request-QuerySessionContext"></a>
A structure used as a protocol between query engines and Lake Formation or AWS Glue. Contains both a Lake Formation generated authorization identifier and information from the request's authorization context.
Type: [QuerySessionContext](API_QuerySessionContext.md) object
Required: No

 ** [Region](#API_GetUnfilteredPartitionsMetadata_RequestSyntax) **   <a name="Glue-GetUnfilteredPartitionsMetadata-request-Region"></a>
Specified only if the base tables belong to a different AWS Region.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Required: No

 ** [Segment](#API_GetUnfilteredPartitionsMetadata_RequestSyntax) **   <a name="Glue-GetUnfilteredPartitionsMetadata-request-Segment"></a>
The segment of the table's partitions to scan in this request.
Type: [Segment](API_Segment.md) object
Required: No

 ** [SupportedPermissionTypes](#API_GetUnfilteredPartitionsMetadata_RequestSyntax) **   <a name="Glue-GetUnfilteredPartitionsMetadata-request-SupportedPermissionTypes"></a>
A list of supported permission types.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 255 items.
Valid Values: `COLUMN_PERMISSION | CELL_FILTER_PERMISSION | NESTED_PERMISSION | NESTED_CELL_PERMISSION`
Required: Yes

 ** [TableName](#API_GetUnfilteredPartitionsMetadata_RequestSyntax) **   <a name="Glue-GetUnfilteredPartitionsMetadata-request-TableName"></a>
The name of the table that contains the partition.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\t]*`
Required: Yes

## Response Syntax
<a name="API_GetUnfilteredPartitionsMetadata_ResponseSyntax"></a>

```
{
   "NextToken": "string",
   "UnfilteredPartitions": [
      {
         "AuthorizedColumns": [ "string" ],
         "IsRegisteredWithLakeFormation": boolean,
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
   ]
}
```

## Response Elements
<a name="API_GetUnfilteredPartitionsMetadata_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [NextToken](#API_GetUnfilteredPartitionsMetadata_ResponseSyntax) **   <a name="Glue-GetUnfilteredPartitionsMetadata-response-NextToken"></a>
A continuation token, if the returned list of partitions does not include the last one.
Type: String

 ** [UnfilteredPartitions](#API_GetUnfilteredPartitionsMetadata_ResponseSyntax) **   <a name="Glue-GetUnfilteredPartitionsMetadata-response-UnfilteredPartitions"></a>
A list of requested partitions.
Type: Array of [UnfilteredPartition](API_UnfilteredPartition.md) objects

## Errors
<a name="API_GetUnfilteredPartitionsMetadata_Errors"></a>

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

 ** PermissionTypeMismatchException **
The operation timed out.
 ** Message **
There is a mismatch between the SupportedPermissionType used in the query request and the permissions defined on the target table.
HTTP Status Code: 400

## See Also
<a name="API_GetUnfilteredPartitionsMetadata_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/glue-2017-03-31/GetUnfilteredPartitionsMetadata)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/glue-2017-03-31/GetUnfilteredPartitionsMetadata)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/glue-2017-03-31/GetUnfilteredPartitionsMetadata)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/glue-2017-03-31/GetUnfilteredPartitionsMetadata)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/glue-2017-03-31/GetUnfilteredPartitionsMetadata)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/glue-2017-03-31/GetUnfilteredPartitionsMetadata)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/glue-2017-03-31/GetUnfilteredPartitionsMetadata)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/glue-2017-03-31/GetUnfilteredPartitionsMetadata)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/glue-2017-03-31/GetUnfilteredPartitionsMetadata)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/glue-2017-03-31/GetUnfilteredPartitionsMetadata)
