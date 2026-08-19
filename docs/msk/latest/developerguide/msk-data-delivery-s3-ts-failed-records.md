---
source_url: https://docs.aws.amazon.com/msk/latest/developerguide/msk-data-delivery-s3-ts-failed-records.html
---

# Failed records (FailedRecordCount greater than 0)
<a name="msk-data-delivery-s3-ts-failed-records"></a>
+ **Symptom:** `FailedRecordCount`, or `DLQDeliverySuccess`, is greater than 0.
+ **Causes:** The record format does not conform to the configured source data type.
+ **Resolution:** Inspect the DLQ entries and Amazon CloudWatch Logs for the failure reason, then fix the producer data so records conform.
