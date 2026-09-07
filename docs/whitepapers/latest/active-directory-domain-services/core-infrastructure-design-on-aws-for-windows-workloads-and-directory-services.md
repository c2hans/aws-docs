---
source_url: https://docs.aws.amazon.com/whitepapers/latest/active-directory-domain-services/core-infrastructure-design-on-aws-for-windows-workloads-and-directory-services.html
---

 This whitepaper is for historical reference only. Some content might be outdated and some links might not be available.

# Core infrastructure design on AWS for Windows Workloads and Directory Services
<a name="core-infrastructure-design-on-aws-for-windows-workloads-and-directory-services"></a>

## Planning AWS accounts and Organization
<a name="planning-aws-accounts-and-organization"></a>

 AWS Organizations helps you centrally manage your AWS accounts, identity services, and access policies for your workloads on AWS. Whether you are a growing startup or a large enterprise, Organizations helps you to centrally manage billing; control access, compliance, and security; and share resources across your AWS accounts. For more information, refer to the [AWS Organizations User Guide](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_introduction.html).

 With AWS Organizations you can centrally define critical resources and make them available to accounts across your organization. For example, you can authenticate against your central identity store and enable applications deployed in other accounts to access it.

 If your users need to manage AWS services and access AWS applications with their Active Directory credentials, we recommend integrating your identity service with the management account in AWS Organizations.
+  Deploy AWS Managed AD in the management account with trust to your on-premises Active Directory to allow users from any trusted domain to access AWS Applications. Share AWS Managed AD to other accounts across your organization.
+  Deploy AWS IAM Identity Center in the management account to centrally manage access to multiple AWS accounts and business applications and provide users with single sign-on access to all their assigned accounts and applications from one place. IAM Identity Center also includes built-in integrations to many business applications, such as Salesforce, Box, and Microsoft Office 365.

## Network design considerations for AWS Managed Microsoft AD
<a name="network-design-considerations-for-aws-managed-microsoft-ad"></a>

 Network design for Microsoft workloads and directory services consists of network connectivity and DNS names resolution.

 To plan the network topology for your organization, refer to the whitepaper [Building a Scalable and Secure Multi-VPC AWS Network Infrastructure](https://docs.aws.amazon.com/whitepapers/latest/building-scalable-secure-multi-vpc-network-infrastructure/welcome.html), and consider the following recommendations:
+  Plan your IP networks for Microsoft workloads without overlapping address spaces. Microsoft [does not recommend](https://learn.microsoft.com/en-us/troubleshoot/windows-server/active-directory/support-for-active-directory-over-nat) using Active Directory over NAT.
+  Place directory services into a centralized VPC that is reachable from any other VPC with workloads depending on Active Directory.
+  By default, instances that you launch into a VPC cannot communicate with your on-premises network. To extend your existing AD DS into the AWS Cloud, you must connect your on-premises network to the VPC in one of two ways: by using Virtual Private Network (VPN) tunnels or by using AWS Direct Connect. To connect multiple VPCs in AWS, you can use VPC peering or AWS Transit Gateway.

### Network port requirements and security groups
<a name="network-port-requirements-and-security-groups"></a>

 Active Directory requires certain network ports to be open to allow traffic for LDAP, AD DS replication, user authentication, Windows Time services, Distributed File System (DFS), and many more. When you deploy Active Directory on EC2 instances using the [AWS Quick Start](https://aws.amazon.com/quickstart/architecture/active-directory-ds/) or AWS Managed Microsoft AD, it automatically creates a new security group with all required port rules. If you manually deploy your Active Directory, you need to create a security group and configure rules for all required network protocols.

 For a complete list of ports, see [Active Directory and Active Directory Domain Services](http://technet.microsoft.com/library/dd772723(v%3Dws.10).aspx) [Port Requirements](http://technet.microsoft.com/library/dd772723(v%3Dws.10).aspx) in the Microsoft TechNet Library.

### DNS names resolution
<a name="dns-names-resolution"></a>

 Active Directory [heavily relies on DNS services](https://docs.microsoft.com/en-us/windows-server/identity/ad-ds/plan/dns-and-ad-ds) and hosts its own DNS services on domain controllers. To establish seamless name resolution in all your VPCs and your on-premises network, create a [Route 53 Resolver](https://aws.amazon.com/blogs/aws/new-amazon-route-53-resolver-for-hybrid-clouds/), deploy inbound/outbound endpoints in your VPC, and configure conditional forwarders to all of your Active Directory domains (including AWS Managed AD and on-premises Active Directory) in the Route 53 Resolver.

 Share centralized Route 53 Resolver endpoints across all VPC in your organization. Create conditional forwarders on your on-premises DNS servers for all Route 53 DNS zones and DNS zones on AWS Managed AD and point them to Route 53 Resolver Endpoints.

![Diagram showing Route 53 resolver configuration for hybrid network](https://docs.aws.amazon.com/whitepapers/latest/active-directory-domain-services/images/route53-resolver-configuration.png)

 Here are design considerations for DNS resolution:
+  Make all Active Directory DNS domains resolvable for all clients, because they are using it to locate Active Directory services and register their DNS names using dynamic updates.
+  Try to keep the DNS name resolution local to the AWS Region to reduce latency.
+  Use Amazon DNS Server (.2 resolver) as a forwarder for all other DNS domains that are not authoritative on your DNS Servers on Active Directory domain controllers. This setup allows your DCs to recursively resolve records in Amazon Route 53 private zone and use Route 53 Resolver conditional forwarders.
+  Use Route 53 Resolver Endpoints to create DNS resolution hub and manage DNS traffic by creating conditional forwarders. For more information on designing a DNS name resolution strategy in a hybrid scenario, see the [Amazon Route 53 Resolver for Hybrid Clouds](https://aws.amazon.com/blogs/aws/new-amazon-route-53-resolver-for-hybrid-clouds/) blog post.

**Note**
The Amazon EC2 instance [limits the number of packets](https://docs.aws.amazon.com/vpc/latest/userguide/vpc-dns.html) that can be sent to the Amazon provided DNS server to a maximum of 1024 packets per second per network interface. This limit cannot be increased. If you run into this performance limit, you must set up conditional forwarding for Amazon Route 53 private zones to use the Amazon DNS Server (.2 resolver) and use root hints for internet name resolution. This setup reduces the chances of you exceeding the 1024 packet limit on AWS DNS resolver.
