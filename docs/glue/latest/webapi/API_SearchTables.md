---
source_url: https://docs.aws.amazon.com/glue/latest/webapi/API_SearchTables.html
---

# SearchTables
<a name="API_SearchTables"></a>

Searches a set of tables based on properties in the table metadata as well as on the parent database. You can search against text or filter conditions.

You can only get tables that you have access to based on the security policies defined in Lake Formation. You need at least a read-only access to the table for it to be returned. If you do not have access to all the columns in the table, these columns will not be searched against when returning the list of tables back to you. If you have access to the columns but not the data in the columns, those columns and the associated metadata for those columns will be included in the search.

## Request Syntax
<a name="API_SearchTables_RequestSyntax"></a>

```
{
   "CatalogId": "{{string}}",
   "Filters": [
      {
         "Comparator": "{{string}}",
         "Key": "{{string}}",
         "Value": "{{string}}"
      }
   ],
   "IncludeStatusDetails": {{boolean}},
   "MaxResults": {{number}},
   "NextToken": "{{string}}",
   "ResourceShareType": "{{string}}",
   "SearchText": "{{string}}",
   "SortCriteria": [
      {
         "FieldName": "{{string}}",
         "Sort": "{{string}}"
      }
   ]
}
```

## Request Parameters
<a name="API_SearchTables_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [CatalogId](#API_SearchTables_RequestSyntax) **   <a name="Glue-SearchTables-request-CatalogId"></a>
A unique identifier, consisting of ` account_id `.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\t]*`
Required: No

 ** [Filters](#API_SearchTables_RequestSyntax) **   <a name="Glue-SearchTables-request-Filters"></a>
A list of key-value pairs, and a comparator used to filter the search results. Returns all entities matching the predicate.
The `Comparator` member of the `PropertyPredicate` struct is used only for time fields, and can be omitted for other field types. Also, when comparing string values, such as when `Key=Name`, a fuzzy match algorithm is used. The `Key` field (for example, the value of the `Name` field) is split on certain punctuation characters, for example, -, :, \#, etc. into tokens. Then each token is exact-match compared with the `Value` member of `PropertyPredicate`. For example, if `Key=Name` and `Value=link`, tables named `customer-link` and `xx-link-yy` are returned, but `xxlinkyy` is not returned.
Type: Array of [PropertyPredicate](API_PropertyPredicate.md) objects
Required: No

 ** [IncludeStatusDetails](#API_SearchTables_RequestSyntax) **   <a name="Glue-SearchTables-request-IncludeStatusDetails"></a>
Specifies whether to include status details related to a request to create or update an AWS Glue Data Catalog view.
Type: Boolean
Required: No

 ** [MaxResults](#API_SearchTables_RequestSyntax) **   <a name="Glue-SearchTables-request-MaxResults"></a>
The maximum number of tables to return in a single response.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 1000.
Required: No

 ** [NextToken](#API_SearchTables_RequestSyntax) **   <a name="Glue-SearchTables-request-NextToken"></a>
A continuation token, included if this is a continuation call.
Type: String
Required: No

 ** [ResourceShareType](#API_SearchTables_RequestSyntax) **   <a name="Glue-SearchTables-request-ResourceShareType"></a>
Allows you to specify that you want to search the tables shared with your account. The allowable values are `FOREIGN` or `ALL`.
+ If set to `FOREIGN`, will search the tables shared with your account.
+ If set to `ALL`, will search the tables shared with your account, as well as the tables in yor local account.
Type: String
Valid Values: `FOREIGN | ALL | FEDERATED`
Required: No

 ** [SearchText](#API_SearchTables_RequestSyntax) **   <a name="Glue-SearchTables-request-SearchText"></a>
A string used for a text search.
Specifying a value in quotes filters based on an exact match to the value.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Required: No

 ** [SortCriteria](#API_SearchTables_RequestSyntax) **   <a name="Glue-SearchTables-request-SortCriteria"></a>
A list of criteria for sorting the results by a field name, in an ascending or descending order.
Type: Array of [SortCriterion](API_SortCriterion.md) objects
Array Members: Minimum number of 0 items. Maximum number of 1 item.
Required: No

## Response Syntax
<a name="API_SearchTables_ResponseSyntax"></a>

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
<a name="API_SearchTables_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [NextToken](#API_SearchTables_ResponseSyntax) **   <a name="Glue-SearchTables-response-NextToken"></a>
A continuation token, present if the current list segment is not the last.
Type: String

 ** [TableList](#API_SearchTables_ResponseSyntax) **   <a name="Glue-SearchTables-response-TableList"></a>
A list of the requested `Table` objects. The `SearchTables` response returns only the tables that you have access to.
Type: Array of [Table](API_Table.md) objects

## Errors
<a name="API_SearchTables_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

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
<a name="API_SearchTables_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/glue-2017-03-31/SearchTables)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/glue-2017-03-31/SearchTables)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/glue-2017-03-31/SearchTables)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/glue-2017-03-31/SearchTables)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/glue-2017-03-31/SearchTables)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/glue-2017-03-31/SearchTables)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/glue-2017-03-31/SearchTables)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/glue-2017-03-31/SearchTables)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/glue-2017-03-31/SearchTables)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/glue-2017-03-31/SearchTables)
