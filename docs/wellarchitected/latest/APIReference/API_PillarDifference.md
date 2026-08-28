---
source_url: https://docs.aws.amazon.com/wellarchitected/latest/APIReference/API_PillarDifference.html
---

# PillarDifference
<a name="API_PillarDifference"></a>

A pillar difference return object.

## Contents
<a name="API_PillarDifference_Contents"></a>

 ** DifferenceStatus **   <a name="wellarchitected-Type-PillarDifference-DifferenceStatus"></a>
Indicates the type of change to the pillar.
Type: String
Valid Values: `UPDATED | NEW | DELETED`
Required: No

 ** PillarId **   <a name="wellarchitected-Type-PillarDifference-PillarId"></a>
The ID used to identify a pillar, for example, `security`.
A pillar is identified by its [PillarReviewSummary:PillarId](API_PillarReviewSummary.md#wellarchitected-Type-PillarReviewSummary-PillarId).
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Required: No

 ** PillarName **   <a name="wellarchitected-Type-PillarDifference-PillarName"></a>
The name of the pillar.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Required: No

 ** QuestionDifferences **   <a name="wellarchitected-Type-PillarDifference-QuestionDifferences"></a>
List of question differences.
Type: Array of [QuestionDifference](API_QuestionDifference.md) objects
Required: No

## See Also
<a name="API_PillarDifference_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/wellarchitected-2020-03-31/PillarDifference)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/wellarchitected-2020-03-31/PillarDifference)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/wellarchitected-2020-03-31/PillarDifference)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Well-Architected Tool. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query wellarchitected` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
