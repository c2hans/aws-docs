---
source_url: https://docs.aws.amazon.com/lake-formation/latest/APIReference/API_ListPermissions.html
---

# ListPermissions
<a name="API_ListPermissions"></a>

Returns a list of the principal permissions on the resource, filtered by the permissions of the caller. For example, if you are granted an ALTER permission, you are able to see only the principal permissions for ALTER.

This operation returns only those permissions that have been explicitly granted. If both `Principal` and `Resource` parameters are provided, the response returns effective permissions rather than the explicitly granted permissions.

For information about permissions, see [Security and Access Control to Metadata and Data](https://docs.aws.amazon.com/lake-formation/latest/dg/security-data-access.html).

## Request Syntax
<a name="API_ListPermissions_RequestSyntax"></a>

```
POST /ListPermissions HTTP/1.1
Content-type: application/json

{
   "CatalogId": "{{string}}",
   "IncludeRelated": "{{string}}",
   "MaxResults": {{number}},
   "NextToken": "{{string}}",
   "Principal": {
      "DataLakePrincipalIdentifier": "{{string}}"
   },
   "Resource": {
      "Catalog": {
         "Id": "{{string}}"
      },
      "Database": {
         "CatalogId": "{{string}}",
         "Name": "{{string}}"
      },
      "DataCellsFilter": {
         "DatabaseName": "{{string}}",
         "Name": "{{string}}",
         "TableCatalogId": "{{string}}",
         "TableName": "{{string}}"
      },
      "DataLocation": {
         "CatalogId": "{{string}}",
         "ResourceArn": "{{string}}"
      },
      "LFTag": {
         "CatalogId": "{{string}}",
         "TagKey": "{{string}}",
         "TagValues": [ "{{string}}" ]
      },
      "LFTagExpression": {
         "CatalogId": "{{string}}",
         "Name": "{{string}}"
      },
      "LFTagPolicy": {
         "CatalogId": "{{string}}",
         "Expression": [
            {
               "TagKey": "{{string}}",
               "TagValues": [ "{{string}}" ]
            }
         ],
         "ExpressionName": "{{string}}",
         "ResourceType": "{{string}}"
      },
      "Table": {
         "CatalogId": "{{string}}",
         "DatabaseName": "{{string}}",
         "Name": "{{string}}",
         "TableWildcard": {
         }
      },
      "TableWithColumns": {
         "CatalogId": "{{string}}",
         "ColumnNames": [ "{{string}}" ],
         "ColumnWildcard": {
            "ExcludedColumnNames": [ "{{string}}" ]
         },
         "DatabaseName": "{{string}}",
         "Name": "{{string}}"
      }
   },
   "ResourceType": "{{string}}"
}
```

## URI Request Parameters
<a name="API_ListPermissions_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_ListPermissions_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [CatalogId](#API_ListPermissions_RequestSyntax) **   <a name="lakeformation-ListPermissions-request-CatalogId"></a>
The identifier for the Data Catalog. By default, the account ID. The Data Catalog is the persistent metadata store. It contains database definitions, table definitions, and other control information to manage your AWS Lake Formation environment.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\t]*`
Required: No

 ** [IncludeRelated](#API_ListPermissions_RequestSyntax) **   <a name="lakeformation-ListPermissions-request-IncludeRelated"></a>
Indicates that related permissions should be included in the results when listing permissions on a table resource.
Set the field to `TRUE` to show the cell filters on a table resource. Default is `FALSE`. The Principal parameter must not be specified when requesting cell filter information.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 5.
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\t]*`
Required: No

 ** [MaxResults](#API_ListPermissions_RequestSyntax) **   <a name="lakeformation-ListPermissions-request-MaxResults"></a>
The maximum number of results to return.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 1000.
Required: No

 ** [NextToken](#API_ListPermissions_RequestSyntax) **   <a name="lakeformation-ListPermissions-request-NextToken"></a>
A continuation token, if this is not the first call to retrieve this list.
Type: String
Required: No

 ** [Principal](#API_ListPermissions_RequestSyntax) **   <a name="lakeformation-ListPermissions-request-Principal"></a>
Specifies a principal to filter the permissions returned.
Type: [DataLakePrincipal](API_DataLakePrincipal.md) object
Required: No

 ** [Resource](#API_ListPermissions_RequestSyntax) **   <a name="lakeformation-ListPermissions-request-Resource"></a>
A resource where you will get a list of the principal permissions.
This operation does not support getting privileges on a table with columns. Instead, call this operation on the table, and the operation returns the table and the table w columns.
Type: [Resource](API_Resource.md) object
Required: No

 ** [ResourceType](#API_ListPermissions_RequestSyntax) **   <a name="lakeformation-ListPermissions-request-ResourceType"></a>
Specifies a resource type to filter the permissions returned.
Type: String
Valid Values: `CATALOG | DATABASE | TABLE | DATA_LOCATION | LF_TAG | LF_TAG_POLICY | LF_TAG_POLICY_DATABASE | LF_TAG_POLICY_TABLE | LF_NAMED_TAG_EXPRESSION`
Required: No

## Response Syntax
<a name="API_ListPermissions_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "NextToken": "string",
   "PrincipalResourcePermissions": [
      {
         "AdditionalDetails": {
            "ResourceShare": [ "string" ]
         },
         "Condition": {
            "Expression": "string"
         },
         "LastUpdated": number,
         "LastUpdatedBy": "string",
         "Permissions": [ "string" ],
         "PermissionsWithGrantOption": [ "string" ],
         "Principal": {
            "DataLakePrincipalIdentifier": "string"
         },
         "Resource": {
            "Catalog": {
               "Id": "string"
            },
            "Database": {
               "CatalogId": "string",
               "Name": "string"
            },
            "DataCellsFilter": {
               "DatabaseName": "string",
               "Name": "string",
               "TableCatalogId": "string",
               "TableName": "string"
            },
            "DataLocation": {
               "CatalogId": "string",
               "ResourceArn": "string"
            },
            "LFTag": {
               "CatalogId": "string",
               "TagKey": "string",
               "TagValues": [ "string" ]
            },
            "LFTagExpression": {
               "CatalogId": "string",
               "Name": "string"
            },
            "LFTagPolicy": {
               "CatalogId": "string",
               "Expression": [
                  {
                     "TagKey": "string",
                     "TagValues": [ "string" ]
                  }
               ],
               "ExpressionName": "string",
               "ResourceType": "string"
            },
            "Table": {
               "CatalogId": "string",
               "DatabaseName": "string",
               "Name": "string",
               "TableWildcard": {
               }
            },
            "TableWithColumns": {
               "CatalogId": "string",
               "ColumnNames": [ "string" ],
               "ColumnWildcard": {
                  "ExcludedColumnNames": [ "string" ]
               },
               "DatabaseName": "string",
               "Name": "string"
            }
         }
      }
   ]
}
```

## Response Elements
<a name="API_ListPermissions_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [NextToken](#API_ListPermissions_ResponseSyntax) **   <a name="lakeformation-ListPermissions-response-NextToken"></a>
A continuation token, if this is not the first call to retrieve this list.
Type: String

 ** [PrincipalResourcePermissions](#API_ListPermissions_ResponseSyntax) **   <a name="lakeformation-ListPermissions-response-PrincipalResourcePermissions"></a>
A list of principals and their permissions on the resource for the specified principal and resource types.
Type: Array of [PrincipalResourcePermissions](API_PrincipalResourcePermissions.md) objects

## Errors
<a name="API_ListPermissions_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InternalServiceException **
An internal service error occurred.
 ** Message **
A message describing the problem.
HTTP Status Code: 500

 ** InvalidInputException **
The input provided was not valid.
 ** Message **
A message describing the problem.
HTTP Status Code: 400

 ** OperationTimeoutException **
The operation timed out.
 ** Message **
A message describing the problem.
HTTP Status Code: 400

## See Also
<a name="API_ListPermissions_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/lakeformation-2017-03-31/ListPermissions)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/lakeformation-2017-03-31/ListPermissions)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/lakeformation-2017-03-31/ListPermissions)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/lakeformation-2017-03-31/ListPermissions)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/lakeformation-2017-03-31/ListPermissions)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/lakeformation-2017-03-31/ListPermissions)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/lakeformation-2017-03-31/ListPermissions)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/lakeformation-2017-03-31/ListPermissions)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/lakeformation-2017-03-31/ListPermissions)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/lakeformation-2017-03-31/ListPermissions)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Lake Formation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query lake-formation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
