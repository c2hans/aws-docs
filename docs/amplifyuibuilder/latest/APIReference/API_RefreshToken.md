---
source_url: https://docs.aws.amazon.com/amplifyuibuilder/latest/APIReference/API_RefreshToken.html
---

# RefreshToken
<a name="API_RefreshToken"></a>

**Note**
This is for internal use.

Amplify uses this action to refresh a previously issued access token that might have expired.

## Request Syntax
<a name="API_RefreshToken_RequestSyntax"></a>

```
POST /tokens/{{provider}}/refresh HTTP/1.1
Content-type: application/json

{
   "clientId": "{{string}}",
   "token": "{{string}}"
}
```

## URI Request Parameters
<a name="API_RefreshToken_RequestParameters"></a>

The request uses the following URI parameters.

 ** [provider](#API_RefreshToken_RequestSyntax) **   <a name="amplifyuibuilder-RefreshToken-request-uri-provider"></a>
The third-party provider for the token. The only valid value is `figma`.
Valid Values: `figma`
Required: Yes

## Request Body
<a name="API_RefreshToken_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [clientId](#API_RefreshToken_RequestSyntax) **   <a name="amplifyuibuilder-RefreshToken-request-clientId"></a>
The ID of the client to request the token from.
Type: String
Required: No

 ** [token](#API_RefreshToken_RequestSyntax) **   <a name="amplifyuibuilder-RefreshToken-request-token"></a>
The token to use to refresh a previously issued access token that might have expired.
Type: String
Required: Yes

## Response Syntax
<a name="API_RefreshToken_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "accessToken": "string",
   "expiresIn": number
}
```

## Response Elements
<a name="API_RefreshToken_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [accessToken](#API_RefreshToken_ResponseSyntax) **   <a name="amplifyuibuilder-RefreshToken-response-accessToken"></a>
The access token.
Type: String

 ** [expiresIn](#API_RefreshToken_ResponseSyntax) **   <a name="amplifyuibuilder-RefreshToken-response-expiresIn"></a>
The date and time when the new access token expires.
Type: Integer

## Errors
<a name="API_RefreshToken_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InvalidParameterException **
An invalid or out-of-range value was supplied for the input parameter.
HTTP Status Code: 400

## See Also
<a name="API_RefreshToken_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/amplifyuibuilder-2021-08-11/RefreshToken)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/amplifyuibuilder-2021-08-11/RefreshToken)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/amplifyuibuilder-2021-08-11/RefreshToken)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/amplifyuibuilder-2021-08-11/RefreshToken)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/amplifyuibuilder-2021-08-11/RefreshToken)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/amplifyuibuilder-2021-08-11/RefreshToken)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/amplifyuibuilder-2021-08-11/RefreshToken)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/amplifyuibuilder-2021-08-11/RefreshToken)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/amplifyuibuilder-2021-08-11/RefreshToken)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/amplifyuibuilder-2021-08-11/RefreshToken)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AmplifyUIBuilder. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query amplifyuibuilder` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
