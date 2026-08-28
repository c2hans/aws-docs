---
source_url: https://docs.aws.amazon.com/sesmailmanager/latest/APIReference/API_RuleBooleanExpression.html
---

# RuleBooleanExpression
<a name="API_RuleBooleanExpression"></a>

A boolean expression to be used in a rule condition.

## Contents
<a name="API_RuleBooleanExpression_Contents"></a>

 ** Evaluate **   <a name="sesmailmanager-Type-RuleBooleanExpression-Evaluate"></a>
The operand on which to perform a boolean condition operation.
Type: [RuleBooleanToEvaluate](API_RuleBooleanToEvaluate.md) object
 **Note: **This object is a Union. Only one member of this object can be specified or returned.
Required: Yes

 ** Operator **   <a name="sesmailmanager-Type-RuleBooleanExpression-Operator"></a>
The matching operator for a boolean condition expression.
Type: String
Valid Values: `IS_TRUE | IS_FALSE`
Required: Yes

## See Also
<a name="API_RuleBooleanExpression_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/mailmanager-2023-10-17/RuleBooleanExpression)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/mailmanager-2023-10-17/RuleBooleanExpression)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/mailmanager-2023-10-17/RuleBooleanExpression)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon SES Mail Manager. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query sesmailmanager` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
