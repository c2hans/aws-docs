---
source_url: https://docs.aws.amazon.com/lake-formation/latest/APIReference/API_GetEffectivePermissionsForPath.html
---

# GetEffectivePermissionsForPath
<a name="API_GetEffectivePermissionsForPath"></a>

Returns the Lake Formation permissions for a specified table or database resource located at a path in Amazon S3. `GetEffectivePermissionsForPath` will not return databases and tables if the catalog is encrypted.

## Request Syntax
<a name="API_GetEffectivePermissionsForPath_RequestSyntax"></a>

```
POST /GetEffectivePermissionsForPath HTTP/1.1
Content-type: application/json

{
   "CatalogId": "{{string}}",
   "MaxResults": {{number}},
   "NextToken": "{{string}}",
   "ResourceArn": "{{string}}"
}
```

## URI Request Parameters
<a name="API_GetEffectivePermissionsForPath_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_GetEffectivePermissionsForPath_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [CatalogId](#API_GetEffectivePermissionsForPath_RequestSyntax) **   <a name="lakeformation-GetEffectivePermissionsForPath-request-CatalogId"></a>
The identifier for the Data Catalog. By default, the account ID. The Data Catalog is the persistent metadata store. It contains database definitions, table definitions, and other control information to manage your AWS Lake Formation environment.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\t]*`
Required: No

 ** [MaxResults](#API_GetEffectivePermissionsForPath_RequestSyntax) **   <a name="lakeformation-GetEffectivePermissionsForPath-request-MaxResults"></a>
The maximum number of results to return.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 1000.
Required: No

 ** [NextToken](#API_GetEffectivePermissionsForPath_RequestSyntax) **   <a name="lakeformation-GetEffectivePermissionsForPath-request-NextToken"></a>
A continuation token, if this is not the first call to retrieve this list.
Type: String
Required: No

 ** [ResourceArn](#API_GetEffectivePermissionsForPath_RequestSyntax) **   <a name="lakeformation-GetEffectivePermissionsForPath-request-ResourceArn"></a>
The Amazon Resource Name (ARN) of the resource for which you want to get permissions.
Type: String
Required: Yes

## Response Syntax
<a name="API_GetEffectivePermissionsForPath_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "NextToken": "string",
   "Permissions": [
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
<a name="API_GetEffectivePermissionsForPath_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [NextToken](#API_GetEffectivePermissionsForPath_ResponseSyntax) **   <a name="lakeformation-GetEffectivePermissionsForPath-response-NextToken"></a>
A continuation token, if this is not the first call to retrieve this list.
Type: String

 ** [Permissions](#API_GetEffectivePermissionsForPath_ResponseSyntax) **   <a name="lakeformation-GetEffectivePermissionsForPath-response-Permissions"></a>
A list of the permissions for the specified table or database resource located at the path in Amazon S3.
Type: Array of [PrincipalResourcePermissions](API_PrincipalResourcePermissions.md) objects

## Errors
<a name="API_GetEffectivePermissionsForPath_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** EntityNotFoundException **
A specified entity does not exist.
 ** Message **
A message describing the problem.
HTTP Status Code: 400

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
<a name="API_GetEffectivePermissionsForPath_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/lakeformation-2017-03-31/GetEffectivePermissionsForPath)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/lakeformation-2017-03-31/GetEffectivePermissionsForPath)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/lakeformation-2017-03-31/GetEffectivePermissionsForPath)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/lakeformation-2017-03-31/GetEffectivePermissionsForPath)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/lakeformation-2017-03-31/GetEffectivePermissionsForPath)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/lakeformation-2017-03-31/GetEffectivePermissionsForPath)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/lakeformation-2017-03-31/GetEffectivePermissionsForPath)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/lakeformation-2017-03-31/GetEffectivePermissionsForPath)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/lakeformation-2017-03-31/GetEffectivePermissionsForPath)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/lakeformation-2017-03-31/GetEffectivePermissionsForPath)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Lake Formation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query lake-formation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
