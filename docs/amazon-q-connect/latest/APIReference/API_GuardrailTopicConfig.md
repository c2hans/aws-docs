---
source_url: https://docs.aws.amazon.com/amazon-q-connect/latest/APIReference/API_GuardrailTopicConfig.html
---

# GuardrailTopicConfig
<a name="API_amazon-q-connect_GuardrailTopicConfig"></a>

Details about topics for the AI Guardrail to identify and deny.

## Contents
<a name="API_amazon-q-connect_GuardrailTopicConfig_Contents"></a>

 ** definition **   <a name="connect-Type-amazon-q-connect_GuardrailTopicConfig-definition"></a>
A definition of the topic to deny.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 200.
Required: Yes

 ** name **   <a name="connect-Type-amazon-q-connect_GuardrailTopicConfig-name"></a>
The name of the topic to deny.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Pattern: `[0-9a-zA-Z-_ !?.]+`
Required: Yes

 ** type **   <a name="connect-Type-amazon-q-connect_GuardrailTopicConfig-type"></a>
Specifies to deny the topic.
Type: String
Valid Values: `DENY`
Required: Yes

 ** examples **   <a name="connect-Type-amazon-q-connect_GuardrailTopicConfig-examples"></a>
A list of prompts, each of which is an example of a prompt that can be categorized as belonging to the topic.
Type: Array of strings
Array Members: Minimum number of 0 items.
Length Constraints: Minimum length of 1. Maximum length of 100.
Required: No

## See Also
<a name="API_amazon-q-connect_GuardrailTopicConfig_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/qconnect-2020-10-19/GuardrailTopicConfig)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/qconnect-2020-10-19/GuardrailTopicConfig)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/qconnect-2020-10-19/GuardrailTopicConfig)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Connect Customer. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query connect` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
