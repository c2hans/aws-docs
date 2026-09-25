---
source_url: https://docs.aws.amazon.com/cloudwatch-omni/latest/APIReference/API_NotificationTrigger.html
---

# NotificationTrigger
<a name="API_NotificationTrigger"></a>

Trigger conditions for a notification rule. `stateValues` entries combine with OR semantics; empty / omitted = any state.

## Contents
<a name="API_NotificationTrigger_Contents"></a>

 ** stateValues **   <a name="cloudwatchomni-Type-NotificationTrigger-stateValues"></a>
Alert state(s) that trigger this rule. Empty / omitted = any state.
Type: Array of strings
Array Members: Minimum number of 0 items. Maximum number of 4 items.
Valid Values: `OK | WARNING | CRITICAL | NODATA`
Required: No

## See Also
<a name="API_NotificationTrigger_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/cloudwatchomni-2025-01-01/NotificationTrigger)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cloudwatchomni-2025-01-01/NotificationTrigger)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cloudwatchomni-2025-01-01/NotificationTrigger)
