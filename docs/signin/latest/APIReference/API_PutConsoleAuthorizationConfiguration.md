---
source_url: https://docs.aws.amazon.com/signin/latest/APIReference/API_PutConsoleAuthorizationConfiguration.html
---

# PutConsoleAuthorizationConfiguration
<a name="API_PutConsoleAuthorizationConfiguration"></a>

Enables AWS Management Console authorization configuration for an AWS account or organization. The operation automatically detects whether the `targetId` is an account ID or an organization ID, and applies the appropriate authorization scope.

## Request Syntax
<a name="API_PutConsoleAuthorizationConfiguration_RequestSyntax"></a>

```
{
   "targetId": "{{string}}"
}
```

## Request Parameters
<a name="API_PutConsoleAuthorizationConfiguration_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [targetId](#API_PutConsoleAuthorizationConfiguration_RequestSyntax) **   <a name="signin-PutConsoleAuthorizationConfiguration-request-targetId"></a>
The target identifier for the configuration. Accepts a 12-digit account ID, an organization ID (`o-xxxxxxxxxx`), or null/empty to use the caller's account ID. The scope is detected automatically based on the format.
Type: String
Length Constraints: Minimum length of 12. Maximum length of 32.
Pattern: `(\d{12}|o-[a-z0-9]{10}|r-[0-9a-z]{4,32})`
Required: No

## Response Syntax
<a name="API_PutConsoleAuthorizationConfiguration_ResponseSyntax"></a>

```
{
   "consoleAuthorizationEnabled": boolean,
   "scope": "string",
   "targetId": "string"
}
```

## Response Elements
<a name="API_PutConsoleAuthorizationConfiguration_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [consoleAuthorizationEnabled](#API_PutConsoleAuthorizationConfiguration_ResponseSyntax) **   <a name="signin-PutConsoleAuthorizationConfiguration-response-consoleAuthorizationEnabled"></a>
Indicates whether AWS Management Console authorization is enabled for the target.
Type: Boolean

 ** [scope](#API_PutConsoleAuthorizationConfiguration_ResponseSyntax) **   <a name="signin-PutConsoleAuthorizationConfiguration-response-scope"></a>
The scope that was applied to the configuration. Indicates whether the operation was applied at the account or organization level.
Type: String

 ** [targetId](#API_PutConsoleAuthorizationConfiguration_ResponseSyntax) **   <a name="signin-PutConsoleAuthorizationConfiguration-response-targetId"></a>
The target identifier for which AWS Management Console authorization was configured.
Type: String
Length Constraints: Minimum length of 12. Maximum length of 32.
Pattern: `(\d{12}|o-[a-z0-9]{10}|r-[0-9a-z]{4,32})`

## Errors
<a name="API_PutConsoleAuthorizationConfiguration_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You do not have sufficient access to perform this action.
HTTP Status Code: 400

 ** ConflictException **
The request conflicts with the current state of the resource. For example, this exception is thrown when a client provides the same `ClientToken` for requests with differing parameter values, or the same parameter values with different `ClientToken` within the expiration window.
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
<a name="API_PutConsoleAuthorizationConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/signincontrolplane-2022-07-26/PutConsoleAuthorizationConfiguration)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/signincontrolplane-2022-07-26/PutConsoleAuthorizationConfiguration)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/signincontrolplane-2022-07-26/PutConsoleAuthorizationConfiguration)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/signincontrolplane-2022-07-26/PutConsoleAuthorizationConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/signincontrolplane-2022-07-26/PutConsoleAuthorizationConfiguration)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/signincontrolplane-2022-07-26/PutConsoleAuthorizationConfiguration)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/signincontrolplane-2022-07-26/PutConsoleAuthorizationConfiguration)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/signincontrolplane-2022-07-26/PutConsoleAuthorizationConfiguration)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/signincontrolplane-2022-07-26/PutConsoleAuthorizationConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/signincontrolplane-2022-07-26/PutConsoleAuthorizationConfiguration)
