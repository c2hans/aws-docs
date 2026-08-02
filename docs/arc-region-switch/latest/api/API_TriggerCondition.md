---
source_url: https://docs.aws.amazon.com/arc-region-switch/latest/api/API_TriggerCondition.html
---

# TriggerCondition
<a name="API_TriggerCondition"></a>

Defines a condition that must be met for a trigger to fire.

## Contents
<a name="API_TriggerCondition_Contents"></a>

 ** associatedAlarmName **   <a name="regionswitch-Type-TriggerCondition-associatedAlarmName"></a>
The name of the CloudWatch alarm associated with the condition.
Type: String
Required: Yes

 ** condition **   <a name="regionswitch-Type-TriggerCondition-condition"></a>
The condition that must be met. Valid values include `green` and `red`.
Type: String
Valid Values: `red | green`
Required: Yes

## See Also
<a name="API_TriggerCondition_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/arc-region-switch-2022-07-26/TriggerCondition)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/arc-region-switch-2022-07-26/TriggerCondition)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/arc-region-switch-2022-07-26/TriggerCondition)
