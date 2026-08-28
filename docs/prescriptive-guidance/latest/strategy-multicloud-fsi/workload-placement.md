---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/strategy-multicloud-fsi/workload-placement.html
---

# Establish a workload placement strategy
<a name="workload-placement"></a>

When you define your workload placement strategy for a multicloud environment, first [choose a primary CSP](recommendations.md) that meets the general needs of your organization. This provider should offer a robust set of services, security features that meet or exceed your needs, and cost efficiency. Your organization can then follow a clear process to select additional cloud providers based on specific criteria:
+ **Organizational structure**.** **Consider how your organization is structured today (for example, by departments, business lines, or geographic locations), particularly if you need to comply with data sovereignty or other regulatory requirements. Also consider enterprise architecture, communications, operating procedures, and other influences from [Conway's Law](https://www.melconway.com/Home/Committees_Paper.html) as inputs. Don't force workload placement or operations in ways that create friction with your existing culture or business operations.
+ **Workload performance**. Consider how your applications are structured. For SaaS applications, determine their preferred CSP, if there is one. Different CSPs offer unique performance benefits for specific workloads. For example, some providers might provide an infrastructure that better supports applications or SaaS partners because of native optimizations or specialized services.
+ **Security and compliance**.** **CSPs offer unique security features and compliance certifications. In a multicloud environment, all providers must meet your organization's security and regulatory requirements. Evaluate the security measures and compliance capabilities of each CSP to maintain a strong security posture across your multicloud infrastructure. Consider data residency and the physical fault isolation boundaries that each CSP supports.
+ **Data management and integration**. Data management can become more complex in a multicloud environment. Evaluate how data will be stored, accessed, and integrated across different CSPs. You must have a cohesive data strategy that ensures data consistency, availability, and security across all cloud platforms. Federated data governance requires a strong *trust but verify* approach to data management, and adding metadata in other CSP environments can introduce unplanned scope expansion, which increases risk and potential exposure to unauthorized parties. Be prepared to maintain materialized views of your data in other clouds.
+ **Cost management and optimization**. Multicloud environments can complicate cost tracking and optimization efforts, and many CSPs offer different cloud operating models and tools for assistance. Implement robust cloud financial management practices in your [landing zone](https://docs.aws.amazon.com/prescriptive-guidance/latest/migration-aws-environment/understanding-landing-zones.html) early in your adoption to monitor usage, control costs, and maximize the value of your cloud investments.

We recommend that you establish a multicloud governance framework that includes criteria for selecting additional CSPs. This framework should evaluate factors such as the cost, performance, security, and compliance capabilities of additional providers.

No single approach works best for all organizations, but successful multicloud implementations often use a scoreboard, such as in the following example, to evaluate and compare CSPs.

|
|
| Capabilities | CSP1 score | CSP2 score |
| --- |--- |--- |
| Landing zone alignment to organizational structure | 5.00 | 5.00 |
| Workload performance | 4.00 | 5.00 |
| Security | 4.00 | 3.00 |
| Data management | 3.00 | 3.00 |
| Cost optimization | 4.00 | 3.00 |
| Exit capabilities | 4.00 | 3.00 |
| Partner ecosystem | 5.00 | 5.00 |
| Operational excellence | 5.00 | 4.00 |
| Reliability | 5.00 | 4.00 |
| Sustainability | 4.00 | 4.00 |
| **Total** | **4.30** | **3.90** |

However, this table isn't a fully developed example and doesn't reflect the weight or bias of each capability. For example, your business might require greater emphasis on exit capabilities compared with other capabilities. The key is to have a structured, systematic, repeatable, and deterministic method for selecting CSPs.

Each workload might require a minimum score per capability to meet external constraints. For example, payment processing applications might require a minimum score for reliability and de-emphasize cost as a consideration.

After you select and enable your CSPs—including setting up a secure landing zone, training your IT staff, and establishing a CCoE—follow a prescriptive selection process to determine which CSP will host each workload in production. In rare instances, the same application might be placed concurrently in multiple CSPs; however, this is not typical except for ISV and SaaS workloads. The placement strategy can be documented in a flowchart that addresses the considerations discussed in this paper. The following diagram provides an example.

![CSP selection process for multicloud.](http://docs.aws.amazon.com/prescriptive-guidance/latest/strategy-multicloud-fsi/images/guide-img/79fe34d7-841b-4bd6-a6da-96f5401c6a67/images/349f20f9-008c-4f62-8a4b-fea1971833e5.png)

We recommend that you follow a phased approach with checkpoints to develop your workload placement strategy. Remember that multicloud is a strategy, not a goal. It requires balancing business value, technological feasibility, product velocity, and cost.

Develop a clear business case for using multiple providers. Do not proceed without documented justification. Next, map each critical capability for your cloud environments against your business requirements. A "no" response to any critical capability question disqualifies the workload. A multicloud approach is feasible only when a workload meets all your business and technical requirements.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Prescriptive Guidance. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prescriptive-guidance` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
