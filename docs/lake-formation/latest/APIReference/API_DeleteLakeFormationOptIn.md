---
source_url: https://docs.aws.amazon.com/lake-formation/latest/APIReference/API_DeleteLakeFormationOptIn.html
---

# DeleteLakeFormationOptIn
<a name="API_DeleteLakeFormationOptIn"></a>

Remove the Lake Formation permissions enforcement of the given databases, tables, and principals.

## Request Syntax
<a name="API_DeleteLakeFormationOptIn_RequestSyntax"></a>

```
POST /DeleteLakeFormationOptIn HTTP/1.1
Content-type: application/json

{
   "Condition": {
      "Expression": "{{string}}"
   },
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
```

## URI Request Parameters
<a name="API_DeleteLakeFormationOptIn_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_DeleteLakeFormationOptIn_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [Condition](#API_DeleteLakeFormationOptIn_RequestSyntax) **   <a name="lakeformation-DeleteLakeFormationOptIn-request-Condition"></a>
A Lake Formation condition, which applies to permissions and opt-ins that contain an expression.
Type: [Condition](API_Condition.md) object
Required: No

 ** [Principal](#API_DeleteLakeFormationOptIn_RequestSyntax) **   <a name="lakeformation-DeleteLakeFormationOptIn-request-Principal"></a>
The AWS Lake Formation principal. Supported principals are IAM users or IAM roles.
Type: [DataLakePrincipal](API_DataLakePrincipal.md) object
Required: Yes

 ** [Resource](#API_DeleteLakeFormationOptIn_RequestSyntax) **   <a name="lakeformation-DeleteLakeFormationOptIn-request-Resource"></a>
A structure for the resource.
Type: [Resource](API_Resource.md) object
Required: Yes

## Response Syntax
<a name="API_DeleteLakeFormationOptIn_ResponseSyntax"></a>

```
HTTP/1.1 200
```

## Response Elements
<a name="API_DeleteLakeFormationOptIn_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors
<a name="API_DeleteLakeFormationOptIn_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
Access to a resource was denied.
 ** Message **
A message describing the problem.
HTTP Status Code: 403

 ** ConcurrentModificationException **
Two processes are trying to modify a resource simultaneously.
 ** Message **
A message describing the problem.
HTTP Status Code: 400

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
<a name="API_DeleteLakeFormationOptIn_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/lakeformation-2017-03-31/DeleteLakeFormationOptIn)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/lakeformation-2017-03-31/DeleteLakeFormationOptIn)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/lakeformation-2017-03-31/DeleteLakeFormationOptIn)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/lakeformation-2017-03-31/DeleteLakeFormationOptIn)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/lakeformation-2017-03-31/DeleteLakeFormationOptIn)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/lakeformation-2017-03-31/DeleteLakeFormationOptIn)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/lakeformation-2017-03-31/DeleteLakeFormationOptIn)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/lakeformation-2017-03-31/DeleteLakeFormationOptIn)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/lakeformation-2017-03-31/DeleteLakeFormationOptIn)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/lakeformation-2017-03-31/DeleteLakeFormationOptIn)
