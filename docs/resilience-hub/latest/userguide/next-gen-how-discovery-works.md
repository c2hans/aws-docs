---
source_url: https://docs.aws.amazon.com/resilience-hub/latest/userguide/next-gen-how-discovery-works.html
---

# How dependency discovery works
<a name="next-gen-how-discovery-works"></a>

Dependency discovery analyzes Route 53 DNS resolver query logs to identify every domain name that your service's compute resources resolve. This reveals the full set of external dependencies without requiring any agents, code changes, or instrumentation.

| Feature | Detail |
| --- | --- |
| Lookback window | 35 days of historical DNS query data |
| Continuous monitoring | Ongoing discovery summarized by hour |
| Supported dependency types | AWS services, internal endpoints, third-party endpoints |
| Attribution | Dependencies are attributed to specific compute resources within your service |
| Setup | No agents or code changes required – enable in minutes |

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Resilience Hub. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query resilience-hub` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
