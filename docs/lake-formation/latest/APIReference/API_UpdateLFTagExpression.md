---
source_url: https://docs.aws.amazon.com/lake-formation/latest/APIReference/API_UpdateLFTagExpression.html
---

# UpdateLFTagExpression
<a name="API_UpdateLFTagExpression"></a>

Updates the name of the LF-Tag expression to the new description and expression body provided. Updating a LF-Tag expression immediately changes the permission boundaries of all existing `LFTagPolicy` permission grants that reference the given LF-Tag expression.

## Request Syntax
<a name="API_UpdateLFTagExpression_RequestSyntax"></a>

```
POST /UpdateLFTagExpression HTTP/1.1
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
<a name="API_UpdateLFTagExpression_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_UpdateLFTagExpression_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [CatalogId](#API_UpdateLFTagExpression_RequestSyntax) **   <a name="lakeformation-UpdateLFTagExpression-request-CatalogId"></a>
The identifier for the Data Catalog. By default, the account ID.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\t]*`
Required: No

 ** [Description](#API_UpdateLFTagExpression_RequestSyntax) **   <a name="lakeformation-UpdateLFTagExpression-request-Description"></a>
The description with information about the saved LF-Tag expression.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 2048.
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\r\n\t]*`
Required: No

 ** [Expression](#API_UpdateLFTagExpression_RequestSyntax) **   <a name="lakeformation-UpdateLFTagExpression-request-Expression"></a>
The LF-Tag expression body composed of one more LF-Tag key-value pairs.
Type: Array of [LFTag](API_LFTag.md) objects
Required: Yes

 ** [Name](#API_UpdateLFTagExpression_RequestSyntax) **   <a name="lakeformation-UpdateLFTagExpression-request-Name"></a>
The name for the LF-Tag expression.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\t]*`
Required: Yes

## Response Syntax
<a name="API_UpdateLFTagExpression_ResponseSyntax"></a>

```
HTTP/1.1 200
```

## Response Elements
<a name="API_UpdateLFTagExpression_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors
<a name="API_UpdateLFTagExpression_Errors"></a>

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
<a name="API_UpdateLFTagExpression_Examples"></a>

### Request example
<a name="API_UpdateLFTagExpression_Example_1"></a>

This example illustrates one usage of UpdateLFTagExpression.

```
{
  "CatalogId": "123456789012",
  "Name": "city_department",
  "Description": "An updated description",
  "Expression": [
    {
      "TagKey": "Department",
      "TagValues": [
        "Sales"
      ]
    }
  ]
}
```

### Response example
<a name="API_UpdateLFTagExpression_Example_2"></a>

This example illustrates one usage of UpdateLFTagExpression.

```
{}
```

## See Also
<a name="API_UpdateLFTagExpression_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/lakeformation-2017-03-31/UpdateLFTagExpression)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/lakeformation-2017-03-31/UpdateLFTagExpression)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/lakeformation-2017-03-31/UpdateLFTagExpression)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/lakeformation-2017-03-31/UpdateLFTagExpression)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/lakeformation-2017-03-31/UpdateLFTagExpression)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/lakeformation-2017-03-31/UpdateLFTagExpression)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/lakeformation-2017-03-31/UpdateLFTagExpression)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/lakeformation-2017-03-31/UpdateLFTagExpression)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/lakeformation-2017-03-31/UpdateLFTagExpression)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/lakeformation-2017-03-31/UpdateLFTagExpression)
