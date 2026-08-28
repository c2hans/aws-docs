---
source_url: https://docs.aws.amazon.com/bedrock/latest/APIReference/API_AutomatedReasoningPolicyDefinitionElement.html
---

# AutomatedReasoningPolicyDefinitionElement
<a name="API_AutomatedReasoningPolicyDefinitionElement"></a>

Represents a single element in an Automated Reasoning policy definition, such as a rule, variable, or type definition.

## Contents
<a name="API_AutomatedReasoningPolicyDefinitionElement_Contents"></a>

**Important**
This data type is a UNION, so only one of the following members can be specified when used or returned.

 ** policyDefinitionRule **   <a name="bedrock-Type-AutomatedReasoningPolicyDefinitionElement-policyDefinitionRule"></a>
A rule element within the policy definition that contains a formal logical expression used for validation.
Type: [AutomatedReasoningPolicyDefinitionRule](API_AutomatedReasoningPolicyDefinitionRule.md) object
Required: No

 ** policyDefinitionType **   <a name="bedrock-Type-AutomatedReasoningPolicyDefinitionElement-policyDefinitionType"></a>
A custom type element within the policy definition that defines a set of possible values for variables.
Type: [AutomatedReasoningPolicyDefinitionType](API_AutomatedReasoningPolicyDefinitionType.md) object
Required: No

 ** policyDefinitionVariable **   <a name="bedrock-Type-AutomatedReasoningPolicyDefinitionElement-policyDefinitionVariable"></a>
A variable element within the policy definition that represents a concept used in logical expressions and rules.
Type: [AutomatedReasoningPolicyDefinitionVariable](API_AutomatedReasoningPolicyDefinitionVariable.md) object
Required: No

## See Also
<a name="API_AutomatedReasoningPolicyDefinitionElement_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-2023-04-20/AutomatedReasoningPolicyDefinitionElement)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-2023-04-20/AutomatedReasoningPolicyDefinitionElement)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-2023-04-20/AutomatedReasoningPolicyDefinitionElement)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Bedrock. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query bedrock` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
