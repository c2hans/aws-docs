---
source_url: https://docs.aws.amazon.com/mediatailor/latest/ug/stream-reqmts.html
---

# Input source requirements for MediaTailor ad insertion
<a name="stream-reqmts"></a>

A input source must meet the following requirements to work with MediaTailor:
+ Use Apple HLS (HTTP Live Streaming) or MPEG DASH (Dynamic Adaptive Streaming over HTTP)
+ Use live streaming or video on demand (VOD)
+ Be accessible on the public internet and have a public IP address
+ Use standard HTTP ports (port 80) or HTTPS ports (port 443). MediaTailor does not support custom ports for origin server communication.
+ Contain ad markers in one of the formats described in the [Getting started with MediaTailor ad insertion tutorial](getting-started-ad-insertion.md#getting-started-prep-stream)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Elemental MediaTailor. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query mediatailor` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
