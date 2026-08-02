---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/security-reference-architecture-iot/device-identities.html
---

# Capability 3. Providing strong device identities and secure device access and management
<a name="device-identities"></a>

|  |
| --- |
| Influence the future of the AWS Security Reference Architecture (AWS SRA) by taking a [short survey](https://amazonmr.au1.qualtrics.com/jfe/form/SV_e3XI1t37KMHU2ua). |

This capability supports best practices 6 and 7 from the [AWS SRA best practices for IoT](iot-sra.md#iot-sra-best-practices).

In the rapidly evolving landscape of IoT, IIoT, and OT, ensuring the security and integrity of connected devices is paramount. This capability focuses on implementing robust device identity lifecycle management and secure update mechanisms. It is crucial for maintaining the trustworthiness of devices throughout their operational lifespan, from initial deployment to retirement, while ensuring that they remain current with the latest security patches and firmware updates.

## Rationale
<a name="device-identities-rationale"></a>

Devices that form part of IoT, IIoT, and cloud-connected OT solutions continuously interact with one another and with cloud services to exchange data, and, in some cases, to facilitate critical processes. The security of these devices is not just a technical requirement but a core business imperative. Strong device identities form the foundation of this security framework and enable reliable authentication and authorization. Devices, ranging from factory floor sensors to smart grid gateways, must conclusively establish their authenticity when they access on-premises data sources, network resources, or cloud services. This establishment of trust is essential to help prevent unauthorized access and potential compromises that could result in operational disruptions or data breaches.

The dynamic nature of IoT and IIoT environments also necessitates an active approach to device management. Devices require regular updates with the latest security patches and firmware to address newly discovered vulnerabilities and to enhance functionality. A comprehensive identity and management system facilitates the secure and timely distribution of these updates across device fleets. Additionally, it enables fine-grained access control and ensures that each device operates under the principle of least privilege to access only the resources that are necessary for its designated function. This system manages the entire lifecycle of device identities, from initial provisioning through potential repurposing or recommissioning, to eventual decommissioning.

## Security considerations
<a name="device-identities-considerations"></a>

The implementation of strong device identities and secure management practices addresses several critical security risks. Device impersonation poses a significant threat, because attackers can potentially gain unauthorized access to sensitive systems by mimicking legitimate devices. This risk is compounded by weak authentication mechanisms and overly permissive access controls, which can lead to unauthorized access to devices and associated cloud resources.

Outdated software and firmware present another substantial challenge. Unpatched devices remain susceptible to known security flaws and create potential entry points for malicious actors. The update process introduces additional risks, because insecure update mechanisms can be used for supply chain attacks and enable the distribution of malicious code across device fleets. Furthermore, inadequate protection of device credentials, including cryptographic keys and certificates, can result in widespread system compromise if these credentials are obtained by unauthorized parties. The implementation of this capability helps mitigate these risks by establishing a robust framework for device authentication, authorization, and lifecycle management.

## Remediations
<a name="device-identities-remediations"></a>

### Data protection
<a name="data-protection.73aeba05-bc40-58f5-bd08-300d49a1721b"></a>

Implement cryptographic signing and verification for all software and firmware updates to help ensure authenticity and integrity. Use [AWS Signer](https://docs.aws.amazon.com/signer/latest/developerguide/) for code signing capabilities to help ensure the trust and integrity of code that's created for IoT devices. Store updates securely by using [Amazon Simple Storage Service](https://aws.amazon.com/s3/) (Amazon S3) with appropriate permissions, access roles, and encryption settings, such as server-side encryption by using AWS managed keys or customer managed keys. Implement version control and rollback capabilities by using [AWS IoT Jobs](https://docs.aws.amazon.com/iot/latest/developerguide/iot-jobs.html) and [AWS IoT Device Management Software Package Catalog](https://docs.aws.amazon.com/iot/latest/developerguide/software-package-catalog.html) to maintain version history and to revert to previous versions if necessary.

Develop and implement a robust update strategy that includes gradual rollouts to catch defects and to ensure that all devices of the same type aren't affected simultaneously. Design the update process to be responsive to vulnerabilities and to be scalable for managing updates across large fleets of diverse devices. Use AWS IoT Jobs and AWS IoT Device Management for scalable and secure distribution of updates. Implement monitoring and logging of update processes to detect anomalies and maintain audit trails. Make sure that update mechanisms are resilient to intermittent connectivity and resource constraints that are common in IoT environments. Consider implementing cancel, rollback or fallback, and failed update handling procedures.

### Identity and access management
<a name="identity-and-access-management.1da11219-ce94-5327-8142-273cc5a298f4"></a>

Provision devices that have unique identities by using X.509 certificates or other strong credentials. Implement a comprehensive device identity lifecycle management system that covers provisioning, rotation, and revocation of credentials. Use the security features in AWS IoT Core for device authentication and authorization. Use [AWS Private Certificate Authority](https://aws.amazon.com/private-ca/)to provision and manage device certificates. Use [AWS Certificate Manager (ACM)](https://aws.amazon.com/certificate-manager/) to manage server keys or certificates for applications. Employ [Amazon Cognito](https://aws.amazon.com/cognito/) to manage user identities that are associated with device management interfaces. Use [AWS Secrets Manager](https://aws.amazon.com/secrets-manager/) to securely store and manage device secrets, and encrypt them by using [AWS Key Management Service](https://aws.amazon.com/kms/) (AWS KMS). Implement hardware-protected modules such as Trusted Platform Modules (TPMs), where available, to establish a root of trust on devices.

### Network security
<a name="network-security.44137336-c123-5117-a7b1-a027926d6938"></a>

Use secure communication protocols such as MQTT over TLS for device-to-cloud communications. Where possible, implement [AWS PrivateLink VPC endpoints](https://docs.aws.amazon.com/vpc/latest/privatelink/create-interface-endpoint.html) for secure configuration management and update downloads. Apply network segmentation to isolate IoT and IIoT devices from other critical network assets. Use [AWS IoT Device Defender](https://docs.aws.amazon.com/iot-device-defender/latest/devguide/what-is-device-defender.html) to continuously audit and monitor the security posture of your device fleet, including checking for compliance with security best practices such as the principle of least privilege and unique identity per device.
