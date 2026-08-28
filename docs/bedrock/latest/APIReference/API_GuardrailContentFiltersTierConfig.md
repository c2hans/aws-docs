---
source_url: https://docs.aws.amazon.com/bedrock/latest/APIReference/API_GuardrailContentFiltersTierConfig.html
---

# GuardrailContentFiltersTierConfig
<a name="API_GuardrailContentFiltersTierConfig"></a>

The tier that your guardrail uses for content filters. Consider using a tier that balances performance, accuracy, and compatibility with your existing generative AI workflows.

## Contents
<a name="API_GuardrailContentFiltersTierConfig_Contents"></a>

 ** tierName **   <a name="bedrock-Type-GuardrailContentFiltersTierConfig-tierName"></a>
The tier that your guardrail uses for content filters. Valid values include:
+  `CLASSIC` tier – Provides established guardrails functionality supporting English, French, and Spanish languages.
+  `STANDARD` tier – Provides a more robust solution than the `CLASSIC` tier and has more comprehensive language support. This tier requires that your guardrail use [cross-Region inference](https://docs.aws.amazon.com/bedrock/latest/userguide/guardrails-cross-region.html).
Type: String
Valid Values: `CLASSIC | STANDARD`
Required: Yes

## See Also
<a name="API_GuardrailContentFiltersTierConfig_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-2023-04-20/GuardrailContentFiltersTierConfig)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-2023-04-20/GuardrailContentFiltersTierConfig)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-2023-04-20/GuardrailContentFiltersTierConfig)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Bedrock. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query bedrock` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
