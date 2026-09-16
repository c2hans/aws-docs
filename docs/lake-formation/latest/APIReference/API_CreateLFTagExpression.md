---
source_url: https://docs.aws.amazon.com/lake-formation/latest/APIReference/API_CreateLFTagExpression.html
---

# CreateLFTagExpression
<a name="API_CreateLFTagExpression"></a>

Creates a new LF-Tag expression with the provided name, description, catalog ID, and expression body. This call fails if a LF-Tag expression with the same name already exists in the caller’s account or if the underlying LF-Tags don't exist. To call this API operation, caller needs the following Lake Formation permissions:

 `CREATE_LF_TAG_EXPRESSION` on the root catalog resource.

 `GRANT_WITH_LF_TAG_EXPRESSION` on all underlying LF-Tag key:value pairs included in the expression.

## Request Syntax
<a name="API_CreateLFTagExpression_RequestSyntax"></a>

```
POST /CreateLFTagExpression HTTP/1.1
Content-type: application/json

{
   "CatalogId": "{{string}}",
   "Description": "{{string}}",
   "Expression": [
      {
         "TagKey": "{{string}}",
         "TagValues": [ "{{string}}" ]
      }
   ],
   "Name": "{{string}}"
}
```

## URI Request Parameters
<a name="API_CreateLFTagExpression_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_CreateLFTagExpression_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [CatalogId](#API_CreateLFTagExpression_RequestSyntax) **   <a name="lakeformation-CreateLFTagExpression-request-CatalogId"></a>
The identifier for the Data Catalog. By default, the account ID. The Data Catalog is the persistent metadata store. It contains database definitions, table definitions, and other control information to manage your AWS Lake Formation environment.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\t]*`
Required: No

 ** [Description](#API_CreateLFTagExpression_RequestSyntax) **   <a name="lakeformation-CreateLFTagExpression-request-Description"></a>
A description with information about the LF-Tag expression.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 2048.
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\r\n\t]*`
Required: No

 ** [Expression](#API_CreateLFTagExpression_RequestSyntax) **   <a name="lakeformation-CreateLFTagExpression-request-Expression"></a>
A list of LF-Tag conditions (key-value pairs).
Type: Array of [LFTag](API_LFTag.md) objects
Required: Yes

 ** [Name](#API_CreateLFTagExpression_RequestSyntax) **   <a name="lakeformation-CreateLFTagExpression-request-Name"></a>
A name for the expression.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\t]*`
Required: Yes

## Response Syntax
<a name="API_CreateLFTagExpression_ResponseSyntax"></a>

```
HTTP/1.1 200
```

## Response Elements
<a name="API_CreateLFTagExpression_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors
<a name="API_CreateLFTagExpression_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
Access to a resource was denied.
 ** Message **
A message describing the problem.
HTTP Status Code: 403

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
<a name="API_CreateLFTagExpression_Examples"></a>

### Example
<a name="API_CreateLFTagExpression_Example_1"></a>

This example illustrates one usage of CreateLFTagExpression.

```
{
  "CatalogId": "123456789012",
  "Name": "city_department",
  "Description": "A tag expression for city: NYC or Paris and department: Sales",
  "Expression": [
    {
      "TagKey": "City",
      "TagValues": [
        "NYC",
        "Paris"
      ]
    },
    {
      "TagKey": "Department",
      "TagValues": [
        "Sales"
      ]
    }
  ]
}
```

## See Also
<a name="API_CreateLFTagExpression_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/lakeformation-2017-03-31/CreateLFTagExpression)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/lakeformation-2017-03-31/CreateLFTagExpression)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/lakeformation-2017-03-31/CreateLFTagExpression)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/lakeformation-2017-03-31/CreateLFTagExpression)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/lakeformation-2017-03-31/CreateLFTagExpression)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/lakeformation-2017-03-31/CreateLFTagExpression)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/lakeformation-2017-03-31/CreateLFTagExpression)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/lakeformation-2017-03-31/CreateLFTagExpression)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/lakeformation-2017-03-31/CreateLFTagExpression)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/lakeformation-2017-03-31/CreateLFTagExpression)
