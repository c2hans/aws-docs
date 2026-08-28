---
source_url: https://docs.aws.amazon.com/amazonq/latest/api-reference/API_TopicConfiguration.html
---

# TopicConfiguration
<a name="API_TopicConfiguration"></a>

The topic specific controls configured for an Amazon Q Business application.

## Contents
<a name="API_TopicConfiguration_Contents"></a>

 ** name **   <a name="qbusiness-Type-TopicConfiguration-name"></a>
A name for your topic control configuration.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 36.
Pattern: `[a-zA-Z0-9][a-zA-Z0-9-]{0,35}`
Required: Yes

 ** rules **   <a name="qbusiness-Type-TopicConfiguration-rules"></a>
Rules defined for a topic configuration.
Type: Array of [Rule](API_Rule.md) objects
Array Members: Minimum number of 0 items. Maximum number of 10 items.
Required: Yes

 ** description **   <a name="qbusiness-Type-TopicConfiguration-description"></a>
A description for your topic control configuration. Use this to outline how the large language model (LLM) should use this topic control configuration.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 350.
Pattern: `\P{C}*`
Required: No

 ** exampleChatMessages **   <a name="qbusiness-Type-TopicConfiguration-exampleChatMessages"></a>
A list of example phrases that you expect the end user to use in relation to the topic.
Type: Array of strings
Array Members: Minimum number of 0 items. Maximum number of 5 items.
Length Constraints: Minimum length of 0. Maximum length of 350.
Pattern: `\P{C}*`
Required: No

## See Also
<a name="API_TopicConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/qbusiness-2023-11-27/TopicConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/qbusiness-2023-11-27/TopicConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/qbusiness-2023-11-27/TopicConfiguration)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Q Business. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query amazonq` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
