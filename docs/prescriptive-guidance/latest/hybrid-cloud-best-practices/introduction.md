---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/hybrid-cloud-best-practices/introduction.html
---

# Best practices for building a hybrid cloud architecture with AWS services
<a name="introduction"></a>

*Leonardo Alberto Solano Alvarado, Tom Gadomski, Len Gomes, Obed Gutierrez, Dionysios Kakaletris, Matt Price, and Vamsi Krishna Yamavarapu, Amazon Web Services*

Many businesses and organizations have adopted cloud computing as a key aspect of their technology strategy. They typically migrate their workloads to the AWS Cloud to increase agility, cost savings, performance, availability, resilience, and scalability. Most applications can be easily migrated, but some applications must remain on premises to take advantage of the low latency and local data processing of the on-premises environment, to avoid high data transfer costs, or for regulatory compliance. Furthermore, a subset of applications might need to be re-architected or modernized before they can be moved to the cloud. This leads many organizations to seek hybrid cloud architectures to integrate their on-premises and cloud operations to support a broad spectrum of use cases. This hybrid approach can provide the benefits of both on-premises and cloud-based computing, and can be particularly useful for edge computing scenarios.

When you build a hybrid cloud with AWS, we recommend that you determine your hybrid cloud strategy and your technical strategy:
+ A **hybrid cloud strategy** provides guidelines that govern the consumption of cloud and on-premises resources to support your business objectives. This guidance describes common use cases for building a hybrid cloud, such as supporting ongoing migration to the cloud, ensuring business continuity during disasters, extending cloud infrastructure to the on-premises environment to support low-latency applications, or expanding your international presence on AWS. Defining this strategy helps you identify and define your business objectives for building a hybrid cloud, and provides guidelines for workload placements on the hybrid cloud.
+ A **technical strategy** for the hybrid cloud identifies the guiding tenets of the hybrid cloud architecture and defines an implementation framework. This guidance outlines common requirements for a consistently deployed and managed hybrid cloud architecture to help you define principles for a planned hybrid cloud implementation. These requirements include standardized interfaces for resource provisioning and management across your cloud infrastructure.

This guide describes an operations and management framework to help solutions architects and operators identify the building blocks, best practices, and AWS hybrid cloud and in-Region services to implement a hybrid cloud with AWS.

Many organizations have used the solutions described in this guide to successfully deploy hybrid cloud environments that take advantage of the scale, agility, innovation, and global footprint provided by the AWS Cloud. (See [case studies](https://aws.amazon.com/hybrid/#Customers).) [AWS hybrid cloud services](https://aws.amazon.com/hybrid/) deliver a consistent AWS experience from the cloud to on premises, and at the edge. Services such as AWS Outposts and AWS Local Zones place compute, storage, database, and other select AWS services close to large population and industry centers when you need low latency between end-user devices or existing on-premises data centers and workload servers.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Prescriptive Guidance. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prescriptive-guidance` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
