---
source_url: https://docs.aws.amazon.com/whitepapers/latest/nhs-cloud-security-guidance-using-aws/principle-2-asset-protection-and-resilience.html
---

 This whitepaper is for historical reference only. Some content might be outdated and some links might not be available.

# Principle 2: Asset protection and resilience
<a name="principle-2-asset-protection-and-resilience"></a>

****
 User data, and the assets storing or processing it, should be protected against physical tampering, loss, damage, or seizure.

## Section 2.1: Physical location and legal jurisdiction
<a name="section-2.1-physical-location-and-legal-jurisdiction"></a>

****
 The Service User should only use Cloud Infrastructures to store and process data that are physically located within the UK, European Economic Area (EEA), a country deemed adequate by the European Commission, or in the US where covered by Privacy Shield.

 **Applicable risk classes:** All
+  **AWS Regions** — An AWS Region is a geographical locality from which services are delivered, and in which the underlying physical infrastructure to support these exists. The vast majority of these are fully automated, provided on a self-service basis to customers, and are the locations where systems deployed to AWS actually run. It is entirely up to customers which of these Regions they choose to use; data in AWS stay in the Region they are stored, and are moved only in automated response to customer requests, via the AWS Management Console, API, or Command Line Interface.

   At the time of writing, AWS has Regions in the UK, Ireland, Frankfurt, Paris, and Stockholm. AWS is certified under [Privacy Shield](https://www.privacyshield.gov/list), so customers subject to this requirement may also use Regions in the United States: Virginia, California, Oregon, and Ohio. For an up-to-date list of Regions, see [Global Infrastructure](https://aws.amazon.com/about-aws/global-infrastructure/). AWS is covered under Amazon.com’s certification, confirmation of which may be found at [https://www.privacyshield.gov/list](https://www.privacyshield.gov/list).

****
 The Service User should review the Cloud Provider’s terms and conditions (T&Cs) to ensure they are compliant with the Data Protection Act (DPA) and the General Data Protection Regulation (GDPR).
+  **Compliance** — AWS Terms and Conditions are compliant with the UK’s G-Cloud Framework, the Data Protection Act, and the EU’s General Data Protection Regulation. For more information about compliance specifically, see [AWS Compliance](https://aws.amazon.com/compliance).

## Section 2.2: Data centre security
<a name="section-2.2-data-centre-security"></a>

 This is entirely AWS responsibility; other than to satisfy themselves of AWS having fulfilled this, there is no action for customers to take in support of this section of Principle 2. AWS provides a wide range of third-party compliance reports that customers can use for assurance purposes. For details, see [AWS Compliance Programs](https://aws.amazon.com/compliance/programs).

## Section 2.3: Data at rest protection
<a name="section-2.3-data-at-rest-protection"></a>

****
 The Service User should ensure that the encryption is appropriately configured when you implement the system on your chosen cloud provider.

## Encryption
<a name="encryption"></a>

 Customers have the option of ensuring that all data stored in AWS are encrypted. Precisely how this is done varies from one storage service to another. A basic introduction on how to go about this is provided in the paragraphs below. For more detail, see the [Security Learning](https://aws.amazon.com/security/security-learning/) page.
+  [Amazon Elastic Block Store](https://aws.amazon.com/ebs/) (Amazon EBS) presents storage as disk volumes to Amazon Elastic Compute Cloud (Amazon EC2) virtual machine instances. To encrypt these volumes, customers need only to check a box or set the appropriate API or command line parameter to enable this. Snapshots of those volumes are also automatically encrypted. The encryption key is unique to the volume in question, and is in turn encrypted by a primary key, protected by the AWS Key Management Service (AWS KMS). For details on how to implement this, see [Amazon EBS encryption](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/EBSEncryption.html).
+  [Amazon Relational Database Service](https://aws.amazon.com/rds/) (Amazon RDS) is a service for customers that require managed relational databases, and offers various encryption options, depending on the RDBMS engine chosen. For details, see [Encrypting Amazon RDS resources](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Overview.Encryption.html).
+  [Amazon DynamoDB](https://aws.amazon.com/dynamodb/) is the AWS NoSQL database service, enabling unstructured and semi-structured data to be written and retrieved in a flexible fashion. To encrypt data stored in DynamoDB, see [Amazon DynamoDB Encryption at Rest](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/EncryptionAtRest.html).
+  [Amazon Simple Storage Service](https://aws.amazon.com/s3/) (Amazon S3) is the AWS object storage service, available in the form of configurable *buckets* (customer-named containers for those objects). Customers have the option of specifying that specific objects or entire buckets be encrypted. For details, see [Protecting data using encryption](https://docs.aws.amazon.com/AmazonS3/latest/dev/UsingEncryption.html).
+  [Amazon Glacier](https://aws.amazon.com/s3/glacier/) is an archive storage service. Data stored in Amazon Glacier are encrypted as standard, using the 256-bit Advanced Encryption Standard (AES-256).
+  [Amazon Elastic File System](https://aws.amazon.com/efs/) (Amazon EFS) is a shared file system, presented over the NFS protocol. To encrypt data stored on this service, see [Data encryption in Amazon EFS](https://docs.aws.amazon.com/efs/latest/ug/encryption.html).
+  [AWS Storage Gateway](https://aws.amazon.com/storagegateway/) presents network-accessible volumes or virtual tape libraries to client applications, storing the data for these in Amazon S3 in encrypted form as standard. Customers have the choice over whether to use keys managed by AWS Key Management Service (AWS KMS) to encrypt data, or Amazon S3’s Server-Side Encryption (SSE) keys. For more details, see [Data encryption using AWS KMS](https://docs.aws.amazon.com/storagegateway/latest/userguide/encryption.html).
+  [AWS Snowball Edge](https://aws.amazon.com/snowball/) transfers large volumes of data between on-premises environments and AWS. Customers may use the AWS Snowball Edge service, which provides a robust portable appliance with 80 TB or more of storage to which customers can copy data for transfer to their AWS environment via physical shipment. Data is written to a Snowball Edge with AES-256 encryption as standard, and the keys are never stored on the device. For more detail, see [Security in AWS Snowball Edge](https://docs.aws.amazon.com/snowball/latest/ug/security.html#encryption).

## Section 2.4: Data sanitisation
<a name="section-2.4-data-sanitisation"></a>

****
 The process of provisioning, migrating, and deprovisioning resources should not result in unauthorised access to user data. The NHS recommends explicit overwriting of storage before reallocation.

 There are no obligations on the Service User in this section, since this activity falls to AWS under the Shared Responsibility Model for Security. Details of the standards to which AWS adheres when performing this are available in the [AWS Artifact](https://aws.amazon.com/artifact/) portal.

## Section 2.5: Equipment disposal
<a name="section-2.5-equipment-disposal"></a>

****
 Once equipment used to deliver a service reaches the end of its useful life, it should be disposed of in a way which does not compromise the security of the service, or user data stored in the service. The NHS recommends that a recognised standard for equipment disposal is followed.

 There are no obligations on the Service User in this section either.

## Section 2.6: Physical resilience and availability
<a name="section-2.6-physical-resilience-and-availability"></a>

****
 Services have varying levels of resilience, which will affect their ability to operate normally in the event of failures, incidents, or attacks. A service without guarantees of availability may become unavailable, potentially for prolonged periods, regardless of the impact on customer business.
 The NHS recommends that the service provider commits to a Service Level Agreement (SLA) AND analysis of the service design.

 A growing number of services on AWS have Service Level Agreements (SLAs), details of which are specific to each service. It is not feasible to provide an exhaustive list here, but following are links to these details for a subset of services:
+  [Amazon EC2 Service Level Agreement](https://aws.amazon.com/compute/sla/)
+  [Amazon S3 Service Level Agreement](https://aws.amazon.com/s3/sla/)
+  [AWS Direct Connect Service Level Agreement](https://aws.amazon.com/directconnect/sla/)
+  [AWS Lambda Service Level Agreement](https://aws.amazon.com/lambda/sla/)
+  [Amazon Neptune Service Level Agreement](https://aws.amazon.com/neptune/sla/)
+  [Amazon RDS Service Level Agreement](https://aws.amazon.com/rds/sla/)

****
 The Service User should design for failure. Solutions should be architected for cloud such that they are resilient regardless of the underlying cloud infrastructure.

 **Applicable risk classes:** All
+  **AWS Well-Architected Framework** — AWS offers the [Well-Architected Framework](https://docs.aws.amazon.com/wellarchitected/latest/framework/welcome.html) to design and implement workloads in the cloud using AWS best practices. The Framework entails five Pillars, likened to aspects of the workload to consider when evaluating it. One of these is the [Reliability Pillar](https://docs.aws.amazon.com/wellarchitected/latest/reliability-pillar/welcome.html), which provides detailed guidance as to how to design and implement robust systems in the AWS Cloud.

   The accompanying [AWS Well-Architected Tool](https://aws.amazon.com/well-architected-tool/) is now available to customers in the AWS Management Console to enable them to evaluate their workloads against best practices, with the help of with a [Well-Architected Partner](https://aws.amazon.com/architecture/well-architected/partners/), if desired.

   In addition, when deploying third-party software into AWS, customers should follow vendor-recommended High Availability (HA) architecture practices.

****
 The Service User should use at least one Availability Zone/Data Centre.

 **Applicable risk classes:** I-II

 This recommendation applies to workloads with relatively low availability requirements, for which the trade-off of uptime and cost is biased towards the latter. Examples include Development and Test workloads. AWS recommends that customers use the principles of infrastructure as code (IaC) to at least be able to reproduce to another Availability Zone resources deployed to an unusable one in the event of failure.

****
 The Service User should have resilient network links to the Availability Zone/Data Centre.

 **Applicable risk classes:** I-II

 Since the impact of connectivity failure to the chosen AWS Region would be to render the workloads in question inaccessible, it is highly advisable to establish resilient connectivity. For workloads tolerant to network performance variations, this may be achieved very cost-effectively over existing internet connections, using an [AWS Site-to-Site VPN](https://docs.aws.amazon.com/vpn/latest/s2svpn/VPC_VPN.html).

 Those requiring more consistent network performance, but which are still cost-constrained may make use of an [AWS Direct Connect](https://docs.aws.amazon.com/directconnect/latest/UserGuide/Welcome.html) link, with a VPN connection as a fallback. Finally, it is possible to make use of a [Direct Connect Link Aggregation Group](https://docs.aws.amazon.com/directconnect/latest/UserGuide/lags.html) (LAG) using multiple connections for both added resilience and consistent performance even in the event of the failure of one connection.

 For more details, see the [Building a Scalable and Secure Multi-VPC AWS Network Infrastructure](https://aws.amazon.com/answers/networking/aws-multiple-data-center-ha-network-connectivity/) whitepaper.

****
 The Service User should use multiple Availability Zones/Data Centres.

 **Applicable risk class:** III

 In cases where availability is more important, the impact of services failing in a given Availability Zone is correspondingly greater, the measures appropriate to managing the risk are more extensive. Every AWS Region includes at least two Availability Zones, located in physically separate locations with independent risk profiles, but geographically near enough to support synchronous data replication. This affords customers the flexibility to deploy workloads with higher availability requirements to multiple Availability Zones without potential compromise to data integrity.

 For more information, see the [Well-Architected Framework Reliability Pillar](https://docs.aws.amazon.com/wellarchitected/latest/reliability-pillar/welcome.html) and [AWS Global Infrastructure](https://aws.amazon.com/about-aws/global-infrastructure/).

****
 The Service User should have resilient network links to each Availability Zone/Data Centre.

 **Applicable risk class:** III

 Whether using an AWS Site-to-Site VPN (which is configured by default with two tunnels) or a Direct Connect Link Aggregation Group with multiple connections, resilient connectivity to an AWS Region is automatically available to all Availability Zones in that Region. All that is required to make use of it is to deploy resources to more than one Availability Zone.

****
 The Service User should use different cloud vendors or multiple Regions from the same vendor.

 **Applicable risk classes:** IV-V

 This recommendation addresses the possibility of an entire Region becoming unavailable for a time, stipulating the use of other cloud service providers or additional AWS Regions to manage this risk. While the first of these is beyond the scope of this whitepaper, the second is covered in some depth in the *Multi-Region Scenarios* section in the Reliability Pillar of the AWS Well-Architected Framework. It covers a range of Recovery Time and Recovery Point availability goals, discussing the implications of each in terms of both uptime and cost.

****
 The Service User should have resilient network links to each Region / vendor.

 **Applicable risk classes:** IV-V

 This is achievable in two ways:
+  By using the [Direct Connect gateway](https://docs.aws.amazon.com/directconnect/latest/UserGuide/direct-connect-gateways.html), which enables fault-tolerant connectivity to multiple AWS Regions from one resilient set of Direct Connect links; and
+  By establishing separate Direct Connect links to multiple AWS Regions using different Points of Presence, peering the VPCs in these Regions with one another to facilitate data synchronisation. See the [Multiple Region Multi-VPC Connectivity](https://d0.awsstatic.com/aws-answers/AWS_Multiple_Region_Multi_VPC_Connectivity.pdf) AWS Solution Brief for more details.

****
 The Service User should ensure their system has DDoS protection. This may be provided by the Cloud vendor or a third party.

 **Applicable risk classes:** IV-V

 For Distributed Denial of Service (DDoS) protection, customers may use [AWS Shield](https://docs.aws.amazon.com/waf/latest/developerguide/shield-chapter.html), a managed service to help prevent DDoS attacks and minimise their impact. It is available at two tiers: AWS Shield Standard (protecting against all known layer 3 and 4 attacks), and AWS Shield Advanced (providing protection against application layer attacks and associated charge spikes for a number of AWS services, and access to the AWS DDoS Response Team). There is no charge for the Standard tier of the service.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Whitepapers. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query whitepapers` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
