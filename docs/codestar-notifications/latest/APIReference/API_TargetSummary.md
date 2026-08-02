---
source_url: https://docs.aws.amazon.com/codestar-notifications/latest/APIReference/API_TargetSummary.html
---

# TargetSummary
<a name="API_TargetSummary"></a>

Information about the targets specified for a notification rule.

## Contents
<a name="API_TargetSummary_Contents"></a>

 ** TargetAddress **   <a name="codestarnotifications-Type-TargetSummary-TargetAddress"></a>
The Amazon Resource Name (ARN) of the Amazon Q Developer in chat applications topic or Amazon Q Developer in chat applications client.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 320.
Required: No

 ** TargetStatus **   <a name="codestarnotifications-Type-TargetSummary-TargetStatus"></a>
The status of the target.
Type: String
Valid Values: `PENDING | ACTIVE | UNREACHABLE | INACTIVE | DEACTIVATED`
Required: No

 ** TargetType **   <a name="codestarnotifications-Type-TargetSummary-TargetType"></a>
The type of the target (for example, `SNS`).
+ Amazon Q Developer in chat applications topics are specified as `SNS`.
+ Amazon Q Developer in chat applications clients for Slack are specified as `AWSChatbotSlack`.
+ Amazon Q Developer in chat applications clients for Microsoft Teams are specified as `AWSChatbotMicrosoftTeams`.
Type: String
Pattern: `^[A-Za-z]+$`
Required: No

## See Also
<a name="API_TargetSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/codestar-notifications-2019-10-15/TargetSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/codestar-notifications-2019-10-15/TargetSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/codestar-notifications-2019-10-15/TargetSummary)
