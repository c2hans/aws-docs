---
source_url: https://docs.aws.amazon.com/cloudwatch-omni/latest/APIReference/API_AlertEvaluation.html
---

# AlertEvaluation
<a name="API_AlertEvaluation"></a>

Evaluation cadence. `intervalSeconds` must be one of {30, 60, 120, 300, 600, 900, 1800, 3600}; `pendingDurationSeconds` and `recoveryDurationSeconds` must be multiples of `intervalSeconds`. A duration of 0 means fire/clear immediately with no delay.

On UpdateAlert a supplied evaluation block is replaced whole, not merged: an omitted `pendingDurationSeconds` or `recoveryDurationSeconds` is cleared to unset (no such duration), not preserved and not defaulted to 0. `intervalSeconds` is required whenever the block is present. All enforced server-side / by the front-door validator.

## Contents
<a name="API_AlertEvaluation_Contents"></a>

 ** intervalSeconds **   <a name="cloudwatchomni-Type-AlertEvaluation-intervalSeconds"></a>
The interval between evaluations, in seconds.
Type: Integer
Required: Yes

 ** pendingDurationSeconds **   <a name="cloudwatchomni-Type-AlertEvaluation-pendingDurationSeconds"></a>
The duration a breach must persist before the alert fires, in seconds.
Type: Integer
Required: No

 ** recoveryDurationSeconds **   <a name="cloudwatchomni-Type-AlertEvaluation-recoveryDurationSeconds"></a>
The duration a recovery must persist before the alert clears, in seconds.
Type: Integer
Required: No

## See Also
<a name="API_AlertEvaluation_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/cloudwatchomni-2025-01-01/AlertEvaluation)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cloudwatchomni-2025-01-01/AlertEvaluation)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cloudwatchomni-2025-01-01/AlertEvaluation)
