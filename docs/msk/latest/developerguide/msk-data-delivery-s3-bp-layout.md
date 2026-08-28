---
source_url: https://docs.aws.amazon.com/msk/latest/developerguide/msk-data-delivery-s3-bp-layout.html
---

# Object layout
<a name="msk-data-delivery-s3-bp-layout"></a>
+ Choose an output key template with time-based placeholders that matches how you query the data downstream.
+ Use GZIP or ZSTD compression to reduce storage costs for text-based payloads; choose the storage class (`STANDARD`, `INTELLIGENT_TIERING`, `GLACIER_IR`) based on access patterns.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Managed Streaming for Apache Kafka. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query msk` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
