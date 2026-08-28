---
source_url: https://docs.aws.amazon.com/resilience-hub/latest/userguide/next-gen-data-retention.html
---

# Data retention
<a name="next-gen-data-retention"></a>

The following table shows retention periods for data stored by Next generation Resilience Hub.

| Data type | Retention |
| --- | --- |
| Assessment results and failure mode findings | 2 years |
| System and service event logs | 2 years |
| Discovered resources | 1 year TTL |
| Topology snapshots | 2 years |
| Dependency data | Duration of enablement \+ 30-day lookback |

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Resilience Hub. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query resilience-hub` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
