---
source_url: https://docs.aws.amazon.com/pinpoint/latest/apireference_smsvoicev2/API_FieldCondition.html
---

# FieldCondition
<a name="API_FieldCondition"></a>

A single condition on a dependency field's value. Conditions are combined into a **ConditionalRule** and evaluated together with logical AND.

## Contents
<a name="API_FieldCondition_Contents"></a>

 ** DependsOnFieldPath **   <a name="pinpoint-Type-FieldCondition-DependsOnFieldPath"></a>
The path of the field whose value determines this condition, for example **companyInfo.businessType**.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Pattern: `[A-Za-z0-9_\.]+`
Required: Yes

 ** Operator **   <a name="pinpoint-Type-FieldCondition-Operator"></a>
The comparison operator to apply between the dependency field's value and **Values**. Valid values are **EQUALS**, **NOT\_EQUALS**, **IN**, **NOT\_IN**, **HAS\_VALUE**, and **NO\_VALUE**. Operators not in this list are treated as evaluating to false, which causes the containing rule to be skipped. This allows forward-compatible additions of new operators without breaking older SDK clients.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[A-Za-z0-9_]+`
Required: Yes

 ** Values **   <a name="pinpoint-Type-FieldCondition-Values"></a>
The values to compare the dependency field's value against. Required for the **EQUALS**, **NOT\_EQUALS**, **IN**, and **NOT\_IN** operators. Omitted for **HAS\_VALUE** and **NO\_VALUE**, which test only presence.
Type: Array of strings
Array Members: Minimum number of 0 items. Maximum number of 20 items.
Length Constraints: Minimum length of 1. Maximum length of 256.
Required: No

## See Also
<a name="API_FieldCondition_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/pinpoint-sms-voice-v2-2022-03-31/FieldCondition)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/pinpoint-sms-voice-v2-2022-03-31/FieldCondition)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/pinpoint-sms-voice-v2-2022-03-31/FieldCondition)
