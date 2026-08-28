---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/strategy-multicloud/tenet-4.html
---

# Tenet 4. Do not spread contiguous workloads across clouds
<a name="tenet-4"></a>

Spreading contiguous workloads across multiple cloud providers creates unnecessary complexity, risk, and cost. When workloads that process and analyze data together span multiple providers, organizations face challenges in data movement, synchronization, and consistency. Teams must navigate different APIs, management interfaces, security models, and operational processes for each provider, which increases the likelihood of errors and adds operational overhead. This complexity increases the chances of errors and operational overhead, and can hinder agility and scalability.

However, in some practical scenarios, organizations might need to distribute contiguous workloads across clouds because of specific business or technical requirements. In these cases, we recommend that you establish clear criteria and guiding principles to evaluate the trade-offs, and ensure that the approach aligns with your organization's overall multicloud strategy.

When organizations choose to distribute workloads across multiple clouds, adopting an architecture that's centered on messaging and loose coupling can alleviate many of the associated challenges. This is the best way to separate concerns between clouds and to reduce the scope of impact if a provider is impaired. Operations that are the most time-bound, such as financial transactions, should ideally be kept within a single environment. An outage in one environment should never be allowed to endanger workloads in another environment.

**Our guidance:**
+ Design cloud workloads for operational independence to minimize real-time dependencies between providers. When workload distribution is necessary, implement efficient bulk data transfer mechanisms instead of maintaining constant cross-cloud connections.
+ Evaluate each proposed distributed workload against clear business criteria. Consider both the strategic benefits and the operational complexity introduced by the distribution.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Prescriptive Guidance. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prescriptive-guidance` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
