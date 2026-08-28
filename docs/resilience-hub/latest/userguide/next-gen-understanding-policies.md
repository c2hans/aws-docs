---
source_url: https://docs.aws.amazon.com/resilience-hub/latest/userguide/next-gen-understanding-policies.html
---

# Understanding resilience policies
<a name="next-gen-understanding-policies"></a>

Resilience policies define the resilience requirements for your application. Each policy specifies targets that Next generation Resilience Hub evaluates during failure mode assessments to determine whether your application meets your resilience goals.

Different stakeholders care about different aspects of resilience:
+ **Central SRE teams** focus on disaster recovery (RTO/RPO) and availability targets.
+ **Service teams** focus on operational performance (latency, error rates, throughput).
+ **Compliance teams** focus on data protection (RPO for data durability).

Modular policies let each stakeholder define their requirements independently, then apply them at the appropriate level of the application hierarchy.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Resilience Hub. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query resilience-hub` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
