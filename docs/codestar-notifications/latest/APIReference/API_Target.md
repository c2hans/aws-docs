---
source_url: https://docs.aws.amazon.com/codestar-notifications/latest/APIReference/API_Target.html
---

# Target
<a name="API_Target"></a>

Information about the Amazon Q Developer in chat applications topics or Amazon Q Developer in chat applications clients associated with a notification rule.

## Contents
<a name="API_Target_Contents"></a>

 ** TargetAddress **   <a name="codestarnotifications-Type-Target-TargetAddress"></a>
The Amazon Resource Name (ARN) of the Amazon Q Developer in chat applications topic or Amazon Q Developer in chat applications client.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 320.
Required: No

 ** TargetType **   <a name="codestarnotifications-Type-Target-TargetType"></a>
The target type. Can be an Amazon Q Developer in chat applications topic or Amazon Q Developer in chat applications client.
+ Amazon Q Developer in chat applications topics are specified as `SNS`.
+ Amazon Q Developer in chat applications clients are specified as `AWSChatbotSlack`.
+ Amazon Q Developer in chat applications clients for Microsoft Teams are specified as `AWSChatbotMicrosoftTeams`.
Type: String
Pattern: `^[A-Za-z]+$`
Required: No

## See Also
<a name="API_Target_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/codestar-notifications-2019-10-15/Target)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/codestar-notifications-2019-10-15/Target)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/codestar-notifications-2019-10-15/Target)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CodeStar Notifications. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query codestar-notifications` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
