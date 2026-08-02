---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/security-reference-architecture-iot/iot-capabilities.html
---

# IoT security capabilities
<a name="iot-capabilities"></a>

|  |
| --- |
| Influence the future of the AWS Security Reference Architecture (AWS SRA) by taking a [short survey](https://amazonmr.au1.qualtrics.com/jfe/form/SV_e3XI1t37KMHU2ua). |

This section discusses secure access, usage, and implementation recommendations for the IoT security capabilities discussed in the previous section.

**Important**
Use a common framework such as [MITRE ATT&CK](https://attack.mitre.org/) or [ISA/IEC 62443](https://www.isa.org/standards-and-publications/isa-standards/isa-iec-62443-series-of-standards) to [conduct a cyber security risk assessment](https://aws.amazon.com/blogs/iot/assessing-ot-and-iiot-cybersecurity-risk/) and use the outputs to inform the adoption of relevant capabilities. Your choice depends on your organization's familiarity with these frameworks and the expectations of your regulatory or compliance auditors.

## Risk assessment guidance
<a name="iot-risk-assessment"></a>

Whether you're deploying consumer IoT devices, industrial IoT workloads, or operational technologies, you should first evaluate the risks and threats associated with your deployment. For example, one common threat to IoT devices listed in the MITRE ATT&CK framework is Network Denial of Service (T1498). The definition of a denial-of-service (DoS) attack against an IoT device is disallowing status or command and control communications to and from an IoT device and its controllers. In the case of a consumer IoT device, such as a smart bulb, the inability to communicate status or receive updates from a central control location could create problems but would likely not have critical consequences. However, in an OT and IIoT system that manages a water treatment facility, utility, or smart factory, losing the ability to receive commands to open or shut key valves could create a larger impact to operations, safety, and the environment. For this reason, consider the impact of various common threats, understand how they apply to your use cases, and determine ways to mitigate them. Key recommendations include:
+ Identify, manage, and track gaps and vulnerabilities. Create and maintain an up-to-date threat model that you can monitor your systems against.
+ Maintain an asset inventory of all connected assets and an up-to-date network architecture.
+ Segment your systems based on their risk assessment. Some IoT and IT systems might share the same risks. In this scenario, use a predefined zoning model with appropriate controls between them.
+ Follow a micro-segmentation approach to isolate the impact of an event.
+ Use appropriate security mechanisms to control information flow between network segments.
+ Understand the potential effects of indirect impact on communications channels. For example, if a communications channel is shared with some other workload, a DoS event on that other workload could affect the network communications of the IIoT or OT workload.
+ Regularly identify and review security event minimization opportunities as your solution evolves.

In OT or IIoT environments, consider partitioning the system under consideration (SuC) into separate zones and conduits in accordance with [ISA/IEC 62443-3-2, Security Risk Assessment for System Design](https://www.automation.com/article/white-paper-excerpt-leveraging-isa-62443-3-2-for-iacs-risk-assessment-and-risk-related-strategies). The intent is to identify assets that share common security characteristics in order to establish a set of common security requirements that reduce cybersecurity risk. Partitioning the SuC into zones and conduits can also help reduce overall risk by limiting the impact of a cyber incident. Zone and conduit diagrams can assist in detailed OT or IIoT cybersecurity risk assessments and help in identifying threats and vulnerabilities, determining consequences and risks, and providing remediations or control measures to safeguard assets from cyber events.

## Recommended AWS services
<a name="iot-aws-services"></a>

When you build your environment in the AWS Cloud, use foundational services such as Amazon Virtual Private Cloud (Amazon VPC), VPC security groups, and network access control lists (network ACLs) to implement micro-segmentation. We recommend that you use multiple AWS accounts to help isolate IoT, IIoT, and OT applications, data, and business processes across your environment, and use AWS Organizations for better manageability and centralized insight.

For more information, see the [Security Pillar – AWS Well-Architected Framework](https://docs.aws.amazon.com/wellarchitected/latest/security-pillar/welcome.html) and the AWS whitepaper [Organizing your AWS environment using multiple accounts.](https://docs.aws.amazon.com/whitepapers/latest/organizing-your-aws-environment/benefits-of-using-multiple-aws-accounts.html)
