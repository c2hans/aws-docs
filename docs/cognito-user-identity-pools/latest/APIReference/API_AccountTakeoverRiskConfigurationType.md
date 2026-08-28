---
source_url: https://docs.aws.amazon.com/cognito-user-identity-pools/latest/APIReference/API_AccountTakeoverRiskConfigurationType.html
---

# AccountTakeoverRiskConfigurationType
<a name="API_AccountTakeoverRiskConfigurationType"></a>

The settings for automated responses and notification templates for adaptive authentication with threat protection features.

This data type is a request parameter of [SetRiskConfiguration](API_SetRiskConfiguration.md) and a response parameter of [DescribeRiskConfiguration](API_DescribeRiskConfiguration.md).

## Contents
<a name="API_AccountTakeoverRiskConfigurationType_Contents"></a>

 ** Actions **   <a name="CognitoUserPools-Type-AccountTakeoverRiskConfigurationType-Actions"></a>
A list of account-takeover actions for each level of risk that Amazon Cognito might assess with threat protection.
Type: [AccountTakeoverActionsType](API_AccountTakeoverActionsType.md) object
Required: Yes

 ** NotifyConfiguration **   <a name="CognitoUserPools-Type-AccountTakeoverRiskConfigurationType-NotifyConfiguration"></a>
The settings for composing and sending an email message when threat protection assesses a risk level with adaptive authentication. When you choose to notify users in `AccountTakeoverRiskConfiguration`, Amazon Cognito sends an email message using the method and template that you set with this data type.
Type: [NotifyConfigurationType](API_NotifyConfigurationType.md) object
Required: No

## See Also
<a name="API_AccountTakeoverRiskConfigurationType_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/cognito-idp-2016-04-18/AccountTakeoverRiskConfigurationType)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cognito-idp-2016-04-18/AccountTakeoverRiskConfigurationType)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cognito-idp-2016-04-18/AccountTakeoverRiskConfigurationType)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Cognito User Pools. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query cognito-user-identity-pools` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
