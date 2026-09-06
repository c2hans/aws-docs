---
source_url: https://docs.aws.amazon.com/lake-formation/latest/APIReference/API_BatchRevokePermissions.html
---

# BatchRevokePermissions
<a name="API_BatchRevokePermissions"></a>

Batch operation to revoke permissions from the principal.

## Request Syntax
<a name="API_BatchRevokePermissions_RequestSyntax"></a>

```
POST /BatchRevokePermissions HTTP/1.1
Content-type: application/json

{
   "CatalogId": "{{string}}",
   "Entries": [
      {
         "Condition": {
            "Expression": "{{string}}"
         },
         "Id": "{{string}}",
         "Permissions": [ "{{string}}" ],
         "PermissionsWithGrantOption": [ "{{string}}" ],
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
         }
      }
   ]
}
```

## URI Request Parameters
<a name="API_BatchRevokePermissions_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_BatchRevokePermissions_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [CatalogId](#API_BatchRevokePermissions_RequestSyntax) **   <a name="lakeformation-BatchRevokePermissions-request-CatalogId"></a>
The identifier for the Data Catalog. By default, the account ID. The Data Catalog is the persistent metadata store. It contains database definitions, table definitions, and other control information to manage your AWS Lake Formation environment.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\t]*`
Required: No

 ** [Entries](#API_BatchRevokePermissions_RequestSyntax) **   <a name="lakeformation-BatchRevokePermissions-request-Entries"></a>
A list of up to 20 entries for resource permissions to be revoked by batch operation to the principal.
Type: Array of [BatchPermissionsRequestEntry](API_BatchPermissionsRequestEntry.md) objects
Required: Yes

## Response Syntax
<a name="API_BatchRevokePermissions_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "Failures": [
      {
         "Error": {
            "ErrorCode": "string",
            "ErrorMessage": "string"
         },
         "RequestEntry": {
            "Condition": {
               "Expression": "string"
            },
            "Id": "string",
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
      }
   ]
}
```

## Response Elements
<a name="API_BatchRevokePermissions_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [Failures](#API_BatchRevokePermissions_ResponseSyntax) **   <a name="lakeformation-BatchRevokePermissions-response-Failures"></a>
A list of failures to revoke permissions to the resources.
Type: Array of [BatchPermissionsFailureEntry](API_BatchPermissionsFailureEntry.md) objects

## Errors
<a name="API_BatchRevokePermissions_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

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
<a name="API_BatchRevokePermissions_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/lakeformation-2017-03-31/BatchRevokePermissions)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/lakeformation-2017-03-31/BatchRevokePermissions)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/lakeformation-2017-03-31/BatchRevokePermissions)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/lakeformation-2017-03-31/BatchRevokePermissions)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/lakeformation-2017-03-31/BatchRevokePermissions)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/lakeformation-2017-03-31/BatchRevokePermissions)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/lakeformation-2017-03-31/BatchRevokePermissions)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/lakeformation-2017-03-31/BatchRevokePermissions)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/lakeformation-2017-03-31/BatchRevokePermissions)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/lakeformation-2017-03-31/BatchRevokePermissions)
