---
source_url: https://docs.aws.amazon.com/pinpoint/latest/apireference_smsvoicev2/API_ConditionalRule.html
---

# ConditionalRule
<a name="API_ConditionalRule"></a>

A single conditional rule that resolves to a field behavior when all of its conditions evaluate to true. Conditions within a rule are combined with logical AND: all conditions must match for the rule to fire.

## Contents
<a name="API_ConditionalRule_Contents"></a>

 ** Conditions **   <a name="pinpoint-Type-ConditionalRule-Conditions"></a>
The conditions that must all evaluate to true for this rule to match. Conditions are combined with logical AND. Use multiple rules with the same **RuleBehavior** to express logical OR.
Type: Array of [FieldCondition](API_FieldCondition.md) objects
Array Members: Minimum number of 1 item. Maximum number of 5 items.
Required: Yes

 ** RuleBehavior **   <a name="pinpoint-Type-ConditionalRule-RuleBehavior"></a>
The field behavior that applies when all conditions in this rule match. Valid values are **REQUIRED**, **OPTIONAL**, and **DISALLOWED**.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[A-Za-z0-9_]+`
Required: Yes

 ** ConditionalValidation **   <a name="pinpoint-Type-ConditionalRule-ConditionalValidation"></a>
Optional per-rule validation constraints (minimum length, maximum length, regex pattern, allowed select values) that override the field's default validation when this rule matches.
Type: [ConditionalValidation](API_ConditionalValidation.md) object
Required: No

## See Also
<a name="API_ConditionalRule_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/pinpoint-sms-voice-v2-2022-03-31/ConditionalRule)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/pinpoint-sms-voice-v2-2022-03-31/ConditionalRule)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/pinpoint-sms-voice-v2-2022-03-31/ConditionalRule)
