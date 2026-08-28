---
source_url: https://docs.aws.amazon.com/bedrock/latest/APIReference/API_GuardrailContentPolicyConfig.html
---

# GuardrailContentPolicyConfig
<a name="API_GuardrailContentPolicyConfig"></a>

Contains details about how to handle harmful content.

## Contents
<a name="API_GuardrailContentPolicyConfig_Contents"></a>

 ** filtersConfig **   <a name="bedrock-Type-GuardrailContentPolicyConfig-filtersConfig"></a>
Contains the type of the content filter and how strongly it should apply to prompts and model responses.
Type: Array of [GuardrailContentFilterConfig](API_GuardrailContentFilterConfig.md) objects
Array Members: Minimum number of 1 item. Maximum number of 6 items.
Required: Yes

 ** tierConfig **   <a name="bedrock-Type-GuardrailContentPolicyConfig-tierConfig"></a>
The tier that your guardrail uses for content filters.
Type: [GuardrailContentFiltersTierConfig](API_GuardrailContentFiltersTierConfig.md) object
Required: No

## See Also
<a name="API_GuardrailContentPolicyConfig_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-2023-04-20/GuardrailContentPolicyConfig)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-2023-04-20/GuardrailContentPolicyConfig)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-2023-04-20/GuardrailContentPolicyConfig)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Bedrock. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query bedrock` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
