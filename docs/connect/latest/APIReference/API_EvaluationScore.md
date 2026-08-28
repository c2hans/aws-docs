---
source_url: https://docs.aws.amazon.com/connect/latest/APIReference/API_EvaluationScore.html
---

# EvaluationScore
<a name="API_EvaluationScore"></a>

Information about scores of a contact evaluation item (section or question).

## Contents
<a name="API_EvaluationScore_Contents"></a>

 ** AppliedWeight **   <a name="connect-Type-EvaluationScore-AppliedWeight"></a>
Weight applied to this evaluation score.
Type: Double
Required: No

 ** AutomaticFail **   <a name="connect-Type-EvaluationScore-AutomaticFail"></a>
The flag that marks the item as automatic fail. If the item or a child item gets an automatic fail answer, this flag will be true.
Type: Boolean
Required: No

 ** EarnedPoints **   <a name="connect-Type-EvaluationScore-EarnedPoints"></a>
The points earned for the item.
Type: Integer
Required: No

 ** MaxBasePoint **   <a name="connect-Type-EvaluationScore-MaxBasePoint"></a>
The maximum base points possible for the item.
Type: Integer
Required: No

 ** NotApplicable **   <a name="connect-Type-EvaluationScore-NotApplicable"></a>
The flag to mark the item as not applicable for scoring.
Type: Boolean
Required: No

 ** Percentage **   <a name="connect-Type-EvaluationScore-Percentage"></a>
The score percentage for an item in a contact evaluation.
Type: Double
Required: No

 ** PerformanceCategory **   <a name="connect-Type-EvaluationScore-PerformanceCategory"></a>
The performance category for the score.
Type: String
Valid Values: `NEEDS_IMPROVEMENT | EXCEEDS_EXPECTATIONS`
Required: No

## See Also
<a name="API_EvaluationScore_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/connect-2017-08-08/EvaluationScore)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/connect-2017-08-08/EvaluationScore)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/connect-2017-08-08/EvaluationScore)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Connect Customer. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query connect` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
