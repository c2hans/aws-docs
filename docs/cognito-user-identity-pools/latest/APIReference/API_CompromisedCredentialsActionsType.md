---
source_url: https://docs.aws.amazon.com/cognito-user-identity-pools/latest/APIReference/API_CompromisedCredentialsActionsType.html
---

# CompromisedCredentialsActionsType
<a name="API_CompromisedCredentialsActionsType"></a>

Settings for user pool actions when Amazon Cognito detects compromised credentials with threat protection in full-function `ENFORCED` mode.

This data type is a request parameter of [SetRiskConfiguration](API_SetRiskConfiguration.md) and a response parameter of [DescribeRiskConfiguration](API_DescribeRiskConfiguration.md).

## Contents
<a name="API_CompromisedCredentialsActionsType_Contents"></a>

 ** EventAction **   <a name="CognitoUserPools-Type-CompromisedCredentialsActionsType-EventAction"></a>
The action that Amazon Cognito takes when it detects compromised credentials.
Type: String
Valid Values: `BLOCK | NO_ACTION`
Required: Yes

## See Also
<a name="API_CompromisedCredentialsActionsType_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/cognito-idp-2016-04-18/CompromisedCredentialsActionsType)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cognito-idp-2016-04-18/CompromisedCredentialsActionsType)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cognito-idp-2016-04-18/CompromisedCredentialsActionsType)
