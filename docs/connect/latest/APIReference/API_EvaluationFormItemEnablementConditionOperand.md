---
source_url: https://docs.aws.amazon.com/connect/latest/APIReference/API_EvaluationFormItemEnablementConditionOperand.html
---

# EvaluationFormItemEnablementConditionOperand
<a name="API_EvaluationFormItemEnablementConditionOperand"></a>

An operand of the enablement condition.

## Contents
<a name="API_EvaluationFormItemEnablementConditionOperand_Contents"></a>

**Important**
This data type is a UNION, so only one of the following members can be specified when used or returned.

 ** Condition **   <a name="connect-Type-EvaluationFormItemEnablementConditionOperand-Condition"></a>
A condition for item enablement.
Type: [EvaluationFormItemEnablementCondition](API_EvaluationFormItemEnablementCondition.md) object
Required: No

 ** Expression **   <a name="connect-Type-EvaluationFormItemEnablementConditionOperand-Expression"></a>
An expression of the enablement condition.
Type: [EvaluationFormItemEnablementExpression](API_EvaluationFormItemEnablementExpression.md) object
Required: No

## See Also
<a name="API_EvaluationFormItemEnablementConditionOperand_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/connect-2017-08-08/EvaluationFormItemEnablementConditionOperand)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/connect-2017-08-08/EvaluationFormItemEnablementConditionOperand)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/connect-2017-08-08/EvaluationFormItemEnablementConditionOperand)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Connect Customer. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query connect` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
