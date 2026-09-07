---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/hybrid-cloud-best-practices/security.html
---

# Security at the edge
<a name="security"></a>

In the AWS Cloud, security is the top priority. As organizations adopt the scalability and flexibility of the cloud, AWS helps them adopt security, identity, and compliance as key business factors. AWS integrates security into its core infrastructure and offers services to help you meet your unique cloud security requirements. When you expand the scope of your architecture into the AWS Cloud, you benefit from the integration of infrastructures such as Local Zones and Outposts into AWS Regions. This integration enables AWS to extend a select group of core security services to the edge.

Security is a shared responsibility between AWS and you. The [AWS shared responsibility model](https://aws.amazon.com/compliance/shared-responsibility-model/) differentiates between the security *of* the cloud and security *in* the cloud:
+ **Security of the cloud** – AWS is responsible for protecting the infrastructure that runs AWS services in the AWS Cloud. AWS also provides you with services that you can use securely. Third-party auditors regularly test and verify the effectiveness of AWS security as part of [AWS compliance programs](https://aws.amazon.com/compliance/programs/).
+ **Security in the cloud** – Your responsibility is determined by the AWS service that you use. You are also responsible for other factors, including the sensitivity of your data, your company's requirements, and applicable laws and regulations.

## Data protection
<a name="data-protection"></a>

The AWS shared responsibility model applies to data protection in AWS Outposts and AWS Local Zones. As described in this model, AWS is responsible for protecting the global infrastructure that runs the AWS Cloud (*security of the cloud*). You are responsible for maintaining control over your content that is hosted on this infrastructure (*security in the cloud*). This content includes the security configuration and management tasks for the AWS services that you use.

For data protection purposes, we recommend that you protect AWS account credentials and set up individual users with [AWS Identity and Access Management (IAM)](https://docs.aws.amazon.com/IAM/latest/UserGuide/introduction.html) or [AWS IAM Identity Center](https://docs.aws.amazon.com/singlesignon/latest/userguide/what-is.html). This gives each user only the permissions necessary to fulfill their job duties.

### Encryption at rest
<a name="encryption-at-rest.c1b21784-3913-5a66-a673-547dc8433661"></a>

#### Encryption in EBS volumes
<a name="encryption-in-ebs-volumes.21c9cf1f-d89b-53d6-949d-3752ad021394"></a>

With AWS Outposts, all data is encrypted at rest. The key material is wrapped with an external key, the Nitro Security Key (NSK), which is stored in a removable device. The NSK is required to decrypt the data on your Outpost rack. You can use Amazon EBS encryption for your EBS volumes and snapshots. Amazon EBS encryption uses [AWS Key Management Service (AWS KMS)](https://docs.aws.amazon.com/kms/latest/developerguide/overview.html) and KMS keys.

In the case of Local Zones,** **all EBS volumes are encrypted by default in all Local Zones, except to for the list documented in the [AWS Local Zones FAQ](https://aws.amazon.com/about-aws/global-infrastructure/localzones/faqs/#:~:text=What%E2%80%99s%20the%20default%20encryption%20behavior%20of%20EBS%20volumes%20in%20Local%20Zones%3F) (see the question: *What's the default encryption behavior of EBS volumes in Local Zones?*), unless encryption is enabled for the account.

#### Encryption in Amazon S3 on Outposts
<a name="encryption-in-9999999999999999s3onoutpostslong-.c67adbeb-6cb5-538e-a22b-363ca414ccca"></a>

By default, all data stored in Amazon S3 on Outposts is encrypted by using server-side encryption with Amazon S3 managed encryption keys (SSE-S3). You can optionally use server-side encryption with customer-provided encryption keys (SSE-C). To use SSE-C, specify an encryption key as part of your object API requests. Server-side encryption encrypts only the object data, not the object metadata.

**Note**
Amazon S3 on Outposts doesn't support server-side encryption with KMS keys (SSE-KMS).

### Encryption in transit
<a name="encryption-in-transit.c4431593-80d9-532d-b944-90abfc5a8da6"></a>

For AWS Outposts, the service link is a necessary connection between your Outposts server and your chosen AWS Region (or home Region) and allows for the management of the Outpost and the exchange of traffic to and from the AWS Region. The service link uses an AWS managed VPN to communicate with the home Region. Each host inside AWS Outposts creates a set of VPN tunnels to split control plane traffic and VPC traffic. Depending on the service link connectivity (internet or Direct Connect) for AWS Outposts, those tunnels require firewall ports to be opened for the service link to create the overlay on top of it. For detailed technical information about the security of AWS Outposts and the service link, see [Connectivity through service link](https://docs.aws.amazon.com/outposts/latest/userguide/service-links.html) and [Infrastructure security in AWS Outposts](https://docs.aws.amazon.com/outposts/latest/server-userguide/infrastructure-security.html) in the AWS Outposts documentation[.](https://docs.aws.amazon.com/outposts/latest/server-userguide/infrastructure-security.html)

The AWS Outposts service link creates encrypted tunnels that establish control plane and data plane connectivity to the parent AWS Region, as illustrated in the following diagram.

![Anchor VPC considerations.](https://docs.aws.amazon.com/prescriptive-guidance/latest/hybrid-cloud-best-practices/images/guide-img/117f803b-a3ee-4c57-ae66-84b53da14c2b/images/594dbd32-b42a-4147-9452-5e7f6dca0f2f.png)

Each AWS Outposts host (compute and storage) requires these encrypted tunnels over well-known TCP and UDP ports to communicate with its parent Region. The following table shows the source and destination ports and addresses for the UDP and TCP protocols.

|
|
| Protocol | Source port | Source address | Destination port | Destination address |
| --- |--- |--- |--- |--- |
| UDP | 443 | AWS Outposts service link /26 | 443 | AWS Outposts Region's public routes or anchor VPC CIDR |
| TCP | 1025-65535 | AWS Outposts service link /26 | 443 | AWS Outposts Region's public routes or anchor VPC CIDR |

** **

Local Zones are also connected to the parent Region through the redundant and very high-bandwidth global private backbone of Amazon. This connection gives applications that are running in Local Zones fast, secure, and seamless access to other AWS services. As long as Local Zones are part of the AWS global infrastructure, all data flowing over the AWS global network is automatically encrypted at the physical layer before it leaves AWS secured facilities. If you have specific requirements to encrypt the data in transit between your on-premises locations and Direct Connect PoPs to access a Local Zone, you can enable MAC Security (MACsec) between your on-premises router or switch and the Direct Connect endpoint. For more information, see the AWS blog post [Adding MACsec security to Direct Connect connections](https://aws.amazon.com/blogs/networking-and-content-delivery/adding-macsec-security-to-aws-direct-connect-connections/).

### Data deletion
<a name="data-deletion.11963dda-0e8e-5c91-9ce0-b5608e5bc1ca"></a>

When you stop or terminate an EC2 instance in AWS Outposts, the memory allocated to it is scrubbed (set to zero) by the hypervisor before it is allocated to a new instance, and every block of storage is reset. Deleting data from the Outpost hardware involves the use of specialized hardware. The NSK is a small device, illustrated in the following photograph, that attaches to the front of every compute or storage unit in an Outpost. It is designed to provide a mechanism to prevent your data from being exposed from your data center or colocation site. Data on the Outpost device is protected by wrapping keying material used to encrypt the device and storing the wrapped material on the NSK. When you return an Outpost host, you destroy the NSK by turning a small screw on the chip that crushes the NSK and physically destroys the chip. Destroying the NSK shreds the data cryptographically on your Outpost.

![NSK device in Outposts.](https://docs.aws.amazon.com/prescriptive-guidance/latest/hybrid-cloud-best-practices/images/guide-img/117f803b-a3ee-4c57-ae66-84b53da14c2b/images/b96c33a1-9ae5-4d48-9676-b6fe817cd98b.jpeg)

## Identity and access management
<a name="security-iam"></a>

AWS Identity and Access Management (IAM) is an AWS service that helps an administrator securely control access to AWS resources. IAM administrators control who can be authenticated (signed in) and authorized (have permissions) to use AWS Outposts resources. If you have an AWS account, you can use IAM at no additional charge.

The following table lists the IAM features that you can use with AWS Outposts.

|
|
| IAM feature | AWS Outposts support |
| --- |--- |
| Identity-based policies | Yes |
| Resource-based policies | Yes\* |
| Policy actions | Yes |
| Policy resources | Yes |
| Policy condition keys (service-specific) | Yes |
| Access control lists (ACLs) | No |
| Attribute-based access control (ABAC) (tags in policies) | Yes |
| Temporary credentials | Yes |
| Principal permissions | Yes |
| Service roles | No |
| Service-linked roles | Yes |

\*In addition to IAM identity-based policies, Amazon S3 on Outposts supports both bucket and access point policies. These are [resource-based policies](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_identity-vs-resource.html) that are attached to the Amazon S3 on Outposts resource.

For more information about how these features are supported in AWS Outposts, see the [AWS Outposts user guide](https://docs.aws.amazon.com/outposts/latest/userguide/security_iam_service-with-iam.html).

## Infrastructure security
<a name="infrastructure-security"></a>

Infrastructure protection is a key part of an information security program. It ensures that workload systems and services are protected against unintended and unauthorized access, and potential vulnerabilities. For example, you define trust boundaries (for example, network and account boundaries), system security configuration and maintenance (for example, hardening, minimization, and patching), operating system authentication and authorizations (for example, users, keys, and access levels), and other appropriate policy-enforcement points (for example, web application firewalls or API gateways).

AWS provides a number of approaches to infrastructure protection, as discussed in the following sections.

### Protecting networks
<a name="protecting-networks.e78b3a13-ac43-58b0-86b4-f826a10fce51"></a>

Your users might be part of your workforce or your customers, and can be located anywhere. For this reason, you can't trust everyone who has access to your network. When you follow the principle of applying security at all layers, you employ a [zero trust](https://aws.amazon.com/blogs/security/zero-trust-architectures-an-aws-perspective/) approach. In the zero trust security model, application components or microservices are considered discrete, and no component or microservice trusts any other component or microservice. To achieve zero trust security, follow these recommendations:
+ [Create network layers](https://docs.aws.amazon.com/wellarchitected/latest/security-pillar/sec_network_protection_create_layers.html). Layered networks help logically group similar networking components. They also shrink the potential scope of impact of unauthorized network access.
+ [Control traffic layers](https://docs.aws.amazon.com/wellarchitected/latest/security-pillar/sec_network_protection_layered.html). Apply multiple controls with a defense-in-depth approach for both inbound and outbound traffic. This includes the use of security groups (stateful inspection firewalls), network ACLs, subnets, and route tables.
+ [Implement inspection and protection](https://docs.aws.amazon.com/wellarchitected/latest/security-pillar/sec_network_protection_inspection.html). Inspect and filter your traffic at each layer. You can inspect your VPC configurations for potential unintended access by using [Network Access Analyzer](https://docs.aws.amazon.com/vpc/latest/network-access-analyzer/what-is-vaa.html). You can specify your network access requirements and identify potential network paths that do not meet them.

### Protecting compute resources
<a name="protecting-compute-resources.d23e6ea6-23b2-54c4-8bb2-918c777f822b"></a>

Compute resources include EC2 instances, containers, AWS Lambda functions, database services, IoT devices, and more. Each compute resource type requires a different approach to security. However, these resources do share common strategies that you need to consider: *defense in depth*, *vulnerability management*, *reduction in attack surface*, *automation of configuration and operation*, and *performing actions at a distance*.

Here's general guidance for protecting your compute resources for key services:
+ [Create and maintain a vulnerability management program](https://docs.aws.amazon.com/wellarchitected/latest/security-pillar/sec_protect_compute_vulnerability_management.html). Regularly scan and patch resources such as EC2 instances, Amazon Elastic Container Service (Amazon ECS) containers, and Amazon Elastic Kubernetes Service (Amazon EKS) workloads.
+ [Automate compute protection](https://docs.aws.amazon.com/wellarchitected/latest/security-pillar/sec_protect_compute_auto_protection.html). Automate your protective compute mechanisms, including vulnerability management, reduction in attack surface, and management of resources. This automation frees up time that you can use to secure other aspects of your workload, and helps reduce the risk of human error.
+ [Reduce the attack surface](https://docs.aws.amazon.com/wellarchitected/latest/security-pillar/sec_protect_compute_reduce_surface.html). Reduce your exposure to unintended access by hardening your operating systems and minimizing the components, libraries, and externally consumable services that you use.

In addition, for each AWS service that you use, check the specific security recommendations in the [service documentation](https://docs.aws.amazon.com/).

## Internet access
<a name="internet-access"></a>

Both AWS Outposts and Local Zones provide architectural patterns that give your workloads access to and from the internet. When you use these patterns, consider internet consumption from the Region a viable option only if you use it for patching, updating, accessing Git repositories that are external to AWS, and similar scenarios. For this architectural pattern, the concepts of [centralized inbound inspection](https://docs.aws.amazon.com/whitepapers/latest/building-scalable-secure-multi-vpc-network-infrastructure/centralized-inbound-inspection.html) and [centralized internet egress](https://docs.aws.amazon.com/whitepapers/latest/building-scalable-secure-multi-vpc-network-infrastructure/centralized-egress-to-internet.html) apply. These access patterns use AWS Transit Gateway, NAT gateways, network firewalls, and other components that reside in AWS Regions, but are connected to AWS Outposts or Local Zones through the data path between the Region and the edge.

Local Zones adopts a network construct called a *network border group*, which is used in AWS Regions. AWS advertises public IP addresses from these unique groups. A network border group consists of Availability Zones, Local Zones, or Wavelength Zones. You can explicitly allocate a pool of public IP addresses for use in a network border group. You can use a network border group to extend the internet gateway to Local Zones by allowing Elastic IP addresses to be served from the group. This option requires that you deploy other components to complement the core services available in Local Zones. Those components might come from ISVs and help you build inspection layers in your Local Zone, as described in the AWS blog post [Hybrid inspection architectures with AWS Local Zones](https://aws.amazon.com/blogs/networking-and-content-delivery/hybrid-inspection-architectures-with-aws-local-zone/).

In AWS Outposts, if you want to use the local gateway (LGW) to reach the internet from your network, you must modify the custom route table that's associated with the AWS Outposts subnet. The route table must have a default route entry (0.0.0.0/0) that uses the LGW as the next hop. You are responsible for implementing the remaining security controls in your local network, including perimeter defenses such as firewalls and intrusion prevention systems or intrusion detection systems (IPS/IDS). This aligns with the shared responsibility model, which divides security duties between you and the cloud provider.

### Internet access through the parent AWS Region
<a name="internet-access-through-the-parent-9999999999999999aws-region-.af600f2c-1422-5f57-be74-7459861fc459"></a>

In this option, the workloads in the Outpost access the internet through the [service link](https://docs.aws.amazon.com/outposts/latest/userguide/service-links.html) and the internet gateway in the parent AWS Region. Outbound traffic to the internet can be routed through the NAT gateway that's instantiated in your VPC. For additional security for your ingress and egress traffic, you can use AWS security services such as AWS WAF, AWS Shield, and Amazon CloudFront in the AWS Region.

The following diagram shows traffic between the workload in the AWS Outposts instance and the internet going through the parent AWS Region.

![Workloads in Outpost accessing the internet through the parent AWS Region.](https://docs.aws.amazon.com/prescriptive-guidance/latest/hybrid-cloud-best-practices/images/guide-img/117f803b-a3ee-4c57-ae66-84b53da14c2b/images/da2fa497-28e8-4672-8b62-e09fd5002dc6.png)

### Internet access through your local data center's network
<a name="internet-access-through-your-local-data-center9999999999999999apos-s-network.f948a3b3-e800-54b9-a935-c59929bb10fe"></a>

In this option, the workloads in the Outpost access the internet through your local data center. The workload traffic that accesses the internet traverses through your local internet point of presence and egresses locally. In this case, your local data center's network security infrastructure is responsible for securing the AWS Outposts workload traffic.

The following image shows traffic between a workload in the AWS Outposts subnet and the internet going through a data center.

![Workloads in Outpost accessing the internet through a local network.](https://docs.aws.amazon.com/prescriptive-guidance/latest/hybrid-cloud-best-practices/images/guide-img/117f803b-a3ee-4c57-ae66-84b53da14c2b/images/ed0961d9-80a8-48fa-b1da-7125768086a4.png)

## Infrastructure governance
<a name="infrastructure-governance"></a>

Regardless of whether your workloads are deployed in an AWS Region, Local Zone, or Outpost, you can use AWS Control Tower for infrastructure governance. AWS Control Tower offers a straightforward way to set up and govern an AWS multi-account environment, following prescriptive best practices. AWS Control Tower orchestrates the capabilities of several other AWS services, including AWS Organizations, AWS Service Catalog, and IAM Identity Center(see [all integrated services](https://docs.aws.amazon.com/controltower/latest/userguide/integrated-services.html)) to build a landing zone in less than an hour. Resources are set up and managed on your behalf.

AWS Control Tower provides unified governance across all AWS environments, including Regions, Local Zones (low-latency extensions), and Outposts (on-premises infrastructure). This helps ensure consistent security and compliance across your entire hybrid cloud architecture. For more information, see the [AWS Control Tower documentation](https://docs.aws.amazon.com/controltower/latest/userguide/what-is-control-tower.html).

You can configure AWS Control Tower and capabilities such as guardrails to comply with data residency requirements in governments and regulated industries such as Financial Services Institutions (FSIs). To understand how to deploy guardrails for data residency at the edge, see the following:
+ [Best practices for managing data residency in AWS Local Zones using landing zone controls](https://aws.amazon.com/blogs/compute/best-practices-for-managing-data-residency-in-aws-local-zones-using-landing-zone-controls/) (AWS blog post)
+ [Architecting for data residency with AWS Outposts rack and landing zone guardrails ](https://aws.amazon.com/blogs/compute/architecting-for-data-residency-with-aws-outposts-rack-and-landing-zone-guardrails/)(AWS blog post)
+ [Data Residency with Hybrid Cloud Services Lens](https://docs.aws.amazon.com/wellarchitected/latest/data-residency-hybrid-cloud-services-lens/data-residency-with-hybrid-cloud-services-lens.html) (AWS Well-Architected Framework documentation)

### Sharing Outposts resources
<a name="sharing-outposts-resources.41b32ec4-3560-5596-a674-c65b6a5fa555"></a>

Because an Outpost is a finite infrastructure that lives in your data center or in a co-location space, for centralized governance of AWS Outposts, you need to centrally control which accounts AWS Outposts resources are shared with.

With Outpost sharing, Outpost owners can share their Outposts and Outpost resources, including Outpost sites and subnets, with other AWS accounts that are in the same organization in AWS Organizations. As an Outpost owner, you can create and manage Outpost resources from a central location, and share the resources across multiple AWS accounts within your AWS organization. This allows other consumers to use Outpost sites, configure VPCs, and launch and run instances on the shared Outpost.

Shareable resources in AWS Outposts are:
+ Allocated dedicated hosts
+ Capacity reservations
+ Customer-owned IP (CoIP) address pools
+ Local gateway route tables
+ Outposts
+ Amazon S3 on Outposts
+ Sites
+ Subnets

To follow the best practices for sharing Outposts resources in a multi-account environment, see the following AWS blog posts:
+ [Sharing AWS Outposts in a multi-account AWS environment: Part 1](https://aws.amazon.com/blogs/mt/best-practices-aws-outposts-in-a-multi-account-aws-environment-part-1/)
+ [Sharing AWS Outposts in a multi-account AWS environment: Part 2](https://aws.amazon.com/blogs/mt/best-practices-aws-outposts-in-a-multi-account-aws-environment-part-2/)
