---
source_url: https://docs.aws.amazon.com/msk/latest/developerguide/msk-data-delivery-bp-layout.html
---

# S3 object layout (S3 bucket)
<a name="msk-data-delivery-bp-layout"></a>
+ Choose an output key template with time-based placeholders that matches how you query the data downstream.
+ Use GZIP or ZSTD compression to reduce storage costs for text-based payloads; choose the storage class (`STANDARD`, `INTELLIGENT_TIERING`, `GLACIER_IR`) based on access patterns.
