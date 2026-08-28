---
source_url: https://docs.aws.amazon.com/signin/latest/APIReference/API_GetConsoleAuthorizationConfiguration.html
---

# GetConsoleAuthorizationConfiguration
<a name="API_GetConsoleAuthorizationConfiguration"></a>

Retrieves AWS Management Console authorization configuration for an AWS account or organization. The operation automatically detects whether the `targetId` is an account ID or an organization ID.

## Request Syntax
<a name="API_GetConsoleAuthorizationConfiguration_RequestSyntax"></a>

```
{
   "targetId": "{{string}}"
}
```

## Request Parameters
<a name="API_GetConsoleAuthorizationConfiguration_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [targetId](#API_GetConsoleAuthorizationConfiguration_RequestSyntax) **   <a name="signin-GetConsoleAuthorizationConfiguration-request-targetId"></a>
The target identifier to retrieve the configuration for. Accepts a 12-digit account ID, an organization ID (`o-xxxxxxxxxx`), or null/empty to use the caller's account ID.
Type: String
Length Constraints: Minimum length of 12. Maximum length of 32.
Pattern: `(\d{12}|o-[a-z0-9]{10}|r-[0-9a-z]{4,32})`
Required: No

## Response Syntax
<a name="API_GetConsoleAuthorizationConfiguration_ResponseSyntax"></a>

```
{
   "consoleAuthorizationEnabled": boolean,
   "scope": "string",
   "targetId": "string"
}
```

## Response Elements
<a name="API_GetConsoleAuthorizationConfiguration_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [consoleAuthorizationEnabled](#API_GetConsoleAuthorizationConfiguration_ResponseSyntax) **   <a name="signin-GetConsoleAuthorizationConfiguration-response-consoleAuthorizationEnabled"></a>
Indicates whether AWS Management Console authorization is enabled for the target.
Type: Boolean

 ** [scope](#API_GetConsoleAuthorizationConfiguration_ResponseSyntax) **   <a name="signin-GetConsoleAuthorizationConfiguration-response-scope"></a>
The scope of the configuration. Indicates whether the configuration applies at the account or organization level.
Type: String

 ** [targetId](#API_GetConsoleAuthorizationConfiguration_ResponseSyntax) **   <a name="signin-GetConsoleAuthorizationConfiguration-response-targetId"></a>
The target identifier the configuration applies to.
Type: String
Length Constraints: Minimum length of 12. Maximum length of 32.
Pattern: `(\d{12}|o-[a-z0-9]{10}|r-[0-9a-z]{4,32})`

## Errors
<a name="API_GetConsoleAuthorizationConfiguration_Errors"></a>

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
<a name="API_GetConsoleAuthorizationConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/signincontrolplane-2022-07-26/GetConsoleAuthorizationConfiguration)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/signincontrolplane-2022-07-26/GetConsoleAuthorizationConfiguration)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/signincontrolplane-2022-07-26/GetConsoleAuthorizationConfiguration)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/signincontrolplane-2022-07-26/GetConsoleAuthorizationConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/signincontrolplane-2022-07-26/GetConsoleAuthorizationConfiguration)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/signincontrolplane-2022-07-26/GetConsoleAuthorizationConfiguration)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/signincontrolplane-2022-07-26/GetConsoleAuthorizationConfiguration)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/signincontrolplane-2022-07-26/GetConsoleAuthorizationConfiguration)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/signincontrolplane-2022-07-26/GetConsoleAuthorizationConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/signincontrolplane-2022-07-26/GetConsoleAuthorizationConfiguration)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Sign-In. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query signin` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
