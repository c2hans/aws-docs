---
source_url: https://docs.aws.amazon.com/msk/latest/developerguide/msk-data-delivery-s3-ts-suspended.html
---

# Channel is suspended
<a name="msk-data-delivery-s3-ts-suspended"></a>
+ **Symptom:** Delivery was working, then the Channel becomes `SUSPENDED` and no new data appears at the destination.
+ **Causes:** The S3 bucket owner does not match the expected account.
+ **Resolution:** The Channel is suspended. If needed, create a new Channel.
