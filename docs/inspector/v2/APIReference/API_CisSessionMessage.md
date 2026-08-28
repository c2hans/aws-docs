---
source_url: https://docs.aws.amazon.com/inspector/v2/APIReference/API_CisSessionMessage.html
---

# CisSessionMessage
<a name="API_CisSessionMessage"></a>

The CIS session message.

## Contents
<a name="API_CisSessionMessage_Contents"></a>

 ** cisRuleDetails **   <a name="inspector2-Type-CisSessionMessage-cisRuleDetails"></a>
The CIS rule details for the CIS session message.
Type: Base64-encoded binary data object
Length Constraints: Minimum length of 0. Maximum length of 1000.
Required: Yes

 ** ruleId **   <a name="inspector2-Type-CisSessionMessage-ruleId"></a>
The rule ID for the CIS session message.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 500.
Required: Yes

 ** status **   <a name="inspector2-Type-CisSessionMessage-status"></a>
The status of the CIS session message.
Type: String
Valid Values: `FAILED | PASSED | NOT_EVALUATED | INFORMATIONAL | UNKNOWN | NOT_APPLICABLE | ERROR`
Required: Yes

## See Also
<a name="API_CisSessionMessage_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/inspector2-2020-06-08/CisSessionMessage)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/inspector2-2020-06-08/CisSessionMessage)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/inspector2-2020-06-08/CisSessionMessage)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Inspector. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query inspector` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
