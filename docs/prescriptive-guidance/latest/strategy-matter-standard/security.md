---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/strategy-matter-standard/security.html
---

# Security
<a name="security"></a>

*Security by design *is the practice of incorporating security functions during the device design stage, rather than as an afterthought during the later stages of development*.* Encrypted communication and over-the-air (OTA) updates are examples of security by design. Matter helps provide a foundation for smart-home devices by implementing security by design, starting in a trusted, secure manufacturing facility. Matter is designed so that only owners of a known, trusted Product Attestation Authority (PAA) certificate authority (CA) can manufacture and provision Matter devices.

The Matter security framework has evolved across multiple releases through Matter version 1.5. For example, Matter 1.4.2 (June 2025) introduced cryptography improvements based on Platform Security Architecture (PSA). The Connectivity Standards Alliance (CSA), which oversees the Matter standard, maintains a dedicated Vulnerability Reporting Program to manage security disclosures for the standard.

## Device authentication
<a name="device-authentication"></a>

Matter devices must authenticate themselves to each other and to a controller before they can communicate. Only authorized devices can connect to the Matter fabric. During manufacturing, the manufacturer provisions each device with a unique identity and an X.509 certificate called the *Device Attestation Certificate (DAC)*. When the device attempts to connect to the Matter fabric for the first time, the commissioner device checks the validity of the DAC and verifies that a known and trusted Product Attestation Intermediate (PAI) certificate authority (CA) signed it. The commissioner device also checks whether the device adheres to Matter specifications, protocols, and security standards. The commissioner device grants the device access to the Matter fabric only if all checks succeed.

The Connectivity Standards Alliance (CSA) maintains a list of authorized Product Attestation Authorities (PAAs) and publishes them through the Distributed Compliance Ledger (DCL). The DCL is a blockchain-based system that provides transparent, tamper-resistant records of certified devices and trusted certificate authorities. Manufacturers can apply to become PAAs or work with existing authorized PAAs to provision their devices. The DCL also supports Observer Nodes that stakeholders can use to monitor the certification process.

## Encrypted communication
<a name="encrypted-communication"></a>

After the device joins the Matter fabric, encryption helps protect all data that passes between devices. The devices help preserve data integrity by using a multi-tiered approach. The Matter commissioner performs key exchange and signature verification by using the ECC-256 secp256r1 curve. After the devices exchange keys, they encrypt data in transit by using AES-256. For each message, the devices use the SHA-256 algorithm to verify that no one altered the data during transmission.

Matter version 1.4 introduced Enhanced Multi-Admin capabilities with Home Router Access Protocol (HRAP). These capabilities help improve security when multiple Matter controllers manage a device simultaneously. This enhancement helps protect credential sharing and access control when a device participates in multiple Matter fabrics. Each fabric maintains its own security context, which helps prevent a compromise in one fabric from affecting others.

## Over-the-air updates
<a name="ota-updates"></a>

The Matter standard also requires devices to implement security controls for over-the-air (OTA) updates. OTA updates are a critical part of smart-home deployments because they let devices receive security updates and new features. Manufacturers must sign each firmware update for Matter devices with their private key. The device verifies the payload signature by using the corresponding asymmetric public key. After the device verifies the payload signature, it can commit the image to its bootloader and reset. During the boot process, the device must verify the image again to confirm that it has not been tampered with, and the device also verifies that it is running the latest known version.

Matter version 1.4.2 (June 2025) introduced significant improvements to the OTA update infrastructure, including better transport reliability and enhanced testing frameworks. These improvements have made OTA updates more robust and reliable in production deployments. However, manufacturers should note that Matter's OTA mechanism has limitations regarding sequential updates and rollback capabilities. For devices that require fine-grained update control, fleet management, or A/B testing of firmware, manufacturers may need to supplement Matter's OTA with direct cloud connectivity to their own update infrastructure.
