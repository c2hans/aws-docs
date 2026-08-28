---
source_url: https://docs.aws.amazon.com/singlesignon/latest/PortalAPIReference/API_Logout.html
---

# Logout
<a name="API_Logout"></a>

Removes the locally stored SSO tokens from the client-side cache and sends an API call to the IAM Identity Center service to invalidate the corresponding server-side IAM Identity Center sign in session.

**Note**
If a user uses IAM Identity Center to access the AWS CLI, the user’s IAM Identity Center sign in session is used to obtain an IAM session, as specified in the corresponding IAM Identity Center permission set. More specifically, IAM Identity Center assumes an IAM role in the target account on behalf of the user, and the corresponding temporary AWS credentials are returned to the client.
After user logout, any existing IAM role sessions that were created by using IAM Identity Center permission sets continue based on the duration configured in the permission set. For more information, see [User authentications](https://docs.aws.amazon.com/singlesignon/latest/userguide/authconcept.html) in the *IAM Identity Center User Guide*.

## Request Syntax
<a name="API_Logout_RequestSyntax"></a>

```
POST /logout HTTP/1.1
x-amz-sso_bearer_token: {{accessToken}}
```

## URI Request Parameters
<a name="API_Logout_RequestParameters"></a>

The request uses the following URI parameters.

 ** [accessToken](#API_Logout_RequestSyntax) **   <a name="singlesignon-Logout-request-accessToken"></a>
The token issued by the `CreateToken` API call. For more information, see [CreateToken](https://docs.aws.amazon.com/singlesignon/latest/OIDCAPIReference/API_CreateToken.html) in the *IAM Identity Center OIDC API Reference Guide*.
Required: Yes

## Request Body
<a name="API_Logout_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_Logout_ResponseSyntax"></a>

```
HTTP/1.1 200
```

## Response Elements
<a name="API_Logout_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors
<a name="API_Logout_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InvalidRequestException **
Indicates that a problem occurred with the input to the request. For example, a required parameter might be missing or out of range.
HTTP Status Code: 400

 ** TooManyRequestsException **
Indicates that the request is being made too frequently and is more than what the server can handle.
HTTP Status Code: 429

 ** UnauthorizedException **
Indicates that the request is not authorized. This can happen due to an invalid access token in the request.
HTTP Status Code: 401

## See Also
<a name="API_Logout_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/sso-2019-06-10/Logout)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/sso-2019-06-10/Logout)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sso-2019-06-10/Logout)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/sso-2019-06-10/Logout)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sso-2019-06-10/Logout)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/sso-2019-06-10/Logout)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/sso-2019-06-10/Logout)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/sso-2019-06-10/Logout)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/sso-2019-06-10/Logout)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sso-2019-06-10/Logout)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for IAM Identity Center. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query singlesignon` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
