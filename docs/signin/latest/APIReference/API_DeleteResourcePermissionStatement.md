---
source_url: https://docs.aws.amazon.com/signin/latest/APIReference/API_DeleteResourcePermissionStatement.html
---

# DeleteResourcePermissionStatement
<a name="API_DeleteResourcePermissionStatement"></a>

Removes a permission statement from the account's AWS Sign-In resource-based policy.

## Request Syntax
<a name="API_DeleteResourcePermissionStatement_RequestSyntax"></a>

```
{
   "clientToken": "{{string}}",
   "statementId": "{{string}}"
}
```

## Request Parameters
<a name="API_DeleteResourcePermissionStatement_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [clientToken](#API_DeleteResourcePermissionStatement_RequestSyntax) **   <a name="signin-DeleteResourcePermissionStatement-request-clientToken"></a>
A unique, case-sensitive identifier that you provide to ensure the idempotency of the request. If not provided, the AWS SDK will automatically generate one for you.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[!-~]+`
Required: No

 ** [statementId](#API_DeleteResourcePermissionStatement_RequestSyntax) **   <a name="signin-DeleteResourcePermissionStatement-request-statementId"></a>
The unique identifier of the permission statement to delete.
Type: String
Pattern: `[A-Za-z0-9+/]{64}=?`
Required: Yes

## Response Elements
<a name="API_DeleteResourcePermissionStatement_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors
<a name="API_DeleteResourcePermissionStatement_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You do not have sufficient access to perform this action.
HTTP Status Code: 400

 ** InternalServerException **
The request processing has failed because of an unknown error, exception or failure with an internal server.
HTTP Status Code: 500

 ** ResourceNotFoundException **
The request was denied because the specified resource was not found.
HTTP Status Code: 400

 ** TooManyRequestsError **
The request was denied due to rate limiting.
HTTP Status Code: 400

 ** ValidationException **
The request failed because it contains a syntax error.
HTTP Status Code: 400

## See Also
<a name="API_DeleteResourcePermissionStatement_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/signincontrolplane-2022-07-26/DeleteResourcePermissionStatement)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/signincontrolplane-2022-07-26/DeleteResourcePermissionStatement)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/signincontrolplane-2022-07-26/DeleteResourcePermissionStatement)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/signincontrolplane-2022-07-26/DeleteResourcePermissionStatement)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/signincontrolplane-2022-07-26/DeleteResourcePermissionStatement)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/signincontrolplane-2022-07-26/DeleteResourcePermissionStatement)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/signincontrolplane-2022-07-26/DeleteResourcePermissionStatement)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/signincontrolplane-2022-07-26/DeleteResourcePermissionStatement)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/signincontrolplane-2022-07-26/DeleteResourcePermissionStatement)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/signincontrolplane-2022-07-26/DeleteResourcePermissionStatement)
