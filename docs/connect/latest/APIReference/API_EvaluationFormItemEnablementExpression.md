---
source_url: https://docs.aws.amazon.com/connect/latest/APIReference/API_EvaluationFormItemEnablementExpression.html
---

# EvaluationFormItemEnablementExpression

An expression that defines a basic building block of conditional enablement.

## Contents
<a name="API_EvaluationFormItemEnablementExpression_Contents"></a>

 ** Comparator **   <a name="connect-Type-EvaluationFormItemEnablementExpression-Comparator"></a>
A comparator to be used against a list of values. `IN`, `NOT_IN`, `ALL_IN`, and `EXACT` compare sets of values. `GREATER_THAN`, `LESS_THAN`, `GREATER_THAN_OR_EQUAL_TO`, and `LESS_THAN_OR_EQUAL_TO` compare a single numeric or date and time value. `EQUAL_TO` and `NOT_EQUAL_TO` compare a single value.
Type: String
Valid Values: `IN | NOT_IN | ALL_IN | EXACT | GREATER_THAN | LESS_THAN | GREATER_THAN_OR_EQUAL_TO | LESS_THAN_OR_EQUAL_TO | EQUAL_TO | NOT_EQUAL_TO`
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
