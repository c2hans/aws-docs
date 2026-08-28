---
source_url: https://docs.aws.amazon.com/cognito-user-identity-pools/latest/APIReference/API_CompromisedCredentialsRiskConfigurationType.html
---

# CompromisedCredentialsRiskConfigurationType
<a name="API_CompromisedCredentialsRiskConfigurationType"></a>

Settings for compromised-credentials actions and authentication-event sources with threat protection in full-function `ENFORCED` mode.

This data type is a request parameter of [SetRiskConfiguration](API_SetRiskConfiguration.md) and a response parameter of [DescribeRiskConfiguration](API_DescribeRiskConfiguration.md).

## Contents
<a name="API_CompromisedCredentialsRiskConfigurationType_Contents"></a>

 ** Actions **   <a name="CognitoUserPools-Type-CompromisedCredentialsRiskConfigurationType-Actions"></a>
Settings for the actions that you want your user pool to take when Amazon Cognito detects compromised credentials.
Type: [CompromisedCredentialsActionsType](API_CompromisedCredentialsActionsType.md) object
Required: Yes

 ** EventFilter **   <a name="CognitoUserPools-Type-CompromisedCredentialsRiskConfigurationType-EventFilter"></a>
Settings for the sign-in activity where you want to configure compromised-credentials actions. Defaults to all events.
Type: Array of strings
Valid Values: `SIGN_IN | PASSWORD_CHANGE | SIGN_UP`
Required: No

## See Also
<a name="API_CompromisedCredentialsRiskConfigurationType_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/cognito-idp-2016-04-18/CompromisedCredentialsRiskConfigurationType)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cognito-idp-2016-04-18/CompromisedCredentialsRiskConfigurationType)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cognito-idp-2016-04-18/CompromisedCredentialsRiskConfigurationType)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Cognito User Pools. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query cognito-user-identity-pools` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
