---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/encryption-best-practices/encryption-strategy-in-aws.html
---

# Encryption strategy in AWS

This section provides recommendations that apply when encrypting data in the AWS Cloud. These general encryption best practices are not specific to AWS services. This section includes the following topics:
+ Encryption of data at rest
+ Encryption of data in transit
+ AWS options to help protect data in use

## Encryption of data at rest in AWS
<a name="encryption-of-data-at-rest-in-aws"></a>

AWS has adopted transparent encryption of data at rest as the standard security posture across its service portfolio. This encryption is transparent to you and helps protect your data at rest without requiring explicit configuration. Unless you choose to use customer-managed keys in AWS KMS, transparent encryption remains in effect across all applicable services and deployment paths.

You can encrypt data using server-side encryptionor client-side encryption basedon factors such as data classification, the need for end-to-end encryption, or technical limitations that prevent you from using end-to-end encryption:
+ Server-side encryption is the act of encrypting data at its destination, by the application or service that receives it and owns the security of its storage layer. By default, server-side encryption happens transparently using keys that AWS manages on your behalf in AWS KMS, but you can also opt in to using a customer-managed key from AWS KMS that you manage directly. Customer-managed keys in AWS KMS give you more control over creation, rotation, sharing (for example, with software vendors), and governance. With transparent encryption, the AWS service controls when the key is used to encrypt and decrypt your data in response to your requests to write and read your data. With a customer-managed key, you define permissions that control when the AWS service can use your key for encryption and decryption in response to your requests to write and read your data.
+ Client-side encryption is the act of encrypting data locally before the target application or service receives it. The AWS service receives encrypted data; it does not play a role in encrypting or decrypting it. For client-side encryption, you can use the [AWS Encryption SDK](https://docs.aws.amazon.com/encryption-sdk/latest/developer-guide/introduction.html), optionally integrated with AWS KMS for key management, or use other encryption libraries and key management solutions.

  For more information and detailed examples for specific use cases, refer to the*Data Encryption *section of any AWS service's documentation.

## Encryption of data in transit in AWS
<a name="encryption-of-data-in-transit-in-aws"></a>

Encryption in transit protects data as it moves across networks between services, applications, and users. Encryption in transit relies on servers and clients negotiating a secure channel.

Servers, whether operated by you or by a service provider, support a specific protocol (such as Transport Layer Security (TLS), SSH File Transfer Protocol (SFTP), or Internet Protocol Security (IPsec)), and various cryptographic options for use within that protocol. You typically configure servers with a policy that specifies encryption settings such as permitted protocol versions, permitted cipher suites, permitted hashes, and permitted key exchange mechanisms. When a client tries to connect to a server, it advertises the session parameters it can support. Servers select the specific parameters for a given session from within the common capabilities of both the client and the server. If there are no common capabilities (meaning that the client doesn't meet the server's security configuration), the server rejects the connection.

A certificate establishes the cryptographic identity of a server. The server presents the certificate to the client to demonstrate authenticity and to bootstrap the secure channel. In mutual authentication scenarios, certificates are associated with a client as well.

AWS encrypts data in transit within AWS infrastructure at multiple layers of the Open Systems Interconnection (OSI) model.

### Application and transport layer protection
<a name="application-and-transport-layer-protection.7bf12113-3e69-5160-855c-9c7fc76aae8d"></a>

At the application through transport layers (Layers 7 through 4), AWS services support protocols including TLS, SSH, and SFTP to help you protect data in transit.

All AWS public service endpoints, such as those used to interact with [Amazon S3](https://docs.aws.amazon.com/AmazonS3/latest/userguide/), AWS KMS, or [Amazon EC2](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/), enforce use of the TLS protocol to secure communications. These endpoints, which AWS owns and manages, enforce a minimum of TLS 1.2, with preference for TLS 1.3 wherever your client software supports it (see [Faster AWS cloud connections with TLS 1.3](https://aws.amazon.com/blogs/security/faster-aws-cloud-connections-with-tls-1-3/)). As encryption guidelines evolve, AWS upgrades these endpoints and publishes corresponding updates to client-side SDKs and libraries. Use the latest guidance when you configure your clients.

AWS services that manage resources on your behalf support encryption of data in transit by using TLS or another protocol suited to the service. These services can also let you adjust encryption settings to meet your compliance and interoperability needs. Services that support configurable encryption in transit for customer-controlled, AWS-managed endpoints include networking services (for example, [Elastic Load Balancing](https://docs.aws.amazon.com/elasticloadbalancing/latest/userguide/) and [Amazon API Gateway](https://docs.aws.amazon.com/apigateway/latest/developerguide/)), database services (for example, [Amazon RDS](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/), Amazon RDS Proxy, and [Amazon Aurora](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/CHAP_AuroraOverview.html)), data and storage services (for example, [AWS Transfer Family](https://docs.aws.amazon.com/transfer/latest/userguide/)), IoT services, and identity services (for example, [Amazon Cognito](https://docs.aws.amazon.com/cognito/latest/developerguide/what-is-amazon-cognito.html)). Services that offer customer-controlled endpoints integrate with [AWS Certificate Manager](https://docs.aws.amazon.com/acm/latest/userguide/acm-overview.html) (ACM) for certificate provisioning, lifecycle management, and improved crypto-agility.

### Network and physical layer protection (Layers 3 through 1)
<a name="network-and-physical-layer-protection--layers-3-through-1-.398ceefa-762a-59d2-bc18-b218b6fe06d9"></a>

Below the application layer, AWS provides options for encryption in the network stack. At Layer 3, services such as AWS Site-to-Site VPN, AWS Client VPN, AWS Transit Gateway VPN attachments, and Nitro-based Amazon EC2 instances support encryption across IPsec links and between compute instances. You can enable [VPC encryption controls](https://docs.aws.amazon.com/vpc/latest/userguide/vpc-encryption-controls.html) to observe and govern encryption at Layers 3 and above within a VPC. At Layer 2, [AWS Direct Connect supports MACsec](https://docs.aws.amazon.com/directconnect/latest/UserGuide/MACsec.html) for dedicated point-to-point encryption on dedicated connections, with partner-configurable encryption available for hosted connections. At the physical layer, AWS encrypts VPC traffic between Availability Zones and between Regions before data leaves secured facilities, with no action required from you.

For detailed encryption configuration guidance specific to each AWS service, consult the service's documentation.

## AWS options to help protect data in use
<a name="aws-options-to-help-protect-data-in-use"></a>

In general, encrypted data cannot be computed on without first being decrypted; data must generally exist in plaintext within the CPU during active processing. This means there is a window where sensitive information resides unencrypted, which is an inherent characteristic of general-purpose computing. While cryptographic techniques for computing on encrypted data exist, they remain limited to narrow use cases. For most workloads, an effective protection for data in use is hardware-enforced isolation, which helps prevent unauthorized parties from accessing memory during computation. AWS provides hardware-enforced isolation for these scenarios. AWS continues to invest in cryptographic computing for scenarios where parties need to derive insights from sensitive data without exposing it to each other. Today, services like AWS Clean Rooms (see [What is AWS Clean Rooms?](https://docs.aws.amazon.com/clean-rooms/latest/userguide/)) address this for collaborative analytics use cases.

**Hardware isolation including no operator access**

AWS helps protect data in use through hardware-enforced isolation that helps prevent unauthorized parties, including other customer tenants , and AWS operators, from accessing customer data during processing. The AWS Nitro System achieves this through hardware-enforced isolation: physical CPU cores and memory pages are pinned exclusively to each instance and are not shared across workloads. The Nitro Hypervisor, a purpose-built and deliberately minimized component, provides strong resource isolation without the shared memory optimizations common in general-purpose hypervisors that create side-channel exposure. This design helps mitigate the class of CPU-based side-channel attacks that depend on shared access to caches or execution threads. In addition, the Nitro System has [no operator access by design](https://docs.aws.amazon.com/whitepapers/latest/security-design-of-aws-nitro-system/no-aws-operator-access.html).

AWS offers Amazon EC2 instance types with memory encryption for workloads where compliance requirements call for cryptographic protection of data in physical memory, or where your threat model requires protection against physical memory access beyond the hardware isolation that the Nitro System provides. For more information, see [Data protection in Amazon EC2](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/data-protection.html) for configurable options. To learn more about the service, see [What is Amazon EC2?](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/)

**Cryptographic computing**

Encryption at rest and encryption in transit have well-established standards and controls. Beyond these, certain cryptographic techniques enable processing encrypted data without decrypting it. These techniques can help you handle sensitive data. AWS offers capabilities in this space for specific use cases. AWS Clean Rooms supports multi-party data collaboration without requiring participants to share raw data, and AWS has released homomorphic encryption toolkits for research workloads. If you are exploring multi-party collaboration, privacy-preserving machine learning, federated learning, encrypted search, or privacy-preserving analytics, contact AWS to learn about currently available capabilities. For more information, see [Cryptographic computing](https://aws.amazon.com/security/cryptographic-computing/).
