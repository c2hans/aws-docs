---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/transitioning-from-vmware-to-the-aws-cloud/application-rehosting.html
---

# Application rehosting

Organizations can rehost their existing VMware virtual machines, datastore storage, and virtual networks to the AWS Cloud, where business applications can operate efficiently. The following topics provide guidance for rehosting your existing VMware workloads to AWS services across compute, storage, and network components.

## Rehosting virtual machines to the AWS Cloud
<a name="rehosting-virtual-machines"></a>

Amazon Elastic Compute Cloud (Amazon EC2) instances and VMware vSphere virtual machines (VMs) differ fundamentally in their architecture and storage approach. vSphere VMs store data as file sets such as Virtual Machine Disk (VMDK). Amazon EC2 instances use Amazon Machine Images (AMIs) and Amazon Elastic Block Store (Amazon EBS) volumes.

Organizations can migrate to AWS by using AWS Transform MGN, which supports VM migration from any supported operating system to Amazon EC2.

The following key elements highlight the architectural and operational differences between vSphere VMs and Amazon EC2 instances:
+ **File format** – In vSphere, virtual machines are organized as a collection of files. These files include the .vmx file that handles configuration settings and .vmdk files that contain the virtual disk data. Also included are various auxiliary files (.nvram, .vmsd, .vmsn, and .vmss) that manage different VM states and functions. In contrast, Amazon EC2 doesn't rely on specific file formats. Instead, Amazon EC2 uses Amazon Machine Images (AMIs) as templates that contain all the necessary information and configurations needed to launch instances.
+ **Storage** – In vSphere, the complete virtual machine environment—including the operating system, applications, and data—is consolidated within .vmdk virtual disk files. The .vmdk files are stored in datastores and managed through vSAN volumes. Amazon EC2, however, uses a more modular approach where the instance's root volume is created from an AMI snapshot and stored as an [Amazon EBS volume](https://docs.aws.amazon.com/ebs/latest/userguide/ebs-volumes.html). This approach provides the flexibility to attach additional EBS volumes or instance store volumes as needed.
+ **Portability** – AMIs from the existing instance can be copied or shared across different AWS Regions or AWS accounts.
+ **Scalability** – Amazon EC2 offers dynamic scaling capabilities. Its auto scaling features can automatically adjust the number of instances based on demand, enabling seamless scaling up or down in response to workload requirements.
+ **Snapshots and backups** – Amazon EC2 takes a volume-centric approach, allowing for independent creation of EBS volume snapshots, which can then be used to create new volumes or AMIs. Integrated AWS services complement this Amazon EC2 capability, such as AWS Backup for comprehensive backup management.
+ **Management** – AWS provides multiple management options including the graphical [AWS Management Console](https://docs.aws.amazon.com/awsconsolehelpdocs/latest/gsg/what-is.html), the [AWS Command Line Interface (AWS CLI)](https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-welcome.html), [AWS SDKs](https://docs.aws.amazon.com/sdkref/latest/guide/overview.html), and infrastructure as code (IaC) through [AWS CloudFormation](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html). These options offer greater flexibility in how users interact with and manage their resources.

For containerized workloads, VMware provides vSphere with Tanzu Platform, which enables you to run and manage containerized applications alongside traditional virtual machines in your existing infrastructure. AWS provides multiple container services that help you deploy, manage, and scale containers in the cloud.

The following recommendations can help you identify which AWS container service aligns most closely with your workload requirements:
+ **Amazon Elastic Container Registry** – Use Amazon ECR with any AWS container orchestration service to store your container images. For more information, see the [Amazon ECR documentation](https://docs.aws.amazon.com/AmazonECR/latest/userguide/what-is-ecr.html).
+ **Amazon Elastic Container Service** – Use Amazon ECS to break monolith apps into microservices, migrate to the cloud, or run batch processing workloads. For more information, see the [Amazon ECS documentation](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/Welcome.html).
+ **Amazon Elastic Kubernetes Service** – Use Amazon EKS to run Kubernetes on AWS, build hybrid applications across the cloud and on premises, or deploy machine learning (ML) models. For more information, see the [Amazon EKS documentation](https://docs.aws.amazon.com/eks/latest/userguide/what-is-eks.html).
+ **AWS Fargate** – Use Fargate with Amazon ECS to launch serverless containers or build a platform as a service (PaaS). For more information, see the [Fargate documentation](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/AWS_Fargate.html).
+ **Amazon Elastic Compute Cloud** – Use Amazon EC2 with any of the AWS management services for the maximum control over your launch type. For more information, see the [Amazon EC2 documentation](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/concepts.html).

For more detailed information about AWS containers and suitable options for your organization, see [Containers on AWS](https://aws.amazon.com/containers/).

## Rehosting datastores to the AWS Cloud
<a name="rehosting-datastores"></a>

You can migrate VMware vSphere datastores, which function as storage repositories for virtual machine files and other data, to AWS storage services.

When moving data to the cloud, it's important to understand where you're moving it, the potential use cases, the type of data you're moving, and the network resources available. Your organization can choose from among several AWS services, based on your storage needs and workload characteristics:
+ For persistent block storage, consider Amazon Elastic Block Store (Amazon EBS).
+ For scalable file storage, consider Amazon Elastic File System (Amazon EFS).
+ For object storage, consider Amazon Simple Storage Service (Amazon S3).

For block-level storage, you can migrate VMware VMFS and vSAN datastores to Amazon EBS, which provides persistent storage volumes for EC2 instances. You can migrate existing Server Message Block (SMB) or Network File System (NFS) servers to Amazon FSx to reduce operational overheads, take advantage of elastic scaling, and increase availability. Amazon FSx is compatible with NetApp ONTAP, Windows File Server, Lustre, and OpenZFS. For modern file sharing services that don't require configuration of SMB or NFS, Amazon EFS is a serverless, fully elastic, fully managed file storage solution.

The following table highlights storage options that are optimized for specific circumstances. Use it to help determine the option that's appropriate for your use case.

|  |  |  |
| --- |--- |--- |
| Storage type | What is it optimized for? | AWS storage services or tools |
| Block | Applications that require low-latency, high-performance durable storage attached to single Amazon EC2 instances or containers, such as databases and general-purpose local instance storage. | [Amazon EBS](https://docs.aws.amazon.com/ebs/latest/userguide/what-is-ebs.html)<br />[Amazon EC2 instance store](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/InstanceStorage.html) |
| File system | Applications and workloads that require shared read and write access across multiple Amazon EC2 instances or containers or from multiple on-premises servers. Examples include team file shares, highly available enterprise applications, analytics workloads, and ML training. | [Amazon EFS](https://docs.aws.amazon.com/efs/latest/ug/whatisefs.html)<br />[Amazon FSx](https://docs.aws.amazon.com/fsx/)<br />[Amazon FSx for Lustre](https://docs.aws.amazon.com/fsx/latest/LustreGuide/what-is.html)<br />[Amazon FSx for NetApp ONTAP](https://docs.aws.amazon.com/fsx/latest/ONTAPGuide/what-is-fsx-ontap.html)<br />[Amazon FSx for OpenZFS](https://docs.aws.amazon.com/fsx/latest/OpenZFSGuide/what-is-fsx.html)<br />[Amazon FSx for Windows File Server](https://docs.aws.amazon.com/fsx/latest/WindowsGuide/what-is.html)<br />[Amazon S3 File Gateway](https://docs.aws.amazon.com/filegateway/latest/files3/what-is-file-s3.html)<br />[Amazon FSx File Gateway](https://docs.aws.amazon.com/filegateway/latest/filefsxw/what-is-file-fsxw.html) |
| Object | Read-heavy workloads such as content distribution, web hosting, big data analytics, and ML workflows. Well-suited for scenarios where data needs to be stored, accessed, and distributed globally over the internet. | [Amazon S3](https://docs.aws.amazon.com/AmazonS3/latest/userguide/GetStartedWithS3.html) |
| Cache | Fully managed, scalable, and high-speed cache on AWS for processing file data that's stored in disparate locations. Examples include on-premises NFS file systems, and/or in cloud file systems (FSx for OpenZFS or FSx for ONTAP), and Amazon S3. | [Amazon File Cache](https://docs.aws.amazon.com/fsx/latest/FileCacheGuide/getting-started.html) |
| Hybrid/Edge | Deliver low-latency data to on-premises applications and provide on-premises applications access to cloud-backed storage. | [AWS Storage Gateway Tape Gateway](https://docs.aws.amazon.com/storagegateway/latest/tgw/WhatIsStorageGateway.html)<br />[AWS Storage Gateway Volume Gateway](https://docs.aws.amazon.com/storagegateway/latest/vgw/WhatIsStorageGateway.html) |

The following table provides a detailed look at your online and offline options.

|  |  |  |  |
| --- |--- |--- |--- |
| Migration options | When speed is the priority | When bandwidth is important | AWS storage services or tools |
| Online | Online is optimized for frequent updates to data. Use it for time-critical or ongoing workloads. | Consider scheduling your transfer during off hours when you have sufficient bandwidth. | [AWS DataSync](https://docs.aws.amazon.com/datasync/latest/userguide/setting-up.html)<br />[AWS Transfer Family](https://docs.aws.amazon.com/transfer/latest/userguide/getting-started.html)<br />[FSx for ONTAP SnapMirror](https://docs.aws.amazon.com/fsx/latest/ONTAPGuide/scheduled-replication.html)<br />[Storage Gateway](https://docs.aws.amazon.com/storagegateway/) |
| Offline | Suitable for one-time or periodic uploads—and when data can be static in transit. | This choice makes sense when you need to use only the minimum available bandwidth—and you prefer the predictability of physical moves. | [AWS Snowball](https://aws.amazon.com/snowball/) |

For more information about storage options, see the AWS Decision Guide [Choosing an AWS storage service](https://docs.aws.amazon.com/decision-guides/latest/storage-on-aws-how-to-choose/choosing-aws-storage-service.html).

## Rehosting virtual networks to the AWS Cloud
<a name="rehosting-virtual-network"></a>

VMware virtual networking capabilities can be redesigned for AWS by using Amazon Virtual Private Cloud (Amazon VPC). You can manage the IP address usage of the resources running in your VPCs by using Amazon VPC IP Address Manager (IPAM). Amazon VPC provides logically isolated virtual networks with configurable subnets, routing tables, and security groups for traffic control and additional protection through AWS Network Firewall and Web Application Firewall. Amazon VPC doesn't require configuration of port groups or VLAN tagging unlike existing on-premises VMware vSwitch. The AWS approach makes management simpler while maintaining functionality. For more information, see [How Amazon VPC works](https://docs.aws.amazon.com/vpc/latest/userguide/how-it-works.html).

With AWS Transit Gateway, you can connect VPCs, AWS accounts, and on-premises networks to a single gateway. Transit Gateway acts as a cloud router, managing traffic between VPCs and on-premises networks through a central hub. With this capability, you can design and implement networks at scale.

AWS offers services and tools to help organizations maintain network monitoring and visibility, such as Amazon CloudWatch, AWS CloudTrail, Reachability Analyzer, Amazon VPC Lattice, and VPC Flow Logs. Organizations can use these integrated services and tools to get the required insights from application networking.

For VMware NSX specific use cases, AWS offers a different approach by managing the underlying network infrastructure, eliminating the need for complex network virtualization management. To address sophisticated networking requirements, you can deploy AWS networking and security services either individually or in combination. With this flexibility, organizations can redirect their focus from infrastructure maintenance to business-driven objectives.

The following table provides an overview of AWS networking and content delivery services that are optimized for specific scenarios.

|  |  |  |
| --- |--- |--- |
| Service category | What is it optimized for? | AWS networking and content delivery services |
| Network foundations | Getting started with AWS networking services and connecting your VPCs securely. | [Amazon VPC](https://docs.aws.amazon.com/vpc/latest/userguide/what-is-amazon-vpc.html)<br />[AWS PrivateLink](https://docs.aws.amazon.com/vpc/latest/privatelink/what-is-privatelink.html)<br />[AWS Transit Gateway](https://docs.aws.amazon.com/vpc/latest/tgw/what-is-transit-gateway.html) |
| Global and hybrid connectivity | Help to ensure private, secure, and global network connectivity. | [AWS Client VPN](https://docs.aws.amazon.com/vpn/latest/clientvpn-user/client-vpn-user-what-is.html)<br />[AWS Cloud WAN](https://docs.aws.amazon.com/network-manager/latest/cloudwan/what-is-cloudwan.html)<br />[AWS Direct Connect](https://docs.aws.amazon.com/directconnect/latest/UserGuide/Welcome.html)<br />[AWS Site-to-Site VPN](https://docs.aws.amazon.com/vpn/latest/s2svpn/VPC_VPN.html) |
| Edge networking and content delivery | Low latency, reliable traffic routing to and from your workloads. | [Amazon CloudFront](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/Introduction.html)<br />[AWS Global Accelerator](https://docs.aws.amazon.com/global-accelerator/latest/dg/what-is-global-accelerator.html)<br />[Amazon Route 53](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/Welcome.html)<br />[AWS Data Transfer Terminal](https://docs.aws.amazon.com/datatransferterminal/latest/userguide/what-is-dtt.html) |
| Application networking | Help to ensure that your workloads are highly available, adapt to demand, and can communicate with each other. | [Amazon API Gateway](https://docs.aws.amazon.com/apigateway/latest/developerguide/welcome.html)<br />[Amazon VPC IPAM](https://docs.aws.amazon.com/vpc/latest/ipam/what-it-is-ipam.html)<br />[Amazon VPC Lattice](https://docs.aws.amazon.com/vpc-lattice/latest/ug/what-is-vpc-lattice.html)<br />[Elastic Load Balancing](https://docs.aws.amazon.com/elasticloadbalancing/latest/userguide/what-is-load-balancing.html) |
| Network security and remote access | Protect your workloads against malware, DDoS, SQL injection, and cross-site scripting attacks. | [AWS Firewall Manager](https://docs.aws.amazon.com/waf/latest/developerguide/fms-chapter.html)<br />[AWS Network Firewall](https://docs.aws.amazon.com/network-firewall/latest/developerguide/what-is-aws-network-firewall.html)<br />[AWS Shield](https://docs.aws.amazon.com/waf/latest/developerguide/shield-chapter.html)<br />[AWS Verified Access](https://docs.aws.amazon.com/verified-access/latest/ug/what-is-verified-access.html)<br />[AWS WAF](https://docs.aws.amazon.com/waf/latest/developerguide/waf-chapter.html) |

For more information, see the AWS Decision Guide [Choosing an AWS networking and content delivery service](https://docs.aws.amazon.com/decision-guides/latest/networking-on-aws-how-to-choose/choosing-networking-and-content-delivery-service.html?did=wp_card&trk=wp_card).
