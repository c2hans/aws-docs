---
source_url: https://docs.aws.amazon.com/bedrock/latest/APIReference/API_AutomatedReasoningPolicyAddRuleAnnotation.html
---

# AutomatedReasoningPolicyAddRuleAnnotation
<a name="API_AutomatedReasoningPolicyAddRuleAnnotation"></a>

An annotation for adding a new rule to an Automated Reasoning policy using a formal logical expression.

## Contents
<a name="API_AutomatedReasoningPolicyAddRuleAnnotation_Contents"></a>

 ** expression **   <a name="bedrock-Type-AutomatedReasoningPolicyAddRuleAnnotation-expression"></a>
The formal logical expression that defines the rule, using mathematical notation and referencing policy variables and types.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 2048.
Pattern: `[\s\S]+`
Required: Yes

## See Also
<a name="API_AutomatedReasoningPolicyAddRuleAnnotation_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-2023-04-20/AutomatedReasoningPolicyAddRuleAnnotation)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-2023-04-20/AutomatedReasoningPolicyAddRuleAnnotation)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-2023-04-20/AutomatedReasoningPolicyAddRuleAnnotation)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Bedrock. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query bedrock` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
