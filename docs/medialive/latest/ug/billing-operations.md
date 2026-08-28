---
source_url: https://docs.aws.amazon.com/medialive/latest/ug/billing-operations.html
---

# Billing operations
<a name="billing-operations"></a>

The *Operation* field in your billing report identifies the type of MediaLive charge. The following table describes each operation.

| Operation | Description |
| --- | --- |
| CHANNEL\_INPUT | Charges for processing running inputs |
| CHANNEL\_OUTPUT | Charges for processing running outputs |
| CHANNEL\_FEATURE | Charges for add-on features such as Advanced Audio (Dolby), Audio Normalization (DTS), Motion Graphics (MGHD, MGUHD), and Nielsen Watermarking |
| CHANNEL\_ACTIVE | Charges for MediaLive Anywhere active channels |
| ACTIVE\_MULTIPLEX | Charges for running multiplexers |
| INACTIVE\_CHANNEL | Idle channel charges |
| INACTIVE\_INPUT | Idle push input charges |
| INACTIVE\_MULTIPLEX | Idle multiplexer charges |

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for MediaLive. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query medialive` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
