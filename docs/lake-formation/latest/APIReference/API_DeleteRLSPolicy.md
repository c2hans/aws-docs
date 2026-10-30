---
source_url: https://docs.aws.amazon.com/lake-formation/latest/APIReference/API_DeleteRLSPolicy.html
---

# DeleteRLSPolicy
<a name="API_DeleteRLSPolicy"></a>

Deletes a row-level security policy. Any active attachments of the policy are automatically removed as part of the deletion, so you do not need to detach the policy first.

## Request Syntax
<a name="API_DeleteRLSPolicy_RequestSyntax"></a>

```
POST /DeleteRLSPolicy HTTP/1.1
Content-type: application/json

{
   "Name": "{{string}}"
}
```

## URI Request Parameters
<a name="API_DeleteRLSPolicy_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_DeleteRLSPolicy_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [Name](#API_DeleteRLSPolicy_RequestSyntax) **   <a name="lakeformation-DeleteRLSPolicy-request-Name"></a>
The name of the row-level security policy to delete.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\t]*`
Required: Yes

## Response Syntax
<a name="API_DeleteRLSPolicy_ResponseSyntax"></a>

```
HTTP/1.1 200
```

## Response Elements
<a name="API_DeleteRLSPolicy_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors
<a name="API_DeleteRLSPolicy_Errors"></a>

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
<a name="API_DeleteRLSPolicy_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/lakeformation-2017-03-31/DeleteRLSPolicy)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/lakeformation-2017-03-31/DeleteRLSPolicy)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/lakeformation-2017-03-31/DeleteRLSPolicy)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/lakeformation-2017-03-31/DeleteRLSPolicy)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/lakeformation-2017-03-31/DeleteRLSPolicy)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/lakeformation-2017-03-31/DeleteRLSPolicy)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/lakeformation-2017-03-31/DeleteRLSPolicy)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/lakeformation-2017-03-31/DeleteRLSPolicy)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/lakeformation-2017-03-31/DeleteRLSPolicy)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/lakeformation-2017-03-31/DeleteRLSPolicy)
