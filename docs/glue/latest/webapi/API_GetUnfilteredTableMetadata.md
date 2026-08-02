---
source_url: https://docs.aws.amazon.com/glue/latest/webapi/API_GetUnfilteredTableMetadata.html
---

# GetUnfilteredTableMetadata
<a name="API_GetUnfilteredTableMetadata"></a>

Allows a third-party analytical engine to retrieve unfiltered table metadata from the Data Catalog.

For IAM authorization, the public IAM action associated with this API is `glue:GetTable`.

## Request Syntax
<a name="API_GetUnfilteredTableMetadata_RequestSyntax"></a>

```
{
   "AuditContext": {
      "AdditionalAuditContext": "{{string}}",
      "AllColumnsRequested": {{boolean}},
      "RequestedColumns": [ "{{string}}" ]
   },
   "CatalogId": "{{string}}",
   "DatabaseName": "{{string}}",
   "Name": "{{string}}",
   "ParentResourceArn": "{{string}}",
   "Permissions": [ "{{string}}" ],
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
   "RootResourceArn": "{{string}}",
   "SupportedDialect": {
      "Dialect": "{{string}}",
      "DialectVersion": "{{string}}"
   },
   "SupportedPermissionTypes": [ "{{string}}" ]
}
```

## Request Parameters
<a name="API_GetUnfilteredTableMetadata_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [AuditContext](#API_GetUnfilteredTableMetadata_RequestSyntax) **   <a name="Glue-GetUnfilteredTableMetadata-request-AuditContext"></a>
A structure containing Lake Formation audit context information.
Type: [AuditContext](API_AuditContext.md) object
Required: No

 ** [CatalogId](#API_GetUnfilteredTableMetadata_RequestSyntax) **   <a name="Glue-GetUnfilteredTableMetadata-request-CatalogId"></a>
The catalog ID where the table resides.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\t]*`
Required: Yes

 ** [DatabaseName](#API_GetUnfilteredTableMetadata_RequestSyntax) **   <a name="Glue-GetUnfilteredTableMetadata-request-DatabaseName"></a>
(Required) Specifies the name of a database that contains the table.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\t]*`
Required: Yes

 ** [Name](#API_GetUnfilteredTableMetadata_RequestSyntax) **   <a name="Glue-GetUnfilteredTableMetadata-request-Name"></a>
(Required) Specifies the name of a table for which you are requesting metadata.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\t]*`
Required: Yes

 ** [ParentResourceArn](#API_GetUnfilteredTableMetadata_RequestSyntax) **   <a name="Glue-GetUnfilteredTableMetadata-request-ParentResourceArn"></a>
The resource ARN of the view.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Required: No

 ** [Permissions](#API_GetUnfilteredTableMetadata_RequestSyntax) **   <a name="Glue-GetUnfilteredTableMetadata-request-Permissions"></a>
The Lake Formation data permissions of the caller on the table. Used to authorize the call when no view context is found.
Type: Array of strings
Valid Values: `ALL | SELECT | ALTER | DROP | DELETE | INSERT | CREATE_DATABASE | CREATE_TABLE | DATA_LOCATION_ACCESS`
Required: No

 ** [QuerySessionContext](#API_GetUnfilteredTableMetadata_RequestSyntax) **   <a name="Glue-GetUnfilteredTableMetadata-request-QuerySessionContext"></a>
A structure used as a protocol between query engines and Lake Formation or AWS Glue. Contains both a Lake Formation generated authorization identifier and information from the request's authorization context.
Type: [QuerySessionContext](API_QuerySessionContext.md) object
Required: No

 ** [Region](#API_GetUnfilteredTableMetadata_RequestSyntax) **   <a name="Glue-GetUnfilteredTableMetadata-request-Region"></a>
Specified only if the base tables belong to a different AWS Region.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Required: No

 ** [RootResourceArn](#API_GetUnfilteredTableMetadata_RequestSyntax) **   <a name="Glue-GetUnfilteredTableMetadata-request-RootResourceArn"></a>
The resource ARN of the root view in a chain of nested views.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Required: No

 ** [SupportedDialect](#API_GetUnfilteredTableMetadata_RequestSyntax) **   <a name="Glue-GetUnfilteredTableMetadata-request-SupportedDialect"></a>
A structure specifying the dialect and dialect version used by the query engine.
Type: [SupportedDialect](API_SupportedDialect.md) object
Required: No

 ** [SupportedPermissionTypes](#API_GetUnfilteredTableMetadata_RequestSyntax) **   <a name="Glue-GetUnfilteredTableMetadata-request-SupportedPermissionTypes"></a>
Indicates the level of filtering a third-party analytical engine is capable of enforcing when calling the `GetUnfilteredTableMetadata` API operation. Accepted values are:
+  `COLUMN_PERMISSION` - Column permissions ensure that users can access only specific columns in the table. If there are particular columns contain sensitive data, data lake administrators can define column filters that exclude access to specific columns.
+  `CELL_FILTER_PERMISSION` - Cell-level filtering combines column filtering (include or exclude columns) and row filter expressions to restrict access to individual elements in the table.
+  `NESTED_PERMISSION` - Nested permissions combines cell-level filtering and nested column filtering to restrict access to columns and/or nested columns in specific rows based on row filter expressions.
+  `NESTED_CELL_PERMISSION` - Nested cell permissions combines nested permission with nested cell-level filtering. This allows different subsets of nested columns to be restricted based on an array of row filter expressions.
Note: Each of these permission types follows a hierarchical order where each subsequent permission type includes all permission of the previous type.
Important: If you provide a supported permission type that doesn't match the user's level of permissions on the table, then Lake Formation raises an exception. For example, if the third-party engine calling the `GetUnfilteredTableMetadata` operation can enforce only column-level filtering, and the user has nested cell filtering applied on the table, Lake Formation throws an exception, and will not return unfiltered table metadata and data access credentials.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 255 items.
Valid Values: `COLUMN_PERMISSION | CELL_FILTER_PERMISSION | NESTED_PERMISSION | NESTED_CELL_PERMISSION`
Required: Yes

## Response Syntax
<a name="API_GetUnfilteredTableMetadata_ResponseSyntax"></a>

```
{
   "AuthorizedColumns": [ "string" ],
   "CellFilters": [
      {
         "ColumnName": "string",
         "RowFilterExpression": "string"
      }
   ],
   "IsMaterializedView": boolean,
   "IsMultiDialectView": boolean,
   "IsProtected": boolean,
   "IsRegisteredWithLakeFormation": boolean,
   "Permissions": [ "string" ],
   "QueryAuthorizationId": "string",
   "ResourceArn": "string",
   "RowFilter": "string",
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
<a name="API_GetUnfilteredTableMetadata_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [AuthorizedColumns](#API_GetUnfilteredTableMetadata_ResponseSyntax) **   <a name="Glue-GetUnfilteredTableMetadata-response-AuthorizedColumns"></a>
A list of column names that the user has been granted access to.
Type: Array of strings
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\t]*`

 ** [CellFilters](#API_GetUnfilteredTableMetadata_ResponseSyntax) **   <a name="Glue-GetUnfilteredTableMetadata-response-CellFilters"></a>
A list of column row filters.
Type: Array of [ColumnRowFilter](API_ColumnRowFilter.md) objects

 ** [IsMaterializedView](#API_GetUnfilteredTableMetadata_ResponseSyntax) **   <a name="Glue-GetUnfilteredTableMetadata-response-IsMaterializedView"></a>
Indicates if a table is a materialized view.
Type: Boolean

 ** [IsMultiDialectView](#API_GetUnfilteredTableMetadata_ResponseSyntax) **   <a name="Glue-GetUnfilteredTableMetadata-response-IsMultiDialectView"></a>
Specifies whether the view supports the SQL dialects of one or more different query engines and can therefore be read by those engines.
Type: Boolean

 ** [IsProtected](#API_GetUnfilteredTableMetadata_ResponseSyntax) **   <a name="Glue-GetUnfilteredTableMetadata-response-IsProtected"></a>
A flag that instructs the engine not to push user-provided operations into the logical plan of the view during query planning. However, if set this flag does not guarantee that the engine will comply. Refer to the engine's documentation to understand the guarantees provided, if any.
Type: Boolean

 ** [IsRegisteredWithLakeFormation](#API_GetUnfilteredTableMetadata_ResponseSyntax) **   <a name="Glue-GetUnfilteredTableMetadata-response-IsRegisteredWithLakeFormation"></a>
A Boolean value that indicates whether the partition location is registered with Lake Formation.
Type: Boolean

 ** [Permissions](#API_GetUnfilteredTableMetadata_ResponseSyntax) **   <a name="Glue-GetUnfilteredTableMetadata-response-Permissions"></a>
The Lake Formation data permissions of the caller on the table. Used to authorize the call when no view context is found.
Type: Array of strings
Valid Values: `ALL | SELECT | ALTER | DROP | DELETE | INSERT | CREATE_DATABASE | CREATE_TABLE | DATA_LOCATION_ACCESS`

 ** [QueryAuthorizationId](#API_GetUnfilteredTableMetadata_ResponseSyntax) **   <a name="Glue-GetUnfilteredTableMetadata-response-QueryAuthorizationId"></a>
A cryptographically generated query identifier generated by AWS Glue or Lake Formation.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\t]*`

 ** [ResourceArn](#API_GetUnfilteredTableMetadata_ResponseSyntax) **   <a name="Glue-GetUnfilteredTableMetadata-response-ResourceArn"></a>
The resource ARN of the parent resource extracted from the request.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.

 ** [RowFilter](#API_GetUnfilteredTableMetadata_ResponseSyntax) **   <a name="Glue-GetUnfilteredTableMetadata-response-RowFilter"></a>
The filter that applies to the table. For example when applying the filter in SQL, it would go in the `WHERE` clause and can be evaluated by using an `AND` operator with any other predicates applied by the user querying the table.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 2048.
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\r\n\t]*`

 ** [Table](#API_GetUnfilteredTableMetadata_ResponseSyntax) **   <a name="Glue-GetUnfilteredTableMetadata-response-Table"></a>
A Table object containing the table metadata.
Type: [Table](API_Table.md) object

## Errors
<a name="API_GetUnfilteredTableMetadata_Errors"></a>

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
<a name="API_GetUnfilteredTableMetadata_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/glue-2017-03-31/GetUnfilteredTableMetadata)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/glue-2017-03-31/GetUnfilteredTableMetadata)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/glue-2017-03-31/GetUnfilteredTableMetadata)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/glue-2017-03-31/GetUnfilteredTableMetadata)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/glue-2017-03-31/GetUnfilteredTableMetadata)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/glue-2017-03-31/GetUnfilteredTableMetadata)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/glue-2017-03-31/GetUnfilteredTableMetadata)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/glue-2017-03-31/GetUnfilteredTableMetadata)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/glue-2017-03-31/GetUnfilteredTableMetadata)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/glue-2017-03-31/GetUnfilteredTableMetadata)
