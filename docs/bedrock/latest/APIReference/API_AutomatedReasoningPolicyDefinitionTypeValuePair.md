---
source_url: https://docs.aws.amazon.com/bedrock/latest/APIReference/API_AutomatedReasoningPolicyDefinitionTypeValuePair.html
---

# AutomatedReasoningPolicyDefinitionTypeValuePair
<a name="API_AutomatedReasoningPolicyDefinitionTypeValuePair"></a>

Associates a type name with a specific value name, used for referencing type values in rules and other policy elements.

## Contents
<a name="API_AutomatedReasoningPolicyDefinitionTypeValuePair_Contents"></a>

 ** typeName **   <a name="bedrock-Type-AutomatedReasoningPolicyDefinitionTypeValuePair-typeName"></a>
The name of the custom type that contains the referenced value.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[A-Za-z][A-Za-z0-9_]*`
Required: Yes

 ** valueName **   <a name="bedrock-Type-AutomatedReasoningPolicyDefinitionTypeValuePair-valueName"></a>
The name of the specific value within the type.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[A-Za-z][A-Za-z0-9_]*`
Required: Yes

## See Also
<a name="API_AutomatedReasoningPolicyDefinitionTypeValuePair_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-2023-04-20/AutomatedReasoningPolicyDefinitionTypeValuePair)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-2023-04-20/AutomatedReasoningPolicyDefinitionTypeValuePair)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-2023-04-20/AutomatedReasoningPolicyDefinitionTypeValuePair)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Bedrock. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query bedrock` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
