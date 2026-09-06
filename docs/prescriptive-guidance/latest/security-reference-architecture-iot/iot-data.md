---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/security-reference-architecture-iot/iot-data.html
---

# Capability 4. Providing data protection and governance
<a name="iot-data"></a>

|  |
| --- |
| Influence the future of the AWS Security Reference Architecture (AWS SRA) by taking a [short survey](https://amazonmr.au1.qualtrics.com/jfe/form/SV_e3XI1t37KMHU2ua). |

This capability supports best practice 8 from the [AWS SRA best practices for IoT](iot-sra.md#iot-sra-best-practices).

Capability 4 addresses the critical need to secure IoT and IIoT data throughout its entire lifecycle, from edge devices to cloud storage and processing systems. It encompasses robust encryption mechanisms for both data at rest and data in transit as well as establishing thorough data governance practices.

## Rationale
<a name="iot-data-rationale"></a>

Industrial systems can generate, process, and store vast amounts of sensitive information, including proprietary manufacturing processes, equipment performance data, and critical operational telemetry. Unauthorized access to, or manipulation of, this data can result in significant consequences that range from intellectual property theft to operational disruptions and safety incidents. Implementing robust encryption and data governance practices addresses these risks directly. It helps safeguard valuable information assets and helps ensure the continuity of industrial operations.

## Security considerations
<a name="iot-data-considerations"></a>

The implementation of robust data protection and governance measures addresses several security risks in IoT, IIoT, and OT environments. Primary concerns include unauthorized access to sensitive data that's stored on IoT devices and edge gateways, and the interception of data during transmission between devices and cloud systems.

## Remediations
<a name="iot-data-remediations"></a>

### Data protection
<a name="data-protection.dbd951d1-5956-510c-b409-b8aff1d847e3"></a>

**Data at rest encryption**:** **Information that's stored on deployed devices such as sensors or cameras might seem harmless, but when the physical control of a device isn't guaranteed, that information can be a target for unauthorized actors. Examples include cached videos on consumer cameras, proprietary machine learning (ML) models in industrial applications, and configuration data for operational environments. For deployed devices, the best practice is to encrypt all data that's stored at rest when possible. This includes:
+ Device storage: Encrypt local storage on IoT devices by using hardware-based encryption (when available) or strong software encryption.
+ Edge gateways: Implement full-disk encryption on edge gateways and local servers.
+ Cloud storage: Use AWS-managed encryption services for data that's stored in the cloud, as described in the [AWS KMS section](https://docs.aws.amazon.com/prescriptive-guidance/latest/security-reference-architecture/application.html#app-kms) in the Application account of the *AWS SRA – core architecture*.

Implement mechanisms for clearing information that's stored in devices. This might be necessary when devices are repurposed or sold and change ownership.

**Data in transit encryption:** Encrypt all data in transit, including sensor and device, administration, provisioning, and deployment data. Nearly all modern IoT devices have the capacity to perform encryption of network traffic, so take advantage of that ability and protect both data plane and control plane communications. This practice helps ensure both the confidentiality of the data and the integrity of monitoring signals. For protocols that can't be encrypted, consider whether an edge device that's closer to the IoT asset can accept the communication and convert it to a secure protocol before sending it outside the local perimeter.

Key practices include:
+ Use TLS for all MQTT and HTTP communications (that is, use MQTTS and HTTPS). Secure communications are recommended regardless of the network packet routing path, whether it's confined to the AWS backbone or not.
+ Implement secure MQTT for IoT messaging, including at the edge.
+ Use AWS Site-to-Site VPN, AWS PrivateLink, and AWS Direct Connect for secure communication between on-premises components and AWS. These services provide more predictable network routing or packet encapsulation compared with internet-accessible API endpoints.
