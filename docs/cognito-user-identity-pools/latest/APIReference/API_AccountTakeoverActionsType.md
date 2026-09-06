---
source_url: https://docs.aws.amazon.com/cognito-user-identity-pools/latest/APIReference/API_AccountTakeoverActionsType.html
---

# AccountTakeoverActionsType
<a name="API_AccountTakeoverActionsType"></a>

A list of account-takeover actions for each level of risk that Amazon Cognito might assess with threat protection features.

This data type is a request parameter of [SetRiskConfiguration](API_SetRiskConfiguration.md) and a response parameter of [DescribeRiskConfiguration](API_DescribeRiskConfiguration.md).

## Contents
<a name="API_AccountTakeoverActionsType_Contents"></a>

 ** HighAction **   <a name="CognitoUserPools-Type-AccountTakeoverActionsType-HighAction"></a>
The action that you assign to a high-risk assessment by threat protection.
Type: [AccountTakeoverActionType](API_AccountTakeoverActionType.md) object
Required: No

 ** LowAction **   <a name="CognitoUserPools-Type-AccountTakeoverActionsType-LowAction"></a>
The action that you assign to a low-risk assessment by threat protection.
Type: [AccountTakeoverActionType](API_AccountTakeoverActionType.md) object
Required: No

 ** MediumAction **   <a name="CognitoUserPools-Type-AccountTakeoverActionsType-MediumAction"></a>
The action that you assign to a medium-risk assessment by threat protection.
Type: [AccountTakeoverActionType](API_AccountTakeoverActionType.md) object
Required: No

## See Also
<a name="API_AccountTakeoverActionsType_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/cognito-idp-2016-04-18/AccountTakeoverActionsType)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cognito-idp-2016-04-18/AccountTakeoverActionsType)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cognito-idp-2016-04-18/AccountTakeoverActionsType)
