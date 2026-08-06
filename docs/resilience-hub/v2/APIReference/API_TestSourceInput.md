---
source_url: https://docs.aws.amazon.com/resilience-hub/v2/APIReference/API_TestSourceInput.html
---

# TestSourceInput
<a name="API_TestSourceInput"></a>

Identifies a monitoring source to add to or remove from a test. Exactly one member is set.

## Contents
<a name="API_TestSourceInput_Contents"></a>

**Important**
This data type is a UNION, so only one of the following members can be specified when used or returned.

 ** observabilityAlarm **   <a name="ngresiliencehub-Type-TestSourceInput-observabilityAlarm"></a>
An observability alarm included for visibility only.
Type: [ObservabilityAlarmInput](API_ObservabilityAlarmInput.md) object
Required: No

 ** successCriteriaAlarm **   <a name="ngresiliencehub-Type-TestSourceInput-successCriteriaAlarm"></a>
A success criteria alarm that determines whether the test passes or fails.
Type: [SuccessCriteriaAlarmInput](API_SuccessCriteriaAlarmInput.md) object
Required: No

## See Also
<a name="API_TestSourceInput_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/resiliencehubv2-2026-02-17/TestSourceInput)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/resiliencehubv2-2026-02-17/TestSourceInput)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/resiliencehubv2-2026-02-17/TestSourceInput)
