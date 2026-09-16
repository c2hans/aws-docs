---
source_url: https://docs.aws.amazon.com/codeguru/latest/reviewer-api/API_CreateConnectionToken.html
---

# CreateConnectionToken
<a name="API_CreateConnectionToken"></a>

**Note**
As of November 7, 2025, you cannot create new repository associations in Amazon CodeGuru Reviewer. To learn about services with capabilities similar to CodeGuru Reviewer, see [Amazon CodeGuru Reviewer availability change](https://docs.aws.amazon.com/codeguru/latest/reviewer-ug/codeguru-reviewer-availability-change.html).

Creates a connection token for third-party repository integration with CodeGuru Reviewer.

## Request Syntax
<a name="API_CreateConnectionToken_RequestSyntax"></a>

```
POST /token HTTP/1.1
Content-type: application/json

{
   "AuthCode": "{{string}}",
   "AuthToken": {
      "CreationTime": {{number}},
      "Scopes": [ "{{string}}" ],
      "Token": "{{string}}",
      "User": "{{string}}"
   },
   "ProviderType": "{{string}}",
   "State": "{{string}}"
}
```

## URI Request Parameters
<a name="API_CreateConnectionToken_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_CreateConnectionToken_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [AuthCode](#API_CreateConnectionToken_RequestSyntax) **   <a name="reviewer-CreateConnectionToken-request-AuthCode"></a>
The authorization code used for establishing the connection.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `\S+`
Required: No

 ** [AuthToken](#API_CreateConnectionToken_RequestSyntax) **   <a name="reviewer-CreateConnectionToken-request-AuthToken"></a>
The authentication token used for establishing the connection.
Type: [AuthorizationToken](API_AuthorizationToken.md) object
Required: No

 ** [ProviderType](#API_CreateConnectionToken_RequestSyntax) **   <a name="reviewer-CreateConnectionToken-request-ProviderType"></a>
The type of third-party provider for the connection.
Type: String
Valid Values: `CodeCommit | GitHub | Bitbucket | GitHubEnterpriseServer | S3Bucket`
Required: Yes

 ** [State](#API_CreateConnectionToken_RequestSyntax) **   <a name="reviewer-CreateConnectionToken-request-State"></a>
The state parameter used for OAuth flow security.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Required: No

## Response Syntax
<a name="API_CreateConnectionToken_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "ConnectionToken": "string"
}
```

## Response Elements
<a name="API_CreateConnectionToken_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [ConnectionToken](#API_CreateConnectionToken_ResponseSyntax) **   <a name="reviewer-CreateConnectionToken-response-ConnectionToken"></a>
The generated connection token for third-party repository access.
Type: String
Length Constraints: Minimum length of 8. Maximum length of 2048.
Pattern: `\S+`

## Errors
<a name="API_CreateConnectionToken_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You do not have sufficient access to perform this action.
HTTP Status Code: 403

 ** InternalServerException **
The server encountered an internal error and is unable to complete the request.
HTTP Status Code: 500

 ** ThrottlingException **
The request was denied due to request throttling.
HTTP Status Code: 429

 ** ValidationException **
The input fails to satisfy the specified constraints.
HTTP Status Code: 400

## See Also
<a name="API_CreateConnectionToken_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/codeguru-reviewer-2019-09-19/CreateConnectionToken)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/codeguru-reviewer-2019-09-19/CreateConnectionToken)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/codeguru-reviewer-2019-09-19/CreateConnectionToken)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/codeguru-reviewer-2019-09-19/CreateConnectionToken)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/codeguru-reviewer-2019-09-19/CreateConnectionToken)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/codeguru-reviewer-2019-09-19/CreateConnectionToken)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/codeguru-reviewer-2019-09-19/CreateConnectionToken)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/codeguru-reviewer-2019-09-19/CreateConnectionToken)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/codeguru-reviewer-2019-09-19/CreateConnectionToken)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/codeguru-reviewer-2019-09-19/CreateConnectionToken)
