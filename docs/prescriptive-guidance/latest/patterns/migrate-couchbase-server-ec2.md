---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/migrate-couchbase-server-ec2.html
---

# Migrate a Couchbase Server database to Amazon EC2
<a name="migrate-couchbase-server-ec2"></a>

*Subhani Shaik, Amazon Web Services*

## Summary
<a name="migrate-couchbase-server-ec2-summary"></a>

This pattern describes how you can migrate Couchbase Server from an on-premises environment to Amazon Elastic Compute Cloud (Amazon EC2) on AWS.

Couchbase Server is a distributed NoSQL (JSON document) database that provides relational database capabilities. Migrating a Couchbase Server database to AWS can provide increased scalability, improved performance, cost efficiency, enhanced security, simplified management, and global reach, which can benefit applications that require high availability and low latency data access. You also gain access to advanced features through AWS managed services.

Couchbase Server on AWS provides the following key features:
+ Memory-first architecture
+ High availability, disaster recovery, and load balancing
+ Multi-master, multi-Region deployment for optimal performance

For more information about key benefits, see the [Additional information](#migrate-couchbase-server-ec2-additional) section and the [Couchbase website](https://www.couchbase.com/partners/amazon/).

## Prerequisites and limitations
<a name="migrate-couchbase-server-ec2-prereqs"></a>

**Prerequisites**
+ An active AWS account with a virtual private cloud (VPC), two Availability Zones, private subnets, and a security group. For instructions, see [Create a VPC](https://docs.aws.amazon.com/vpc/latest/userguide/create-vpc.html) in the Amazon Virtual Private Cloud (Amazon VPC) documentation.
+ Connectivity enabled between source and target environments. For information about the TCX ports used by Couchbase Server, see the [Couchbase documentation](https://docs.couchbase.com/server/current/install/install-ports.html).

## Architecture
<a name="migrate-couchbase-server-ec2-architecture"></a>

The following diagram shows the high-level architecture for migrating Couchbase Server to AWS.

![Migration architecture for rehosting Couchbase Server on AWS.](https://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/images/pattern-img/4cedced2-3528-4f12-b19e-7d389e820cc1/images/ac22133a-895f-4999-b1e1-57f69e83a326.png)

From the on-premises Couchbase cluster, data moves through a customer gateway by using [AWS Direct Connect](https://aws.amazon.com/directconnect/). The data passes through a router and an Direct Connect route and reaches the VPC through an [AWS Virtual Private Network (Site-to-Site VPN)](https://aws.amazon.com/vpn/) gateway. The VPC contains an EC2 instance that is running Couchbase Server. The AWS infrastructure also includes [AWS Identity and Access Management (IAM)](https://aws.amazon.com/iam/) for access control, [AWS Key Management Service (AWS KMS)](https://aws.amazon.com/kms/) for data encryption, [Amazon Elastic Block Store (Amazon EBS)](https://aws.amazon.com/ebs/) for block storage, and [Amazon Simple Storage Service (Amazon S3)](https://aws.amazon.com/s3/) for data storage.

## Tools
<a name="migrate-couchbase-server-ec2-tools"></a>

**AWS services**
+ [Amazon Elastic Compute Cloud (Amazon EC2)](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/concepts.html) provides scalable computing capacity in the AWS Cloud. You can launch as many virtual servers as you need and quickly scale them up or down.
+ [AWS Direct Connect](https://docs.aws.amazon.com/directconnect/latest/UserGuide/Welcome.html) links your internal network to a Direct Connect location over a standard Ethernet fiber-optic cable. With this connection, you can create virtual interfaces directly to public AWS services while bypassing internet service providers in your network path.

## Best practices
<a name="migrate-couchbase-server-ec2-best-practices"></a>
+ [Installing and configuring Couchbase](https://docs.couchbase.com/server/current/install/install-intro.html) on different operating platforms
+ [Best practices](https://docs.couchbase.com/server/current/cloud/couchbase-cloud-deployment.html#aws-best-practices) for deploying Couchbase Server on AWS
+ [Creating a Couchbase cluster](https://docs.couchbase.com/server/current/manage/manage-nodes/create-cluster.html)
+ [Performance best practices](https://docs.couchbase.com/dotnet-sdk/current/project-docs/performance.html) for Couchbase applications
+ [Security best practices](https://docs.couchbase.com/server/current/learn/security/security-overview.html) for Couchbase Server
+ [Storage best practices](https://www.couchbase.com/forums/t/what-is-the-best-document-storage-strategy-in-couchbase/1573) for Couchbase Server databases

## Epics
<a name="migrate-couchbase-server-ec2-epics"></a>

### Deploy an Amazon EC2 instance for Couchbase Server
<a name="deploy-an-ec2-instance-for-couchbase-server"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Open the Amazon EC2 console. | Sign in to the [AWS Management Console](https://console.aws.amazon.com/) and open the [Amazon EC2 console](https://console.aws.amazon.com/ec2/). | DevOps engineer, Couchbase administrator |
| Deploy an Amazon EC2 instance. | Launch an EC2 instance that matches the on-premises Couchbase Server configurations. For more information about how to deploy an EC2 instance, see [Launch an Amazon EC2 instance](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/LaunchingAndUsingInstances.html) in the Amazon EC2 documentation. | DevOps engineer, Couchbase administrator |

### Install and configure Couchbase Server on Amazon EC2
<a name="install-and-configure-couchbase-server-on-ec2"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Install a Couchbase cluster. | Review [Couchbase Server deployment guidelines](https://docs.couchbase.com/server/current/install/install-production-deployment.html) before you install Couchbase Server on Amazon EC2.<br />To install Couchbase Server, see the [Couchbase Server documentation](https://docs.couchbase.com/server/current/install/install-intro.html) | Couchbase administrator |
| Configure the cluster. | To configure the cluster, see [Cluster Configuration Options](https://docs.couchbase.com/cloud/clusters/databases.html#cluster-configuration-options) in the Couchbase documentation. | Couchbase administrator |

### Add a new node and rebalance the Couchbase cluster
<a name="add-a-new-node-and-rebalance-the-couchbase-cluster"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Add a node for the EC2 instance. | Add the newly deployed EC2 instance that has Couchbase installed to the existing on-premises cluster. For instructions, see [Add a Node and Rebalance](https://docs.couchbase.com/server/current/manage/manage-nodes/add-node-and-rebalance.html) in the Couchbase Server documentation. | Couchbase administrator |
| Rebalance the cluster. | The rebalancing process makes the newly added node with the EC2 instance an active member of the Couchbase cluster. For instructions, see [Add a Node and Rebalance](https://docs.couchbase.com/server/current/manage/manage-nodes/add-node-and-rebalance.html) in the Couchbase Server documentation | Couchbase administrator |

### Reconfigure connections
<a name="reconfigure-connections"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Remove the on-premises nodes and rebalance. | You can now remove the on-premises nodes from the cluster. After removing the nodes, follow the rebalance process to redistribute data, indexes, event processing, and query processing among available nodes in the cluster. For instructions, see [Remove a Node and Rebalance](https://docs.couchbase.com/server/current/manage/manage-nodes/remove-node-and-rebalance.html) in the Couchbase Server documentation. | Couchbase administrator |
| Update connection parameters. | Update your application's connection parameters to use the new Amazon EC2 IP address, so your application can connect to the new node. | Couchbase application developer |

## Related resources
<a name="migrate-couchbase-server-ec2-resources"></a>
+ [Couchbase Server Services](https://docs.couchbase.com/server/current/learn/services-and-indexes/services/services.html)
+ [Deploy Couchbase Server Using AWS Marketplace](https://docs.couchbase.com/server/current/cloud/couchbase-aws-marketplace.html)
+ [Connect to Couchbase Server](https://docs.couchbase.com/server/current/guides/connect.html)
+ [Manage Buckets](https://docs.couchbase.com/server/current/manage/manage-buckets/bucket-management-overview.html)
+ [Cross Data Center Replication (XDCR)](https://docs.couchbase.com/server/current/learn/clusters-and-availability/xdcr-overview.html)
+ [Couchbase Inc. License Agreement](https://www.couchbase.com/LA20190115/)

## Additional information
<a name="migrate-couchbase-server-ec2-additional"></a>

**Key benefits**

Migrating your Couchbase database to AWS provides the following advantages:

**Scalability**. You can scale your Couchbase cluster up or down based on demand without having to manage physical hardware, so you can easily accommodate fluctuating data volumes and application usage. AWS provides:
+ Vertical and horizontal scaling options
+ [Global deployment](https://aws.amazon.com/about-aws/global-infrastructure/) capabilities
+ Load balancing across AWS Regions
+ [Database scaling solutions](https://aws.amazon.com/blogs/database/scaling-your-amazon-rds-instance-vertically-and-horizontally/)
+ [Content delivery](https://aws.amazon.com/solutions/content-delivery/) optimization

**Performance optimization**. AWS provides a high-performance network infrastructure and [optimized instance types](https://aws.amazon.com/ec2/instance-types/) to ensure fast data access and low latency for your Couchbase database.
+ [High performance computing (HPC)](https://aws.amazon.com/hpc/) options
+ Global content delivery through [Amazon CloudFront](https://aws.amazon.com/cloudfront/)
+ Multiple [storage options](https://aws.amazon.com/products/storage/)
+ Advanced [database services](https://aws.amazon.com/products/databases/), including Amazon Relational Database Service (Amazon RDS) and Amazon DynamoDB
+ Low-latency connections with [Direct Connect](https://aws.amazon.com/directconnect/)

**Cost optimization**. Select the appropriate instance type and configuration to balance performance and cost based on your workload. Pay only for the resources you use. This can potentially reduce your operational costs by eliminating the need to manage on-premises hardware and taking advantage of AWS Cloud economies of scale.
+ [Reserved instances ](https://aws.amazon.com/ec2/pricing/reserved-instances/)can help you plan ahead and reduce your costs substantially when you use Couchbase on AWS.
+ [Automatic scaling](https://aws.amazon.com/autoscaling/) prevents over-provisioning and helps you optimize your utilization and cost efficiencies.

**Enhanced security**. Benefit from the robust security features on AWS, such as data encryption, access controls, and security groups to help protect the sensitive data you store in Couchbase. Additional benefits:
+ The [AWS Shared Responsibility Model](https://aws.amazon.com/compliance/shared-responsibility-model/) clearly differentiates between the security *of* the cloud (AWS responsibility) and security *in* the cloud (customer responsibility).
+ [AWS compliance](https://aws.amazon.com/compliance/) supports major security standards.
+ AWS provides advanced [encryption](https://docs.aws.amazon.com/prescriptive-guidance/latest/encryption-best-practices/welcome.html) options.
+ [AWS Identity and Access Management (IAM)](https://aws.amazon.com/iam/) helps you manage secure access to your resources.

**Simplified management**. AWS provides managed services for Couchbase, so you can focus on application development instead of managing the underlying infrastructure.

**Global reach**. You can deploy your Couchbase cluster across multiple AWS Regions to achieve low latency for users around the world. You can deploy your databases entirely in the cloud or in a hybrid environment. You can safeguard your data with built-in enterprise-grade security and fast, efficient bidirectional synchronization of data from the edge to the cloud. At the same time, you can simplify development with a consistent programming model for building web and mobile apps.

**Business continuity**:
+ **Data backup and recovery**. In case of an issue, you can use [AWS Backup](https://aws.amazon.com/backup/) to ensure data resiliency and easy recovery. For disaster recovery options, see the [AWS Well-Architected Framework documentation](https://docs.aws.amazon.com/whitepapers/latest/disaster-recovery-workloads-on-aws/disaster-recovery-options-in-the-cloud.html).
+ **Couchbase multi-Region deployment**: To deploy a Couchbase database in a multi-Region AWS environment, you can subscribe to Couchbase Server in [AWS Marketplace](https://aws.amazon.com/marketplace/pp/prodview-zy5g2wqmqdyzw), use [AWS CloudFormation](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html)templates to create separate Couchbase clusters in each Region, and then configure cross-Region replication to synchronize data across Regions. This configuration ensures high availability and geographic redundancy across multiple Regions. For more information, see [Deploy Couchbase Server Using AWS Marketplace](https://docs.couchbase.com/server/current/cloud/couchbase-aws-marketplace.html) in the Couchbase documentation.

**Infrastructure agility**:
+ Rapid [resource provisioning](https://aws.amazon.com/products/management-and-governance/use-cases/provisioning-and-orchestration/) and deprovisioning
+ [Global infrastructure](https://aws.amazon.com/about-aws/global-infrastructure/regions_az/) reach
+ [Automatic scaling ](https://docs.aws.amazon.com/autoscaling/ec2/userguide/as-scale-based-on-demand.html)based on demand
+ [Infrastructure as Code (IaC)](https://aws.amazon.com/what-is/iac/) for consistent deployments
+ Multiple[ instance types ](https://aws.amazon.com/ec2/instance-types/)that are optimized for different workloads

**Innovation enablement**:
+ Access to the latest technologies, including [AI/ML](https://aws.amazon.com/ai/generative-ai/),[ IoT](https://aws.amazon.com/iot/), and [analytics](https://aws.amazon.com/big-data/datalakes-and-analytics/)
+ [Managed services](https://aws.amazon.com/blogs/architecture/reduce-operational-load-using-aws-managed-services-for-your-data-solutions/), which reduce operational overhead
+ [Modern application](https://aws.amazon.com/modern-apps/) development practices
+ [Serverless ](https://aws.amazon.com/serverless/)computing options

**Operational excellence**:
+ [Centralized monitoring and logging](https://docs.aws.amazon.com/prescriptive-guidance/latest/designing-control-tower-landing-zone/logging-monitoring.html)
+ [Automated resource management](https://aws.amazon.com/systems-manager/)
+ [Predictive maintenance](https://aws.amazon.com/what-is/predictive-maintenance/) capabilities
+ [Enhanced visibility](https://aws.amazon.com/about-aws/whats-new/2024/12/amazon-cloudwatch-provides-centralized-visibility-telemetry-configurations/) into resource usage
+ [Streamlined deployment processes](https://aws.amazon.com/blogs/mt/streamline-change-processes-and-improve-governance-with-aws-well-architected/)

**Modernization opportunities**:
+ [Microservices](https://aws.amazon.com/microservices/) architecture
+ [DevOps](https://aws.amazon.com/devops/) practices implementation
+ [Cloud-native](https://aws.amazon.com/what-is/cloud-native/) application development
+ [Legacy application modernization](https://docs.aws.amazon.com/prescriptive-guidance/latest/strategy-modernizing-applications/welcome.html)

**Competitive advantages**:
+ [Faster time to market](https://aws.amazon.com/blogs/smb/accelerate-time-to-market-and-business-growth-with-an-automated-software-as-a-service-platform/)
+ Improved[ customer experience](https://aws.amazon.com/blogs/publicsector/improving-customer-experience-for-the-public-sector-using-aws-services/)
+ [Data-driven](https://aws.amazon.com/data/data-driven-decision-making/) decision-making
+ Enhanced [business intelligence](https://aws.amazon.com/what-is/business-intelligence/)
