---
source_url: https://docs.aws.amazon.com/cloudwatch-omni/latest/APIReference/API_AlertCondition.html
---

# AlertCondition
<a name="API_AlertCondition"></a>

The condition that determines when the alert fires.

On UpdateAlert a supplied condition is replaced whole, not merged: an omitted `warningThreshold` or `criticalThreshold` removes that tier, and an omitted `thresholdField` clears it. A condition must keep at least one tier. `thresholdMode` and `comparator` are optional at the Smithy level (so a single-tier condition is expressible) but are required whenever a threshold is present; enforced by the service-side validator.

## Contents
<a name="API_AlertCondition_Contents"></a>

 ** comparator **   <a name="cloudwatchomni-Type-AlertCondition-comparator"></a>
The comparison operator applied to the threshold.
Type: String
Valid Values: `GT | LT | GTE | LTE`
Required: No

 ** criticalThreshold **   <a name="cloudwatchomni-Type-AlertCondition-criticalThreshold"></a>
The value at which the alert enters the CRITICAL state.
Type: Double
Required: No

 ** thresholdField **   <a name="cloudwatchomni-Type-AlertCondition-thresholdField"></a>
The field the threshold is evaluated against.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 256.
Required: No

 ** thresholdMode **   <a name="cloudwatchomni-Type-AlertCondition-thresholdMode"></a>
How the threshold is applied to query results.
Type: String
Valid Values: `COUNT_OF_RESULTS | FIELD_VALUE`
Required: No

 ** warningThreshold **   <a name="cloudwatchomni-Type-AlertCondition-warningThreshold"></a>
The value at which the alert enters the WARNING state.
Type: Double
Required: No

## See Also
<a name="API_AlertCondition_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/cloudwatchomni-2025-01-01/AlertCondition)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cloudwatchomni-2025-01-01/AlertCondition)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cloudwatchomni-2025-01-01/AlertCondition)
