---
source_url: https://docs.aws.amazon.com/wellarchitected/latest/APIReference/API_ChoiceAnswer.html
---

# ChoiceAnswer
<a name="API_ChoiceAnswer"></a>

A choice that has been answered on a question in your workload.

## Contents
<a name="API_ChoiceAnswer_Contents"></a>

 ** ChoiceId **   <a name="wellarchitected-Type-ChoiceAnswer-ChoiceId"></a>
The ID of a choice.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Required: No

 ** Notes **   <a name="wellarchitected-Type-ChoiceAnswer-Notes"></a>
The notes associated with a choice.
Type: String
Length Constraints: Maximum length of 250.
Required: No

 ** Reason **   <a name="wellarchitected-Type-ChoiceAnswer-Reason"></a>
The reason why a choice is non-applicable to a question in your workload.
Type: String
Valid Values: `OUT_OF_SCOPE | BUSINESS_PRIORITIES | ARCHITECTURE_CONSTRAINTS | OTHER | NONE`
Required: No

 ** Status **   <a name="wellarchitected-Type-ChoiceAnswer-Status"></a>
The status of a choice.
Type: String
Valid Values: `SELECTED | NOT_APPLICABLE | UNSELECTED`
Required: No

## See Also
<a name="API_ChoiceAnswer_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/wellarchitected-2020-03-31/ChoiceAnswer)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/wellarchitected-2020-03-31/ChoiceAnswer)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/wellarchitected-2020-03-31/ChoiceAnswer)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Well-Architected Tool. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query wellarchitected` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
