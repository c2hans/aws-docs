---
source_url: https://docs.aws.amazon.com/wellarchitected/2024-06-27/framework/rel_fault_isolation_select_location.html
---

This is an earlier version of the AWS Well-Architected Framework. For the latest version, see [AWS Well-Architected Framework](https://docs.aws.amazon.com/wellarchitected/latest/framework/welcome.html).

# REL10-BP02 Select the appropriate locations for your multi-location deployment
<a name="rel_fault_isolation_select_location"></a>

 **Desired outcome:** For high availability, always (when possible) deploy your workload components to multiple Availability Zones (AZs). For workloads with extreme resilience requirements, carefully evaluate the options for a multi-Region architecture.

![Diagram showing a resilient multi-AZ database deployment with backup to another AWS Region](http://docs.aws.amazon.com/wellarchitected/2024-06-27/framework/images/multi-az-architecture.png)

 **Common anti-patterns:**
+  Choosing to design a multi-Region architecture when a multi-AZ architecture would satisfy requirements.
+  Not accounting for dependencies between application components if resilience and multi-location requirements differ between those components.

 **benefits of establishing this best practice:** For resilience, you should use an approach that builds layers of defense. One layer protects against smaller, more common, disruptions by building a highly available architecture using multiple AZs. Another layer of defense is meant to protect against rare events like widespread natural disasters and Region-level disruptions. This second layer involves architecting your application to span multiple AWS Regions.
+  The difference between a 99.5% availability and 99.99% availability is over 3.5 hours per month. The expected availability of a workload can only reach “four nines” if it is in multiple AZs.
+  By running your workload in multiple AZs, you can isolate faults in power, cooling, and networking, and most natural disasters like fire and flood.
+  Implementing a multi-Region strategy for your workload helps protect it against widespread natural disasters that affect a large geographic region of a country, or technical failures of Region-wide scope. Be aware that implementing a multi-Region architecture can be significantly complex, and is usually not required for most workloads.

 **Level of risk exposed if this best practice is not established:** High

## Implementation guidance
<a name="implementation-guidance"></a>

 For a disaster event based on disruption or partial loss of one Availability Zone, implementing a highly available workload in multiple Availability Zones within a single AWS Region helps mitigate against natural and technical disasters. Each AWS Region is comprised of multiple Availability Zones, each isolated from faults in the other zones and separated by a meaningful distance. However, for a disaster event that includes the risk of losing multiple Availability Zone components, which are a significant distance away from each other, you should implement disaster recovery options to mitigate against failures of a Region-wide scope. For workloads that require extreme resilience (critical infrastructure, health-related applications, financial system infrastructure, etc.), a multi-Region strategy may be required.

### Implementation Steps
<a name="implementation-steps"></a>

1.  Evaluate your workload and determine whether the resilience needs can be met by a multi-AZ approach (single AWS Region), or if they require a multi-Region approach. Implementing a multi-Region architecture to satisfy these requirements will introduce additional complexity, therefore carefully consider your use case and its requirements. Resilience requirements can almost always be met using a single AWS Region. Consider the following possible requirements when determining whether you need to use multiple Regions:

   1.  **Disaster recovery (DR)**: For a disaster event based on disruption or partial loss of one Availability Zone, implementing a highly available workload in multiple Availability Zones within a single AWS Region helps mitigate against natural and technical disasters. For a disaster event that includes the risk of losing multiple Availability Zone components, which are a significant distance away from each other, you should implement disaster recovery across multiple Regions to mitigate against natural disasters or technical failures of a Region-wide scope.

   1.  **High availability (HA)**: A multi-Region architecture (using multiple AZs in each Region) can be used to achieve greater then four 9’s (> 99.99%) availability.

   1.  **Stack localization**: When deploying a workload to a global audience, you can deploy localized stacks in different AWS Regions to serve audiences in those Regions. Localization can include language, currency, and types of data stored.

   1.  **Proximity to users:** When deploying a workload to a global audience, you can reduce latency by deploying stacks in AWS Regions close to where the end users are.

   1.  **Data residency**: Some workloads are subject to data residency requirements, where data from certain users must remain within a specific country’s borders. Based on the regulation in question, you can choose to deploy an entire stack, or just the data, to the AWS Region within those borders.

1.  Here are some examples of multi-AZ functionality provided by AWS services:

   1.  To protect workloads using EC2 or ECS, deploy an Elastic Load Balancer in front of the compute resources. Elastic Load Balancing then provides the solution to detect instances in unhealthy zones and route traffic to the healthy ones.

      1.  [Getting started with Application Load Balancers](https://docs.aws.amazon.com/elasticloadbalancing/latest/application/application-load-balancer-getting-started.html)

      1.  [Getting started with Network Load Balancers](https://docs.aws.amazon.com/elasticloadbalancing/latest/network/network-load-balancer-getting-started.html)

   1.  In the case of EC2 instances running commercial off-the-shelf software that do not support load balancing, you can achieve a form of fault tolerance by implementing a multi-AZ disaster recovery methodology.

      1. [REL13-BP02 Use defined recovery strategies to meet the recovery objectives](rel_planning_for_recovery_disaster_recovery.md)

   1.  For Amazon ECS tasks, deploy your service evenly across three AZs to achieve a balance of availability and cost.

      1.  [Amazon ECS availability best practices \| Containers](https://aws.amazon.com/blogs/containers/amazon-ecs-availability-best-practices/)

   1.  For non-Aurora Amazon RDS, you can choose Multi-AZ as a configuration option. Upon failure of the primary database instance, Amazon RDS automatically promotes a standby database to receive traffic in another availability zone. Multi-Region read-replicas can also be created to improve resilience.

      1.  [Amazon RDS Multi AZ Deployments](https://aws.amazon.com/rds/features/multi-az/)

      1.  [Creating a read replica in a different AWS Region](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_ReadRepl.XRgn.html)

1.  Here are some examples of multi-Region functionality provided by AWS services:

   1.  For Amazon S3 workloads, where multi-AZ availability is provided automatically by the service, consider Multi-Region Access Points if a multi-Region deployment is needed.

      1.  [Multi-Region Access Points in Amazon S3](https://docs.aws.amazon.com/AmazonS3/latest/userguide/MultiRegionAccessPoints.html)

   1.  For DynamoDB tables, where multi-AZ availability is provided automatically by the service, you can easily convert existing tables to global tables to take advantage of multiple regions.

      1.  [Convert Your Single-Region Amazon DynamoDB Tables to Global Tables](https://aws.amazon.com/blogs/aws/new-convert-your-single-region-amazon-dynamodb-tables-to-global-tables/)

   1.  If your workload is fronted by Application Load Balancers or Network Load Balancers, use AWS Global Accelerator to improve the availability of your application by directing traffic to multiple regions that contain healthy endpoints.

      1.  [Endpoints for standard accelerators in AWS Global Accelerator - AWS Global Accelerator (amazon.com)](https://docs.aws.amazon.com/global-accelerator/latest/dg/about-endpoints.html)

   1.  For applications that leverage AWS EventBridge, consider cross-Region buses to forward events to other Regions you select.

      1.  [Sending and receiving Amazon EventBridge events between AWS Regions](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-cross-region.html)

   1.  For Amazon Aurora databases, consider Aurora global databases, which span multiple AWS regions. Existing clusters can be modified to add new Regions as well.

      1.  [Getting started with Amazon Aurora global databases](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/aurora-global-database-getting-started.html)

   1.  If your workload includes AWS Key Management Service (AWS KMS) encryption keys, consider whether multi-Region keys are appropriate for your application.

      1.  [Multi-Region keys in AWS KMS](https://docs.aws.amazon.com/kms/latest/developerguide/multi-region-keys-overview.html)

   1.  For other AWS service features, see this blog series on [Creating a Multi-Region Application with AWS Services series](https://aws.amazon.com/blogs/architecture/tag/creating-a-multi-region-application-with-aws-services-series/)

 **Level of effort for the Implementation Plan:** Moderate to High

## Resources
<a name="resources"></a>

 **Related documents:**
+  [Creating a Multi-Region Application with AWS Services series](https://aws.amazon.com/blogs/architecture/tag/creating-a-multi-region-application-with-aws-services-series/)
+  [Disaster Recovery (DR) Architecture on AWS, Part IV: Multi-site Active/Active](https://aws.amazon.com/blogs/architecture/disaster-recovery-dr-architecture-on-aws-part-iv-multi-site-active-active/)
+  [AWS Global Infrastructure](https://aws.amazon.com/about-aws/global-infrastructure)
+  [AWS Local Zones FAQ](https://aws.amazon.com/about-aws/global-infrastructure/localzones/faqs/)
+  [Disaster Recovery (DR) Architecture on AWS, Part I: Strategies for Recovery in the Cloud](https://aws.amazon.com/blogs/architecture/disaster-recovery-dr-architecture-on-aws-part-i-strategies-for-recovery-in-the-cloud/)
+  [Disaster recovery is different in the cloud](https://docs.aws.amazon.com/whitepapers/latest/disaster-recovery-workloads-on-aws/disaster-recovery-is-different-in-the-cloud.html)
+  [Global Tables: Multi-Region Replication with DynamoDB](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/GlobalTables.html)

 **Related videos:**
+  [AWS re:Invent 2018: Architecture Patterns for Multi-Region Active-Active Applications (ARC209-R2)](https://youtu.be/2e29I3dA8o4)
+  [Auth0: Multi-Region High-Availability Architecture that Scales to 1.5B\+ Logins a Month with automated failover](https://www.youtube.com/watch?v=vGywoYc_sA8)

 **Related examples:**
+  [Disaster Recovery (DR) Architecture on AWS, Part I: Strategies for Recovery in the Cloud](https://aws.amazon.com/blogs/architecture/disaster-recovery-dr-architecture-on-aws-part-i-strategies-for-recovery-in-the-cloud/)
+  [DTCC achieves resilience well beyond what they can do on premises](https://aws.amazon.com/solutions/case-studies/DTCC/)
+  [Expedia Group uses a multi-Region, multi-Availability Zone architecture with a proprietary DNS service to add resilience to the applications](https://aws.amazon.com/solutions/case-studies/expedia/)
+  [Uber: Disaster Recovery for Multi-Region Kafka](https://www.uber.com/blog/kafka/)
+  [Netflix: Active-Active for Multi-Regional Resilience](https://netflixtechblog.com/active-active-for-multi-regional-resiliency-c47719f6685b)
+  [How we build Data Residency for Atlassian Cloud](https://www.atlassian.com/engineering/how-we-build-data-residency-for-atlassian-cloud)
+  [Intuit TurboTax runs across two Regions](https://www.youtube.com/watch?v=286XyWx5xdQ)
