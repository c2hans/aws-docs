---
source_url: https://docs.aws.amazon.com/lake-formation/latest/APIReference/API_GetLFTagExpression.html
---

# GetLFTagExpression
<a name="API_GetLFTagExpression"></a>

Returns the details about the LF-Tag expression. The caller must be a data lake admin or must have `DESCRIBE` permission on the LF-Tag expression resource.

## Request Syntax
<a name="API_GetLFTagExpression_RequestSyntax"></a>

```
POST /GetLFTagExpression HTTP/1.1
Content-type: application/json

{
   "CatalogId": "{{string}}",
   "Name": "{{string}}"
}
```

## URI Request Parameters
<a name="API_GetLFTagExpression_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_GetLFTagExpression_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [CatalogId](#API_GetLFTagExpression_RequestSyntax) **   <a name="lakeformation-GetLFTagExpression-request-CatalogId"></a>
The identifier for the Data Catalog. By default, the account ID.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\t]*`
Required: No

 ** [Name](#API_GetLFTagExpression_RequestSyntax) **   <a name="lakeformation-GetLFTagExpression-request-Name"></a>
The name for the LF-Tag expression
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\t]*`
Required: Yes

## Response Syntax
<a name="API_GetLFTagExpression_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "CatalogId": "string",
   "Description": "string",
   "Expression": [
      {
         "TagKey": "string",
         "TagValues": [ "string" ]
      }
   ],
   "Name": "string"
}
```

## Response Elements
<a name="API_GetLFTagExpression_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [CatalogId](#API_GetLFTagExpression_ResponseSyntax) **   <a name="lakeformation-GetLFTagExpression-response-CatalogId"></a>
The identifier for the Data Catalog. By default, the account ID in which the LF-Tag expression is saved.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\t]*`

 ** [Description](#API_GetLFTagExpression_ResponseSyntax) **   <a name="lakeformation-GetLFTagExpression-response-Description"></a>
The description with information about the LF-Tag expression.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 2048.
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\r\n\t]*`

 ** [Expression](#API_GetLFTagExpression_ResponseSyntax) **   <a name="lakeformation-GetLFTagExpression-response-Expression"></a>
The body of the LF-Tag expression. It is composed of one or more LF-Tag key-value pairs.
Type: Array of [LFTag](API_LFTag.md) objects

 ** [Name](#API_GetLFTagExpression_ResponseSyntax) **   <a name="lakeformation-GetLFTagExpression-response-Name"></a>
The name for the LF-Tag expression.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\t]*`

## Errors
<a name="API_GetLFTagExpression_Errors"></a>

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

## Examples
<a name="API_GetLFTagExpression_Examples"></a>

### Request example
<a name="API_GetLFTagExpression_Example_1"></a>

This example illustrates one usage of GetLFTagExpression.

```
{
  "CatalogId": "123456789012",
  "Name": "city_department"
}
```

### Response example
<a name="API_GetLFTagExpression_Example_2"></a>

This example illustrates one usage of GetLFTagExpression.

```
{
  "Name": "city_department",
  "Description": "A tag expression for city: NYC or Paris and department: Sales",
  "CatalogId": "328665898768",
  "Expression": [
    {
      "TagKey": "city",
      "TagValues": [
        "paris",
        "nyc"
      ]
    },
    {
      "TagKey": "department",
      "TagValues": [
        "sales"
      ]
    }
  ]
}
```

## See Also
<a name="API_GetLFTagExpression_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/lakeformation-2017-03-31/GetLFTagExpression)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/lakeformation-2017-03-31/GetLFTagExpression)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/lakeformation-2017-03-31/GetLFTagExpression)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/lakeformation-2017-03-31/GetLFTagExpression)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/lakeformation-2017-03-31/GetLFTagExpression)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/lakeformation-2017-03-31/GetLFTagExpression)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/lakeformation-2017-03-31/GetLFTagExpression)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/lakeformation-2017-03-31/GetLFTagExpression)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/lakeformation-2017-03-31/GetLFTagExpression)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/lakeformation-2017-03-31/GetLFTagExpression)
