---
source_url: https://docs.aws.amazon.com/cognitoidentity/latest/APIReference/API_RulesConfigurationType.html
---

# RulesConfigurationType
<a name="API_RulesConfigurationType"></a>

A container for rules.

## Contents
<a name="API_RulesConfigurationType_Contents"></a>

 ** Rules **   <a name="CognitoIdentity-Type-RulesConfigurationType-Rules"></a>
An array of rules. You can specify up to 25 rules per identity provider.
Rules are evaluated in order. The first one to match specifies the role.
Type: Array of [MappingRule](API_MappingRule.md) objects
Array Members: Minimum number of 1 item. Maximum number of 25 items.
Required: Yes

## See Also
<a name="API_RulesConfigurationType_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/cognito-identity-2014-06-30/RulesConfigurationType)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cognito-identity-2014-06-30/RulesConfigurationType)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cognito-identity-2014-06-30/RulesConfigurationType)
