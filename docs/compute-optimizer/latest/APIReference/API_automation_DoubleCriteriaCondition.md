---
source_url: https://docs.aws.amazon.com/compute-optimizer/latest/APIReference/API_automation_DoubleCriteriaCondition.html
---

# DoubleCriteriaCondition
<a name="API_automation_DoubleCriteriaCondition"></a>

Defines a condition for filtering based on double/floating-point numeric values with comparison operators.

## Contents
<a name="API_automation_DoubleCriteriaCondition_Contents"></a>

 ** comparison **   <a name="computeoptimizer-Type-automation_DoubleCriteriaCondition-comparison"></a>
The comparison operator to use, such as equals, greater than, less than, etc.
Type: String
Valid Values: `StringEquals | StringNotEquals | StringEqualsIgnoreCase | StringNotEqualsIgnoreCase | StringLike | StringNotLike | NumericEquals | NumericNotEquals | NumericLessThan | NumericLessThanEquals | NumericGreaterThan | NumericGreaterThanEquals`
Required: No

 ** values **   <a name="computeoptimizer-Type-automation_DoubleCriteriaCondition-values"></a>
The list of double values to compare against using the specified comparison operator.
Type: Array of doubles
Required: No

## See Also
<a name="API_automation_DoubleCriteriaCondition_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/compute-optimizer-automation-2025-09-22/DoubleCriteriaCondition)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/compute-optimizer-automation-2025-09-22/DoubleCriteriaCondition)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/compute-optimizer-automation-2025-09-22/DoubleCriteriaCondition)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Compute Optimizer. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query compute-optimizer` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
