---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/security-reference-architecture-iot/secure-edge.html
---

# Capability 1. Providing secure edge computing and connectivity
<a name="secure-edge"></a>

|  |
| --- |
| Influence the future of the AWS Security Reference Architecture (AWS SRA) by taking a [short survey](https://amazonmr.au1.qualtrics.com/jfe/form/SV_e3XI1t37KMHU2ua). |

This capability supports best practices 3, 4, and 5 from the [AWS SRA best practices for IoT](iot-sra.md#iot-sra-best-practices).

The [AWS shared responsibility model](https://aws.amazon.com/compliance/shared-responsibility-model/) extends to the industrial IoT edge and into environments where devices are deployed. In the environments where devices are deployed, often called *IoT edge locations*, customers' responsibilities are much broader than they are in the cloud environment. Security of the IoT edge is the AWS customer's responsibility and includes securing the edge network, the edge network perimeter, and devices in the edge network; securely connecting to the cloud; handling software updates of edge equipment and devices; and edge network logging, monitoring, and auditing, as key examples. AWS is responsible for AWS-provided edge software such as AWS IoT Greengrass and AWS IoT SiteWise Edge, and AWS edge infrastructure such as AWS Outposts.

## Rationale
<a name="secure-edge-rationale"></a>

As industrial operations increasingly adopt cloud technologies, there's a growing need to bridge the gap between traditional OT systems and modern IT infrastructure. This capability addresses the necessity for secure, low-latency processing at the edge while also ensuring robust connectivity to AWS Cloud resources. By implementing edge gateways and secure connectivity methods, organizations can maintain the performance and reliability required for critical industrial processes while they take advantage of the scalability and advanced analytics capabilities of cloud services.

This capability is also essential for maintaining a strong security posture in IIoT and OT environments. OT systems often involve legacy devices and protocols that might lack built-in security features and become vulnerable to cyber threats. By incorporating secure edge computing and connectivity solutions, organizations can implement crucial security measures such as network segmentation, protocol conversion, and secure tunneling closer to the data source. This approach helps protect sensitive industrial data and systems and also enables compliance with industry-specific security standards and regulations. Additionally, it provides a framework for securely managing and updating edge devices, which further enhances the overall security and reliability of IIoT and OT deployments.

## Security considerations
<a name="secure-edge-considerations"></a>

The implementation of secure edge computing and connectivity in IoT, IIoT, and OT solutions presents a multifaceted risk landscape. Key threats include inadequate network segmentation between IT and OT systems, security weaknesses in legacy industrial protocols, and the inherent limitations of edge devices that have limited resources. These factors create potential entry points and avenues for threat propagation. The transmission of sensitive industrial data between edge devices and cloud services can also introduce risks of interception and manipulation, and insecure cloud connections can expose systems to internet-based threats. Additional concerns include the potential for lateral movement within industrial networks, lack of visibility into edge device activities, physical security risks for remotely located infrastructure, and supply chain vulnerabilities that can introduce compromised components. Collectively, these threats underscore the critical need for robust security measures in edge computing and connectivity solutions for industrial environments.

## Remediations
<a name="secure-edge-remediations"></a>

### Data protection
<a name="data-protection.35c6a9b9-73a8-50e6-8990-86eb1058312d"></a>

To address data protection concerns, implement encryption for data in transit and at rest. Use secure protocols such as MQTT over TLS, HTTPS, and WebSockets over HTTPS. For communications with IoT devices, and generally within IoT industrial edge environments, consider using secure versions of industrial protocols such as CIP Security, Modbus Secure, and Open Platform Communications Unified Architecture (OPC UA) with security mode enabled. When secure protocols aren't natively supported, employ [protocol converters](https://aws.amazon.com/blogs/iot/aws-iot-sitewise-adds-support-for-10-new-industrial-protocols-with-domatica-easyedge-integration/) or gateways to translate insecure protocols into secure ones as close to the data source as possible. For critical systems that require strict data flow control, consider implementing unidirectional gateways or data diodes. Use [AWS IoT SiteWise Edge](https://aws.amazon.com/iot-sitewise/sitewise-edge/) gateways with OPC UA security mode for industrial data sources, and use [AWS IoT Greengrass](https://docs.aws.amazon.com/greengrass/v2/developerguide/what-is-iot-greengrass.html) for secure local MQTT broker configurations. When protocol-level security isn't possible, consider implementing an encryption overlay by using VPNs or other tunneling technologies to protect data in transit.

In the context of the AWS SRA for IoT, IIoT, and OT environments, secure protocol usage and conversion should be implemented at multiple levels:
+ Level 1. By using an AWS IoT SiteWise Edge gateway connected to an industrial data source that supports OPC UA with security mode.
+ Level 2. By using an AWS IoT SiteWise Edge gateway combined with a partner data source that supports legacy protocols to achieve required protocol conversion.
+ Level 3. By using a secure local MQTT broker configuration with MQTT brokers that are supported through AWS IoT Greengrass.

### Identity and access management
<a name="identity-and-access-management.b91e2530-e2f8-538a-ba4b-6f445fd0aafc"></a>

Implement robust identity and access management practices to mitigate unauthorized access risks. Use strong authentication methods, including multi-factor authentication where possible, and apply the principle of least privilege. For edge device management, use [AWS Systems Manager](https://aws.amazon.com/systems-manager/) for secure access and configuration of edge computing resources. Use [AWS IoT Device Management](https://aws.amazon.com/iot-device-management/) and [AWS IoT Greengrass](https://docs.aws.amazon.com/greengrass/v2/developerguide/what-is-iot-greengrass.html) for secure management of IoT devices. When you use AWS IoT SiteWise gateways, employ [AWS OpsHub](https://docs.aws.amazon.com/snowball/latest/developer-guide/aws-opshub.html) for secure management. For edge infrastructure, consider [AWS Outposts](https://aws.amazon.com/outposts/) as a fully managed service that consistently applies best practices to AWS resources at the edge.

### Network security
<a name="network-security.6e0f1c10-3fa4-5163-829e-0ef9e39e7a45"></a>

Secure connectivity between the industrial edge and the AWS Cloud is a critical component for the successful deployment of IoT, IIoT, and OT workloads in the cloud. As shown in the AWS SRA, AWS offers multiple ways and design patterns to establish a secure connection to the AWS environment from the industrial edge.

The connection can be achieved in one of three ways:
+ By setting up a secure VPN connection toAWS over the internet
+ By establishing a dedicated private connection through [AWS Direct Connect](https://aws.amazon.com/directconnect/)
+ By using secure TLS connections to AWS IoT public endpoints

These options provide a reliable and encrypted communication channel between the industrial edge and the AWS infrastructure, in alignment with the security guidelines outlined in the National Institute of Standards and Technology (NIST) [Guide to Operational Technology (OT) Security (NIST SP 800-82 Rev. 3)](https://csrc.nist.gov/pubs/sp/800/82/r3/final) which warrants the need to* "*use secure connections … between network segments, such as between a regional center and primary control centers and between remote station and control centers."

After you establish a secure connection to workloads running in AWS and to AWS services, use [virtual private cloud (VPC) endpoints](https://docs.aws.amazon.com/vpc/latest/privatelink/create-interface-endpoint.html) whenever possible. VPC endpoints enable you to connect privately to supported Regional AWS services without using the public IP addresses of these AWS services. This approach further helps enhance security by establishing private connections between your VPC and AWS services, and aligns with NIST SP 800-82 Rev. 3 recommendations for secure data transmissions and network segmentation.

You can configure VPC endpoint policies to control and limit access to only the required resources, applying the principle of least privilege. This helps reduce the attack surface and minimize the risk of unauthorized access to sensitive IoT, IIoT, and OT workloads. If the VPC endpoint for the required service isn't available, you could establish a secure connection by using TLS over the public internet. The best practice in such scenarios is to [route these connections through a TLS proxy and a firewall](https://docs.aws.amazon.com/greengrass/v2/developerguide/allow-device-traffic.html), as shown previously in the [Infrastructure OU – Network account](https://docs.aws.amazon.com/prescriptive-guidance/latest/security-reference-architecture/network.html) section of the *AWS SRA – core architecture* guide.

Some environments might have requirements to send data in one direction to AWS while physically blocking traffic in the opposite direction. If your environment has this requirement, you can use data diodes and unidirectional gateways. Unidirectional gateways consist of a combination of hardware and software. The gateway is physically able to send data in only one direction, so there is no possibility of IT-based or internet-based security events pivoting into the OT networks. Unidirectional gateways can be a secure alternative to firewalls. They meet several industrial security standards, such as the [North American Electric Reliability Corporation Critical Infrastructure Protection (NERC CIP),](https://www.nerc.com/pa/Stand/Pages/Project-2014-XX-Critical-Infrastructure-Protection-Version-5-Revisions.aspx) the [International Society of Automation and International Electrotechnical Commission (ISA/IEC) 62443](https://www.isa.org/standards-and-publications/isa-standards/isa-iec-62443-series-of-standards), the [Nuclear Energy Institute (NEI) 08-09](https://www.nrc.gov/docs/ML1011/ML101180437.pdf), the [U.S. Nuclear Regulatory Commission (NRC) 5.71](https://www.nrc.gov/docs/ML0903/ML090340159.pdf), and [CLC/TS 50701](https://www.en-standard.eu/clc/ts-50701-2021-railway-applications-cybersecurity/). They are also supported by the [Industry IoT Consortium's Industrial Internet Security Framework](https://www.iiconsortium.org/iisf/), which provides guidance on protecting safety networks and control networks with unidirectional gateway technology. NIST SP 800-82 states that using unidirectional gateways might provide additional protections associated with system compromises at higher levels or tiers within the environment. This solution enables regulated industries and critical infrastructure sectors to take advantage of cloud services on AWS (such as IoT and AI/ML services) while preventing remote events from penetrating back into protected industrial networks. OT devices that are behind the data diode and unidirectional gateway need to be locally managed. The data diode function is a networking-related function. The data diodes and unidirectional gateways, when deployed into the AWS environment to support the IoT industrial edge, should be deployed into the Industrial Isolation networking account so they are embedded between levels in the OT network.
