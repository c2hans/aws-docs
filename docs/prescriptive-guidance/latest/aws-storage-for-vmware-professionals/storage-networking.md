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
| Network protocols | + Fibre Channel<br />+ Internet Small Computer Systems Interface (iSCSI)<br />+ Network File System (NFS)<br />+ VMkernel ports for storage traffic | + S3 transfer acceleration<br />+ AWS PrivateLink<br />+ Private IPs<br />+ VPC endpoints |
| Network configuration | + Dedicated VMkernel interface for vSAN<br />+ Manual configuration of iSCSI initiators<br />+ Storage-specific virtual switches (vSwitches)<br />+ VMkernel network adapters | + AWS PrivateLink for private IP access<br />+ Integration with AWS network architecture<br />+ Private VPC access endpoints<br />+ VPC integration |
| Security | + iSCSI authentication—Challenge-Handshake Authentication Protocol (CHAP)<br />+ NFS permissions<br />+ vSphere permissions | + Access control list (ACL) bucket policies<br />+ IAM policies<br />+ Security groups<br />+ VPC endpoints |
| IP management | + Manual IP management<br />+ Static IP assignment to VMkernel adapters | + Automated IP management<br />+ Elastic IPs<br />+ Private IPs via VPC endpoints<br />+ VPC subnets |

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

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Prescriptive Guidance. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prescriptive-guidance` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
