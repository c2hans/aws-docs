---
source_url: https://docs.aws.amazon.com/resilience-hub/v2/APIReference/API_TestRunSourceSummary.html
---

# TestRunSourceSummary
<a name="API_TestRunSourceSummary"></a>

A monitoring-source snapshot captured for a test run. Exactly one member is set.

## Contents
<a name="API_TestRunSourceSummary_Contents"></a>

**Important**
This data type is a UNION, so only one of the following members can be specified when used or returned.

 ** observabilityAlarm **   <a name="ngresiliencehub-Type-TestRunSourceSummary-observabilityAlarm"></a>
An observability alarm snapshot captured for the test run.
Type: [TestRunObservabilityAlarmSummary](API_TestRunObservabilityAlarmSummary.md) object
Required: No

 ** successCriteriaAlarm **   <a name="ngresiliencehub-Type-TestRunSourceSummary-successCriteriaAlarm"></a>
A success criteria alarm snapshot captured for the test run.
Type: [TestRunSuccessCriteriaAlarmSummary](API_TestRunSuccessCriteriaAlarmSummary.md) object
Required: No

## See Also
<a name="API_TestRunSourceSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/resiliencehubv2-2026-02-17/TestRunSourceSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/resiliencehubv2-2026-02-17/TestRunSourceSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/resiliencehubv2-2026-02-17/TestRunSourceSummary)
