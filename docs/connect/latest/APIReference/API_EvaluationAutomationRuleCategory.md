---
source_url: https://docs.aws.amazon.com/connect/latest/APIReference/API_EvaluationAutomationRuleCategory.html
---

# EvaluationAutomationRuleCategory
<a name="API_EvaluationAutomationRuleCategory"></a>

The Contact Lens category used by evaluation automation.

## Contents
<a name="API_EvaluationAutomationRuleCategory_Contents"></a>

 ** Category **   <a name="connect-Type-EvaluationAutomationRuleCategory-Category"></a>
A category label.
Type: String
Required: Yes

 ** Condition **   <a name="connect-Type-EvaluationAutomationRuleCategory-Condition"></a>
An automation condition for a Contact Lens category.
Type: String
Valid Values: `PRESENT | NOT_PRESENT`
Required: Yes

 ** PointsOfInterest **   <a name="connect-Type-EvaluationAutomationRuleCategory-PointsOfInterest"></a>
A point of interest in a contact transcript that indicates match of condition.
Type: Array of [EvaluationTranscriptPointOfInterest](API_EvaluationTranscriptPointOfInterest.md) objects
Array Members: Minimum number of 0 items. Maximum number of 100 items.
Required: No

## See Also
<a name="API_EvaluationAutomationRuleCategory_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/connect-2017-08-08/EvaluationAutomationRuleCategory)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/connect-2017-08-08/EvaluationAutomationRuleCategory)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/connect-2017-08-08/EvaluationAutomationRuleCategory)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Connect Customer. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query connect` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
