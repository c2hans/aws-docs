---
source_url: https://docs.aws.amazon.com/amazonq/latest/api-reference/API_ContentBlockerRule.html
---

# ContentBlockerRule
<a name="API_ContentBlockerRule"></a>

A rule for configuring how Amazon Q Business responds when it encounters a a blocked topic. You can configure a custom message to inform your end users that they have asked about a restricted topic and suggest any next steps they should take.

## Contents
<a name="API_ContentBlockerRule_Contents"></a>

 ** systemMessageOverride **   <a name="qbusiness-Type-ContentBlockerRule-systemMessageOverride"></a>
The configured custom message displayed to an end user informing them that they've used a blocked phrase during chat.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 350.
Pattern: `\P{C}*`
Required: No

## See Also
<a name="API_ContentBlockerRule_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/qbusiness-2023-11-27/ContentBlockerRule)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/qbusiness-2023-11-27/ContentBlockerRule)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/qbusiness-2023-11-27/ContentBlockerRule)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Q Business. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query amazonq` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
