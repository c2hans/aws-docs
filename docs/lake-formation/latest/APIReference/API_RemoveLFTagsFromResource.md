---
source_url: https://docs.aws.amazon.com/lake-formation/latest/APIReference/API_RemoveLFTagsFromResource.html
---

# RemoveLFTagsFromResource
<a name="API_RemoveLFTagsFromResource"></a>

Removes an LF-tag from the resource. Only database, table, or tableWithColumns resource are allowed. To tag columns, use the column inclusion list in `tableWithColumns` to specify column input.

## Request Syntax
<a name="API_RemoveLFTagsFromResource_RequestSyntax"></a>

```
POST /RemoveLFTagsFromResource HTTP/1.1
Content-type: application/json

{
   "CatalogId": "{{string}}",
   "LFTags": [
      {
         "CatalogId": "{{string}}",
         "TagKey": "{{string}}",
         "TagValues": [ "{{string}}" ]
      }
   ],
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
<a name="API_RemoveLFTagsFromResource_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_RemoveLFTagsFromResource_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [CatalogId](#API_RemoveLFTagsFromResource_RequestSyntax) **   <a name="lakeformation-RemoveLFTagsFromResource-request-CatalogId"></a>
The identifier for the Data Catalog. By default, the account ID. The Data Catalog is the persistent metadata store. It contains database definitions, table definitions, and other control information to manage your AWS Lake Formation environment.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\t]*`
Required: No

 ** [LFTags](#API_RemoveLFTagsFromResource_RequestSyntax) **   <a name="lakeformation-RemoveLFTagsFromResource-request-LFTags"></a>
The LF-tags to be removed from the resource.
Type: Array of [LFTagPair](API_LFTagPair.md) objects
Array Members: Minimum number of 1 item. Maximum number of 50 items.
Required: Yes

 ** [Resource](#API_RemoveLFTagsFromResource_RequestSyntax) **   <a name="lakeformation-RemoveLFTagsFromResource-request-Resource"></a>
The database, table, or column resource where you want to remove an LF-tag.
Type: [Resource](API_Resource.md) object
Required: Yes

## Response Syntax
<a name="API_RemoveLFTagsFromResource_ResponseSyntax"></a>

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
         "LFTag": {
            "CatalogId": "string",
            "TagKey": "string",
            "TagValues": [ "string" ]
         }
      }
   ]
}
```

## Response Elements
<a name="API_RemoveLFTagsFromResource_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [Failures](#API_RemoveLFTagsFromResource_ResponseSyntax) **   <a name="lakeformation-RemoveLFTagsFromResource-response-Failures"></a>
A list of failures to untag a resource.
Type: Array of [LFTagError](API_LFTagError.md) objects

## Errors
<a name="API_RemoveLFTagsFromResource_Errors"></a>

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

 ** GlueEncryptionException **
An encryption operation failed.
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
<a name="API_RemoveLFTagsFromResource_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/lakeformation-2017-03-31/RemoveLFTagsFromResource)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/lakeformation-2017-03-31/RemoveLFTagsFromResource)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/lakeformation-2017-03-31/RemoveLFTagsFromResource)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/lakeformation-2017-03-31/RemoveLFTagsFromResource)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/lakeformation-2017-03-31/RemoveLFTagsFromResource)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/lakeformation-2017-03-31/RemoveLFTagsFromResource)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/lakeformation-2017-03-31/RemoveLFTagsFromResource)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/lakeformation-2017-03-31/RemoveLFTagsFromResource)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/lakeformation-2017-03-31/RemoveLFTagsFromResource)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/lakeformation-2017-03-31/RemoveLFTagsFromResource)
