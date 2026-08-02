---
source_url: https://docs.aws.amazon.com/msk/latest/developerguide/msk-data-delivery-bp-security.html
---

# Security
<a name="msk-data-delivery-bp-security"></a>
+ Scope IAM permissions to the specific destination bucket (and schema registry for Iceberg) used by each Channel.
+ Use the `aws:SourceArn` condition in the trust policy to prevent other clusters or services from assuming the Channel role.
+ Enable CloudTrail logging to audit all Channel API calls.
