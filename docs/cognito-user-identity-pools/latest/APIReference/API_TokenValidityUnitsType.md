---
source_url: https://docs.aws.amazon.com/cognito-user-identity-pools/latest/APIReference/API_TokenValidityUnitsType.html
---

# TokenValidityUnitsType
<a name="API_TokenValidityUnitsType"></a>

The time units that, with `IdTokenValidity`, `AccessTokenValidity`, and `RefreshTokenValidity`, set and display the duration of ID, access, and refresh tokens for an app client. You can assign a separate token validity unit to each type of token.

This data type is a request parameter of [CreateUserPoolClient](API_CreateUserPoolClient.md) and [UpdateUserPoolClient](API_UpdateUserPoolClient.md), and a response parameter of [DescribeUserPoolClient](API_DescribeUserPoolClient.md).

## Contents
<a name="API_TokenValidityUnitsType_Contents"></a>

 ** AccessToken **   <a name="CognitoUserPools-Type-TokenValidityUnitsType-AccessToken"></a>
 A time unit for the value that you set in the `AccessTokenValidity` parameter. The default `AccessTokenValidity` time unit is `hours`. `AccessTokenValidity` duration can range from five minutes to one day.
Type: String
Valid Values: `seconds | minutes | hours | days`
Required: No

 ** IdToken **   <a name="CognitoUserPools-Type-TokenValidityUnitsType-IdToken"></a>
A time unit for the value that you set in the `IdTokenValidity` parameter. The default `IdTokenValidity` time unit is `hours`. `IdTokenValidity` duration can range from five minutes to one day.
Type: String
Valid Values: `seconds | minutes | hours | days`
Required: No

 ** RefreshToken **   <a name="CognitoUserPools-Type-TokenValidityUnitsType-RefreshToken"></a>
A time unit for the value that you set in the `RefreshTokenValidity` parameter. The default `RefreshTokenValidity` time unit is `days`. `RefreshTokenValidity` duration can range from 60 minutes to 10 years.
Type: String
Valid Values: `seconds | minutes | hours | days`
Required: No

## See Also
<a name="API_TokenValidityUnitsType_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/cognito-idp-2016-04-18/TokenValidityUnitsType)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cognito-idp-2016-04-18/TokenValidityUnitsType)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cognito-idp-2016-04-18/TokenValidityUnitsType)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Cognito User Pools. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query cognito-user-identity-pools` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
