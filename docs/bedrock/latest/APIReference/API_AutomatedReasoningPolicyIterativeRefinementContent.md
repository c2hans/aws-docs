---
source_url: https://docs.aws.amazon.com/bedrock/latest/APIReference/API_AutomatedReasoningPolicyIterativeRefinementContent.html
---

# AutomatedReasoningPolicyIterativeRefinementContent
<a name="API_AutomatedReasoningPolicyIterativeRefinementContent"></a>

Configuration for an iterative policy refinement workflow, including source documents to process and optional feedback to guide the refinement.

## Contents
<a name="API_AutomatedReasoningPolicyIterativeRefinementContent_Contents"></a>

 ** documents **   <a name="bedrock-Type-AutomatedReasoningPolicyIterativeRefinementContent-documents"></a>
Source documents used for iterative policy refinement. These documents provide context for refining the policy definition.
Type: Array of [AutomatedReasoningPolicyBuildWorkflowDocument](API_AutomatedReasoningPolicyBuildWorkflowDocument.md) objects
Array Members: Minimum number of 1 item. Maximum number of 5 items.
Required: Yes

 ** feedback **   <a name="bedrock-Type-AutomatedReasoningPolicyIterativeRefinementContent-feedback"></a>
Optional feedback to guide the iterative refinement workflow. Provide specific instructions or constraints for policy refinement.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 4000.
Required: No

## See Also
<a name="API_AutomatedReasoningPolicyIterativeRefinementContent_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-2023-04-20/AutomatedReasoningPolicyIterativeRefinementContent)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-2023-04-20/AutomatedReasoningPolicyIterativeRefinementContent)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-2023-04-20/AutomatedReasoningPolicyIterativeRefinementContent)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Bedrock. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query bedrock` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
