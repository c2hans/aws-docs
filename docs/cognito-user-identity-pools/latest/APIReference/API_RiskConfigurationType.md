---
source_url: https://docs.aws.amazon.com/cognito-user-identity-pools/latest/APIReference/API_RiskConfigurationType.html
---

# RiskConfigurationType
<a name="API_RiskConfigurationType"></a>

The settings of risk configuration for threat protection with threat protection in a user pool.

This data type is a response parameter of [DescribeRiskConfiguration](API_DescribeRiskConfiguration.md) and [SetRiskConfiguration](API_SetRiskConfiguration.md).

## Contents
<a name="API_RiskConfigurationType_Contents"></a>

 ** AccountTakeoverRiskConfiguration **   <a name="CognitoUserPools-Type-RiskConfigurationType-AccountTakeoverRiskConfiguration"></a>
The settings for automated responses and notification templates for adaptive authentication with threat protection.
Type: [AccountTakeoverRiskConfigurationType](API_AccountTakeoverRiskConfigurationType.md) object
Required: No

 ** ClientId **   <a name="CognitoUserPools-Type-RiskConfigurationType-ClientId"></a>
The app client where this configuration is applied. When this parameter isn't present, the risk configuration applies to all user pool app clients that don't have client-level settings.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `[\w+]+`
Required: No

 ** CompromisedCredentialsRiskConfiguration **   <a name="CognitoUserPools-Type-RiskConfigurationType-CompromisedCredentialsRiskConfiguration"></a>
Settings for compromised-credentials actions and authentication types with threat protection in full-function `ENFORCED` mode.
Type: [CompromisedCredentialsRiskConfigurationType](API_CompromisedCredentialsRiskConfigurationType.md) object
Required: No

 ** LastModifiedDate **   <a name="CognitoUserPools-Type-RiskConfigurationType-LastModifiedDate"></a>
The date and time when the item was modified. Amazon Cognito returns this timestamp in UNIX epoch time format. Your SDK might render the output in a human-readable format like ISO 8601 or a Java `Date` object.
Type: Timestamp
Required: No

 ** RiskExceptionConfiguration **   <a name="CognitoUserPools-Type-RiskConfigurationType-RiskExceptionConfiguration"></a>
Exceptions to the risk evaluation configuration, including always-allow and always-block IP address ranges.
Type: [RiskExceptionConfigurationType](API_RiskExceptionConfigurationType.md) object
Required: No

 ** UserPoolId **   <a name="CognitoUserPools-Type-RiskConfigurationType-UserPoolId"></a>
The ID of the user pool that has the risk configuration applied.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 55.
Pattern: `[\w-]+_[0-9a-zA-Z]+`
Required: No

## See Also
<a name="API_RiskConfigurationType_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/cognito-idp-2016-04-18/RiskConfigurationType)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cognito-idp-2016-04-18/RiskConfigurationType)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cognito-idp-2016-04-18/RiskConfigurationType)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Cognito User Pools. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query cognito-user-identity-pools` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
