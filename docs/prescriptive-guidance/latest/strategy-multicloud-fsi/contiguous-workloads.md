---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/strategy-multicloud-fsi/contiguous-workloads.html
---

# Assess the viability of contiguous workloads across CSPs
<a name="contiguous-workloads"></a>

Distributing contiguous workloads across cloud providers introduces challenges and risks that require thoughtful consideration. To evaluate the viability of contiguous workloads, focus on these common considerations for financial services:
+ **Latency**.** **The physical distance between data centers affects performance, particularly for real-time applications (such as real-time payments or trading solutions) that are prevalent in financial services. Weigh geographical diversity against potential performance issues that might affect user experience and operational efficiency.
+ **Predictability of network routing**. Public internet connectivity between clouds lacks the predictability of dedicated network infrastructures. This can lead to inconsistent network performance and bottlenecks. Balance the convenience and cost savings of contiguous workloads against the need for dependable network performance.
+ **Security**. Data transmission over the public internet requires strict security controls. Traffic between CSPs involves greater security risks than traffic within a single provider's network. When you adopt a multicloud strategy, you'll need to strengthen your security measures and possibly increase your cybersecurity investments to protect data in transit.
+ **Complexity of billing**. Handling billing across multiple CSPs can add complexity because CSPs often have different cost models. This can complicate budget management and financial forecasting, and often necessitates advanced financial management tools.
+ **Responsibility boundaries**. Maintaining clear boundaries for managing and securing workloads is challenging in multicloud environments. Each CSP has different policies, and service-level agreements (SLAs) can complicate IT governance. Businesses must define responsibility boundaries clearly to ensure comprehensive coverage of security, compliance, and performance.

You must consider these factors to make informed decisions that align with your strategic goals and operational needs. If you're planning a workload that spans multiple CSPs, follow the recommendations provided in the following sections.

## Domain-based approaches in multicloud implementations
<a name="data-gravity"></a>

In financial services, most firms have workloads with significant data gravity—that is, the data is difficult to move between cloud environments.  Financial systems have strong data gravity constraints because they require real-time transactions and strict operation sequences. Applications that don't have these constraints are easier to run across multiple clouds.

For example, compare your workloads with a workload that runs on a content delivery network (CDN). A CDN is a globally distributed system that has hundreds of points of presence (PoPs) and acts (broadly) as a pass-through cache for web assets. These systems do not** **need strong transactional consistency and are treated differently from financial systems that process credit card payments. The underlying technology and business mechanisms for each system are different.

Financial services workloads have the highest resilience and transactional consistency requirements. These requirements can sometimes conflict with operational resilience and concurrent operations goals if applied across multiple CSPs. Therefore, in some circumstances it might be advisable to keep each application or workload within a single CSP and bound its context within that CSP. If your workload requires concurrent operations across clouds, you should logically split or shard components according to failure domains. This approach removes strong dependencies between CSPs and helps you meet your service-level objectives (SLOs) and service-level agreements (SLAs).

When teams build applications that are distributed across CSPs, this domain-based approach is functionally similar to using a SaaS provider, although that provider is a team within your organization. In this scenario, the considerations discussed in the section [Accelerate and optimize FI operations with SaaS applications](saas.md) also apply to workloads that your organization operates across providers.

## Hard dependencies and synchronous operations
<a name="synchronous-ops"></a>

Workloads that are spread across cloud environments can encounter similar design constraints as workloads that are spread between an on-premises data center and the cloud. When a single, logical operation requires synchronous or real-time API calls, splitting your workload might become logistically challenging and endanger SLAs, SLOs, and overall resilience. For example, if a customer initiates a credit card transaction that requires real-time calls to multiple physical locations, and each location is bound by its own SLAs and internal dependencies, a service interruption in any environment will endanger the entire transaction.

When you operate your system in multiple CSPs, you must turn hard dependencies across environments into soft (flexible), asynchronous dependencies, as illustrated in the following diagram. When API calls are part of your business process, use patterns such as circuit breakers and exponential backoff.

![](http://docs.aws.amazon.com/prescriptive-guidance/latest/strategy-multicloud-fsi/images/guide-img/79fe34d7-841b-4bd6-a6da-96f5401c6a67/images/cf7e2d6a-447e-44ae-b509-8622632dab83.png)

To transfer large amounts of data between cloud environments, use a bulk export approach. This approach enables faster data transfer than a series of synchronous API calls, simplifies data validation, and works with object storage across all cloud providers. One `PUT` operation is cleaner, faster, safer, easier to audit, and less expensive than millions (or billions) of `PUT` operations.

## Impact on SLAs
<a name="sla-impact"></a>

Financial services firms must carefully assess the feasibility, practicality, and implications of multicloud operating models so they can meet their SLAs. Each CSP (and its services) has its own SLAs. If your workloads have stringent SLA requirements, consider the composite SLA between environments to make your workload design decisions.

For example, if your workload in CSP1 has an SLA of 99.99% and your workload in CSP2 has an SLA of 99.99%, the composite SLA is 99.98%. In addition to SLA considerations, you must communicate clearly with your stakeholders on how multicloud operations affect their cross-cloud workloads.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Prescriptive Guidance. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prescriptive-guidance` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
