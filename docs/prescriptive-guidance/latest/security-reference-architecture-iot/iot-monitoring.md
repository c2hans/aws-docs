---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/security-reference-architecture-iot/iot-monitoring.html
---

# Capability 5. Providing security monitoring and incident response
<a name="iot-monitoring"></a>

|  |
| --- |
| Influence the future of the AWS Security Reference Architecture (AWS SRA) by taking a [short survey](https://amazonmr.au1.qualtrics.com/jfe/form/SV_e3XI1t37KMHU2ua). |

This capability supports best practices 9 and 10 from the [AWS SRA best practices for IoT](iot-sra.md#iot-sra-best-practices).

Capability 5 focuses on implementing comprehensive security monitoring and incident response mechanisms across IoT, IIoT, OT, edge, and cloud environments. This capability encompasses the deployment of logging and monitoring mechanisms, centralized management of security alerts, and the creation of incident response playbooks and business continuity plans that are tailored to the unique challenges of hybrid OT and IT architectures.

## Rationale
<a name="iot-monitoring-rationale"></a>

The integration of OT, IoT, and IIoT technologies with traditional IT systems and cloud services introduces new attack vectors and expands the overall cyber attack surface. Security events can originate in OT environments and propagate to IT systems, or they can originate in IT systems and propagate to OT environments. This makes it critical to implement comprehensive security monitoring across the full attack surface. Implementing this capability enables organizations to:
+ Establish a unified view of security across OT, IoT, IIoT, edge, and cloud environments.
+ Detect and respond to security anomalies and threats in real time.
+ Maintain operational continuity in the face of cyber incidents.
+ Enhance overall cybersecurity resilience and reduce the potential impact of security breaches.

Moreover, the development of incident response playbooks and business continuity plans that are specifically tailored to cloud-connected OT and IIoT workloads ensures that organizations can effectively manage and recover from security incidents. This proactive approach minimizes downtime, helps protect against financial losses, and safeguards an organization's reputation in the event of a security breach or operational disruption.

## Security considerations
<a name="iot-monitoring-considerations"></a>

The primary consideration addressed by this capability is the risk of delayed detection of security incidents due to siloed monitoring of OT and IT environments. This might be compounded by the inability to correlate security events across these diverse technology stacks. This fragmentation often results in insufficient visibility into industrial network traffic and anomalies, and leaves critical systems exposed to undetected events. Furthermore, the interconnected nature of modern industrial systems creates the potential for cascading failures, where a security event in one area can rapidly propagate across interconnected OT and IT systems, and can amplify the impact of an incident.

Another significant concern is the incompatibility of traditional response procedures when dealing with hybrid OT/IT security incidents, which require specialized knowledge and coordinated action across multiple domains. This is particularly critical given the increasing threat of cyberphysical events that target industrial processes. Additionally, the unique nature of interconnected OT and IIoT systems often means that recovery mechanisms after a security incident might be insufficient and might potentially lead to prolonged downtime and operational disruptions.

The following illustration shows a unified System and Organization Controls (SOC) architecture for IT and OT systems.

![Unified IT/OT SOC architecture.](http://docs.aws.amazon.com/prescriptive-guidance/latest/security-reference-architecture-iot/images/guide-img/11475282-b3b8-4c97-8919-9954329a1c00/images/33d40d8e-384d-44d8-989e-be350eedd4a3.png)

## Remediations
<a name="iot-monitoring-remediations"></a>

### Security logging and monitoring
<a name="security-logging-and-monitoring.e2eb34ff-7865-5c95-a710-b96aecb28a43"></a>

Use centralized AWS Security Hub CSPM and Amazon Security Lake services to capture and handle events that are relevant to IoT, IIoT, and cloud-connected OT solutions in combination with the rest of your AWS organization. Use separate concerns, responsibilities, IAM permission sets, and identity center assignments to identify the teams that can change the configurations for the AWS accounts that are dedicated to OT, IIoT, and Industrial Isolation account resources. All security events can be sent to Security Hub CSPM to gain a centralized view of security findings across your OT, IoT, IIoT, edge, and cloud environments. Review the logging and monitoring recommendations in the [Log Archive account](https://docs.aws.amazon.com/prescriptive-guidance/latest/security-reference-architecture/log-archive.html) section of the *AWS SRA – core architecture*.

Implement a unified SOC by integrating IT and OT security data in Security Lake, which can provide broad visibility across the IT and OT environments and enable coordinated threat detection, faster incident response, and immediate sharing of indicators of compromise (IoCs) between environments. This allows for better understanding of threat paths and origins across OT, IoT, IIoT, edge, and cloud environments. The [Partner IoT, IIoT, and OT SaaS solutions](iot-sra.md#iot-partner) section shows how OT and IIoT security monitoring solutions from AWS Partner Network (APN) providers and others can be used to complement the IoT edge and cloud security services provided by AWS.

### Incident response
<a name="incident-response.c0541321-5496-5895-902a-0e597f1a7147"></a>

Begin by identifying potential incident scenarios that are specific to your deployment, such as IoT device or edge gateway compromise, operational data breaches, or disruptions to industrial processes. For each scenario, create detailed response procedures (playbooks) that outline steps for detection, containment, eradication, and recovery. These playbooks should clearly define roles and responsibilities, communication protocols, and escalation procedures. Test these playbooks by using tabletop exercises. These exercises test the procedures and educate the teams that will have to implement the procedures under the pressure of an actual ongoing incident.

Implement continuous health checks and monitoring systems to detect anomalies before they escalate into major incidents. Automate initial response actions where possible to contain events quickly and to return systems to a known good state. As your IoT environment matures, regularly review and update these playbooks to address new threats and incorporate lessons learned from previous incidents or simulations.

For business continuity and disaster recovery, define clear parameters for system behavior during failures or disruptions. Determine whether systems should fail open or closed, if recovery should be automatic or require human intervention, and the conditions under which manual controls should be enabled or disabled. These decisions should be based on the criticality of the systems and potential impact on safety, operations, and the environment. Test your continuity and recovery plans to ensure that they perform as expected under various scenarios.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Prescriptive Guidance. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prescriptive-guidance` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
