---
source_url: https://docs.aws.amazon.com/cloudwatch-omni/latest/APIReference/API_AlertStateInfo.html
---

# AlertStateInfo
<a name="API_AlertStateInfo"></a>

Live evaluation state for an alert. Read-only, system-managed.

## Contents
<a name="API_AlertStateInfo_Contents"></a>

 ** value **   <a name="cloudwatchomni-Type-AlertStateInfo-value"></a>
Current flat state.
Type: String
Valid Values: `OK | WARNING | CRITICAL | NODATA`
Required: Yes

 ** contributorSummary **   <a name="cloudwatchomni-Type-AlertStateInfo-contributorSummary"></a>
Counts of contributors currently breaching each severity threshold. Present only when contributor-level tracking is active; absent until the first contributor breaches a `WARNING` or `CRITICAL` threshold.
Type: [ContributorSummary](API_ContributorSummary.md) object
Required: No

 ** data **   <a name="cloudwatchomni-Type-AlertStateInfo-data"></a>
Structured detail about why the alert is in its current state.
Type: [AlertStateData](API_AlertStateData.md) object
Required: No

 ** transitionedAt **   <a name="cloudwatchomni-Type-AlertStateInfo-transitionedAt"></a>
When the alert transitioned to its current state.
Type: Timestamp
Required: No

## See Also
<a name="API_AlertStateInfo_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/cloudwatchomni-2025-01-01/AlertStateInfo)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cloudwatchomni-2025-01-01/AlertStateInfo)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cloudwatchomni-2025-01-01/AlertStateInfo)
