---
source_url: https://docs.aws.amazon.com/whitepapers/latest/next-generation-oss/domain-management.html
---

 This whitepaper is for historical reference only. Some content might be outdated and some links might not be available.

# Domain Management
<a name="domain-management"></a>

 Domain management is undergoing a shift towards a more open approach to reduce network complexity, enable CSPs to either forego domain managers or evolve into open domain managers, and have a multi-vendors approach to domain management. Domain management on AWS helps you reduce the size of your OSS stack, and helps you eliminate infrastructure complexity associated with the operations of domain managers (per NFx, per vendor, and for a given capacity).

 The following reference architecture outlines an example domain management implementation leveraging AWS Outposts for functions requiring low-latency budget. AWS Regions are leveraged for mediation and domain-specific applications that enable engineering, operations, and planning groups to efficiently perform their tasks.

 Amazon S3 provides a scalable solution to host network configuration exports and mediate performance data, providing you with the control to apply Life Cycle Management (LCM) policies that are specific to your needs. Amazon Elastic File System (EFS) provides you with scalable and elastic file storage. You can mount EFS on your on-premise legacy OSS systems using standard Linux commands for mounting a file system via the NFSv4.1 protocol. This enables you to take advantage of the AWS Cloud, even for legacy systems, and enables CSPs to move away from complex and costly hardware expansions.

 Similarly, AWS enables CSPs (and DSPs) to migrate to cloud databases using services such as the [AWS Schema Conversion Tool](https://aws.amazon.com/dms/schema-conversion-tool/) (SCT) and [AWS Database Migration Service](https://aws.amazon.com/dms) (DMS), providing you with the tools to automate schema conversion and data movement. The process of developing APIs is simplified by [AWS API Gateway](https://aws.amazon.com/api-gateway) to expose domain management functions and build ones that spawn domains, NFx, and technologies.

![Diagram showing Domain Management Architecture on AWS](https://docs.aws.amazon.com/whitepapers/latest/next-generation-oss/images/domain-management-architecture.png)

 [Amazon EKS](https://aws.amazon.com/eks) provides you with both Kubernetes namespace capabilities and [AWS Auto-Scaling group](https://docs.aws.amazon.com/autoscaling/ec2/userguide/AutoScalingGroup.html) to reduce infrastructure costs of domain management. CSPs and DSPs can run domain-specific as well as multi-domain domain managers on different namespaces, simplifying their operations. By separating domain managers across namespace and via role-based access control integration with [AWS IAM](https://aws.amazon.com/iam/), it’s possible to control per-domain-level access to the Kubernetes API for compute-level isolation between domains. Further networking and storage-level isolation is also possible via network policies and service mesh, and via volume-defined, per-storage classes. This enables CSPs and DSPs to eliminate the infrastructure complexity of on-premise domain managers, allowing them to take advantage of the AWS Cloud benefits such as elasticity.

 AWS services such as [Amazon CloudWatch](https://aws.amazon.com/cloudwatch/) (CloudWatch) and Kinesis can be leveraged to manage OAM data from traditional network elements, given those elements are running on Linux. For example, CloudWatch agents can be installed on an NFx to collect standard metrics such as CPU utilization, as well as process custom metrics using StatsD or collectd protocols. The [Kinesis Client Library](https://docs.aws.amazon.com/streams/latest/dev/shared-throughput-kcl-consumers.html) (KCL) provides an easy-to-use programming model for processing data. This enables the processing of real-time configuration events and alarm events from NFx. With Prometheus Server Grafana Agent, you can also collect metrics from NFx, which provides Domain Manager with the ability to expose a real-time dashboard for analysis and view of the network it manages. [AWS Systems Manager](https://aws.amazon.com/systems-manager/) provides you with the capability to automate operational tasks across on-premise NFx as well as towards legacy OSS systems. Operators and ISVs can leverage System Manager Agent (SSM Agent) to apply security patches, create automated responses, etc.

 The proposed architecture enables you to migrate legacy domain managers from on-premise to AWS Cloud, and provides you with a path to leverage AWS services natively for OAM data.
