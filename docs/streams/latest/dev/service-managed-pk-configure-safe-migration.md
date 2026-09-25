---
source_url: https://docs.aws.amazon.com/streams/latest/dev/service-managed-pk-configure-safe-migration.html
---

# Safe migration patterns
<a name="service-managed-pk-configure-safe-migration"></a>

Switching the record distribution strategy on a stream takes effect immediately and propagates to all infrastructure within approximately one second. There is no notification, drain, or quiesce mechanism. Active consumers processing records mid-batch see an immediate behavior change. Plan your migration carefully using the following guidance.
