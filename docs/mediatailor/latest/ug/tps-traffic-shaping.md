---
source_url: https://docs.aws.amazon.com/mediatailor/latest/ug/tps-traffic-shaping.html
---

# TPS-based traffic shaping
<a name="tps-traffic-shaping"></a>

AWS Elemental MediaTailor provides two optional traffic shaping approaches to limit the number of requests to the ADS at one time. TPS-based traffic shaping offers an alternative to time-window based traffic shaping for prefetch schedules. This approach provides more intuitive configuration by allowing you to specify your ad decision server (ADS) capacity in terms of transactions per second (TPS) and expected concurrent users, rather than time calculations.

## How TPS-based traffic shaping works
<a name="tps-how-it-works"></a>

Instead of specifying retrieval window durations, you provide the following parameters:

Peak TPS
The maximum number of requests per second that your ADS can handle. This parameter has no default value.

Peak concurrent users
The expected peak number of concurrent viewers for your content. This parameter has no default value.

MediaTailor automatically distributes prefetch requests across time to stay within your specified TPS limit, regardless of the number of concurrent sessions.

**Example TPS-based configuration example**
Your ADS can handle 500 TPS, and you expect 100,000 concurrent viewers during peak times. You configure:
+ Peak TPS: 500
+ Peak concurrent users: 100,000
MediaTailor automatically distributes prefetch requests across time to stay within your specified TPS limit, regardless of the number of concurrent sessions.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Elemental MediaTailor. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query mediatailor` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
