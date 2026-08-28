---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/strategy-matter-standard/security.html
---

# Security
<a name="security"></a>

*Security by design *is the practice of incorporating security functions during the device design stage, rather than as an afterthought during the later stages of development*.* Encrypted communication and over-the-air (OTA) updates are examples of security by design. Matter provides a strong foundation for smart-home devices by implementing security by design, starting in a trusted, secure manufacturing facility. Matter devices can only be manufactured and provisioned by owners of a known, trusted Product Attestation Authority (PAA) certificate authority (CA).

As of Matter version 1.5, the security framework has been continuously strengthened through multiple releases. Matter 1.4.2 (June 2025) introduced PSA-based crypto improvements, enhancing the security foundation. The Connectivity Standards Alliance (CSA), which oversees the Matter standard, maintains a dedicated Vulnerability Reporting Program to manage security disclosures for its protocols.

## Device authentication
<a name="device-authentication"></a>

Matter devices must authenticate themselves to each other and to a controller before they can communicate. Only authorized devices can connect to the Matter fabric. During manufacturing, devices are provisioned with a unique identity and X.509 certificate that is known as the *Device Attestation Certificate (DAC)*. When the device attempts to connect to the Matter fabric for the first time, the commissioner device checks the validity of the DAC and that it is signed by a known and trusted Product Attestation Intermediate (PAI) CA. The commissioner device also checks if the device attempting to connect to the network adheres to Matter's specifications, protocols, and security standards. The device is granted access to the Matter fabric only if all of the checks are successful.

The CSA maintains a list of authorized Product Attestation Authorities (PAAs) and publishes them through the Distributed Compliance Ledger (DCL). The DCL is a blockchain-based system that provides transparent, tamper-proof records of certified devices and trusted certificate authorities. Manufacturers can apply to become PAAs or work with existing authorized PAAs to provision their devices. The DCL also supports Observer Nodes that stakeholders can use to monitor the certification ecosystem.

## Encrypted communication
<a name="encrypted-communication"></a>

After the device is granted access to the Matter fabric, all data passed between devices is secured by strong encryption. Data integrity is preserved by using a multi-tiered approach. The Matter commissioner performs key exchange and signature verification by using the ECC-256 secp256r1 curve. After keys have been exchanged, the Matter devices encrypt data in transit by using AES-256. For each message, the devices use the SHA-256 algorithm to verify that data was not tampered with during transmission.

Matter version 1.4 introduced Enhanced Multi-Admin capabilities with Home Router Access Protocol (HRAP). This improved security for scenarios where devices are controlled by multiple ecosystems simultaneously. This enhancement ensures that credential sharing and access control remain secure even when a device participates in multiple Matter fabrics. Each fabric maintains its own security context, preventing compromise in one ecosystem from affecting others.

## Over-the-air updates
<a name="ota-updates"></a>

The Matter standard also requires devices to implement a robust security posture for over-the-air (OTA) updates. OTA is a critical part of a smart-home ecosystem so that devices can receive security updates along with new features. Each firmware update for Matter devices must be signed by a manufacturer's private key. The device verifies the payload signature by using the corresponding asymmetrical public key. After the signature of the payload is verified, the device can commit the image to its bootloader and reset. During the boot process, the device must again verify the image to ensure it has not been tampered with, and the device also verifies that it is running the latest known version.

Matter version 1.4.2 (June 2025) introduced significant improvements to the OTA update infrastructure, including better transport reliability and enhanced testing frameworks. These improvements have made OTA updates more robust and reliable in production deployments. However, manufacturers should note that Matter's OTA mechanism has limitations regarding sequential updates and rollback capabilities. For devices that require fine-grained update control, fleet management, or A/B testing of firmware, manufacturers may need to supplement Matter's OTA with direct cloud connectivity to their own update infrastructure.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Prescriptive Guidance. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prescriptive-guidance` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
