---
source_url: https://docs.aws.amazon.com/wellarchitected/latest/games-industry-lens/gamerel01.html
---

# Workload architecture
<a name="gamerel01"></a>

|  GAMEREL01: Is your game architecture taking advantage of the cloud's resiliency?  |
| --- |
|   |

 AWS infrastructure is built around Regions and Availability Zones. AWS Regions provide multiple physically separated and isolated Availability Zones, which are connected using low-latency, high-throughput, and highly redundant networking. These constructs can be used to architect workloads with reliability goals in focus.

**Topics**
+ [GAMEREL01-BP01 Distribute game infrastructure across multiple Availability Zones and Regions to improve resiliency](gamerel01-bp01.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Well-Architected. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query wellarchitected` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
