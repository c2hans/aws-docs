---
source_url: https://docs.aws.amazon.com/sesmailmanager/latest/APIReference/API_RuleStringExpression.html
---

# RuleStringExpression
<a name="API_RuleStringExpression"></a>

A string expression is evaluated against strings or substrings of the email.

## Contents
<a name="API_RuleStringExpression_Contents"></a>

 ** Evaluate **   <a name="sesmailmanager-Type-RuleStringExpression-Evaluate"></a>
The string to evaluate in a string condition expression.
Type: [RuleStringToEvaluate](API_RuleStringToEvaluate.md) object
 **Note: **This object is a Union. Only one member of this object can be specified or returned.
Required: Yes

 ** Operator **   <a name="sesmailmanager-Type-RuleStringExpression-Operator"></a>
The matching operator for a string condition expression.
Type: String
Valid Values: `EQUALS | NOT_EQUALS | STARTS_WITH | ENDS_WITH | CONTAINS`
Required: Yes

 ** Values **   <a name="sesmailmanager-Type-RuleStringExpression-Values"></a>
The string(s) to be evaluated in a string condition expression. For all operators, except for NOT\_EQUALS, if multiple values are given, the values are processed as an OR. That is, if any of the values match the email's string using the given operator, the condition is deemed to match. However, for NOT\_EQUALS, the condition is only deemed to match if none of the given strings match the email's string.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 10 items.
Length Constraints: Minimum length of 1. Maximum length of 4096.
Required: Yes

## See Also
<a name="API_RuleStringExpression_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/mailmanager-2023-10-17/RuleStringExpression)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/mailmanager-2023-10-17/RuleStringExpression)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/mailmanager-2023-10-17/RuleStringExpression)
