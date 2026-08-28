---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/security-reference-architecture-iot/industrial-isolation.html
---

# Capability 2. Providing an industrial isolation zone between environments
<a name="industrial-isolation"></a>

|  |
| --- |
| Influence the future of the AWS Security Reference Architecture (AWS SRA) by taking a [short survey](https://amazonmr.au1.qualtrics.com/jfe/form/SV_e3XI1t37KMHU2ua). |

This capability supports best practice 2 from the [AWS SRA best practices for IoT](iot-sra.md#iot-sra-best-practices).

Organizations are increasingly connecting OT and IIoT systems to cloud environments. This convergence brings numerous benefits but also introduces unique security challenges. It also requires strict separation between OT, IIoT, and IT environments to limit the potential for attacks to OT or IT systems from affecting business systems for critical infrastructure. A single AWS organization that includes multiple AWS accounts can meet the requirements for implementing this strict separation by using an Industrial Isolation account and separate OUs, separate AWS accounts, and careful configuration of networking between accounts (separate VPCs, AWS Transit Gateway routing, and network inspection firewalls). This approach provides a secure foundation for integrating industrial systems with cloud services while maintaining the strict security and operational requirements that are inherent to OT environments. By implementing this capability, organizations can take advantage of the scalability and advanced services provided by AWS while preserving the integrity, availability, and security of their critical industrial operations.

## Rationale
<a name="industrial-isolation-rationale"></a>

Establishing a separate OU within the AWS organization that is dedicated to IoT, IIoT, and cloud-connected OT workloads helps enhance security by enabling segregation from traditional IT environments. This approach allows organizations to:
+ Directly apply OT security principles and standards to the AWS environment.
+ Accommodate different risk toleration between OT and IT teams.
+ Limit potential impact of security incidents.
+ Enable clear separation of duties between OT and IT personnel.

When you use a dedicated OU for IoT, IIoT, and OT along with segregated networking by using separate VPC configurations to connect VPCs that span multiple accounts, the OU should have the following characteristics:
+ Segregated network architectures should be provided for both the IoT (or OT or IIoT) and the industrial isolation workloads.
+ The OT or IIoT environment within the landing zone should be designed to align with the security requirements that are outlined in ISA/IEC 62443 and NIST SP 800-82 for industrial control systems and operational technology.
+ The Industrial Isolation account should act as a dedicated security perimeter between the OT (or IIoT) environment and the IT environment, and should follow the NIST SP 800-82 guidance on network segmentation and the use of demilitarized zones.
+ The landing zone should have segregated identities or roles, defined within the identity infrastructure, which are separate from IT identities or roles. You can implement these as separate identity center assignments within the AWS IAM Identity Center instance for the AWS organization, to manage access and permissions for the OT (or IIoT) and Industrial Isolation account resources in parallel with the IT environment.
+ The identity and access management policies in the landing zone should be tailored to the unique needs and risk profiles of the OT, IIoT, and industrial isolation components, which might differ from traditional IT environments.
+ The OU should also host services and resources that facilitate secure communication, remote access, and data exchange between the OT (or IIoT) and IT domains, while maintaining strict access controls and monitoring mechanisms.

This separation also creates the opportunity for further enhancements to the security posture of these workloads, by integrating relevant IIoT services and features that are available on AWS, such as AWS IoT Core, AWS IoT Greengrass, AWS IoT Device Defender, AWS IoT Device Management, AWS IoT SiteWise, and AWS IoT TwinMaker. These services help provide secure connectivity, data management, and analytics capabilities that are tailored for the OT and IIoT environments.

For example, the ISA/IEC 62443 standard defines the security requirements for industrial automation and control systems, and NIST SP 800-82 provides guidance on securing industrial control systems, including recommendations for network architecture, remote access, and patch management. By aligning the design and configuration of the dedicated OT portions of the organization with the ISA/IEC 62443 standards and the NIST SP 800-82 guide, organizations can ensure that security controls such as network segmentation, access management, and device hardening are implemented consistently across all components of their AWS landing zone. This can help organizations bridge the gap between traditional IT security and the specific requirements of cloud-connected OT and IIoT systems.

Additional benefits include:
+ **Isolation of OT and IT workloads**: Separate OUs, AWS accounts, and networking configurations allow for better isolation of OT and IT workloads, and ensure that the security, access controls, and resource configurations can be tailored to the specific requirements of each domain. This helps mitigate the risk of cross-contamination, reduces the scope of impact, and ensures that the unique needs of OT and IT systems are addressed.
+ **Tailored configurations**: By using distinct OUs, AWS accounts, and networking configurations, you can configure each environment independently to meet the specific technical requirements of your OT and IT teams. This includes the ability to apply different security controls, such as network ACLs, security groups, and IAM policies, as well as resource-level configurations such as instance types, storage options, and backup/restore mechanisms.
+ **Simplified governance and compliance for showing segregation of duties (SoD)**: Maintaining separate OUs, AWS accounts, and networking configurations simplifies the application of different compliance frameworks, security standards, and regulatory requirements to the OT, IIoT, and IT environments. For OT and IIoT systems, this might include compliance with standards such as ISA/IEC 62443 and NIST SP 800-82, which have specific requirements for secure OT and IIoT system design, deployment, and maintenance. In contrast, the IT systems might have to comply with standards such as ISO 27001 and Payment Card Industry Data Security Standard (PCI DSS).
+ **Scalability and flexibility**: Independent OUs, AWS accounts, and networking configurations provide the ability to scale each environment as needed, without the risk of unintended impacts on the other domain. This allows for more efficient resource allocation, testing processes, and deployment processes that are tailored to the specific requirements of the OT (or IIoT) and IT teams.
+ **Reduced complexity**: Separating the OT and IT environments into distinct OUs, AWS accounts, and networking configurations helps reduce the overall complexity of the AWS infrastructure, and makes it easier to manage, monitor, and troubleshoot each domain independently. This can lead to improved operational efficiency and reduced risk of cross-domain issues.
+ **Specialized tooling and processes**: The OT (or IIoT) and IT teams might require different tools, automation scripts, and operational processes to effectively manage their respective environments. Separate OUs, AWS accounts, and networking configurations enable the implementation of specialized tooling and workflows that are optimized for the unique needs of each domain. For example, OT or IIoT teams might require specific industrial control system (ICS) monitoring and management tools whereas IT teams focus on traditional IT management platforms.
+ **Improved disaster recovery and business continuity**: Maintaining separate OUs, AWS accounts, and networking configurations enhances your organization's ability to ensure business continuity and effective disaster recovery. This is particularly important for OT and IIoT systems, which might have stricter uptime and availability requirements compared with IT systems.

## Security considerations
<a name="industrial-isolation-considerations"></a>

The integration of OT or IIoT systems with cloud environments introduces potential security risks that this capability aims to address. Primarily, it mitigates the threat of lateral movement between IT and OT networks, which could lead to a potential compromise of industrial control systems and other significant OT workloads. Without proper segmentation, a threat actor with malicious intent who gains unauthorized access to the IT network could potentially pivot to the OT network and gain unauthorized access to critical OT systems, which might lead to safety incidents, production downtime, or environmental damage.

Additionally, this capability addresses the risks associated with the unique operational requirements and legacy protocols often found in OT environments. Many industrial systems use proprietary or outdated protocols that lack built-in security features, which make them vulnerable to interception, manipulation, and exploitation when exposed to broader networks. By providing separate OUs, AWS accounts, networking configurations, and an Industrial Isolation account, organizations can implement appropriate protocol conversions, access controls, and monitoring solutions that are specifically tailored to these OT and IIoT communications, to reduce the attack surface and the potential for unauthorized access or data exfiltration.

## Remediations
<a name="industrial-isolation-remediations"></a>

### Data protection
<a name="data-protection.97ba293f-4a83-56f7-a26f-765631238e57"></a>

Latency-sensitive industrial processes and real-time control systems might struggle with the higher network latency inherent in a cloud-based architecture, especially when connecting OT or IIoT equipment over a wide-area network to a remote AWS Region. Additionally, many industrial protocols used in OT environments, such as Modbus, Distributed Network Protocol 3 (DNP3), and proprietary SCADA protocols, were not designed with cloud connectivity in mind. Transmitting these insecure and often unencrypted traffic over public networks introduces a significant risk of interception, tampering, and exploitation. To mitigate these concerns, implement secure [protocol conversion](https://aws.amazon.com/blogs/iot/aws-iot-sitewise-adds-support-for-10-new-industrial-protocols-with-domatica-easyedge-integration/) for legacy industrial communications before transmission over wide-area networks. Deploy specialized OT and IIoT network traffic monitoring and threat detection solutions in both on-premises and cloud environments to identify and respond to potential data breaches or unauthorized access attempts. Regularly review and update data protection measures to maintain alignment with evolving OT and IIoT security standards and best practices.

### Identity and access management
<a name="identity-and-access-management.02c751dc-7ce1-5d75-851b-b04cf6411977"></a>

Establish dedicated IAM Identity Center permission sets and identity center assignments for OT or IIoT access management that are separate from IT systems.  Check for strict separation of concerns or duties in the IAM Identity Center assignments. Configure IAM policies that are specific to OT or IIoT requirements and ensure that the principle of least privilege is applied. Implement strong authentication mechanisms, such as multi-factor authentication, for accessing OT or IIoT resources in the cloud. Regularly audit and review access permissions to maintain a secure posture.

### Network security
<a name="network-security.968ec137-e0d6-5e6f-a600-eb05283dd938"></a>

Design the OT or IIoT network architecture to align with NIST SP 800-82 guidance on segmentation and industrial isolation implementation. Configure security groups and network ACLs to enforce strict traffic control between OT (or IIoT), industrial isolation, and IT networks. Implement AWS IoT security services, such as AWS IoT Device Defender, to enhance the protection of connected industrial assets. Establish secure VPN or AWS Direct Connect links for communication between on-premises OT networks and the AWS Cloud. Regularly conduct network security assessments and penetration testing to identify and address potential vulnerabilities in the OT or IIoT network architecture.

**Note**
In some situations, such as those that involve critical infrastructure or highly regulated or segregated OT environments, or cases where there are requirements for strict separation between OT and IT teams with no common chains of command, you can deploy a separate AWS organization with a landing zone for IoT, IIoT, or OT workloads. In this deployment model, you can configure selective network connectivity between the two separate AWS organizations. However, this model duplicates effort in identity and access management, organization management, security configuration, and logging and monitoring activities, and should be considered only if you can't meet the requirements by using a single AWS organization with separate or dedicated OUs for IoT, IIoT, or OT workloads.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Prescriptive Guidance. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prescriptive-guidance` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
