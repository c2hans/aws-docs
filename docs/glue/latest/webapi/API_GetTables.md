---
source_url: https://docs.aws.amazon.com/glue/latest/webapi/API_GetTables.html
---

# GetTables
<a name="API_GetTables"></a>

Retrieves the definitions of some or all of the tables in a given `Database`.

## Request Syntax
<a name="API_GetTables_RequestSyntax"></a>

```
{
   "AttributesToGet": [ "{{string}}" ],
   "AuditContext": {
      "AdditionalAuditContext": "{{string}}",
      "AllColumnsRequested": {{boolean}},
      "RequestedColumns": [ "{{string}}" ]
   },
   "CatalogId": "{{string}}",
   "DatabaseName": "{{string}}",
   "Expression": "{{string}}",
   "IncludeStatusDetails": {{boolean}},
   "MaxResults": {{number}},
   "NextToken": "{{string}}",
   "QueryAsOfTime": {{number}},
   "TransactionId": "{{string}}"
}
```

## Request Parameters
<a name="API_GetTables_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [AttributesToGet](#API_GetTables_RequestSyntax) **   <a name="Glue-GetTables-request-AttributesToGet"></a>
 Specifies the table fields returned by the `GetTables` call. This parameter doesn’t accept an empty list. The request must include `NAME`.
The following are the valid combinations of values:
+  `NAME` - Names of all tables in the database.
+  `NAME`, `TABLE_TYPE` - Names of all tables and the table types.
Type: Array of strings
Valid Values: `NAME | TABLE_TYPE`
Required: No

 ** [AuditContext](#API_GetTables_RequestSyntax) **   <a name="Glue-GetTables-request-AuditContext"></a>
A structure containing the Lake Formation [audit context](https://docs.aws.amazon.com/glue/latest/webapi/API_AuditContext.html).
Type: [AuditContext](API_AuditContext.md) object
Required: No

 ** [CatalogId](#API_GetTables_RequestSyntax) **   <a name="Glue-GetTables-request-CatalogId"></a>
The ID of the Data Catalog where the tables reside. If none is provided, the AWS account ID is used by default.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\t]*`
Required: No

 ** [DatabaseName](#API_GetTables_RequestSyntax) **   <a name="Glue-GetTables-request-DatabaseName"></a>
The database in the catalog whose tables to list. For Hive compatibility, this name is entirely lowercase.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\t]*`
Required: Yes

 ** [Expression](#API_GetTables_RequestSyntax) **   <a name="Glue-GetTables-request-Expression"></a>
A regular expression pattern. If present, only those tables whose names match the pattern are returned.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 2048.
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\t]*`
Required: No

 ** [IncludeStatusDetails](#API_GetTables_RequestSyntax) **   <a name="Glue-GetTables-request-IncludeStatusDetails"></a>
Specifies whether to include status details related to a request to create or update an AWS Glue Data Catalog view.
Type: Boolean
Required: No

 ** [MaxResults](#API_GetTables_RequestSyntax) **   <a name="Glue-GetTables-request-MaxResults"></a>
The maximum number of tables to return in a single response.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 100.
Required: No

 ** [NextToken](#API_GetTables_RequestSyntax) **   <a name="Glue-GetTables-request-NextToken"></a>
A continuation token, included if this is a continuation call.
Type: String
Required: No

 ** [QueryAsOfTime](#API_GetTables_RequestSyntax) **   <a name="Glue-GetTables-request-QueryAsOfTime"></a>
The time as of when to read the table contents. If not set, the most recent transaction commit time will be used. Cannot be specified along with `TransactionId`.
Type: Timestamp
Required: No

 ** [TransactionId](#API_GetTables_RequestSyntax) **   <a name="Glue-GetTables-request-TransactionId"></a>
The transaction ID at which to read the table contents.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[\p{L}\p{N}\p{P}]*`
Required: No

## Response Syntax
<a name="API_GetTables_ResponseSyntax"></a>

```
{
   "NextToken": "string",
   "TableList": [
      {
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
   ]
}
```

## Response Elements
<a name="API_GetTables_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [NextToken](#API_GetTables_ResponseSyntax) **   <a name="Glue-GetTables-response-NextToken"></a>
A continuation token, present if the current list segment is not the last.
Type: String

 ** [TableList](#API_GetTables_ResponseSyntax) **   <a name="Glue-GetTables-response-TableList"></a>
A list of the requested `Table` objects.
Type: Array of [Table](API_Table.md) objects

## Errors
<a name="API_GetTables_Errors"></a>

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
<a name="API_GetTables_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/glue-2017-03-31/GetTables)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/glue-2017-03-31/GetTables)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/glue-2017-03-31/GetTables)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/glue-2017-03-31/GetTables)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/glue-2017-03-31/GetTables)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/glue-2017-03-31/GetTables)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/glue-2017-03-31/GetTables)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/glue-2017-03-31/GetTables)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/glue-2017-03-31/GetTables)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/glue-2017-03-31/GetTables)
