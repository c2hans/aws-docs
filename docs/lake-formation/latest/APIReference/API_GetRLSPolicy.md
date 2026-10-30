---
source_url: https://docs.aws.amazon.com/lake-formation/latest/APIReference/API_GetRLSPolicy.html
---

# GetRLSPolicy
<a name="API_GetRLSPolicy"></a>

Returns the definition of a row-level security policy, including its attachment columns and filter expression.

## Request Syntax
<a name="API_GetRLSPolicy_RequestSyntax"></a>

```
POST /GetRLSPolicy HTTP/1.1
Content-type: application/json

{
   "Name": "{{string}}"
}
```

## URI Request Parameters
<a name="API_GetRLSPolicy_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_GetRLSPolicy_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [Name](#API_GetRLSPolicy_RequestSyntax) **   <a name="lakeformation-GetRLSPolicy-request-Name"></a>
The name of the row-level security policy to retrieve.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\t]*`
Required: Yes

## Response Syntax
<a name="API_GetRLSPolicy_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "RLSPolicy": {
      "AttachmentColumns": [
         {
            "Name": "string",
            "Type": "string"
         }
      ],
      "CatalogId": "string",
      "FilterExpression": "string",
      "Name": "string"
   }
}
```

## Response Elements
<a name="API_GetRLSPolicy_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [RLSPolicy](#API_GetRLSPolicy_ResponseSyntax) **   <a name="lakeformation-GetRLSPolicy-response-RLSPolicy"></a>
An `RLSPolicy` structure containing the definition of the requested row-level security policy.
Type: [RLSPolicy](API_RLSPolicy.md) object

## Errors
<a name="API_GetRLSPolicy_Errors"></a>

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

## See Also
<a name="API_GetRLSPolicy_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/lakeformation-2017-03-31/GetRLSPolicy)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/lakeformation-2017-03-31/GetRLSPolicy)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/lakeformation-2017-03-31/GetRLSPolicy)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/lakeformation-2017-03-31/GetRLSPolicy)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/lakeformation-2017-03-31/GetRLSPolicy)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/lakeformation-2017-03-31/GetRLSPolicy)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/lakeformation-2017-03-31/GetRLSPolicy)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/lakeformation-2017-03-31/GetRLSPolicy)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/lakeformation-2017-03-31/GetRLSPolicy)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/lakeformation-2017-03-31/GetRLSPolicy)
