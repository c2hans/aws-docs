---
source_url: https://docs.aws.amazon.com/opensearch-service/latest/APIReference/API_AutoTuneMaintenanceSchedule.html
---

# AutoTuneMaintenanceSchedule
<a name="API_AutoTuneMaintenanceSchedule"></a>

**Note**
This object is deprecated. Use the domain's [off-peak window](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/off-peak.html) to schedule Auto-Tune optimizations. For migration instructions, see [Migrating from Auto-Tune maintenance windows](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/off-peak.html#off-peak-migrate).

The Auto-Tune maintenance schedule. For more information, see [Auto-Tune for Amazon OpenSearch Service](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/auto-tune.html).

## Contents
<a name="API_AutoTuneMaintenanceSchedule_Contents"></a>

 ** CronExpressionForRecurrence **   <a name="opensearchservice-Type-AutoTuneMaintenanceSchedule-CronExpressionForRecurrence"></a>
A cron expression for a recurring maintenance schedule during which Auto-Tune can deploy changes.
Type: String
Required: No

 ** Duration **   <a name="opensearchservice-Type-AutoTuneMaintenanceSchedule-Duration"></a>
The duration of the maintenance schedule. For example, `"Duration": {"Value": 2, "Unit": "HOURS"}`.
Type: [Duration](API_Duration.md) object
Required: No

 ** StartAt **   <a name="opensearchservice-Type-AutoTuneMaintenanceSchedule-StartAt"></a>
The Epoch timestamp at which the Auto-Tune maintenance schedule starts.
Type: Timestamp
Required: No

## See Also
<a name="API_AutoTuneMaintenanceSchedule_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/opensearch-2021-01-01/AutoTuneMaintenanceSchedule)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/opensearch-2021-01-01/AutoTuneMaintenanceSchedule)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/opensearch-2021-01-01/AutoTuneMaintenanceSchedule)
