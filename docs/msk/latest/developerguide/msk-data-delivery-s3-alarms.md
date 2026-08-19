---
source_url: https://docs.aws.amazon.com/msk/latest/developerguide/msk-data-delivery-s3-alarms.html
---

# Recommended alarms
<a name="msk-data-delivery-s3-alarms"></a>

| Alarm | Condition | Recommended threshold | Action |
| --- | --- | --- | --- |
| High data freshness | `DeliveryToS3.DataFreshness` exceeds threshold | Above your configured freshness | Investigate throughput or service issues |
| Failed records | `DeliveryToS3.FailedRecordCount` greater than 0 | > 0 for 5 consecutive minutes | Check IAM permissions, destination bucket access, schema/data compatibility |
| DLQ deliveries | `DeliveryToS3.DLQDeliverySuccess` greater than 0 | > 0 | Inspect DLQ entries for the failure reason |
