---
source_url: https://docs.aws.amazon.com/glue/latest/webapi/API_GetUnfilteredPartitionMetadata.html
---

# GetUnfilteredPartitionMetadata
<a name="API_GetUnfilteredPartitionMetadata"></a>

Retrieves partition metadata from the Data Catalog that contains unfiltered metadata.

For IAM authorization, the public IAM action associated with this API is `glue:GetPartition`.

## Request Syntax
<a name="API_GetUnfilteredPartitionMetadata_RequestSyntax"></a>

```
{
   "AuditContext": {
      "AdditionalAuditContext": "{{string}}",
      "AllColumnsRequested": {{boolean}},
      "RequestedColumns": [ "{{string}}" ]
   },
   "CatalogId": "{{string}}",
   "DatabaseName": "{{string}}",
   "PartitionValues": [ "{{string}}" ],
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
   "SupportedPermissionTypes": [ "{{string}}" ],
   "TableName": "{{string}}"
}
```

## Request Parameters
<a name="API_GetUnfilteredPartitionMetadata_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [AuditContext](#API_GetUnfilteredPartitionMetadata_RequestSyntax) **   <a name="Glue-GetUnfilteredPartitionMetadata-request-AuditContext"></a>
A structure containing Lake Formation audit context information.
Type: [AuditContext](API_AuditContext.md) object
Required: No

 ** [CatalogId](#API_GetUnfilteredPartitionMetadata_RequestSyntax) **   <a name="Glue-GetUnfilteredPartitionMetadata-request-CatalogId"></a>
The catalog ID where the partition resides.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\t]*`
Required: Yes

 ** [DatabaseName](#API_GetUnfilteredPartitionMetadata_RequestSyntax) **   <a name="Glue-GetUnfilteredPartitionMetadata-request-DatabaseName"></a>
(Required) Specifies the name of a database that contains the partition.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\t]*`
Required: Yes

 ** [PartitionValues](#API_GetUnfilteredPartitionMetadata_RequestSyntax) **   <a name="Glue-GetUnfilteredPartitionMetadata-request-PartitionValues"></a>
(Required) A list of partition key values.
Type: Array of strings
Length Constraints: Minimum length of 1. Maximum length of 1024.
Required: Yes

 ** [QuerySessionContext](#API_GetUnfilteredPartitionMetadata_RequestSyntax) **   <a name="Glue-GetUnfilteredPartitionMetadata-request-QuerySessionContext"></a>
A structure used as a protocol between query engines and Lake Formation or AWS Glue. Contains both a Lake Formation generated authorization identifier and information from the request's authorization context.
Type: [QuerySessionContext](API_QuerySessionContext.md) object
Required: No

 ** [Region](#API_GetUnfilteredPartitionMetadata_RequestSyntax) **   <a name="Glue-GetUnfilteredPartitionMetadata-request-Region"></a>
Specified only if the base tables belong to a different AWS Region.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Required: No

 ** [SupportedPermissionTypes](#API_GetUnfilteredPartitionMetadata_RequestSyntax) **   <a name="Glue-GetUnfilteredPartitionMetadata-request-SupportedPermissionTypes"></a>
(Required) A list of supported permission types.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 255 items.
Valid Values: `COLUMN_PERMISSION | CELL_FILTER_PERMISSION | NESTED_PERMISSION | NESTED_CELL_PERMISSION`
Required: Yes

 ** [TableName](#API_GetUnfilteredPartitionMetadata_RequestSyntax) **   <a name="Glue-GetUnfilteredPartitionMetadata-request-TableName"></a>
(Required) Specifies the name of a table that contains the partition.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\t]*`
Required: Yes

## Response Syntax
<a name="API_GetUnfilteredPartitionMetadata_ResponseSyntax"></a>

```
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
```

## Response Elements
<a name="API_GetUnfilteredPartitionMetadata_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [AuthorizedColumns](#API_GetUnfilteredPartitionMetadata_ResponseSyntax) **   <a name="Glue-GetUnfilteredPartitionMetadata-response-AuthorizedColumns"></a>
A list of column names that the user has been granted access to.
Type: Array of strings
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\t]*`

 ** [IsRegisteredWithLakeFormation](#API_GetUnfilteredPartitionMetadata_ResponseSyntax) **   <a name="Glue-GetUnfilteredPartitionMetadata-response-IsRegisteredWithLakeFormation"></a>
A Boolean value that indicates whether the partition location is registered with Lake Formation.
Type: Boolean

 ** [Partition](#API_GetUnfilteredPartitionMetadata_ResponseSyntax) **   <a name="Glue-GetUnfilteredPartitionMetadata-response-Partition"></a>
A Partition object containing the partition metadata.
Type: [Partition](API_Partition.md) object

## Errors
<a name="API_GetUnfilteredPartitionMetadata_Errors"></a>

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
<a name="API_GetUnfilteredPartitionMetadata_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/glue-2017-03-31/GetUnfilteredPartitionMetadata)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/glue-2017-03-31/GetUnfilteredPartitionMetadata)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/glue-2017-03-31/GetUnfilteredPartitionMetadata)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/glue-2017-03-31/GetUnfilteredPartitionMetadata)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/glue-2017-03-31/GetUnfilteredPartitionMetadata)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/glue-2017-03-31/GetUnfilteredPartitionMetadata)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/glue-2017-03-31/GetUnfilteredPartitionMetadata)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/glue-2017-03-31/GetUnfilteredPartitionMetadata)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/glue-2017-03-31/GetUnfilteredPartitionMetadata)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/glue-2017-03-31/GetUnfilteredPartitionMetadata)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Glue. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query glue` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
