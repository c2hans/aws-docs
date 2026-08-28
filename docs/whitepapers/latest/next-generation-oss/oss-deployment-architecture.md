---
source_url: https://docs.aws.amazon.com/whitepapers/latest/next-generation-oss/oss-deployment-architecture.html
---

 This whitepaper is for historical reference only. Some content might be outdated and some links might not be available.

# OSS Deployment Architecture
<a name="oss-deployment-architecture"></a>

 While we acknowledge the broad industry definition of what constitutes OSS, the proposed OSS architecture framework focuses on the most critical modules commonly observed in OSS deployments, and their deployment architecture on AWS. The following reference architecture illustrates the deployment strategy of OSS modules on [AWS Regions](https://aws.amazon.com/about-aws/global-infrastructure) and [AWS Outposts](https://aws.amazon.com/outposts) based on their latency needs. For example, a PM/CM Event Collector can run on AWS Outposts, and feed a real-time Self-Organizing Network (SON) application while aggregating events for processing in [AWS Regions](https://aws.amazon.com/about-aws/global-infrastructure/) for applications that do not have a stringent latency budget. Similarly, you can also leverage [AWS Local Zones](https://aws.amazon.com/about-aws/global-infrastructure/localzones/) for latency-sensitive applications while having access to the elasticity, scalability, and security benefits of the cloud.

![Diagram showing OSS Deployment Architecture on AWS](http://docs.aws.amazon.com/whitepapers/latest/next-generation-oss/images/oss-deployment-architecture.png)

 With the exception of Edge analytics and a few Domain Manager functions, the majority of OSS functions can be deployed in centralized AWS Cloud regions given these OSS workloads do not directly participate in network data-lane or network control plane. The ability to deploy in a region means these workloads can be deployed across multi-[Availability Zones](https://aws.amazon.com/about-aws/global-infrastructure/regions_az/), can leverage the full suite of cloud enablers, and can benefit from the full set of cloud elasticity and purchasing options available (including pricing for [Reserved Instance](https://aws.amazon.com/ec2/pricing/reserved-instances/) and [Spot Instance](https://aws.amazon.com/ec2/spot/)). Depending on the Recovery Time Objective (RTO)/Recovery Point Objective (RPO) target and specific disaster recovery requirement, this architecture can be further extended to a multi-region design.

 As illustrated in the previous reference architecture, the proposed OSS deployment on AWS enables a Data Unification layer between OSS, BSS, Software as a Service (SaaS) platforms, and NFx. By leveraging Data Lake and Lake House concepts, DSPs have the ability to optimize data flows between applications, and limit traditional data duplication.

 A cloud-centric model also represents a clear opportunity to implement a shared services model, in which multiple OSS modules (potentially managed by different teams or even supplied by different ISV partners) can be deployed into a consistent, centralized, managed cloud environment (an experience that is enabled by [AWS Organizations](https://aws.amazon.com/organizations) and [AWS Control Tower](https://aws.amazon.com/controltower)), which adheres to a common set of security and audit standards and leverages from a common set of cloud-native capabilities for management and operations. This [landing zone](https://aws.amazon.com/solutions/implementations/aws-landing-zone/) environment can also be extended to network or BSS workloads to maximize synergies across the broader Telco organization.

 Our proposed OSS deployment on AWS allows you to place workloads closer to the network when needed. As such, edge analytics capabilities (such as what’s prescribed by Open Radio Access Network (ORAN) RAN Intelligent Controller (RIC)) can be collocated with network functions, enabling near real-time application.

 The following sub-sections outline the foundational concepts to build an OSS architecture on AWS for domain management, service assurance, service fulfillment, service orchestration, network analytics, and edge analytics.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Whitepapers. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query whitepapers` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
