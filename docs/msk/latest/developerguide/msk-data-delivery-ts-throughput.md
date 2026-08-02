---
source_url: https://docs.aws.amazon.com/msk/latest/developerguide/msk-data-delivery-ts-throughput.html
---

# Throughput exceeds the supported limit
<a name="msk-data-delivery-ts-throughput"></a>
+ **Symptom:** Data freshness climbs or delivery slows during sustained high-throughput periods.
+ **Causes:** The source throughput exceeds what the Channel can deliver at the configured freshness.
+ **Resolution:** Reduce the source produce rate, increase the configured data freshness, or distribute load across multiple topics/Channels. Monitor `DataFreshness` and the `BytesIn` / `BytesOut` metrics to confirm the delivery path keeps up. See the throughput figures in [Amazon MSK Data Delivery quotas](limits.md#msk-data-delivery-quota).
