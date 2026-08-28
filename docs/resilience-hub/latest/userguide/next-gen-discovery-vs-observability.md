---
source_url: https://docs.aws.amazon.com/resilience-hub/latest/userguide/next-gen-discovery-vs-observability.html
---

# How dependency discovery differs from observability tools
<a name="next-gen-discovery-vs-observability"></a>

Dependency discovery focuses on **resilience validation** rather than operational observability:

| Capability | Observability tools (X-Ray, CloudWatch) | Next generation Resilience Hub dependency discovery |
| --- | --- | --- |
| Setup | Requires SDK instrumentation or agents | No agents or code changes – agentless |
| Focus | Performance monitoring, latency debugging | Resilience validation, failure testing |
| Discovery | Reactive – discovers failures during incidents | Proactive – discovers dependencies before incidents |
| Classification | No criticality classification | Hard/soft classification |
| Time to value | Days or weeks of instrumentation | Minutes to enable |

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Resilience Hub. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query resilience-hub` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
