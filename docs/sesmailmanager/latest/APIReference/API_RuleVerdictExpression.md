---
source_url: https://docs.aws.amazon.com/sesmailmanager/latest/APIReference/API_RuleVerdictExpression.html
---

# RuleVerdictExpression
<a name="API_RuleVerdictExpression"></a>

A verdict expression is evaluated against verdicts of the email.

## Contents
<a name="API_RuleVerdictExpression_Contents"></a>

 ** Evaluate **   <a name="sesmailmanager-Type-RuleVerdictExpression-Evaluate"></a>
The verdict to evaluate in a verdict condition expression.
Type: [RuleVerdictToEvaluate](API_RuleVerdictToEvaluate.md) object
 **Note: **This object is a Union. Only one member of this object can be specified or returned.
Required: Yes

 ** Operator **   <a name="sesmailmanager-Type-RuleVerdictExpression-Operator"></a>
The matching operator for a verdict condition expression.
Type: String
Valid Values: `EQUALS | NOT_EQUALS`
Required: Yes

 ** Values **   <a name="sesmailmanager-Type-RuleVerdictExpression-Values"></a>
The values to match with the email's verdict using the given operator. For the EQUALS operator, if multiple values are given, the condition is deemed to match if any of the given verdicts match that of the email. For the NOT\_EQUALS operator, if multiple values are given, the condition is deemed to match of none of the given verdicts match the verdict of the email.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 10 items.
Valid Values: `PASS | FAIL | GRAY | PROCESSING_FAILED`
Required: Yes

## See Also
<a name="API_RuleVerdictExpression_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/mailmanager-2023-10-17/RuleVerdictExpression)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/mailmanager-2023-10-17/RuleVerdictExpression)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/mailmanager-2023-10-17/RuleVerdictExpression)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon SES Mail Manager. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query sesmailmanager` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
