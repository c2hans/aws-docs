---
source_url: https://docs.aws.amazon.com/msk/latest/developerguide/msk-data-delivery-alarms.html
---

# Recommended alarms
<a name="msk-data-delivery-alarms"></a>

| Alarm | Condition | Recommended threshold | Action |
| --- | --- | --- | --- |
| High data freshness | `DataFreshness` exceeds threshold | Above your configured freshness | Investigate throughput or service issues |
| Failed records | `FailedRowCount` / `FailedRecordCount` greater than 0 | > 0 for 5 consecutive minutes | Check IAM permissions, destination bucket access, schema/data compatibility |
| DLQ deliveries | `DLQDeliverySuccess` greater than 0 | > 0 | Inspect DLQ entries for the failure reason |
