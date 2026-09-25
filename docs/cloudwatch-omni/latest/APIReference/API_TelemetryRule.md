---
source_url: https://docs.aws.amazon.com/cloudwatch-omni/latest/APIReference/API_TelemetryRule.html
---

# TelemetryRule
<a name="API_TelemetryRule"></a>

Telemetry-based rule: what to query, how to evaluate the result, what condition makes it fire, and what to do on missing data.

## Contents
<a name="API_TelemetryRule_Contents"></a>

 ** condition **   <a name="cloudwatchomni-Type-TelemetryRule-condition"></a>
The condition that determines when the alert fires.
Type: [AlertCondition](API_AlertCondition.md) object
Required: No

 ** evaluation **   <a name="cloudwatchomni-Type-TelemetryRule-evaluation"></a>
The evaluation cadence and durations.
Type: [AlertEvaluation](API_AlertEvaluation.md) object
Required: No

 ** noData **   <a name="cloudwatchomni-Type-TelemetryRule-noData"></a>
How the alert behaves when a query produces no data.
Type: [NoData](API_NoData.md) object
Required: No

 ** query **   <a name="cloudwatchomni-Type-TelemetryRule-query"></a>
The query expression to evaluate.
Type: [AlertRuleQuery](API_AlertRuleQuery.md) object
Required: No

## See Also
<a name="API_TelemetryRule_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/cloudwatchomni-2025-01-01/TelemetryRule)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cloudwatchomni-2025-01-01/TelemetryRule)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cloudwatchomni-2025-01-01/TelemetryRule)
