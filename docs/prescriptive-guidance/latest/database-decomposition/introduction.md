---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/database-decomposition/introduction.html
---

# Database decomposition on AWS
<a name="introduction"></a>

*Philippe Wanner and Saurabh Sharma, Amazon Web Services*

Database modernization, particularly the decomposition of monolithic databases, is a critical workstream for organizations that want to improve agility, scalability, and performance in their data management systems. As businesses grow and their data needs become more complex, traditional monolithic databases often struggle to keep pace. This leads to performance bottlenecks, maintenance challenges, and difficulty adapting to changing business requirements.

The following are common challenges with monolithic databases:
+ **Business domain misalignment** – Monolithic databases often fail to align technology with distinct business domains, which can limit organizational growth.
+ **Scalability constraints** – Systems frequently hit scaling limits, which creates barriers to business expansion.
+ **Architectural rigidity** – Tightly coupled structures make it difficult to update specific components without affecting the entire system.
+ **Performance degradation** – Growing data loads and increasing user concurrency often lead to deteriorating system performance.

The following are the benefits of database decomposition:
+ **Enhanced business agility** – Decomposition enables rapid adaptation to changing business needs and supports independent scaling.
+ **Optimized performance** – Decomposition helps you create specialized database solutions that are tailored to specific use cases and independently scale each database.
+ **Improved cost management** – Decomposition enables more efficient resource utilization and reduces operational costs.
+ **Flexible licensing options** – Decomposition creates opportunities to transition from costly proprietary licenses to open source alternatives.
+ **Innovation enablement** – Decomposition facilitates the adoption of purpose-built databases for specific workloads.

## Intended audience
<a name="intended-audience"></a>

This guide helps database architects, cloud solutions architects, application development teams, and enterprise architects. It is designed to help you decompose monolithic databases into microservices-aligned data stores, implement domain-driven database architectures, plan database migration strategies, and scale database operations to meet growing business demands. To understand the concepts and recommendations in this guide, you should be familiar with relational and NoSQL database principles, AWS managed database services, and microservices architecture patterns. This guide is intended to help organizations that are in the initial stages of a database decomposition project.

## Objectives
<a name="objectives"></a>

This guide can help your organization achieve the following objectives:
+ Collect requirements for decomposing your target architecture.
+ Develop a systematic methodology for evaluating risk and communicating.
+ Create a decomposition plan.
+ Define success metrics, key performance indicators (KPIs), a mitigation strategy, and a business continuity plan.
+ Establish a better workload elasticity that helps you follow business demand.
+ Learn how to adopt specialized databases for specific use cases, which enables innovation.
+ Strengthen your organization's data security and governance.
+ Reduce costs through the following:
  + Reduced licensing fees
  + Reduced vendor lock-in
  + Improved access to broader community support and innovations
  + Ability to choose different database technologies for different components
  + Gradual migration, which reduces risk and spreads costs over time
  + Improved resource utilization

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Prescriptive Guidance. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prescriptive-guidance` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
