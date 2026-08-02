---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/security-reference-architecture-iot/iot-sra.html
---

# IoT for the AWS SRA
<a name="iot-sra"></a>

|  |
| --- |
| Influence the future of the AWS Security Reference Architecture (AWS SRA) by taking a [short survey](https://amazonmr.au1.qualtrics.com/jfe/form/SV_e3XI1t37KMHU2ua). |

This guide provides recommendations for using IoT securely in industrial and critical infrastructure environments to improve the productivity and efficiency for users and organizations. It focuses on the use of AWS IoT services based on the AWS SRA holistic set of guidelines for deploying an array of AWS security services in a multi-account environment.

This guidance builds upon the [AWS SRA – core architecture](https://docs.aws.amazon.com/prescriptive-guidance/latest/security-reference-architecture/welcome.html) to enable IoT capabilities within an enterprise-grade, secure framework. It covers key security controls such as device identity and asset inventory, AWS Identity and Access Management (IAM) permissions, data protection, network isolation, vulnerability and patch management, logging, monitoring, and incident response that's specific to AWS IoT services.

The target audience for this guidance includes security professionals, architects, and developers who are responsible for securely integrating IoT solutions into their organizations and applications.

## AWS SRA best practices for IoT
<a name="iot-sra-best-practices"></a>

This section explores security considerations and best practices for IoT workloads adapted from the best practices described in the AWS blog post [Ten security golden rules for industrial IoT solutions](https://aws.amazon.com/blogs/iot/ten-security-golden-rules-for-industrial-iot-solutions/). These AWS SRA best practices for IoT are:

1. Assess OT and IIoT cybersecurity risks.

1. Implement strict separation between OT (or IIoT) environments and IT environments.

1. Use gateways for edge computing, network segmentation, security compliance, and to bridge administrative domains. Harden IoT devices and minimize their attack surface.

1. Establish secure connection with AWS by using [AWS Site-to-Site VPN](https://docs.aws.amazon.com/vpn/latest/s2svpn/VPC_VPN.html) or [AWS Direct Connect](https://docs.aws.amazon.com/directconnect/latest/UserGuide/Welcome.html) from the industrial edge. Use virtual private cloud (VPC) endpoints whenever possible.

1. Use secure protocols whenever possible. If you use insecure protocols, convert these into standardized and secure protocols as close to the source as possible.

1. Define appropriate update mechanisms for software and firmware updates.

1. Implement device identity lifecycle management. Apply authentication and access control mechanisms.

1. Secure IoT data at the edge and in the cloud by encrypting data at rest and in transit. Create mechanisms for secure data sharing, governance, and sovereignty.

1. Deploy security auditing and monitoring mechanisms across OT and IIoT. Centrally manage security alerts across OT (or IIoT) and the cloud.

1.  Create incident response playbooks and a business continuity and recovery plan. Test the plan and procedures.

To implement these best practices, this guidance covers the following capabilities:
+ [Capability 1. Providing secure edge computing and connectivity (best practices 3, 4, and 5)](secure-edge.md)
+ [Capability 2. Providing an industrial isolation zone between environments (best practice 2)](industrial-isolation.md)
+ [Capability 3. Providing strong device identities and secure device access and management (best practices 6 and 7)](device-identities.md)
+ [Capability 4. Providing data protection and governance (best practice 8)](iot-data.md)
+ [Capability 5. Providing security monitoring and incident response (best practices 9 and 10)](iot-monitoring.md)

The following sections of this guidance expand on each capability, discuss the capability and its usage, cover security considerations pertaining to the capability, and explain how you can use AWS services and features to address the security considerations (remediation).

The architecture illustrated in the following diagram is an extension of the [AWS SRA diagram](https://docs.aws.amazon.com/prescriptive-guidance/latest/security-reference-architecture/architecture.html) depicted in the *AWS SRA – core architecture* guide. It adds the following elements: customer site and industrial IoT edge, industrial isolation zone account, and IoT, IIoT, or OT software as a service (SaaS) security solutions from AWS Partners.

![AWS services and account structure recommended for IoT functionality.](http://docs.aws.amazon.com/prescriptive-guidance/latest/security-reference-architecture-iot/images/guide-img/11475282-b3b8-4c97-8919-9954329a1c00/images/c4a7d60e-7c06-480c-88c0-ab1ffa174251.png)

[AWS SRA – core architecture](https://docs.aws.amazon.com/prescriptive-guidance/latest/security-reference-architecture/architecture.html)

The top part of the diagram represents the IIoT edge architecture. This is connected to the AWS Cloud organization in the lower part, which is constructed according to the AWS SRA. For a description of each account noted in the AWS organization in the lower part of the diagram, see .  Note that the isolation zone account is treated as an additional Shared Services account in the AWS SRA structure. This account is used to implement IoT-related networking and communications services, which are used by multiple workload accounts that also contain IoT-related processing. The isolation zone account can be considered a peer to the Networking account in the AWS SRA. It is used to manage shared networking and communications processes that are specific to the IIoT edge environments. In addition to the services shown in the diagram, the isolation zone account includes several common security services such as AWS Security Hub CSPM, Amazon GuardDuty, AWS Config, Amazon CloudWatch, and AWS CloudTrail.

For most customers, a single AWS organization with dedicated OUs for IoT, IIoT, and OT workloads is sufficient. You can separate the OT (or IIoT) environments from IT environments by using a isolation zone and the capabilities provided with AWS Organizations, multiple AWS accounts, VPCs, and networking configurations, as shown in the reference architecture.

## Customer site and industrial edge
<a name="industrial-edge"></a>

*Customer site and industrial IoT edge* refers to the specialized computing infrastructure deployed at industrial and OT environments to enable secure data collection, processing, and connectivity close to the source of data generation. This concept addresses the unique challenges of critical infrastructure environments and industrial settings, and supports distributed operations across multiple sites.

You can apply the [Purdue model](https://www.energy.gov/sites/default/files/2022-10/Infra_Topic_Paper_4-14_FINAL.pdf), which is a reference architecture model for the manufacturing industry, to implement different levels in the context of the customer site and industrial edge as follows:
+ **Levels 0-2 – Field devices and local supervisory control:** Industrial equipment, sensors, and actuators are connected by using industrial protocol converters and data diodes. In certain cases, partner edge gateways that run AWS IoT SiteWise Edge are deployed to enable specialized local data acquisition and processing use cases at level 2.
+ **Level 3 – Site operations:** Partner appliances and security sensors can be integrated to support asset discovery, vulnerability detection, and network security monitoring. Edge gateways based on AWS IoT Greengrass and AWS IoT SiteWise Edge are deployed to enable local data acquisition and processing.
+ **Level 3.5 – Industrial isolation zone:** An industrial isolation zone represents a boundary between IT and OT, and controls the communication between the OT and the IT networks. Cloud access and internet access services such as proxies, firewalls, and unidirectional gateways are deployed to this layer to mediate the required connectivity and data flows.
+ **Levels 4-5 – IT network:** Secure connectivity to the cloud is established by using Site-to-Site VPN or Direct Connect. AWS PrivateLink VPC endpoints are used for private access to AWS resources.

## AWS organization
<a name="iot-organization"></a>

A Workloads OU for IoT, IIoT, or OT workloads is created alongside other workload-specific OUs. This OU is dedicated to applications that use relevant AWS IoT services to build and deploy IoT, IIoT, and OT-integrated solutions. The OU contains an Application account (shown in the previous architecture diagram) where you host your solution that provides the required business functionality. Grouping AWS services based on application type helps enforce security controls through OU-specific and AWS account-specific service control policies.

This approach also makes it easier to implement strong access control and least privilege. In addition to these specific OU and accounts, the reference architecture includes additional OUs and accounts that provide foundational security capabilities that apply to all application types. The [Org Management](https://docs.aws.amazon.com/prescriptive-guidance/latest/security-reference-architecture/org-management.html), [Security Tooling](https://docs.aws.amazon.com/prescriptive-guidance/latest/security-reference-architecture/security-tooling.html), [Log Archive](https://docs.aws.amazon.com/prescriptive-guidance/latest/security-reference-architecture/log-archive.html), and [Network](https://docs.aws.amazon.com/prescriptive-guidance/latest/security-reference-architecture/network.html) accounts are discussed in the *AWS SRA – core architecture* guide. These accounts have several additions that pertain to IoT workloads:
+ **Network account** includes provisions for Direct Connect, Site-to-Site VPN, and AWS Transit Gateway. It also provides the possibility of creating a global network across operational assets by using AWS Cloud WAN, depending on the [chosen approach for connecting to the AWS Cloud](https://docs.aws.amazon.com/whitepapers/latest/aws-vpc-connectivity-options/network-to-amazon-vpc-connectivity-options.html). For details, see the [Infrastructure OU – Network account](https://docs.aws.amazon.com/prescriptive-guidance/latest/security-reference-architecture/network.html) section of the in the *AWS SRA – core architecture* guide.
+ **Industrial Isolation account** provides the option to deploy services (such as patching, antivirus, and remote access services) that would otherwise be deployed at the customer site or industrial IoT edge (level 3.5). This account supports scenarios that include robust connectivity between the site, the industrial IoT edge, and the AWS Cloud. These services are specific to servicing the IoT industrial edge and can be considered on the *edge side* instead of the *internet side* of a layered networking model.

Hosting services in the Industrial Isolation account on AWS provide enhanced flexibility, scalability, security, and integration capabilities compared with on-premises solutions, and enable more efficient and flexible management of industrial edge operations. For example, you can provide streaming access to your end-user applications by using [Amazon WorkSpaces Applications](https://aws.amazon.com/appstream2/) and use [Amazon GuardDuty Malware Protection for S3](https://docs.aws.amazon.com/guardduty/latest/ug/gdu-malware-protection-s3.html) to provide malware scanning capabilities as part of a secure file exchange solution that spans IT and OT environments. The Industrial Isolation account uses the shared connectivity constructs in the Network account, such as [Transit Gateway](https://docs.aws.amazon.com/vpc/latest/tgw/what-is-transit-gateway.html), to obtain the required connectivity to the desired on-premises resources.

**Note**
This networking account is labeled *Industrial Isolation* because it serves as a buffer between the industrial IoT edge and the corporate networks that run within AWS accounts that are managed according to the AWS SRA. In this way, the account forms a type of edge between the industrial edge and corporate networking. This is similar to how the Network account in the AWS SRA serves as a buffer between the workloads running in the AWS Cloud (in workload accounts) and both the internet and corporate on-premises IT networks.

## Partner IoT, IIoT, and OT SaaS solutions
<a name="iot-partner"></a>

AWS Partner solutions play a crucial role in helping enhance security monitoring and threat detection across IoT, IIoT, OT, and cloud environments. They complement the native IoT edge and cloud security services from AWS and help provide a more comprehensive security posture through a set of specialized detection and monitoring capabilities. The integration of these specialized OT and IIoT security monitoring capabilities with the broader cloud security offerings from AWS is achieved through services such as AWS Security Hub CSPM and Amazon Security Lake. You can deploy these solutions within your application accounts in your AWS organization. You can also use SaaS solutions that are hosted elsewhere on the internet and managed by third parties. In some cases, these third-party solutions also run on AWS. This scenario can facilitate IAM-based permissions management and AWS-specific network connectivity optimizations. In other cases, the connectivity to these services is configured according to the requirements of the SaaS solution.

These additions enable a more robust, secure, and flexible architecture that's specifically tailored for industrial environments and integrated with the AWS Cloud and AWS IoT services. The IoT components of the AWS SRA architecture address the unique challenges of industrial settings, such as protocol diversity, industrial edge processing requirements, and the need for seamless integration between OT and IT systems.
