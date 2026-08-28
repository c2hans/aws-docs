---
source_url: https://docs.aws.amazon.com/bedrock/latest/APIReference/API_AutomatedReasoningCheckValidFinding.html
---

# AutomatedReasoningCheckValidFinding
<a name="API_AutomatedReasoningCheckValidFinding"></a>

Indicates that the claims are definitively true and logically implied by the premises, with no possible alternative interpretations.

## Contents
<a name="API_AutomatedReasoningCheckValidFinding_Contents"></a>

 ** claimsTrueScenario **   <a name="bedrock-Type-AutomatedReasoningCheckValidFinding-claimsTrueScenario"></a>
An example scenario demonstrating how the claims are logically true.
Type: [AutomatedReasoningCheckScenario](API_AutomatedReasoningCheckScenario.md) object
Required: No

 ** logicWarning **   <a name="bedrock-Type-AutomatedReasoningCheckValidFinding-logicWarning"></a>
Indication of a logic issue with the translation without needing to consider the automated reasoning policy rules.
Type: [AutomatedReasoningCheckLogicWarning](API_AutomatedReasoningCheckLogicWarning.md) object
Required: No

 ** supportingRules **   <a name="bedrock-Type-AutomatedReasoningCheckValidFinding-supportingRules"></a>
The automated reasoning policy rules that support why this result is considered valid.
Type: Array of [AutomatedReasoningCheckRule](API_AutomatedReasoningCheckRule.md) objects
Required: No

 ** translation **   <a name="bedrock-Type-AutomatedReasoningCheckValidFinding-translation"></a>
The logical translation of the input that this finding validates.
Type: [AutomatedReasoningCheckTranslation](API_AutomatedReasoningCheckTranslation.md) object
Required: No

## See Also
<a name="API_AutomatedReasoningCheckValidFinding_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-2023-04-20/AutomatedReasoningCheckValidFinding)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-2023-04-20/AutomatedReasoningCheckValidFinding)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-2023-04-20/AutomatedReasoningCheckValidFinding)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Bedrock. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query bedrock` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
