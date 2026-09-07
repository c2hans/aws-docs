---
source_url: https://docs.aws.amazon.com/whitepapers/latest/disaster-recovery-workloads-on-aws/shared-responsibility-model-for-resiliency.html
---

# Shared Responsibility Model for Resiliency
<a name="shared-responsibility-model-for-resiliency"></a>

 Resiliency is a shared responsibility between AWS and you, the customer. It is important that you understand how disaster recovery and availability, as part of resiliency, operate under this shared model.

## AWS responsibility “Resiliency of the Cloud”
<a name="aws-responsibility-resiliency-of-the-cloud"></a>

 AWS is responsible for resiliency of the infrastructure that runs all of the services offered in the AWS Cloud. This infrastructure comprises the hardware, software, networking, and facilities that run AWS Cloud services. AWS uses commercially reasonable efforts to make these AWS Cloud services available, ensuring service availability meets or exceeds [AWS Service Level Agreements (SLAs)](https://aws.amazon.com/legal/service-level-agreements/).

 The [AWS Global Cloud Infrastructure](https://aws.amazon.com/about-aws/global-infrastructure) is designed to enable customers to build highly resilient workload architectures. Each AWS Region is fully isolated and consists of multiple [Availability Zones](https://aws.amazon.com/about-aws/global-infrastructure/regions_az#Availability_Zones), which are physically isolated partitions of infrastructure. Availability Zones isolate faults that could impact workload resilience, preventing them from impacting other zones in the Region. But at the same time, all zones in an AWS Region are interconnected with high-bandwidth, low-latency networking, over fully redundant, dedicated metro fiber providing high-throughput, low-latency networking between zones. All traffic between zones is encrypted. The network performance is sufficient to accomplish synchronous replication between zones. When an application is partitioned across AZs, companies are better isolated and protected from issues such as power outages, lightning strikes, tornadoes, hurricanes, and more.

## Customer responsibility “Resiliency in the Cloud”
<a name="customer-responsibility-resiliency-in-the-cloud"></a>

 Your responsibility will be determined by the AWS Cloud services that you select. This determines the amount of configuration work you must perform as part of your resiliency responsibilities. For example, a service such as Amazon Elastic Compute Cloud (Amazon EC2) requires the customer to perform all of the necessary resiliency configuration and management tasks. Customers that deploy Amazon EC2 instances are responsible for [deploying EC2 instances across multiple locations](https://docs.aws.amazon.com/wellarchitected/latest/reliability-pillar/use-fault-isolation-to-protect-your-workload.html) (such as AWS Availability Zones), [implementing self-healing](https://docs.aws.amazon.com/wellarchitected/latest/reliability-pillar/design-your-workload-to-withstand-component-failures.html) using services like Amazon EC2 Auto Scaling, as well as using [resilient workload architecture best practices](https://docs.aws.amazon.com/wellarchitected/latest/reliability-pillar/workload-architecture.html) for applications installed on the instances. For managed services, such as Amazon S3 and Amazon DynamoDB, AWS operates the infrastructure layer, the operating system, and platforms, and customers access the endpoints to store and retrieve data. You are responsible for managing resiliency of your data including backup, versioning, and replication strategies.

 Deploying your workload across multiple Availability Zones in an AWS Region is part of a high availability strategy designed to protect workloads by isolating issues to one Availability Zone, and uses the redundancy of the other Availability Zones to continue serving requests. A Multi-AZ architecture is also part of a DR strategy designed to make workloads better isolated and protected from issues such as power outages, lightning strikes, tornadoes, earthquakes, and more. DR strategies may also make use of multiple AWS Regions. For example in an active/passive configuration, service for the workload will fail over from its active region to its DR region if the active Region can no longer serve requests.

![Diagram showing how resiliency is a shared responsibility between AWS and the customer.](https://docs.aws.amazon.com/whitepapers/latest/disaster-recovery-workloads-on-aws/images/shared-responsibility-of-resiliency.png)

*Figure 2 - Resiliency is a shared responsibility between AWS and the customer*
