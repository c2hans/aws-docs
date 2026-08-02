---
source_url: https://docs.aws.amazon.com/whitepapers/latest/applying-security-practices-to-network-workload-for-csps/infrastructure-protection.html
---

 This whitepaper is for historical reference only. Some content might be outdated and some links might not be available.

# Infrastructure protection
<a name="infrastructure-protection"></a>

 Following are some recommended ways to protect your infrastructure on the network layer and on the computer layer.

## Protect the network
<a name="protect-the-network"></a>

 Appropriate network protection controls that complement the business objective and provide the business teams confidence that their network workloads can be operated securely should be introduced into the design of the workload architecture. This section discusses how you can help protect your network domain on the infrastructure level.

 **Protecting the network – at the edge**
+  Analyze the connectivity requirements of the application and apply multiple controls with a defense-in-depth approach for both inbound and outbound traffic, including the use of security groups (stateful firewall), network Access Control Lists (ACLs) (stateless firewall), subnets, and route tables. Security groups and network ACLs are means to secure traffic that leaves and enters the VPC, which is considered to be your network domain.
+  Analyze the option of using native edge protection services such as AWS WAF, AWS Shield, AWS Firewall Manager, and AWS Network Firewall to add additional layers of protection. These are native AWS services that customers can use without the heavy lifting of provisioning and maintaining the needed infrastructure and service. These services can be optionally applied in front of the Network Exposure Function (NEF). The NEF is a component of the 5G SBI architecture that is used to expose network information to external consumers. This information can include network resources, services, capabilities, and performance characteristics, and it can be accessed by other network functions or external entities through a set of APIs (Application Programming Interfaces).
  +  [AWS WAF](https://docs.aws.amazon.com/waf/latest/developerguide/waf-chapter.html) — A web application firewall that helps protect your web applications or APIs against common web exploits and bots that may affect availability, compromise security, or consume excessive resources.
  +  [AWS Shield](https://docs.aws.amazon.com/waf/latest/developerguide/shield-chapter.html) — An AWS service for the protection against Distributed Denial of Service (DDoS) attacks for applications running on AWS. There is also an enhanced version in AWS Shield Advanced. AWS Shield Advanced provides enhanced protections for applications and provides always-on, flow-based monitoring of network traffic and active application monitoring to provide near real-time notifications of suspected DDoS incidents.
  +  [AWS Firewall Manager](https://docs.aws.amazon.com/waf/latest/developerguide/fms-chapter.html) — A service that simplifies your administration and maintenance tasks across multiple accounts and resources for a variety of protections, including AWS WAF, AWS Shield Advanced, Amazon VPC security groups, and AWS Network Firewall.
  +  [AWS Network Firewall](https://docs.aws.amazon.com/network-firewall/latest/developerguide/what-is-aws-network-firewall.html) — A stateful, managed, network firewall and intrusion detection and prevention service for VPC.

 **Protecting the network – within the customer boundaries**
+  Consider using VPC endpoints to privately connect to supported AWS services and VPC endpoint services powered by [AWS PrivateLink](https://aws.amazon.com/privatelink/). AWS PrivateLink provides private connectivity between VPCs, supported AWS services, and your on-premises networks without exposing your traffic to the public internet.
  +  [VPC Endpoint](https://docs.aws.amazon.com/vpc/latest/privatelink/vpc-endpoints.html) — Enables connections between a VPC and supported services, without requiring that you use an internet gateway, NAT device, VPN connection, or AWS Direct Connect connection. In addition, VPC endpoint access is controlled using an endpoint policy. An endpoint policy is a policy document that controls which AWS principal (e.g., user, roles, etc.) can use the VPC endpoint to access an endpoint service.
+  For traffic between customer on-premises deployment (such as Outposts) and [AWS Regions](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Concepts.RegionsAndAvailabilityZones.html), there are multiple layers of encryption to be considered. At the transport layer, for Outposts, AWS encrypts in-transit data between your Outposts instance and its AWS Region. For more information, refer to [Connectivity through service links](https://docs.aws.amazon.com/outposts/latest/userguide/region-connectivity.html#service-links).
+  For on-premises commercial off-the-shelf (COTS) hardware, consider using [AWS Direct Connect](https://aws.amazon.com/directconnect/) to connect your on-premises deployment to the AWS Region. You can use AWS Direct Connect connections that support MACsec to encrypt your data from your on-premises location to the AWS Direct Connect location. You can also combine AWS Site-to-Site VPN with Direct Connect to provide encryption at the transport layer (for example, IPsec VPN). At the application layer, use SSL/TLS to communicate with AWS resources, as mentioned in the [Protect data in transit](data-protection.md#protect-data-in-transit) section.

## Protect the compute
<a name="protect-the-compute"></a>

 To protect the compute in your organization:
+  **Use AWS Nitro-based instances** — AWS Nitro System is the underlying foundation for modern Amazon EC2 instances. There is no operator, administrator, or root access for administration. Access is strictly limited to a set of authenticated, authorized, and audited administrative APIs. None of the APIs have the capability to access customer data.
  +  [Nitro Trusted Platform Module** **](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/nitrotpm.html)(NitroTPM) — [NitroTPM](https://aws.amazon.com/blogs/compute/deep-dive-into-nitrotpm-and-uefi-secure-boot-support-in-amazon-ec2/) can be used for attestation, a process to demonstrate that an EC2 instance meets pre-defined criteria, allowing you to gain confidence in its integrity. It can be used to authenticate an instance requesting access to a resource (such as a service or a database) to be contingent on its health state (for example, patching level, presence of mandated agents, and so on). For example, a private key can be “sealed” to a list of measurements of specific programs allowed to “unseal.”
+  **Evaluate the use of pre-hardened compute** — Hardened images reduce exposure to unintended access by hardening operating systems and minimizing the components, libraries, and external services that are in use.
+  **Patch management** — Rather than patching long lived instances, architect and engineer your workload to allow for newly patched images to take the place of outdated images.

  Consider scanning your container images with Amazon ECR or Amazon Inspector:
  +  [Amazon ECR](https://docs.aws.amazon.com/AmazonECR/latest/userguide/what-is-ecr.html) — An AWS container image registry service. It can perform image scanning that can help identify software vulnerabilities in container images.
  +  [Amazon Inspector](https://aws.amazon.com/inspector/?nc=sn&loc=0) — A vulnerability management service that nearly continuously scans AWS workloads for software vulnerabilities and unintended network exposure. Amazon Inspector automatically discovers and scans running Amazon EC2 instances, container images in [Amazon Elastic Container Registry](https://aws.amazon.com/ecr/) (Amazon ECR), and [AWS Lambda](https://aws.amazon.com/lambda/) functions for known software vulnerabilities and unintended network exposure.
