---
source_url: https://docs.aws.amazon.com/whitepapers/latest/next-generation-oss/security.html
---

 This whitepaper is for historical reference only. Some content might be outdated and some links might not be available.

# Security
<a name="security"></a>

 AWS services provide the necessary framework to secure your OSS solution and the network it manages. This section discusses the AWS services that can help you secure your solution.

## Security of the OSS Solution
<a name="security-of-the-oss-solution"></a>

 [The security pillar of the AWS Well-Architected Framework](https://docs.aws.amazon.com/wellarchitected/latest/security-pillar/welcome.html) provides guidance in developing secure applications and providing the best practices and AWS services recommendations to achieve security excellence.

 [Amazon VPC](https://aws.amazon.com/vpc) allows the creation of private networks and control access to the OSS Solutions using subnets, security groups that are stateful, and Network Access Control Lists (NACL) that are stateless. This enables the isolation of OSS applications from one another, from network elements, and from business and IT applications, ensuring only specific access is allowed.

 OSS application developers can leverage [AWS Key Management Service](https://aws.amazon.com/kms/) (KMS) to create and manage cryptographic keys for data-at-rest encryption for the AWS services discussed previously (such as [Amazon S3](https://aws.amazon.com/s3/), [Amazon EBS](https://aws.amazon.com/ebs), [Amazon RDS](https://aws.amazon.com/rds/), [Redshift](https://aws.amazon.com/redshift), [Amazon ElastiCache](https://aws.amazon.com/elasticache) (ElastiCache), etc.).

 Similarly, OSS applications can leverage [AWS Directory Service](https://aws.amazon.com/directoryservice) to integrate and federate with existing corporate directories to reduce administrative overhead and improve end-user experience. This simplifies CSPs and DSPs’ desired Single Sign On (SSO) for their entire application spectrum, inclusive of network workloads such as OSS.

 [AWS CloudTrail](https://aws.amazon.com/cloudtrail) (CloudTrail) provides a history of AWS API calls, allowing for identification of source IPs for attempted AWS services access. [CloudWatch](https://aws.amazon.com/cloudwatch) Logs allows for a centralized view of all OSS application logs. It makes it easy to search for specific error codes or patterns while providing a highly-scalable service, and it helps you identify operational mistakes.

## Security of the network functions
<a name="security-of-the-network-functions"></a>

 Traditional OSS solutions provide the Public Key Infrastructure (PKI) necessary for the encryption of OAM and network traffic. Monolithic applications from different ISVs required a high level of operational overhead: Many disparate PKIs existed and a complex hierarchical relationship of the various PKIs. [KMS](https://aws.amazon.com/kms/) makes it easy to create and manage cryptographic keys, and provides native integration with AWS CloudTrail to provide you with logs of all key usage. This allows the operator to know what application is being used, and what organization and what users leverage a given key. Various options are available, and they are inclusive of the ability to import your own 256-bit symmetric key. This simplifies your ability to, and increases your control in, encrypting data at rest and in transit, such as configuration data in Amazon S3.

 [AWS Certificate Manager](https://aws.amazon.com/certificate-manager/) (ACM) is a service that simplifies the provisioning, management, and deployment of Secure Sockets Layer (SSL) / Transport Layer Security (TLS) certificates. ACM Private Certificate Authority (CA) enables telecommunication service providers to create a complete CA hierarchy, allowing for a common root and sub-hierarchy for different organizations, traffic-related encryption, and non-traffic data encryption. For example, one sub-CA can be used for encryption of S1U interfaces, while another sub-CA can be used for encrypting domain manager FM interfaces. This reduces the number of CAs managed by a DSP, reducing the cost paid for CAs, supports API-based automation for programmatic deployment, and simplifies the management of Certificate Revocation List (CRL).

## Connectivity
<a name="connectivity"></a>

 [Direct Connect](https://aws.amazon.com/directconnect/) makes it easy to establish a dedicated connection from a DSP on-premise network to its AWS VPCs, inclusive of VPCs running their OSS workloads. This provides a consistent network experience to support the transfer of network OAM data. DSPs can combine Direct Connect with [Site-to-Site VPN](https://aws.amazon.com/vpn/) to provide an end-to-end secure IPSec connection.

 Amazon VPC supports VPC sharing across accounts, allowing you to isolate OSS workloads from network workloads, and enabling the creation, modification, and deletion of OSS applications, in a collocated manner, to network workload without the ability to view, modify, or delete network resources. Network topologies are simplified by interconnecting shared Amazon VPCs using connectivity features, such as [AWSPrivateLink](https://aws.amazon.com/privatelink/), transit gateways, and VPC peering.
