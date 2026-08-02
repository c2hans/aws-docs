---
source_url: https://docs.aws.amazon.com/whitepapers/latest/disaster-recovery-of-on-premises-applications-to-aws/shared-responsibility.html
---

 This whitepaper is for historical reference only. Some content might be outdated and some links might not be available.

# Shared responsibility
<a name="shared-responsibility"></a>

 Disaster recovery is a shared responsibility between AWS and you, the customer. It is important that you understand how disaster recovery and availability, as part of resiliency, operate under this shared model.

## AWS responsibility: Resiliency of the Cloud
<a name="aws-responsibility-resiliency-of-the-cloud"></a>

 AWS is responsible for resiliency of the infrastructure that runs all of the services offered in the AWS Cloud. This infrastructure comprises the hardware, software, networking, and facilities that run AWS Cloud services. AWS uses commercially reasonable efforts to make these AWS Cloud services available, ensuring service availability meets or exceeds [AWS Service Level Agreements (SLAs)](https://aws.amazon.com/legal/service-level-agreements/).

 The [AWS Global Cloud Infrastructure](https://aws.amazon.com/about-aws/global-infrastructure) is designed to enable customers to build highly resilient workload architectures. Each AWS Region is fully isolated and consists of multiple Availability Zones, which are physically isolated partitions of infrastructure. Availability Zones isolate faults that could impact workload resiliency, preventing them from impacting other zones in the AWS Region. At the same time, all zones in an AWS Region are interconnected with high-bandwidth, low-latency networking, over fully redundant, dedicated metro fiber providing high-throughput, low-latency networking between zones. All traffic between zones is encrypted. The network performance is sufficient to accomplish synchronous replication between zones. Availability Zones simplify the process of partitioning applications for high availability.

## Customer responsibility: Resiliency in the Cloud and Outside
<a name="customer-responsibility-resiliency-in-the-cloud-and-outside"></a>

 Your responsibility is determined by the AWS Cloud services that you select. This determines the amount of configuration work you must perform as part of your resiliency responsibilities. You are responsible for managing resiliency of your data and workloads, whether on AWS or outside of it, including disaster recovery, high availability, backup, versioning, and replication strategies.

![This image shows an AWS shared responsibility model](http://docs.aws.amazon.com/whitepapers/latest/disaster-recovery-of-on-premises-applications-to-aws/images/awssharedresponsibilitymodel.png)
