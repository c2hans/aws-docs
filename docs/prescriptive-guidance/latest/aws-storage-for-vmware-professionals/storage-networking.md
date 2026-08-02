---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/aws-storage-for-vmware-professionals/storage-networking.html
---

# Storage networking
<a name="storage-networking"></a>

In VMware environments, storage networking connects ESXi hosts to shared storage systems using protocols like iSCSI, Fibre Channel, and NFS. In contrast, AWS integrates storage services directly within its virtual private cloud (VPC) architecture, eliminating the need for separate storage networking infrastructure. AWS storage services are accessed through service endpoints with built-in security controls and network configurations, as detailed in the following table.

|
|
| Aspect | VMware | AWS |
| --- |--- |--- |
| Network protocols | Fibre ChannelInternet Small Computer Systems Interface (iSCSI)Network File System (NFS)VMkernel ports for storage traffic | S3 transfer accelerationAWS PrivateLinkPrivate IPsVPC endpoints |
| Network configuration | Dedicated VMkernel interface for vSANManual configuration of iSCSI initiatorsStorage-specific virtual switches (vSwitches)VMkernel network adapters | AWS PrivateLink for private IP accessIntegration with AWS network architecturePrivate VPC access endpointsVPC integration |
| Security | iSCSI authentication—Challenge-Handshake Authentication Protocol (CHAP)NFS permissionsvSphere permissions | Access control list (ACL) bucket policiesIAM policiesSecurity groupsVPC endpoints |
| IP management | Manual IP managementStatic IP assignment to VMkernel adapters | Automated IP managementElastic IPsPrivate IPs via VPC endpointsVPC subnets |

As described in the following table, VMware and AWS networking architectures differ in their approaches to configuration, management, and security.

|
|
| Aspect | VMware | AWS |
| --- |--- |--- |
| Configuration | Relies on vSphere (ESXi hosts and vCenter) for configuring VMkernel ports, virtual switches, and explicit protocol setup (iSCSI, NFS, Fibre Channel) | Uses an automated approach that integrates VPCs with endpoint configurations, which requires less manual work |
| Management | Requires manual IP assignment and management through VMkernel adapters | Offers flexibility through elastic IPs and automated IP management through VPC subnets |
| Networking | Uses traditional security methods like Challenge Handshake Authentication Protocol (CHAP) and protocol-specific permissions | Implements a comprehensive security model with IAM, security groups, and multiple layers of access control through VPC endpoints and policies |

AWS handles storage networking with seamless integration into its virtual private cloud (VPC) architecture. Storage services are accessed through service endpoints with built-in security controls and network configurations.
+ **Amazon EFS access points –** Amazon EFS uses mount targets within each Availability Zones for network connectivity and access points to manage application-specific controls. Amazon EFS supports the NFS protocols, making it compatible with legacy systems that require file-level storage.
+ **AWS PrivateLink and Amazon S3 transfer acceleration –** For enhanced security and performance, AWS PrivateLink connects to AWS services using private IP addresses. Amazon S3 provides transfer acceleration, which optimizes upload speeds by routing traffic through Amazon CloudFront edge locations.
+ **VPC endpoints for Amazon S3 and Amazon EFS –** Amazon VPC provides endpoints that allow instances to privately access Amazon S3 and Amazon EFS without traversing the public internet. This reduces latency and improves security by keeping traffic within the AWS network.
