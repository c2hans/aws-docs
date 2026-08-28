---
source_url: https://docs.aws.amazon.com/glue/latest/webapi/API_GetTable.html
---

# GetTable
<a name="API_GetTable"></a>

Retrieves the `Table` definition in a Data Catalog for a specified table.

## Request Syntax
<a name="API_GetTable_RequestSyntax"></a>

```
{
   "AuditContext": {
      "AdditionalAuditContext": "{{string}}",
      "AllColumnsRequested": {{boolean}},
      "RequestedColumns": [ "{{string}}" ]
   },
   "CatalogId": "{{string}}",
   "DatabaseName": "{{string}}",
   "IncludeStatusDetails": {{boolean}},
   "Name": "{{string}}",
   "QueryAsOfTime": {{number}},
   "TransactionId": "{{string}}"
}
```

## Request Parameters
<a name="API_GetTable_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [AuditContext](#API_GetTable_RequestSyntax) **   <a name="Glue-GetTable-request-AuditContext"></a>
A structure containing the Lake Formation [audit context](https://docs.aws.amazon.com/glue/latest/webapi/API_AuditContext.html).
Type: [AuditContext](API_AuditContext.md) object
Required: No

 ** [CatalogId](#API_GetTable_RequestSyntax) **   <a name="Glue-GetTable-request-CatalogId"></a>
The ID of the Data Catalog where the table resides. If none is provided, the AWS account ID is used by default.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\t]*`
Required: No

 ** [DatabaseName](#API_GetTable_RequestSyntax) **   <a name="Glue-GetTable-request-DatabaseName"></a>
The name of the database in the catalog in which the table resides. For Hive compatibility, this name is entirely lowercase.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\t]*`
Required: Yes

 ** [IncludeStatusDetails](#API_GetTable_RequestSyntax) **   <a name="Glue-GetTable-request-IncludeStatusDetails"></a>
Specifies whether to include status details related to a request to create or update an AWS Glue Data Catalog view.
Type: Boolean
Required: No

 ** [Name](#API_GetTable_RequestSyntax) **   <a name="Glue-GetTable-request-Name"></a>
The name of the table for which to retrieve the definition. For Hive compatibility, this name is entirely lowercase.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\t]*`
Required: Yes

 ** [QueryAsOfTime](#API_GetTable_RequestSyntax) **   <a name="Glue-GetTable-request-QueryAsOfTime"></a>
The time as of when to read the table contents. If not set, the most recent transaction commit time will be used. Cannot be specified along with `TransactionId`.
Type: Timestamp
Required: No

 ** [TransactionId](#API_GetTable_RequestSyntax) **   <a name="Glue-GetTable-request-TransactionId"></a>
The transaction ID at which to read the table contents.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[\p{L}\p{N}\p{P}]*`
Required: No

## Response Syntax
<a name="API_GetTable_ResponseSyntax"></a>

```
{
   "Table": {
      "CatalogId": "string",
      "CreatedBy": "string",
      "CreateTime": number,
      "DatabaseName": "string",
      "Description": "string",
      "FederatedTable": {
         "ConnectionName": "string",
         "ConnectionType": "string",
         "DatabaseIdentifier": "string",
         "Identifier": "string"
      },
      "IsMaterializedView": boolean,
      "IsMultiDialectView": boolean,
      "IsRegisteredWithLakeFormation": boolean,
      "LastAccessTime": number,
      "LastAnalyzedTime": number,
      "Name": "string",
      "Owner": "string",
      "Parameters": {
         "string" : "string"
      },
      "PartitionKeys": [
         {
            "Comment": "string",
            "Name": "string",
            "Parameters": {
               "string" : "string"
            },
            "Type": "string"
         }
      ],
      "Retention": number,
      "Status": {
         "Action": "string",
         "Details": {
            "RequestedChange": "Table",
            "ViewValidations": [
               {
                  "Dialect": "string",
                  "DialectVersion": "string",
                  "Error": {
                     "ErrorCode": "string",
                     "ErrorMessage": "string"
                  },
                  "State": "string",
                  "UpdateTime": number,
                  "ViewValidationText": "string"
               }
            ]
         },
         "Error": {
            "ErrorCode": "string",
            "ErrorMessage": "string"
         },
         "RequestedBy": "string",
         "RequestTime": number,
         "State": "string",
         "UpdatedBy": "string",
         "UpdateTime": number
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
      "TableType": "string",
      "TargetTable": {
         "CatalogId": "string",
         "DatabaseName": "string",
         "Name": "string",
         "Region": "string"
      },
      "UpdateTime": number,
      "VersionId": "string",
      "ViewDefinition": {
         "Definer": "string",
         "IsProtected": boolean,
         "LastRefreshType": "string",
         "RefreshSeconds": number,
         "Representations": [
            {
               "Dialect": "string",
               "DialectVersion": "string",
               "IsStale": boolean,
               "ValidationConnection": "string",
               "ViewExpandedText": "string",
               "ViewOriginalText": "string"
            }
         ],
         "SubObjects": [ "string" ],
         "SubObjectVersionIds": [ number ],
         "ViewVersionId": number,
         "ViewVersionToken": "string"
      },
      "ViewExpandedText": "string",
      "ViewOriginalText": "string"
   }
}
```

## Response Elements
<a name="API_GetTable_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [Table](#API_GetTable_ResponseSyntax) **   <a name="Glue-GetTable-response-Table"></a>
The `Table` object that defines the specified table.
Type: [Table](API_Table.md) object

## Errors
<a name="API_GetTable_Errors"></a>

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

 ** ResourceNotReadyException **
A resource was not ready for a transaction.
 ** Message **
A message describing the problem.
HTTP Status Code: 400

## See Also
<a name="API_GetTable_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/glue-2017-03-31/GetTable)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/glue-2017-03-31/GetTable)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/glue-2017-03-31/GetTable)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/glue-2017-03-31/GetTable)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/glue-2017-03-31/GetTable)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/glue-2017-03-31/GetTable)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/glue-2017-03-31/GetTable)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/glue-2017-03-31/GetTable)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/glue-2017-03-31/GetTable)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/glue-2017-03-31/GetTable)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Glue. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query glue` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
