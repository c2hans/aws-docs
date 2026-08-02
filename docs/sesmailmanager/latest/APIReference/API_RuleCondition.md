---
source_url: https://docs.aws.amazon.com/sesmailmanager/latest/APIReference/API_RuleCondition.html
---

# RuleCondition
<a name="API_RuleCondition"></a>

The conditional expression used to evaluate an email for determining if a rule action should be taken.

## Contents
<a name="API_RuleCondition_Contents"></a>

**Important**
This data type is a UNION, so only one of the following members can be specified when used or returned.

 ** BooleanExpression **   <a name="sesmailmanager-Type-RuleCondition-BooleanExpression"></a>
The condition applies to a boolean expression passed in this field.
Type: [RuleBooleanExpression](API_RuleBooleanExpression.md) object
Required: No

 ** DmarcExpression **   <a name="sesmailmanager-Type-RuleCondition-DmarcExpression"></a>
The condition applies to a DMARC policy expression passed in this field.
Type: [RuleDmarcExpression](API_RuleDmarcExpression.md) object
Required: No

 ** IpExpression **   <a name="sesmailmanager-Type-RuleCondition-IpExpression"></a>
The condition applies to an IP address expression passed in this field.
Type: [RuleIpExpression](API_RuleIpExpression.md) object
Required: No

 ** NumberExpression **   <a name="sesmailmanager-Type-RuleCondition-NumberExpression"></a>
The condition applies to a number expression passed in this field.
Type: [RuleNumberExpression](API_RuleNumberExpression.md) object
Required: No

 ** StringExpression **   <a name="sesmailmanager-Type-RuleCondition-StringExpression"></a>
The condition applies to a string expression passed in this field.
Type: [RuleStringExpression](API_RuleStringExpression.md) object
Required: No

 ** VerdictExpression **   <a name="sesmailmanager-Type-RuleCondition-VerdictExpression"></a>
The condition applies to a verdict expression passed in this field.
Type: [RuleVerdictExpression](API_RuleVerdictExpression.md) object
Required: No

## See Also
<a name="API_RuleCondition_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/mailmanager-2023-10-17/RuleCondition)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/mailmanager-2023-10-17/RuleCondition)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/mailmanager-2023-10-17/RuleCondition)
