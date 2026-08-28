---
source_url: https://docs.aws.amazon.com/connect/latest/APIReference/API_EvaluationFormItemEnablementExpression.html
---

# EvaluationFormItemEnablementExpression
<a name="API_EvaluationFormItemEnablementExpression"></a>

An expression that defines a basic building block of conditional enablement.

## Contents
<a name="API_EvaluationFormItemEnablementExpression_Contents"></a>

 ** Comparator **   <a name="connect-Type-EvaluationFormItemEnablementExpression-Comparator"></a>
A comparator to be used against list of values.
Type: String
Valid Values: `IN | NOT_IN | ALL_IN | EXACT`
Required: Yes

 ** Source **   <a name="connect-Type-EvaluationFormItemEnablementExpression-Source"></a>
A source item of enablement expression.
Type: [EvaluationFormItemEnablementSource](API_EvaluationFormItemEnablementSource.md) object
Required: Yes

 ** Values **   <a name="connect-Type-EvaluationFormItemEnablementExpression-Values"></a>
A list of values from source item.
Type: Array of [EvaluationFormItemEnablementSourceValue](API_EvaluationFormItemEnablementSourceValue.md) objects
Required: Yes

## See Also
<a name="API_EvaluationFormItemEnablementExpression_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/connect-2017-08-08/EvaluationFormItemEnablementExpression)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/connect-2017-08-08/EvaluationFormItemEnablementExpression)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/connect-2017-08-08/EvaluationFormItemEnablementExpression)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Connect Customer. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query connect` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
