---
source_url: https://docs.aws.amazon.com/bedrock/latest/APIReference/API_AutomatedReasoningCheckTranslationAmbiguousFinding.html
---

# AutomatedReasoningCheckTranslationAmbiguousFinding
<a name="API_AutomatedReasoningCheckTranslationAmbiguousFinding"></a>

Indicates that the input has multiple valid logical interpretations, requiring additional context or clarification.

## Contents
<a name="API_AutomatedReasoningCheckTranslationAmbiguousFinding_Contents"></a>

 ** differenceScenarios **   <a name="bedrock-Type-AutomatedReasoningCheckTranslationAmbiguousFinding-differenceScenarios"></a>
Scenarios showing how the different translation options differ in meaning.
Type: Array of [AutomatedReasoningCheckScenario](API_AutomatedReasoningCheckScenario.md) objects
Array Members: Minimum number of 0 items. Maximum number of 2 items.
Required: No

 ** options **   <a name="bedrock-Type-AutomatedReasoningCheckTranslationAmbiguousFinding-options"></a>
Different logical interpretations that were detected during translation of the input.
Type: Array of [AutomatedReasoningCheckTranslationOption](API_AutomatedReasoningCheckTranslationOption.md) objects
Array Members: Minimum number of 0 items. Maximum number of 2 items.
Required: No

## See Also
<a name="API_AutomatedReasoningCheckTranslationAmbiguousFinding_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-2023-04-20/AutomatedReasoningCheckTranslationAmbiguousFinding)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-2023-04-20/AutomatedReasoningCheckTranslationAmbiguousFinding)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-2023-04-20/AutomatedReasoningCheckTranslationAmbiguousFinding)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Bedrock. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query bedrock` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
