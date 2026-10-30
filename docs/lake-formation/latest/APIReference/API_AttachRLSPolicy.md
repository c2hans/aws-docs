---
source_url: https://docs.aws.amazon.com/lake-formation/latest/APIReference/API_AttachRLSPolicy.html
---

# AttachRLSPolicy
<a name="API_AttachRLSPolicy"></a>

Attaches a row-level security policy to a resource for a principal. When the principal queries the resource, AWS Lake Formation applies the policy's filter expression so that only the permitted rows are returned.

## Request Syntax
<a name="API_AttachRLSPolicy_RequestSyntax"></a>

```
POST /AttachRLSPolicy HTTP/1.1
Content-type: application/json

{
   "Condition": {
      "Expression": "{{string}}"
   },
   "Name": "{{string}}",
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
      "RLSPolicy": {
         "CatalogId": "{{string}}",
         "Name": "{{string}}"
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
   "SetDefault": {{boolean}}
}
```

## URI Request Parameters
<a name="API_AttachRLSPolicy_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_AttachRLSPolicy_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [Condition](#API_AttachRLSPolicy_RequestSyntax) **   <a name="lakeformation-AttachRLSPolicy-request-Condition"></a>
A Lake Formation condition, which applies to the row-level security policy attachment and contains an expression.
Type: [Condition](API_Condition.md) object
Required: No

 ** [Name](#API_AttachRLSPolicy_RequestSyntax) **   <a name="lakeformation-AttachRLSPolicy-request-Name"></a>
The name of the row-level security policy to attach.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\t]*`
Required: Yes

 ** [Principal](#API_AttachRLSPolicy_RequestSyntax) **   <a name="lakeformation-AttachRLSPolicy-request-Principal"></a>
The principal to which the row-level security policy applies.
Type: [DataLakePrincipal](API_DataLakePrincipal.md) object
Required: No

 ** [Resource](#API_AttachRLSPolicy_RequestSyntax) **   <a name="lakeformation-AttachRLSPolicy-request-Resource"></a>
The resource to which the row-level security policy is attached.
Type: [Resource](API_Resource.md) object
Required: Yes

 ** [SetDefault](#API_AttachRLSPolicy_RequestSyntax) **   <a name="lakeformation-AttachRLSPolicy-request-SetDefault"></a>
Indicates whether this policy becomes the default row-level security policy for the resource. The default policy applies to all principals by default.
Type: Boolean
Required: No

## Response Syntax
<a name="API_AttachRLSPolicy_ResponseSyntax"></a>

```
HTTP/1.1 200
```

## Response Elements
<a name="API_AttachRLSPolicy_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors
<a name="API_AttachRLSPolicy_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
Access to a resource was denied.
 ** Message **
A message describing the problem.
HTTP Status Code: 403

 ** AlreadyExistsException **
A resource to be created or added already exists.
 ** Message **
A message describing the problem.
HTTP Status Code: 400

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

 ** ResourceNumberLimitExceededException **
A resource numerical limit was exceeded.
 ** Message **
A message describing the problem.
HTTP Status Code: 400

## Examples
<a name="API_AttachRLSPolicy_Examples"></a>

### Request example
<a name="API_AttachRLSPolicy_Example_1"></a>

This example illustrates one usage of AttachRLSPolicy.

```
{
   "Name": "sales-east-region",
   "Resource": {
      "Table": {
         "DatabaseName": "sales",
         "Name": "orders"
      }
   },
   "Principal": {
      "DataLakePrincipalIdentifier": "arn:aws:iam::111122223333:role/Analyst"
   },
   "SetDefault": false
}
```

## See Also
<a name="API_AttachRLSPolicy_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/lakeformation-2017-03-31/AttachRLSPolicy)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/lakeformation-2017-03-31/AttachRLSPolicy)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/lakeformation-2017-03-31/AttachRLSPolicy)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/lakeformation-2017-03-31/AttachRLSPolicy)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/lakeformation-2017-03-31/AttachRLSPolicy)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/lakeformation-2017-03-31/AttachRLSPolicy)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/lakeformation-2017-03-31/AttachRLSPolicy)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/lakeformation-2017-03-31/AttachRLSPolicy)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/lakeformation-2017-03-31/AttachRLSPolicy)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/lakeformation-2017-03-31/AttachRLSPolicy)
