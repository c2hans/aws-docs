---
source_url: https://docs.aws.amazon.com/sesmailmanager/latest/APIReference/API_RuleNumberExpression.html
---

# RuleNumberExpression
<a name="API_RuleNumberExpression"></a>

A number expression to match numeric conditions with integers from the incoming email.

## Contents
<a name="API_RuleNumberExpression_Contents"></a>

 ** Evaluate **   <a name="sesmailmanager-Type-RuleNumberExpression-Evaluate"></a>
The number to evaluate in a numeric condition expression.
Type: [RuleNumberToEvaluate](API_RuleNumberToEvaluate.md) object
 **Note: **This object is a Union. Only one member of this object can be specified or returned.
Required: Yes

 ** Operator **   <a name="sesmailmanager-Type-RuleNumberExpression-Operator"></a>
The operator for a numeric condition expression.
Type: String
Valid Values: `EQUALS | NOT_EQUALS | LESS_THAN | GREATER_THAN | LESS_THAN_OR_EQUAL | GREATER_THAN_OR_EQUAL`
Required: Yes

 ** Value **   <a name="sesmailmanager-Type-RuleNumberExpression-Value"></a>
The value to evaluate in a numeric condition expression.
Type: Double
Required: Yes

## See Also
<a name="API_RuleNumberExpression_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/mailmanager-2023-10-17/RuleNumberExpression)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/mailmanager-2023-10-17/RuleNumberExpression)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/mailmanager-2023-10-17/RuleNumberExpression)
