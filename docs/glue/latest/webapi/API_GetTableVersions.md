---
source_url: https://docs.aws.amazon.com/glue/latest/webapi/API_GetTableVersions.html
---

# GetTableVersions
<a name="API_GetTableVersions"></a>

Retrieves a list of strings that identify available versions of a specified table.

## Request Syntax
<a name="API_GetTableVersions_RequestSyntax"></a>

```
{
   "CatalogId": "{{string}}",
   "DatabaseName": "{{string}}",
   "MaxResults": {{number}},
   "NextToken": "{{string}}",
   "TableName": "{{string}}"
}
```

## Request Parameters
<a name="API_GetTableVersions_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [CatalogId](#API_GetTableVersions_RequestSyntax) **   <a name="Glue-GetTableVersions-request-CatalogId"></a>
The ID of the Data Catalog where the tables reside. If none is provided, the AWS account ID is used by default.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\t]*`
Required: No

 ** [DatabaseName](#API_GetTableVersions_RequestSyntax) **   <a name="Glue-GetTableVersions-request-DatabaseName"></a>
The database in the catalog in which the table resides. For Hive compatibility, this name is entirely lowercase.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\t]*`
Required: Yes

 ** [MaxResults](#API_GetTableVersions_RequestSyntax) **   <a name="Glue-GetTableVersions-request-MaxResults"></a>
The maximum number of table versions to return in one response.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 100.
Required: No

 ** [NextToken](#API_GetTableVersions_RequestSyntax) **   <a name="Glue-GetTableVersions-request-NextToken"></a>
A continuation token, if this is not the first call.
Type: String
Required: No

 ** [TableName](#API_GetTableVersions_RequestSyntax) **   <a name="Glue-GetTableVersions-request-TableName"></a>
The name of the table. For Hive compatibility, this name is entirely lowercase.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\t]*`
Required: Yes

## Response Syntax
<a name="API_GetTableVersions_ResponseSyntax"></a>

```
{
   "NextToken": "string",
   "TableVersions": [
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
         },
         "VersionId": "string"
      }
   ]
}
```

## Response Elements
<a name="API_GetTableVersions_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [NextToken](#API_GetTableVersions_ResponseSyntax) **   <a name="Glue-GetTableVersions-response-NextToken"></a>
A continuation token, if the list of available versions does not include the last one.
Type: String

 ** [TableVersions](#API_GetTableVersions_ResponseSyntax) **   <a name="Glue-GetTableVersions-response-TableVersions"></a>
A list of strings identifying available versions of the specified table.
Type: Array of [TableVersion](API_TableVersion.md) objects

## Errors
<a name="API_GetTableVersions_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

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

## See Also
<a name="API_GetTableVersions_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/glue-2017-03-31/GetTableVersions)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/glue-2017-03-31/GetTableVersions)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/glue-2017-03-31/GetTableVersions)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/glue-2017-03-31/GetTableVersions)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/glue-2017-03-31/GetTableVersions)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/glue-2017-03-31/GetTableVersions)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/glue-2017-03-31/GetTableVersions)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/glue-2017-03-31/GetTableVersions)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/glue-2017-03-31/GetTableVersions)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/glue-2017-03-31/GetTableVersions)
