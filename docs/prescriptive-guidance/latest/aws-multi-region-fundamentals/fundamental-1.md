---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/aws-multi-region-fundamentals/fundamental-1.html
---

# Multi-Region fundamental 1: Understanding the requirements
<a name="fundamental-1"></a>

As mentioned previously, high availability and continuity of operations are common reasons for pursuing multi-Region architectures. Availability metrics measure the percentage of time a workload is available for use over a defined period, whereas continuity of operations metrics measure recovery time for large-scale, and typically longer, duration events.

[Measuring availability](https://docs.aws.amazon.com/wellarchitected/latest/reliability-pillar/availability.html) is a nearly continuous process. Specific measurements can vary but typically coalesce around a target availability metric, most often referred to as *nines* (such as 99.99 percent availability). With availability goals, one size does not fit all. You should establish availability goals at a workload level and separate non-critical components from critical components, instead of applying a single goal across all workloads.

For continuity of operations, the following point-in-time measurements are typically used:
+ **Recovery time objective (RTO)** – RTO is the maximum acceptable delay between the interruption of service and restoration of service. This value determines an acceptable duration for which the service is impaired.
+ **Recovery point objective (RPO)** – RPO is the maximum acceptable amount of time since the last data recovery point. This determines what is considered an acceptable data loss between the latest recovery point and a service interruption.

Similar to setting availability goals, RTO and RPO should also be defined at a workload level. More aggressive continuity of operations or high availability requires increased investment. That said, not every application can demand or requires the same level of resilience. Aligning business and IT owners to assess the criticality of applications based on business impact and then tiering them accordingly can help provide a starting point. The following tables provide examples of tiering.

This table shows an example of resilience tiering for service-level agreements (SLAs).

|
|
| Resilience tier | Availability SLA | Acceptable downtime/year |
| --- |--- |--- |
| Platinum | 99.99% | 52.60 minutes |
| Gold | 99.90% | 8.77 hours |
| Silver | 99.5% | 1.83 days |

The following table shows an example of resilience tiering for RTO and RPO.

|
|
| Resilience tier | Maximum RTO | Maximum RPO | Criteria | Cost |
| --- |--- |--- |--- |--- |
| Platinum | 15 minutes | 5 minutes | Mission-critical workloads | $$$ |
| Gold | 15 minutes – 6 hours | 2 hours | Important but not mission-critical workloads | $$ |
| Silver | 6 hours – a few days | 24 hours | Non-critical workloads | $ |

When you design workloads for resilience, consider the relationship between high availability and continuity of operations. For example, if a workload requires 99.99 percent availability, no more than 53 minutes of downtime per year is tolerable. It can take at least 5 minutes to detect a failure and another 10 minutes for an operator to engage, make decisions on recovery steps, and perform these steps. It's not unusual to take 30 to 45 minutes to recover from a single issue. In this case, it's beneficial to have a multi-Region strategy to provide an isolated instance that removes correlated impact. This allows for continued operations by failing over within a bounded time while you triage the initial impairment independently. This is where defining the appropriate bounded recovery time and ensuring there is alignment are required.

A multi-Region approach might be appropriate for mission-critical workloads that have extreme availability needs (for example, 99.99 percent or higher availability) or stringent continuity of operations requirements that can be met only by failing over into another Region. However, these requirements are typically applicable only to a small subset of an enterprise's workload portfolio that has a bounded recovery time measured in minutes or hours. Unless an application needs a recovery time of minutes or a few hours, it might be a better approach to wait for a Regional disruption to the application to be remediated within the affected Region. This approach is typically aligned with lower-tier workloads.

Before implementing a multi-Region architecture, business decision-makers and technical teams should be aligned on cost implications, including operational and infrastructure cost drivers. A typical multi-Region architecture can incur a cost that's twice as large as a single-Region approach. Although there are several multi-Region patterns for business continuity, such as running with a [hot standby](https://docs.aws.amazon.com/whitepapers/latest/disaster-recovery-workloads-on-aws/disaster-recovery-options-in-the-cloud.html#multi-site-activeactive), [warm standby](https://docs.aws.amazon.com/whitepapers/latest/disaster-recovery-workloads-on-aws/disaster-recovery-options-in-the-cloud.html#warm-standby), or [pilot light](https://docs.aws.amazon.com/whitepapers/latest/disaster-recovery-workloads-on-aws/disaster-recovery-options-in-the-cloud.html#pilot-light), the pattern with the lowest risk of meeting recovery objectives will involve running hot standby, and will double the cost for your workload.

## Key guidance
<a name="key-guidance-1"></a>
+ Availability and continuity of operations goals such as RTO and RPO should be established per workload and aligned with business and IT stakeholders.
+ Most availability and continuity of operations goals can be met within a single Region. For goals that cannot be met within a single Region, consider multi-Region with a clear view on trade-offs between cost, complexity, and benefits.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Prescriptive Guidance. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prescriptive-guidance` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
