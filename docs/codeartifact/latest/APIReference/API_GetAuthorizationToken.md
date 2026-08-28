---
source_url: https://docs.aws.amazon.com/codeartifact/latest/APIReference/API_GetAuthorizationToken.html
---

# GetAuthorizationToken
<a name="API_GetAuthorizationToken"></a>

 Generates a temporary authorization token for accessing repositories in the domain. This API requires the `codeartifact:GetAuthorizationToken` and `sts:GetServiceBearerToken` permissions. For more information about authorization tokens, see [AWS CodeArtifact authentication and tokens](https://docs.aws.amazon.com/codeartifact/latest/ug/tokens-authentication.html).

**Note**
CodeArtifact authorization tokens are valid for a period of 12 hours when created with the `login` command. You can call `login` periodically to refresh the token. When you create an authorization token with the `GetAuthorizationToken` API, you can set a custom authorization period, up to a maximum of 12 hours, with the `durationSeconds` parameter.
The authorization period begins after `login` or `GetAuthorizationToken` is called. If `login` or `GetAuthorizationToken` is called while assuming a role, the token lifetime is independent of the maximum session duration of the role. For example, if you call `sts assume-role` and specify a session duration of 15 minutes, then generate a CodeArtifact authorization token, the token will be valid for the full authorization period even though this is longer than the 15-minute session duration.
See [Using IAM Roles](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use.html) for more information on controlling session duration.

## Request Syntax
<a name="API_GetAuthorizationToken_RequestSyntax"></a>

```
POST /v1/authorization-token?domain={{domain}}&domain-owner={{domainOwner}}&duration={{durationSeconds}} HTTP/1.1
```

## URI Request Parameters
<a name="API_GetAuthorizationToken_RequestParameters"></a>

The request uses the following URI parameters.

 ** [domain](#API_GetAuthorizationToken_RequestSyntax) **   <a name="codeartifact-GetAuthorizationToken-request-uri-domain"></a>
 The name of the domain that is in scope for the generated authorization token.
Length Constraints: Minimum length of 2. Maximum length of 50.
Pattern: `[a-z][a-z0-9\-]{0,48}[a-z0-9]`
Required: Yes

 ** [domainOwner](#API_GetAuthorizationToken_RequestSyntax) **   <a name="codeartifact-GetAuthorizationToken-request-uri-domainOwner"></a>
 The 12-digit account number of the AWS account that owns the domain. It does not include dashes or spaces.
Length Constraints: Fixed length of 12.
Pattern: `[0-9]{12}`

 ** [durationSeconds](#API_GetAuthorizationToken_RequestSyntax) **   <a name="codeartifact-GetAuthorizationToken-request-uri-durationSeconds"></a>
The time, in seconds, that the generated authorization token is valid. Valid values are `0` and any number between `900` (15 minutes) and `43200` (12 hours). A value of `0` will set the expiration of the authorization token to the same expiration of the user's role's temporary credentials.
Valid Range: Minimum value of 0. Maximum value of 43200.

## Request Body
<a name="API_GetAuthorizationToken_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_GetAuthorizationToken_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "authorizationToken": "string",
   "expiration": number
}
```

## Response Elements
<a name="API_GetAuthorizationToken_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [authorizationToken](#API_GetAuthorizationToken_ResponseSyntax) **   <a name="codeartifact-GetAuthorizationToken-response-authorizationToken"></a>
 The returned authentication token.
Type: String

 ** [expiration](#API_GetAuthorizationToken_ResponseSyntax) **   <a name="codeartifact-GetAuthorizationToken-response-expiration"></a>
 A timestamp that specifies the date and time the authorization token expires.
Type: Timestamp

## Errors
<a name="API_GetAuthorizationToken_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
 The operation did not succeed because of an unauthorized access attempt.
HTTP Status Code: 403

 ** InternalServerException **
 The operation did not succeed because of an error that occurred inside AWS CodeArtifact.
HTTP Status Code: 500

 ** ResourceNotFoundException **
 The operation did not succeed because the resource requested is not found in the service.
 ** resourceId **
 The ID of the resource.
 ** resourceType **
 The type of AWS resource.
HTTP Status Code: 404

 ** ThrottlingException **
 The operation did not succeed because too many requests are sent to the service.
 ** retryAfterSeconds **
 The time period, in seconds, to wait before retrying the request.
HTTP Status Code: 429

 ** ValidationException **
 The operation did not succeed because a parameter in the request was sent with an invalid value.
 ** reason **

HTTP Status Code: 400

## See Also
<a name="API_GetAuthorizationToken_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/codeartifact-2018-09-22/GetAuthorizationToken)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/codeartifact-2018-09-22/GetAuthorizationToken)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/codeartifact-2018-09-22/GetAuthorizationToken)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/codeartifact-2018-09-22/GetAuthorizationToken)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/codeartifact-2018-09-22/GetAuthorizationToken)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/codeartifact-2018-09-22/GetAuthorizationToken)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/codeartifact-2018-09-22/GetAuthorizationToken)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/codeartifact-2018-09-22/GetAuthorizationToken)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/codeartifact-2018-09-22/GetAuthorizationToken)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/codeartifact-2018-09-22/GetAuthorizationToken)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CodeArtifact. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query codeartifact` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
