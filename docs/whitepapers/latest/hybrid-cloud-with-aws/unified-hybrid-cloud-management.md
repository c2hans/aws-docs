---
source_url: https://docs.aws.amazon.com/whitepapers/latest/hybrid-cloud-with-aws/unified-hybrid-cloud-management.html
---

 This whitepaper is for historical reference only. Some content might be outdated and some links might not be available.

# Unified hybrid cloud management
<a name="unified-hybrid-cloud-management"></a>

 The hybrid cloud management layer provides a unified set of interfaces to consume hybrid cloud services like compute, storage, networking, databases, analytics, and others. These interfaces provide capabilities for provisioning, editing, deleting, monitoring, and operating resources and services on the hybrid cloud. This section describes design practices, components, and AWS services that address the needs of building a unified hybrid cloud management layer in support of hybrid cloud services.

 [AWS Outposts](https://aws.amazon.com/outposts/) natively provides unified hybrid cloud management through the use of the same APIs and management tools across on-premises and AWS infrastructure. AWS Outposts supports [several AWS services](https://aws.amazon.com/outposts/features/), including compute, storage, networking, and higher-level services allowing consistent operations across the hybrid cloud, eliminating the need to build and manage custom software.

## Compute services
<a name="compute-services"></a>

 Compute services in the hybrid cloud provide the interfaces to manage compute (instances, containers, functions) resources. Figure 2 provides an example customer software implementation of a unified management interface for compute services.

 In this example, a hybrid cloud user authenticates with the Identity, security, and access management service of the hybrid cloud to gain authorization to the management interfaces of the compute service. The compute service provides a unified provisioning, monitoring, and operating interface for the user. Internally, the compute service interacts with the core fleet or device management layer for on-premises infrastructure management, [AWS EC2 APIs](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/Welcome.html) for EC2 management, as well as the core services of metrics and logging services for metrics and logging needs and identity, security and access management for gaining access authorization to on-premises and AWS resources through their respective APIs.

![Example of compute service on a hybrid cloud](http://docs.aws.amazon.com/whitepapers/latest/hybrid-cloud-with-aws/images/compute-example-hybrid-cloud.png)

* Example of compute service on a hybrid cloud *

 A consistent mechanism for managing guest operating systems on AWS instances and in on-premises virtual machines across the hybrid cloud provides seamless operations for activities such as software/patch management and policy enforcement. You can manage on-premises servers and AWS EC2 instances with [AWS Systems Manager](https://aws.amazon.com/systems-manager/). Systems Manager provides several [features](https://aws.amazon.com/systems-manager/features/), such as remote command execution, patch management, inventory management, state management, and automation, to help with host management functions.

## Storage services
<a name="storage-services"></a>

 Outside of providing core storage services for block, file, and objects, hybrid cloud use-cases often require moving data between on-premises data centers and AWS. These use cases are cloud bursting for storage, disaster recovery (data replication and backups), distributed data processing (for analytics processing on AWS), or geographic expansion (move data closer to customers). Data movement is required for files, block storage, transactional data in databases, and streaming data.
+  **Files**: The [File Gateway](https://aws.amazon.com/storagegateway/file/) interface[, AWS DataSync](https://aws.amazon.com/datasync/), [AWS Transfer for SFTP](https://aws.amazon.com/sftp/), [Amazon EFS](https://aws.amazon.com/efs/), [Amazon FSx for Lustre](https://aws.amazon.com/fsx/lustre/), and [Amazon FSx for Windows File Server](https://aws.amazon.com/fsx/windows/) are used for integrating files between the environments and enabling cloud bursting, disaster recovery, and application migration use-cases.
+  **Block storage**: [Volume Gateway](https://aws.amazon.com/storagegateway/volume/) provides an on-premises iSCSI interface to provide S3-based storage in AWS (in gateway-cache mode). [AWS Storage Gateway](https://aws.amazon.com/storagegateway) can be used for cloud bursting, storage extension, migration, or backups of block stores.
+  **Transactional data**: [AWS Database Migration Service](https://aws.amazon.com/dms/) (AWS DMS) provides integration between on-premises SQL/NoSQL databases and AWS-based databases (on EC2 or AWS RDS, DynamoDB, DocumentDB) by providing migration and synchronization between the databases. Additionally, DMS can be used to migrate data from on-premises databases to S3 directly for analytics workflow integration.
+  **Streaming data**: Streaming records from on-premises data centers and AWS sources can be collected and analyzed in managed stream stores on AWS, including [Amazon Kinesis](https://aws.amazon.com/kinesis/) and [Amazon MSK](https://aws.amazon.com/msk/).

 The AWS Outposts service also provides on-premises storage with EBS. [S3 on AWS Outposts](https://aws.amazon.com/s3/outposts/) enables customers to store object data on premises using the S3 API.

## Networking and security services
<a name="networking-and-security-services"></a>

 Networking and security services enable you to create and manage networks for applications and secure them on the hybrid cloud. A few major components are discussed here:
+  **Virtual Networking**: Virtual networking enables you to provision logically isolated sections of the infrastructure where they can launch resources. You can define your own IP addressing, subnets, routing policies, securities, and gateways in the virtual network based on the application requirements. On the hybrid cloud, these virtual networks extend between AWS and on-premises infrastructures, allowing applications to function across the environment.

   [Amazon VPC](https://aws.amazon.com/vpc/) enables you to create virtual networks in AWS Regions. [AWS Direct Connect](https://docs.aws.amazon.com/directconnect/latest/UserGuide/WorkingWithVirtualInterfaces.html) private virtual interfaces (VIFs), transit VIFs, and [site-to-site VPN](https://docs.aws.amazon.com/vpn/latest/s2svpn/VPC_VPN.html) provide mechanisms to extend the virtual network between Amazon VPC and on-premises networks.
+  **Load balancing**: In a hybrid environment, load balancers are used to distribute traffic to targets across on-premises and public cloud environments. Load balancers abstract the location of the physical resources in the hybrid cloud by presenting a unified front end for an application service. [AWS Application Load Balancer](https://docs.aws.amazon.com/elasticloadbalancing/latest/application/introduction.html) and [Network Load Balancer](https://docs.aws.amazon.com/elasticloadbalancing/latest/network/introduction.html), deployed in AWS regions, support targets in AWS regions as well as on-premises. They also support containers as targets deployed across the hybrid environment. Application load balancing on AWS Outposts is fully managed, operates in a single subnet, and scales automatically up to the capacity available on the Outposts rack to meet varying levels of application load without manual intervention.
+  **Unified DNS**: As a best practice, internal DNS resolutions for applications and services deployed in virtual networks on the hybrid cloud must be unified across the infrastructure. [AWS Route53 resolver and conditional forwarding rules](https://aws.amazon.com/blogs/security/simplify-dns-management-in-a-multiaccount-environment-with-route-53-resolver/) provide a mechanism to unify DNS resolutions across on-premises DNS servers and resolvers hosted on AWS.

   For public DNS resolutions, internet traffic is routed to the front-ends of web applications deployed on the hybrid cloud through public DNS services like Amazon Route53. In the hybrid cloud, the application front ends (implemented using load balancers or API endpoints on instances) reside either on-premises, in AWS Regions, or split across the infrastructure. AWS Route53 features routing mechanisms for active-backup and active-active hybrid environments.
+  **Infrastructure Security**: Infrastructure security in a hybrid cloud must be applied to all layers of the technology stack across both on-premises and AWS environments. These layers include security at the edge network, perimeter, load balancers, network devices, host and guest operating systems, applications, virtual networks, subnets, and compute. Customers require a common set of security policies that they can apply to AWS or on-premises infrastructure. AWS provides tools like [AWS Web Application Firewall](https://aws.amazon.com/waf/) (WAF), [AWS Shield](https://aws.amazon.com/shield/), [VPC Security Groups](https://docs.aws.amazon.com/vpc/latest/userguide/VPC_SecurityGroups.html), and [VPC Network ACLs](https://docs.aws.amazon.com/vpc/latest/userguide/vpc-network-acls.html) to enforce security boundaries.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Whitepapers. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query whitepapers` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
