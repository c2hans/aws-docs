---
source_url: https://docs.aws.amazon.com/codecatalyst/latest/APIReference/API_CreateAccessToken.html
---

# CreateAccessToken
<a name="API_CreateAccessToken"></a>

Creates a personal access token (PAT) for the current user. A personal access token (PAT) is similar to a password. It is associated with your user identity for use across all spaces and projects in Amazon CodeCatalyst. You use PATs to access CodeCatalyst from resources that include integrated development environments (IDEs) and Git-based source repositories. PATs represent you in Amazon CodeCatalyst and you can manage them in your user settings.For more information, see [Managing personal access tokens in Amazon CodeCatalyst](https://docs.aws.amazon.com/codecatalyst/latest/userguide/ipa-tokens-keys.html).

## Request Syntax
<a name="API_CreateAccessToken_RequestSyntax"></a>

```
PUT /v1/accessTokens HTTP/1.1
Content-type: application/json

{
   "expiresTime": "{{string}}",
   "name": "{{string}}"
}
```

## URI Request Parameters
<a name="API_CreateAccessToken_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_CreateAccessToken_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [expiresTime](#API_CreateAccessToken_RequestSyntax) **   <a name="codecatalyst-CreateAccessToken-request-expiresTime"></a>
The date and time the personal access token expires, in coordinated universal time (UTC) timestamp format as specified in [RFC 3339](https://www.rfc-editor.org/rfc/rfc3339#section-5.6).
Type: Timestamp
Required: No

 ** [name](#API_CreateAccessToken_RequestSyntax) **   <a name="codecatalyst-CreateAccessToken-request-name"></a>
The friendly name of the personal access token.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Required: Yes

## Response Syntax
<a name="API_CreateAccessToken_ResponseSyntax"></a>

```
HTTP/1.1 201
Content-type: application/json

{
   "accessTokenId": "string",
   "expiresTime": "string",
   "name": "string",
   "secret": "string"
}
```

## Response Elements
<a name="API_CreateAccessToken_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 201 response.

The following data is returned in JSON format by the service.

 ** [accessTokenId](#API_CreateAccessToken_ResponseSyntax) **   <a name="codecatalyst-CreateAccessToken-response-accessTokenId"></a>
The system-generated unique ID of the access token.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 36.

 ** [expiresTime](#API_CreateAccessToken_ResponseSyntax) **   <a name="codecatalyst-CreateAccessToken-response-expiresTime"></a>
The date and time the personal access token expires, in coordinated universal time (UTC) timestamp format as specified in [RFC 3339](https://www.rfc-editor.org/rfc/rfc3339#section-5.6). If not specified, the default is one year from creation.
Type: Timestamp

 ** [name](#API_CreateAccessToken_ResponseSyntax) **   <a name="codecatalyst-CreateAccessToken-response-name"></a>
The friendly name of the personal access token.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.

 ** [secret](#API_CreateAccessToken_ResponseSyntax) **   <a name="codecatalyst-CreateAccessToken-response-secret"></a>
The secret value of the personal access token.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 4000.

## Errors
<a name="API_CreateAccessToken_Errors"></a>

 ** AccessDeniedException **
The request was denied because you don't have sufficient access to perform this action. Verify that you are a member of a role that allows this action.
HTTP Status Code: 403

 ** ConflictException **
The request was denied because the requested operation would cause a conflict with the current state of a service resource associated with the request. Another user might have updated the resource. Reload, make sure you have the latest data, and then try again.
HTTP Status Code: 409

 ** ResourceNotFoundException **
The request was denied because the specified resource was not found. Verify that the spelling is correct and that you have access to the resource.
HTTP Status Code: 404

 ** ServiceQuotaExceededException **
The request was denied because one or more resources has reached its limits for the tier the space belongs to. Either reduce the number of resources, or change the tier if applicable.
HTTP Status Code: 402

 ** ThrottlingException **
The request was denied due to request throttling.
HTTP Status Code: 429

 ** ValidationException **
The request was denied because an input failed to satisfy the constraints specified by the service. Check the spelling and input requirements, and then try again.
HTTP Status Code: 400

## See Also
<a name="API_CreateAccessToken_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/codecatalyst-2022-09-28/CreateAccessToken)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/codecatalyst-2022-09-28/CreateAccessToken)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/codecatalyst-2022-09-28/CreateAccessToken)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/codecatalyst-2022-09-28/CreateAccessToken)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/codecatalyst-2022-09-28/CreateAccessToken)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/codecatalyst-2022-09-28/CreateAccessToken)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/codecatalyst-2022-09-28/CreateAccessToken)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/codecatalyst-2022-09-28/CreateAccessToken)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/codecatalyst-2022-09-28/CreateAccessToken)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/codecatalyst-2022-09-28/CreateAccessToken)
