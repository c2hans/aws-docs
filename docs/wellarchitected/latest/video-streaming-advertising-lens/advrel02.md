---
source_url: https://docs.aws.amazon.com/wellarchitected/latest/video-streaming-advertising-lens/advrel02.html
---

# Latency sensitive advertising
<a name="advrel02"></a>

| ADVREL02: How do your latency sensitive advertising workloads react to including throttling and rate-limiting scenarios? |
| --- |
|   |

 Consider strategies for managing latency-sensitive advertising workloads through throttling and rate-limiting implementations. Avoid traditional retry mechanisms for fast-failing services, implement effective caching strategies, and proportionally scale across all system components to maintain consistent performance.

**Topics**
+ [ADVREL02-BP01 To allow fast and graceful failure of latency-sensitive services, avoid exponential backing off and retry](advrel02-bp01.md)
+ [ADVREL02-BP02 Implement a caching strategy](advrel02-bp02.md)
+ [ADVREL02-BP03 Prevent scale mismatch of both internal services and external partners](advrel02-bp03.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Well-Architected. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query wellarchitected` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
