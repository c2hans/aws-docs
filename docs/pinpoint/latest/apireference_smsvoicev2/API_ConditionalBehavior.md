---
source_url: https://docs.aws.amazon.com/pinpoint/latest/apireference_smsvoicev2/API_ConditionalBehavior.html
---

# ConditionalBehavior
<a name="API_ConditionalBehavior"></a>

The set of conditional rules that determine a field's resolved requirement based on the values of other fields in the same registration form. Attached to fields whose **FieldRequirement** is **CONDITIONAL**.

Evaluation proceeds top-to-bottom through **Rules**. The first rule whose conditions all evaluate to true wins and its behavior is returned. If no rule matches, the **DefaultBehavior** is returned.

## Contents
<a name="API_ConditionalBehavior_Contents"></a>

 ** DefaultBehavior **   <a name="pinpoint-Type-ConditionalBehavior-DefaultBehavior"></a>
The field behavior that applies when no conditional rule in **Rules** matches. Valid values are **REQUIRED**, **OPTIONAL**, and **DISALLOWED**.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[A-Za-z0-9_]+`
Required: Yes

 ** Rules **   <a name="pinpoint-Type-ConditionalBehavior-Rules"></a>
An ordered list of conditional rules. Rules are evaluated top-to-bottom and the first rule whose conditions all evaluate to true determines the field's behavior. Rules whose conditions do not all match are skipped and evaluation continues to the next rule.
Type: Array of [ConditionalRule](API_ConditionalRule.md) objects
Array Members: Minimum number of 1 item. Maximum number of 20 items.
Required: Yes

## See Also
<a name="API_ConditionalBehavior_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/pinpoint-sms-voice-v2-2022-03-31/ConditionalBehavior)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/pinpoint-sms-voice-v2-2022-03-31/ConditionalBehavior)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/pinpoint-sms-voice-v2-2022-03-31/ConditionalBehavior)
