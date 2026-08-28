---
source_url: https://docs.aws.amazon.com/cognito-user-identity-pools/latest/APIReference/API_AccountTakeoverActionType.html
---

# AccountTakeoverActionType
<a name="API_AccountTakeoverActionType"></a>

The automated response to a risk level for adaptive authentication in full-function, or `ENFORCED`, mode. You can assign an action to each risk level that threat protection evaluates.

This data type is a request parameter of [SetRiskConfiguration](API_SetRiskConfiguration.md) and a response parameter of [DescribeRiskConfiguration](API_DescribeRiskConfiguration.md).

## Contents
<a name="API_AccountTakeoverActionType_Contents"></a>

 ** EventAction **   <a name="CognitoUserPools-Type-AccountTakeoverActionType-EventAction"></a>
The action to take for the attempted account takeover action for the associated risk level. Valid values are as follows:
+  `BLOCK`: Block the request.
+  `MFA_IF_CONFIGURED`: Present an MFA challenge if possible. MFA is possible if the user pool has active MFA methods that the user can set up. For example, if the user pool only supports SMS message MFA but the user doesn't have a phone number attribute, MFA setup isn't possible. If MFA setup isn't possible, allow the request.
+  `MFA_REQUIRED`: Present an MFA challenge if possible. Block the request if a user hasn't set up MFA. To sign in with required MFA, users must have an email address or phone number attribute, or a registered TOTP factor.
+  `NO_ACTION`: Take no action. Permit sign-in.
Type: String
Valid Values: `BLOCK | MFA_IF_CONFIGURED | MFA_REQUIRED | NO_ACTION`
Required: Yes

 ** Notify **   <a name="CognitoUserPools-Type-AccountTakeoverActionType-Notify"></a>
Determines whether Amazon Cognito sends a user a notification message when your user pools assesses a user's session at the associated risk level.
Type: Boolean
Required: Yes

## See Also
<a name="API_AccountTakeoverActionType_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/cognito-idp-2016-04-18/AccountTakeoverActionType)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cognito-idp-2016-04-18/AccountTakeoverActionType)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cognito-idp-2016-04-18/AccountTakeoverActionType)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Cognito User Pools. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query cognito-user-identity-pools` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
