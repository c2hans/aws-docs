---
source_url: https://docs.aws.amazon.com/lake-formation/latest/APIReference/API_ListLFTagExpressions.html
---

# ListLFTagExpressions
<a name="API_ListLFTagExpressions"></a>

Returns the LF-Tag expressions in caller’s account filtered based on caller's permissions. Data Lake and read only admins implicitly can see all tag expressions in their account, else caller needs DESCRIBE permissions on tag expression.

## Request Syntax
<a name="API_ListLFTagExpressions_RequestSyntax"></a>

```
POST /ListLFTagExpressions HTTP/1.1
Content-type: application/json

{
   "CatalogId": "{{string}}",
   "MaxResults": {{number}},
   "NextToken": "{{string}}"
}
```

## URI Request Parameters
<a name="API_ListLFTagExpressions_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_ListLFTagExpressions_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [CatalogId](#API_ListLFTagExpressions_RequestSyntax) **   <a name="lakeformation-ListLFTagExpressions-request-CatalogId"></a>
The identifier for the Data Catalog. By default, the account ID.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\t]*`
Required: No

 ** [MaxResults](#API_ListLFTagExpressions_RequestSyntax) **   <a name="lakeformation-ListLFTagExpressions-request-MaxResults"></a>
The maximum number of results to return.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 1000.
Required: No

 ** [NextToken](#API_ListLFTagExpressions_RequestSyntax) **   <a name="lakeformation-ListLFTagExpressions-request-NextToken"></a>
A continuation token, if this is not the first call to retrieve this list.
Type: String
Required: No

## Response Syntax
<a name="API_ListLFTagExpressions_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "LFTagExpressions": [
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
   ],
   "NextToken": "string"
}
```

## Response Elements
<a name="API_ListLFTagExpressions_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [LFTagExpressions](#API_ListLFTagExpressions_ResponseSyntax) **   <a name="lakeformation-ListLFTagExpressions-response-LFTagExpressions"></a>
Logical expressions composed of one more LF-Tag key-value pairs.
Type: Array of [LFTagExpression](API_LFTagExpression.md) objects

 ** [NextToken](#API_ListLFTagExpressions_ResponseSyntax) **   <a name="lakeformation-ListLFTagExpressions-response-NextToken"></a>
A continuation token, if this is not the first call to retrieve this list.
Type: String

## Errors
<a name="API_ListLFTagExpressions_Errors"></a>

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
<a name="API_ListLFTagExpressions_Examples"></a>

### Request example
<a name="API_ListLFTagExpressions_Example_1"></a>

This example illustrates one usage of ListLFTagExpressions.

```
{
  "CatalogId": "123456789012",
  "MaxResults": 5,
  "NextToken": "ExampleNa0ZYUnpkWVZVWk5TRFpaVA=="
}
```

### Response example
<a name="API_ListLFTagExpressions_Example_2"></a>

This example illustrates one usage of ListLFTagExpressions.

```
{
  "LFTagExpressions": [
    {
      "Name": "city_department",
      "Description": "An updated description",
      "CatalogId": "123456789012",
      "Expression": [
        {
          "TagKey": "department",
          "TagValues": [
            "sales"
          ]
        }
      ]
    }
  ],
  "NextToken": "ExampleNa0ZYUnpkWVZVWk5TRFpaVA=="
}
```

## See Also
<a name="API_ListLFTagExpressions_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/lakeformation-2017-03-31/ListLFTagExpressions)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/lakeformation-2017-03-31/ListLFTagExpressions)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/lakeformation-2017-03-31/ListLFTagExpressions)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/lakeformation-2017-03-31/ListLFTagExpressions)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/lakeformation-2017-03-31/ListLFTagExpressions)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/lakeformation-2017-03-31/ListLFTagExpressions)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/lakeformation-2017-03-31/ListLFTagExpressions)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/lakeformation-2017-03-31/ListLFTagExpressions)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/lakeformation-2017-03-31/ListLFTagExpressions)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/lakeformation-2017-03-31/ListLFTagExpressions)
