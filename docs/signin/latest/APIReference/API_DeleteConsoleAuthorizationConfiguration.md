---
source_url: https://docs.aws.amazon.com/signin/latest/APIReference/API_DeleteConsoleAuthorizationConfiguration.html
---

# DeleteConsoleAuthorizationConfiguration
<a name="API_DeleteConsoleAuthorizationConfiguration"></a>

Disables AWS Management Console authorization configuration for an AWS account or organization. The operation automatically detects whether the `targetId` is an account ID or an organization ID.

## Request Syntax
<a name="API_DeleteConsoleAuthorizationConfiguration_RequestSyntax"></a>

```
{
   "targetId": "{{string}}"
}
```

## Request Parameters
<a name="API_DeleteConsoleAuthorizationConfiguration_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [targetId](#API_DeleteConsoleAuthorizationConfiguration_RequestSyntax) **   <a name="signin-DeleteConsoleAuthorizationConfiguration-request-targetId"></a>
The target identifier whose AWS Management Console authorization configuration should be disabled. Accepts a 12-digit account ID, an organization ID (`o-xxxxxxxxxx`), or null/empty to use the caller's account ID.
Type: String
Length Constraints: Minimum length of 12. Maximum length of 32.
Pattern: `(\d{12}|o-[a-z0-9]{10}|r-[0-9a-z]{4,32})`
Required: No

## Response Syntax
<a name="API_DeleteConsoleAuthorizationConfiguration_ResponseSyntax"></a>

```
{
   "consoleAuthorizationEnabled": boolean,
   "scope": "string",
   "targetId": "string"
}
```

## Response Elements
<a name="API_DeleteConsoleAuthorizationConfiguration_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [consoleAuthorizationEnabled](#API_DeleteConsoleAuthorizationConfiguration_ResponseSyntax) **   <a name="signin-DeleteConsoleAuthorizationConfiguration-response-consoleAuthorizationEnabled"></a>
Indicates whether AWS Management Console authorization is enabled for the target. After a successful delete, this is `false`.
Type: Boolean

 ** [scope](#API_DeleteConsoleAuthorizationConfiguration_ResponseSyntax) **   <a name="signin-DeleteConsoleAuthorizationConfiguration-response-scope"></a>
The scope of the configuration that was deleted. Indicates whether the operation was applied at the account or organization level.
Type: String

 ** [targetId](#API_DeleteConsoleAuthorizationConfiguration_ResponseSyntax) **   <a name="signin-DeleteConsoleAuthorizationConfiguration-response-targetId"></a>
The target identifier the configuration applied to.
Type: String
Length Constraints: Minimum length of 12. Maximum length of 32.
Pattern: `(\d{12}|o-[a-z0-9]{10}|r-[0-9a-z]{4,32})`

## Errors
<a name="API_DeleteConsoleAuthorizationConfiguration_Errors"></a>

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
<a name="API_DeleteConsoleAuthorizationConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/signincontrolplane-2022-07-26/DeleteConsoleAuthorizationConfiguration)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/signincontrolplane-2022-07-26/DeleteConsoleAuthorizationConfiguration)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/signincontrolplane-2022-07-26/DeleteConsoleAuthorizationConfiguration)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/signincontrolplane-2022-07-26/DeleteConsoleAuthorizationConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/signincontrolplane-2022-07-26/DeleteConsoleAuthorizationConfiguration)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/signincontrolplane-2022-07-26/DeleteConsoleAuthorizationConfiguration)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/signincontrolplane-2022-07-26/DeleteConsoleAuthorizationConfiguration)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/signincontrolplane-2022-07-26/DeleteConsoleAuthorizationConfiguration)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/signincontrolplane-2022-07-26/DeleteConsoleAuthorizationConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/signincontrolplane-2022-07-26/DeleteConsoleAuthorizationConfiguration)
