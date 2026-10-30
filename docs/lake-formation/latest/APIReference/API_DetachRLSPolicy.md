---
source_url: https://docs.aws.amazon.com/lake-formation/latest/APIReference/API_DetachRLSPolicy.html
---

# DetachRLSPolicy
<a name="API_DetachRLSPolicy"></a>

Detaches a row-level security policy from a resource for a principal. After the policy is detached, its filter expression is no longer applied to the principal's queries on that resource.

## Request Syntax
<a name="API_DetachRLSPolicy_RequestSyntax"></a>

```
POST /DetachRLSPolicy HTTP/1.1
Content-type: application/json

{
   "Condition": {
      "Expression": "{{string}}"
   },
   "Name": "{{string}}",
   "Principal": {
      "DataLakePrincipalIdentifier": "{{string}}"
   },
   "RemoveDefault": {{boolean}},
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
   }
}
```

## URI Request Parameters
<a name="API_DetachRLSPolicy_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_DetachRLSPolicy_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [Condition](#API_DetachRLSPolicy_RequestSyntax) **   <a name="lakeformation-DetachRLSPolicy-request-Condition"></a>
A Lake Formation condition, which applies to the row-level security policy attachment and contains an expression.
Type: [Condition](API_Condition.md) object
Required: No

 ** [Name](#API_DetachRLSPolicy_RequestSyntax) **   <a name="lakeformation-DetachRLSPolicy-request-Name"></a>
The name of the row-level security policy to detach.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\t]*`
Required: Yes

 ** [Principal](#API_DetachRLSPolicy_RequestSyntax) **   <a name="lakeformation-DetachRLSPolicy-request-Principal"></a>
The principal for which the row-level security policy is detached.
Type: [DataLakePrincipal](API_DataLakePrincipal.md) object
Required: No

 ** [RemoveDefault](#API_DetachRLSPolicy_RequestSyntax) **   <a name="lakeformation-DetachRLSPolicy-request-RemoveDefault"></a>
Indicates whether to remove this policy as the default row-level security policy for the resource.
Type: Boolean
Required: No

 ** [Resource](#API_DetachRLSPolicy_RequestSyntax) **   <a name="lakeformation-DetachRLSPolicy-request-Resource"></a>
The resource from which the row-level security policy is detached.
Type: [Resource](API_Resource.md) object
Required: Yes

## Response Syntax
<a name="API_DetachRLSPolicy_ResponseSyntax"></a>

```
HTTP/1.1 200
```

## Response Elements
<a name="API_DetachRLSPolicy_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors
<a name="API_DetachRLSPolicy_Errors"></a>

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
<a name="API_DetachRLSPolicy_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/lakeformation-2017-03-31/DetachRLSPolicy)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/lakeformation-2017-03-31/DetachRLSPolicy)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/lakeformation-2017-03-31/DetachRLSPolicy)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/lakeformation-2017-03-31/DetachRLSPolicy)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/lakeformation-2017-03-31/DetachRLSPolicy)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/lakeformation-2017-03-31/DetachRLSPolicy)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/lakeformation-2017-03-31/DetachRLSPolicy)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/lakeformation-2017-03-31/DetachRLSPolicy)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/lakeformation-2017-03-31/DetachRLSPolicy)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/lakeformation-2017-03-31/DetachRLSPolicy)
