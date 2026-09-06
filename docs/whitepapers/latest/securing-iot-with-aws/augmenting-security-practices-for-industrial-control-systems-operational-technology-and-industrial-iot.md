---
source_url: https://docs.aws.amazon.com/whitepapers/latest/securing-iot-with-aws/augmenting-security-practices-for-industrial-control-systems-operational-technology-and-industrial-iot.html
---

 This whitepaper is for historical reference only. Some content might be outdated and some links might not be available.

# Augmenting security practices for industrial control systems, operational technology, and industrial IoT
<a name="augmenting-security-practices-for-industrial-control-systems-operational-technology-and-industrial-iot"></a>

 Industrial IoT is driving changes to the operational technology (OT) landscape, making it more connected. OT such as industrial control systems (ICS) and supervisory control and data acquisition systems (SCADA) is the use of hardware and software to monitor and control physical assets and production operation. Industrial internet of things (IIoT) is the connection of ICS with enterprise systems, business processes, and analytics, and is a key enabler for smart manufacturing and Industry 4.0. The convergence of IT and OT systems is creating a mix of technologies that were designed for remote network environments and ones that were not, which creates risk management difficulties that need to be addressed. This OT and IT convergence introduces new security risks and challenges in the industrial environment which need to be properly managed.

 Although general best practices still apply, there are some additional considerations that should be put in place to support the often times higher criticality and larger impact of OT and IIoT systems. To help companies plan their industrial digital transformation safely and securely, AWS recommends augmenting general best practices with these fundamentals in ICS and OT, and IIoT security.

1.  **Conduct a formal security risk assessment using a common framework (such as [MITRE ATT&CK for ICS](https://collaborate.mitre.org/attackics/index.php/Main_Page)). Use this to inform system design.**
   +  Segment industrial plants networks based on a predefined zoning model that includes establishment of demilitarized zones and control of traffic between zones (for example, according to the [Purdue Model](https://en.wikipedia.org/wiki/Purdue_Enterprise_Reference_Architecture)).
   +  Use application-specific firewalls, unidirectional gateways, and data diodes to control information flow between network segments.
   +  Use protocol converters to convert insecure industrial protocols to secure protocols as close to the device as possible.
   +  If possible, isolate safety networks from business and control networks.
   +  If you are unable to protect insecure industrial assets, isolate or disconnect them from the network.

1.  **Maintain an asset inventory of all IIoT assets, including IT assets required to maintain IIoT operations. Categorize them by safety, criticality, ability to patch, and other actionable criteria.**
   +  Maintain an updated inventory of devices that don’t support modern security controls. Isolate them from the rest of the other OT and IIoT devices by network segmentation. Create a plan to replace them with devices that do support modern security controls.
   +  Conduct security architecture reviews as assets move or become dependent on new systems.
   +  Consider if integrating the IIoT asset information into your enterprise asset management system provides any benefit. Assess the business risk of having a segmented inventory system.
   +  Create and maintain an up-to-date OT and IIoT network architecture showing how these assets are interconnected along their relationships (asset hierarchies).

1.  **Provision modern IIoT devices and systems with unique identities and credentials. Apply authentication and access control mechanisms.**
   +  Assign unique identities to modern IIoT devices so that when a device connects to other devices or cloud services, it must establish trust by authenticating using principals such as X.509 certificates, security tokens, or other credentials.
   +  Create mechanisms to facilitate the generation, distribution, rotation, and revocation of credentials.
   +  Establish root of trust by using hardware-protected modules such as TPMs if available on the device.
   +  Ensure least privilege access controls for IIoT devices, edge gateways, and agent software accessing local and cloud resources.
   +  Avoid hardcoding or storing credentials and secrets locally on OT and IIoT devices.

1.  **Define appropriate update mechanisms for software and firmware updates.**
   +  Maintain an inventory of the deployed software across your OT and IIoT ecosystem, including versions and patch status.
   +  Create mechanisms to identify, network isolate, and replace legacy devices and IIoT systems that are not capable of receiving updates.
   +  Perform deployment of patches for the OT and IIoT devices only after testing the patches in a test environment before implementing them in production.
   +  Create a plan to validate firmware, patches, or any other software, from software providers in the supply chain to ensure their authenticity and validity.
   +  For OT and IIoT systems that cannot be updated, apply compensating measures such as network isolation and continuous monitoring.

1.  **Encrypt persistent data at rest.**
   +  Monitor the production data at rest and in transit to identify potential unauthorized data modification.
   +  When appropriate, based on risk, access controls should also be applied at the connectivity layer using security appliances such as unidirectional network devices or [data diodes](https://en.wikipedia.org/wiki/Unidirectional_network).
   +  Identify and consider the unique capabilities of your OT and IIoT devices. This could include mobility, actuation, sensory data collection and transmission, and ownership transfers that impact your regulatory and legal compliance.
   +  Create mechanisms for secure IIoT data sharing, governance, and sovereignty.

1.  **Encrypt all data in transit, including sensor and device data, administration, and provisioning and deployments.**
   +  Ensure security capabilities and interoperability between industrial protocols when implementing different protocols for various devices within the same system.
   +  Select the newer version of industrial protocols which offer security features, and configure the highest level of encryption available when using ICS protocols such as CIP Security, Modbus Secure, OPC UA, and so on.
   +  When secure industrial protocols are not an option and you use legacy insecure industrial protocols, then tighten the trust boundary using a protocol converter to translate the insecure protocol to a secure protocol as close to the data source as possible. Otherwise, segregate the plant network into smaller cell or area zones by grouping ICS devices into functional areas to limit the scope and area of insecure communications. Use specialized firewall and inspection products that understand ICS protocols to inspect traffic entering and leaving cell or area zones and can detect anomalous behavior in the control network.
   +  Have a mechanism to identify and disable vulnerable wireless networks in the local environment which get installed during proof of concepts, often without the necessary security approvals.

1.  **Secure both the IoT environment and supporting IT environments to the same level of criticality following a well-documented standard. This is especially true for gateways that serve as boundaries between systems.**
   +  Configure, monitor, and securely manage IIoT devices, edge gateways, and virtual machines.
   +  Use secure enclosures to protect OT and IIoT assets.
   +  Establish a mechanism for bidirectional, secure communication to remote devices, which are often behind firewalls.
   +  Provision your IIoT devices and field gateways with credentials that grant only the required privileges.
   +  Regularly review and identify attack surface minimization opportunities as your IIoT ecosystem evolves.

1.  **Deploy security auditing and monitoring mechanisms across your IIoT environment and relevant IT systems.**
   +  Verify that security controls prevent unauthorized access and maintain their integrity in the event of external dependency or internal system failures.
   +  Implement a monitoring solution in the OT and IIoT environments to create an industrial network traffic baseline and monitor anomalies and adherence to the baseline.
   +  Perform periodic reviews of network logs, access control privileges, and asset configurations.

1.  **Create incident response playbooks, and build automation as your security response matures.**
   +  Maintain and regularly exercise a security incident response plan along with containment and recovery mechanisms. This should be in correspondence to the technical skill level of operators of your OT and IIoT elements and their deployment and ownership model.
   +  Ensure that your security operations center is trained and knowledgeable on OT and IIoT security logs, and alerts from the automated tooling.

1.  **Create and test business continuity and recovery plans.**
   +  Focus on ensuring resilience of Industry 4.0 systems by creating a business continuity plan and disaster recovery plan. Test the plans periodically and adapt them according to lessons learned from tests and actual security incidents.
   +  Perform threat and risk assessment of OT and IIoT, and supporting IT systems, and develop written procedures on how to return to the normal, well-defined, state of operation tailored to the assessment’s results.
   +  In business continuity and recovery plans, include third-party aspects.
   +  Conduct ongoing security testing across OT and IIoT periodically to test devices and OT systems, edge gateways, networks, and communication and cloud services.
