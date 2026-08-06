---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/aws-storage-for-vmware-professionals/security-features.html
---

# Security
<a name="security-features"></a>

VMware implements security through vCenter's role-based access controls, vSAN encryption, VM-level security policies, and integration with enterprise identity systems. AWS adheres to a shared responsibility model that provides integrated security layers across storage services.

AWS manages security through AWS Identity and Access Management (IAM), encryption at rest and in transit, VPC network isolation, and automated monitoring through AWS CloudTrail and Amazon GuardDuty. AWS provides resource-level access controls through IAM policies and resource-based policies, managed encryption keys via AWS KMS, and real-time threat detection that scales automatically with infrastructure changes.

The following table summarizes the security configurations and characteristics of VMware and AWS.

|
|
| Aspect | VMware | AWS |
| --- |--- |--- |
| Access control | + Role-based access control (RBAC)<br />+ vSphere permissions | + ACLs<br />+ S3 bucket policies<br />+ IAM<br />+ Security groups |
| Encryption | + External key management server integration<br />+ VM encryption at hypervisor level<br />+ vSAN datastore encryption | + EBS volume encryption<br />+ EFS encryption (at rest and in transit)<br />+ AWS KMS integration<br />+ S3 server-side encryption (SSE) |
| Security monitoring and auditing | + Third-party Security Information and Event Management (SIEM) integration<br />+ vCenter/ESXi event logs<br />+ vRealize Log Insight<br />+ vSAN audit logs | + GuardDuty threat detection<br />+ S3 access logs<br />+ CloudTrail<br />+ AWS Config |
| Data protection | + Critical system file restrictions<br />+ Disabling unnecessary services<br />+ Security patches<br />+ VM hardening | + Blocking S3 public access<br />+ Encryption in transit (SSL/TLS)<br />+ Multi-factor authentication<br />+ VPC endpoints |

The following table provides a detailed comparison of security implementations between VMware and AWS environments, focusing on access control, encryption, monitoring, and data protection approaches.

|
|
| Aspect | VMware | AWS |
| --- |--- |--- |
| Access control | Implements traditional hierarchical security through RBAC, where administrators define user permissions and roles within vSphere. This allows granular control over who can access specific datastores and perform storage-related operations. | Implements a comprehensive approach using IAM, providing fine-grained access control through policies and roles. The combination of bucket policies, ACLs, and security groups offers layers of access control, making it more flexible and scalable than VMware. |
| Encryption | Relies on hypervisor-level encryption for VMs and vSAN datastores, requiring integration with external key management servers. This approach provides strong security but requires manual configuration and management. | Provides built-in encryption capabilities across all storage services. AWS offers encryption options including server-side encryption for S3, EBS volumes, and AWS KMS integration for key management. |
| Monitoring and auditing | Uses vCenter and ESXi logs and consolidates them through Aria Operations for Logs with the ability to integrate third-party SIEM tools for enhanced monitoring. This provides traditional datacenter monitoring and auditing capabilities. | Offers comprehensive monitoring through native services like CloudTrail for API activity tracking, GuardDuty for threat detection, and AWS Config for configuration monitoring. These services provide automated, real-time monitoring and alerting capabilities. |
| Data protection | VMware focuses on VM-level protection through hardening practices and system-level security controls, following a traditional security approach. | Implements layers of protection including network-level controls (VPC endpoints), transport-level security (SSL/TLS), and additional features like S3 block public access. |

## Service-specific security
<a name="service-specific-security.bc397029-9af1-5a5d-b908-e1fa537d894e"></a>

**Amazon EBS encryption –** AWS provides transparent encryption for Amazon EBS volumes at rest and in transit between volumes and instances. Amazon EBS volumes support multiple configurations including standalone and RAID setups, with capabilities for cross-AZ migration through snapshots and dynamic resizing without instance downtime.

**Amazon S3 security –** Amazon S3 enforces encryption using server-side encryption options like SSE-S3 (AWS managed keys), SSE-KMS (customer-managed keys), and SSE-C (customer-provided keys). Access controls include bucket policies, ACLs, and public access blocking to prevent unauthorized exposure.

**Amazon EFS security –** Amazon EFS provides encryption for data at rest and in transit, with access control managed through IAM policies and VPC security groups to restrict file system access to authorized users and services.
