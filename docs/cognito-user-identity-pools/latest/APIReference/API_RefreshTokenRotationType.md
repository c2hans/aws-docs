---
source_url: https://docs.aws.amazon.com/cognito-user-identity-pools/latest/APIReference/API_RefreshTokenRotationType.html
---

# RefreshTokenRotationType
<a name="API_RefreshTokenRotationType"></a>

The configuration of your app client for refresh token rotation. When enabled, your app client issues new ID, access, and refresh tokens when users renew their sessions with refresh tokens. When disabled, token refresh issues only ID and access tokens.

Refresh token rotation must be completed with [GetTokensFromRefreshToken](API_GetTokensFromRefreshToken.md). With refresh token rotation disabled, you can complete token refresh with `GetTokensFromRefreshToken` and with `REFRESH_TOKEN_AUTH` in [InitiateAuth:AuthFlow](API_InitiateAuth.md#CognitoUserPools-InitiateAuth-request-AuthFlow) and [AdminInitiateAuth:AuthFlow](API_AdminInitiateAuth.md#CognitoUserPools-AdminInitiateAuth-request-AuthFlow).

This data type is a request parameter of [CreateUserPoolClient](API_CreateUserPoolClient.md) and [UpdateUserPoolClient](API_UpdateUserPoolClient.md), and a response parameter of [DescribeUserPoolClient](API_DescribeUserPoolClient.md).

## Contents
<a name="API_RefreshTokenRotationType_Contents"></a>

 ** Feature **   <a name="CognitoUserPools-Type-RefreshTokenRotationType-Feature"></a>
The state of refresh token rotation for the current app client.
Type: String
Valid Values: `ENABLED | DISABLED`
Required: Yes

 ** RetryGracePeriodSeconds **   <a name="CognitoUserPools-Type-RefreshTokenRotationType-RetryGracePeriodSeconds"></a>
When you request a token refresh with `GetTokensFromRefreshToken`, the original refresh token that you're rotating out can remain valid for a period of time of up to 60 seconds. This allows for client-side retries. When `RetryGracePeriodSeconds` is `0`, the grace period is disabled and a successful request immediately invalidates the submitted refresh token.
Type: Integer
Valid Range: Minimum value of 0. Maximum value of 60.
Required: No

## See Also
<a name="API_RefreshTokenRotationType_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/cognito-idp-2016-04-18/RefreshTokenRotationType)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cognito-idp-2016-04-18/RefreshTokenRotationType)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cognito-idp-2016-04-18/RefreshTokenRotationType)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Cognito User Pools. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query cognito-user-identity-pools` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
