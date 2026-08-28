---
source_url: https://docs.aws.amazon.com/cognito-user-identity-pools/latest/APIReference/API_EventRiskType.html
---

# EventRiskType
<a name="API_EventRiskType"></a>

The risk evaluation by adaptive authentication, as displayed in an `AdminListUserAuthEvents` response. Contains evaluations of compromised-credentials detection and assessed risk level and action taken by adaptive authentication.

## Contents
<a name="API_EventRiskType_Contents"></a>

 ** CompromisedCredentialsDetected **   <a name="CognitoUserPools-Type-EventRiskType-CompromisedCredentialsDetected"></a>
Indicates whether compromised credentials were detected during an authentication event.
Type: Boolean
Required: No

 ** RiskDecision **   <a name="CognitoUserPools-Type-EventRiskType-RiskDecision"></a>
The action taken by adaptive authentication. If `NoRisk`, your user pool took no action. If `AccountTakeover`, your user pool applied the adaptive authentication automated response that you configured. If `Block`, your user pool prevented the attempt.
Type: String
Valid Values: `NoRisk | AccountTakeover | Block`
Required: No

 ** RiskLevel **   <a name="CognitoUserPools-Type-EventRiskType-RiskLevel"></a>
The risk level that adaptive authentication assessed for the authentication event.
Type: String
Valid Values: `Low | Medium | High`
Required: No

## See Also
<a name="API_EventRiskType_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/cognito-idp-2016-04-18/EventRiskType)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cognito-idp-2016-04-18/EventRiskType)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cognito-idp-2016-04-18/EventRiskType)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Cognito User Pools. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query cognito-user-identity-pools` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
