---
source_url: https://docs.aws.amazon.com/msk/latest/developerguide/msk-data-delivery-ts-suspended.html
---

# Channel is suspended
<a name="msk-data-delivery-ts-suspended"></a>

## Suspension on a previously working Channel
<a name="msk-data-delivery-ts-suspended-working"></a>
+ **Symptom:** Delivery was working, then the Channel becomes `SUSPENDED` and no new data appears at the destination.
+ **Causes:**
  + **For Iceberg destinations:** The destination table created by the Channel may have been deleted.
  + **For S3 destinations:** The S3 bucket owner does not match the expected account.

## Suspension on a Channel that never delivered data
<a name="msk-data-delivery-ts-suspended-never"></a>
+ **Symptom:** No data appears at the destination after the Channel is created, and the Channel becomes `SUSPENDED`.
+ **Causes:**
  + **For Iceberg destinations:** The data type of the configured partition column cannot be transformed to a time-based partition.
+ **Resolution:** The Channel is suspended. If needed, create a new Channel.
